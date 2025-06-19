# Gesture-Controlled-Smart-Home-System-For-Differently-Abled-Persons
This project provides an innovative and accessible smart home control solution specifically designed for differently abled individuals. It offers a multi-modal interface, enabling users to control household appliances like lights and fans through voice commands, hand gestures, or head movements. The system's core lies in a Python script that leverages a webcam for real-time hand and head gesture recognition using MediaPipe, and a microphone for voice commands via the Speech Recognition library.

The recognized commands are then transmitted via serial communication to an ESP32 or Arduino microcontroller. This microcontroller, running a dedicated sketch, receives these commands and actuates connected relays to turn appliances on or off. The Arduino sketch also includes provisions for an IR sensor, hinting at future automation possibilities. This integrated system offers a flexible and intuitive way for individuals with varying physical abilities to interact with their living environment, promoting greater independence and convenience.
## Features

* **Multi-Modal Control:** Seamlessly switch between voice, hand gesture, and head movement control modes.
* **Voice Control:** Speak commands like "hand," "head," or "voice" to switch between control modes.
* **Hand Gesture Control:**
    * **1 Finger:** Turn Bathroom Light ON
    * **2 Fingers:** Turn Bathroom Light OFF
    * **3 Fingers:** Turn Living Room Fan ON
    * **4 Fingers:** Turn Living Room Fan OFF
    * **5 Fingers:** Turn Living Room Light ON
    * **0 Fingers:** Turn Living Room Light OFF
* **Head Gesture Control (Dummy Implementation):**
    * **Left:** Turn Bathroom Light ON
    * **Right:** Turn Bathroom Light OFF
    * **Up:** Turn Living Room Fan ON
    * **Down:** Turn Living Room Fan OFF
    * **Tilt Left:** Turn Living Room Light ON
    * **Tilt Right:** Turn Living Room Light OFF
* **Serial Communication:** Commands are sent from the Python script to the microcontroller via serial.
* **Appliance Control:** Control two lights (Bathroom and Living Room) and one fan (Living Room).
* **IR Sensor Integration (Arduino Side):** The Arduino sketch includes basic support for an IR sensor, allowing it to report "CLOSE" or "FAR" to a "CHECK_IR" command (though this command is not yet integrated into the Python control logic).

## Hardware Requirements

### Computer (for Python Script)

* Webcam (for hand and head gesture recognition)
* Microphone (for voice recognition)

### Microcontroller (e.g., ESP32, Arduino Uno)

* **ESP32/Arduino Board:** The microcontroller to receive commands and control appliances.
* **Relay Modules:** To interface the microcontroller's digital outputs with AC appliances (lights, fan). You will need at least 3 relay modules.
* **LEDs :** Can be used to simulate lights and fan for initial testing.
* **IR Sensor :** If you wish to utilize the IR sensor functionality in the Arduino sketch.
* **Jumper Wires**
* **Breadboard**

## Software Requirements

* **Python 3.x:** Installed on your computer.
* **OpenCV (`cv2`):** `pip install opencv-python`
* **PySerial (`serial`):** `pip install pyserial`
* **MediaPipe (`mediapipe`):** `pip install mediapipe`
* **Speech Recognition (`SpeechRecognition`):** `pip install SpeechRecognition`
* **PyAudio (for Speech Recognition):** `pip install PyAudio` (This might require installing PortAudio development libraries on Linux/macOS before installing PyAudio).
* **Arduino IDE:** For uploading the sketch to your microcontroller.
