import keyboard
import simpleaudio as sa
from random import choice


#play_obj.wait_done()


def on_key_press(event):
    global id
    if event.name == "space":
        wave_obj = sa.WaveObject.from_wave_file("sounds/space.wav")
        play_obj = wave_obj.play()
        print("space")
    elif event.name == "enter":
        wave_obj = sa.WaveObject.from_wave_file("sounds/enter.wav")
        play_obj = wave_obj.play()
        print("enter")
    elif event.name == "backspace":
        wave_obj = sa.WaveObject.from_wave_file("sounds/backspace.wav")
        play_obj = wave_obj.play()
        print("backspace")
    else:
        wave_obj = sa.WaveObject.from_wave_file(choice(["sounds/letter_1.wav", "sounds/letter_2.wav", "sounds/letter_3.wav"]))
        play_obj = wave_obj.play()
        print("Random keys")

    print(f"You typed: {event.name}")

def nothing(event): 
    print(event.name)
    keyboard.on_release_key(event.name, on_key_press)

keyboard.hook(nothing)
keyboard.on_release_key("esc", on_key_press)
keyboard.wait("esc")  # Waits for the 'esc' key to exit the program
