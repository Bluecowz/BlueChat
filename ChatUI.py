from tkinter import Frame, Button, Text, TOP, RIGHT, END, LEFT, BOTTOM, Label
from threading import Thread


class ChatUI:

    def __init__(self, master, chat_client):
        self._chat_client = chat_client
        self._frame = Frame(master)
        self._frame.pack()
        self._send_button = Button(self._frame, text="  SEND  ", command=self.send_message)
        self._send_button.pack(side=BOTTOM)

        self._message = Text(self._frame, height=12)
        self._message.pack(side=BOTTOM)

        self._chat = Text(self._frame, height=64)
        self._chat.pack(side=TOP)

        t = Thread(target=self.message_update)
        t.start()

    def send_message(self):
        self._chat_client.send_message(self._message.get("1.0", 'end-1c'))
        self._message.delete("1.0", END)

    def message_update(self):
        while True:
            message = self._chat_client.message_recv()
            if message is not "":
                self._chat.insert(END, message + "\n")
