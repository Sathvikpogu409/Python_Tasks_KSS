#Smart Home Devices (Multiple Inheritance) 
#A smart home device may have both WiFi connectivity and Voice control features. 
#Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that 
#inherits from both using multiple inheritance.


class WiFiDevice:
    def wifi(self):
        print("WiFi connection is available")


class VoiceAssistant:
    def voice_control(self):
        print("Voice control is available")


class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display(self):
        print("Smart Speaker is ready")


s = SmartSpeaker()
s.display()
s.wifi()
s.voice_control()
