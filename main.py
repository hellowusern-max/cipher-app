import os
import urllib.parse
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

def open_whatsapp_android(url):
    # هذه الدالة تفتح الواتساب في الاندرويد
    try:
        from jnius import autoclass
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
        PythonActivity.mActivity.startActivity(intent)
    except Exception as e:
        # لو نشغل على الكمبيوتر
        try:
            webbrowser.open(url)
        except:
            print(f"Failed to open: {e}")

class CipherApp(App):
    def build(self):
        self.title = "تطبيق التشفير"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        layout.add_widget(Label(text="قسم التشفير", size_hint_y=None, height=30))
        self.enc_input = TextInput(
            hint_text='يرجى كتابة النص الذي تريد تشفيره وارساله',
            multiline=True, size_hint_y=None, height=120
        )
        layout.add_widget(self.enc_input)

        btn_send = Button(text='ارسال', size_hint_y=None, height=50, background_color=(0.2, 0.6, 0.2, 1))
        btn_send.bind(on_press=self.send_whatsapp)
        layout.add_widget(btn_send)

        layout.add_widget(Label(text="قسم فك التشفير", size_hint_y=None, height=30))
        self.dec_input = TextInput(
            hint_text='يرجى لصق النص المراد فك تشفيره',
            multiline=True, size_hint_y=None, height=100
        )
        layout.add_widget(self.dec_input)

        btn_dec = Button(text='فك تشفير', size_hint_y=None, height=50, background_color=(0.3, 0.3, 0.3, 1))
        btn_dec.bind(on_press=self.decrypt_text)
        layout.add_widget(btn_dec)

        self.result_label = Label(text='سيظهر النص المفكوك هنا...', size_hint_y=None, height=100)
        layout.add_widget(self.result_label)

        return layout

    def encod(self, txt):
        txt_bytes = txt.encode('utf-8')
        txt_len = len(txt_bytes)
        key = os.urandom(txt_len)
        encrypted_bytes = bytearray()
        for i in range(txt_len):
            encrypted_bytes.append(txt_bytes[i] ^ key[i])
        en = bytes(encrypted_bytes)
        mid = 4 if len(en) >= 4 else len(en)
        vb = b'008'
        t = en[:mid] + vb + key + vb + en[mid:] + os.urandom(10)
        return t.hex()

    def decode(self, hex_encrypted):
        full_data = bytes.fromhex(hex_encrypted)
        payload = full_data[:-10]
        parts = payload.split(b'008', 2)
        if len(parts) < 3:
            raise ValueError("خطأ في بنية البيانات!")
        en_start, key, en_rest = parts
        encrypted_bytes = en_start + en_rest
        decrypted_bytes = bytearray()
        for i in range(len(encrypted_bytes)):
            decrypted_bytes.append(encrypted_bytes[i] ^ key[i])
        return decrypted_bytes.decode('utf-8')

    def send_whatsapp(self, instance):
        txt = self.enc_input.text.strip()
        if not txt: return
        sk = self.encod(txt)
        encoded_sk = urllib.parse.quote(sk)
        url = f"https://wa.me/736737628?text={encoded_sk}"
        open_whatsapp_android(url)
        self.enc_input.text = ""

    def decrypt_text(self, instance):
        sk = self.dec_input.text.strip()
        if not sk: return
        try:
            res = self.decode(sk)
            self.result_label.text = res
        except Exception:
            self.result_label.text = "خطأ: النص المشفر غير صالح!"

if __name__ == '__main__':
    CipherApp().run()