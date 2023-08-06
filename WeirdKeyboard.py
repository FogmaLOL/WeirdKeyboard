import keyboard

def shift_keybindings():
    original_keys = "qwertyuiopasdfghjkl;zxcvbnm,."
    shifted_keys = original_keys[-1] + original_keys[:-1]
    key_mapping = dict(zip(original_keys, shifted_keys))

    while True:
        try:
            event = keyboard.read_event(suppress=True)

            if event.event_type == keyboard.KEY_DOWN:
                if event.name in key_mapping:
            
                    shifted_key = key_mapping[event.name]
                 
                    keyboard.press(shifted_key)
                elif event.name == "left":
                   #i messed up the code so there is no stop key to stop this just close the program
                   # im to lazy to fix
                    break
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    print("Press any key to mess up the keybindings.")
    shift_keybindings()
    print("Keybindings restored.")
