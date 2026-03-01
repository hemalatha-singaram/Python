class WhatsApp:
    def send_message(self):
        print("Message sent via WhatsApp")
class Instagram():
    def send_message(self):
        print("Message sent via Instagram")
class Twitter():
    def send_message(self):
        print("Message sent via Twitter")
apps=[WhatsApp(),Instagram(),Twitter()]
for app in apps:
    app.send_message()
    