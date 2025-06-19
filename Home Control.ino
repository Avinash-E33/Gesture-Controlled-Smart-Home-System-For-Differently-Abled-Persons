#define BATHROOM_LIGHT_PIN  10
#define LIVINGROOM_LIGHT_PIN 11
#define LIVINGROOM_FAN_PIN   12
#define IR_SENSOR_PIN        14   // IR sensor connected here

String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(115200);

  pinMode(BATHROOM_LIGHT_PIN, OUTPUT);
  pinMode(LIVINGROOM_LIGHT_PIN, OUTPUT);
  pinMode(LIVINGROOM_FAN_PIN, OUTPUT);
  pinMode(IR_SENSOR_PIN, INPUT);

  // Initialize all outputs to LOW
  digitalWrite(BATHROOM_LIGHT_PIN, LOW);
  digitalWrite(LIVINGROOM_LIGHT_PIN, LOW);
  digitalWrite(LIVINGROOM_FAN_PIN, LOW);

  inputString.reserve(200); // Reserve memory to store input commands
}

void loop() {
  if (stringComplete) {
    inputString.trim(); // Remove extra whitespace or newlines

    if (inputString == "BATHROOM_LIGHT_ON") {
      digitalWrite(BATHROOM_LIGHT_PIN, HIGH);
    } else if (inputString == "BATHROOM_LIGHT_OFF") {
      digitalWrite(BATHROOM_LIGHT_PIN, LOW);
    } else if (inputString == "LIVINGROOM_LIGHT_ON") {
      digitalWrite(LIVINGROOM_LIGHT_PIN, HIGH);
    } else if (inputString == "LIVINGROOM_LIGHT_OFF") {
      digitalWrite(LIVINGROOM_LIGHT_PIN, LOW);
    } else if (inputString == "LIVINGROOM_FAN_ON") {
      digitalWrite(LIVINGROOM_FAN_PIN, HIGH);
    } else if (inputString == "LIVINGROOM_FAN_OFF") {
      digitalWrite(LIVINGROOM_FAN_PIN, LOW);
    } else if (inputString == "CHECK_IR") {
      int irValue = digitalRead(IR_SENSOR_PIN);

      if (irValue == LOW) {
        Serial.println("CLOSE"); // Object detected near
      } else {
        Serial.println("FAR");   // No object near
      }
    }

    inputString = "";    // Clear the input
    stringComplete = false; // Reset the flag
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true; // Newline indicates end of command
    } else {
      inputString += inChar;
    }
  }
}