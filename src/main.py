from maze_modes import single_play_mode, text_file_mode

while True:
    try:
        mode_selection = input("Which mode to you want to use? ('single' = Single maze mode, 'text' = maze saved as .txt file, 'help' = description of modes): ")
        if 'single' in mode_selection:
            single_play_mode()    
        elif 'text' in mode_selection:
            text_file_mode()
        elif 'help' in mode_selection:
            print("""           'single' = single maze mode. This mode is where a procedural maze is generated and is played on the terminal
            'text' = Text file mode. This mode is to generate a maze and save it into a .txt file for offline play or printing""")
        else:
            raise ValueError
    except KeyboardInterrupt:
        print("Thanks for playing") 
        break
    except ValueError:
        print("Invalid input, 'single' 'text' 'help' input only")