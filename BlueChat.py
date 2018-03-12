from tkinter import Tk, Text
from ChatUI import ChatUI
from Client import BlueClient


root = Tk()
chat_room = Text
chat = BlueClient("127.0.0.1", "Bluecow")
chat.run_client()
ChatUI(root, chat)
root.title("BlueChat")
root.resizable(height=False, width=False)
root.geometry('{}x{}'.format(400, 300))  # width x height

if __name__ == "__main__":
    root.mainloop()
    chat.close_client()


