from kivy.app import App
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission
from jnius import autoclass

class SMSReaderApp(App):
    def build(self):
        request_permissions([Permission.READ_SMS])
        SMSRetriever = autoclass('android.provider.Telephony$Sms')
        contentResolver = autoclass('org.kivy.android.PythonActivity').mActivity.getContentResolver()
        Uri = autoclass('android.net.Uri')
        sms_inbox = Uri.parse("content://sms/inbox")
        cursor = contentResolver.query(sms_inbox, None, None, None, None)

        messages = []
        if cursor:
            while cursor.moveToNext():
                body = cursor.getString(cursor.getColumnIndex("body"))
                messages.append(body)
            cursor.close()

        return Label(text="\n\n".join(messages[:5]))  # Pehle 5 SMS show karega

if __name__ == '__main__':
    SMSReaderApp().run()
