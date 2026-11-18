class WiFiDevice:
    def wifi(self):
        print("WiFi Connectivity Available")

class VoiceAssistant:
    def voice_control(self):
        print("Voice Control Available")

class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display(self):
        print("Smart Speaker Features:")
        self.wifi()
        self.voice_control()

s1 = SmartSpeaker()
s1.display()
