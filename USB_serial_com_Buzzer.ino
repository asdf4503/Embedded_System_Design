int notes[] = {0, 262, 294, 330, 349, 392, 440, 494};

void setup() {
    Serial.begin(9600);
    pinMode(7, OUTPUT);
}

void loop() {
    while(Serial.available()) {
        int value = Serial.parseInt();
        tone(7, notes[value], 200);
    }
}
