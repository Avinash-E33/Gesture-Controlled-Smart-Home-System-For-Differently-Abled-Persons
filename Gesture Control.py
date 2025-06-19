import cv2
import serial
import time
import random
import mediapipe as mp
import speech_recognition as sr

# Setup Serial Communication
ser = serial.Serial('COM5', 115200)  # Change COM port accordingly
time.sleep(2)  # Wait for the ESP32 connection

# Initialize Camera
cap = cv2.VideoCapture(0)

# Setup Mediapipe for Hand Detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Setup Speech Recognition
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Mode management
mode = "voice"  # Start in voice mode

# Function to detect head movement (dummy/random for now)
def detect_head_movement(frame):
    directions = ["left", "right", "up", "down", "tilt_left", "tilt_right", "center"]
    return random.choice(directions)

# Function to count fingers
def count_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    count = 0

    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    return count

# Function to listen and switch modes using voice
def listen_for_mode():
    global mode
    with mic as source:
        print("Listening for mode command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=3)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Heard: {command}")
        if "hand" in command:
            mode = "hand"
            print("Switched to HAND control mode")
        elif "head" in command:
            mode = "head"
            print("Switched to HEAD control mode")
        elif "voice" in command:
            mode = "voice"
            print("Staying in VOICE control mode")
    except Exception as e:
        print(f"Voice recognition failed: {e}")

# Main loop
while True:
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if mode == "voice":
        listen_for_mode()
        time.sleep(1)  # Pause slightly after listening
    elif mode == "hand":
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                fingers = count_fingers(hand_landmarks)

                if fingers == 1:
                    ser.write(b'BATHROOM_LIGHT_ON\n')
                    print("Bathroom Light ON")
                elif fingers == 2:
                    ser.write(b'BATHROOM_LIGHT_OFF\n')
                    print("Bathroom Light OFF")
                elif fingers == 3:
                    ser.write(b'LIVINGROOM_FAN_ON\n')
                    print("Living Room Fan ON")
                elif fingers == 4:
                    ser.write(b'LIVINGROOM_FAN_OFF\n')
                    print("Living Room Fan OFF")
                elif fingers == 5:
                    ser.write(b'LIVINGROOM_LIGHT_ON\n')
                    print("Living Room Light ON")
                elif fingers == 0:
                    ser.write(b'LIVINGROOM_LIGHT_OFF\n')
                    print("Living Room Light OFF")
    elif mode == "head":
        head_direction = detect_head_movement(frame)

        if head_direction == "left":
            ser.write(b'BATHROOM_LIGHT_ON\n')
            print("Head Left: Bathroom Light ON")
        elif head_direction == "right":
            ser.write(b'BATHROOM_LIGHT_OFF\n')
            print("Head Right: Bathroom Light OFF")
        elif head_direction == "up":
            ser.write(b'LIVINGROOM_FAN_ON\n')
            print("Head Up: Living Room Fan ON")
        elif head_direction == "down":
            ser.write(b'LIVINGROOM_FAN_OFF\n')
            print("Head Down: Living Room Fan OFF")
        elif head_direction == "tilt_left":
            ser.write(b'LIVINGROOM_LIGHT_ON\n')
            print("Tilt Left: Living Room Light ON")
        elif head_direction == "tilt_right":
            ser.write(b'LIVINGROOM_LIGHT_OFF\n')
            print("Tilt Right: Living Room Light OFF")
        else:
            print("Head Center: No action")

    # Display the frame
    cv2.imshow("Control Panel", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.5)  # Control sending rate

# Cleanup
cap.release()
cv2.destroyAllWindows()