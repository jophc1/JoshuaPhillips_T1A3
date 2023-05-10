from maze_modes import single_play_mode, text_file_mode

while True:
    try:
        mode_selection = input("Which mode to you want to use? ('single', 'text', 'help', 'exit'): ")
        if 'single' == mode_selection:
            single_play_mode()    
        elif 'text' == mode_selection:
            text_file_mode()
        elif 'help' == mode_selection:
            print("""           'single' = single maze mode. This mode is where a procedural maze is generated and is played on the terminal
            'text' = Text file mode. This mode is to generate a maze and save it into a .txt file for offline play or printing""")
        elif 'exit' == mode_selection:
            raise KeyboardInterrupt
        else:
            raise ValueError
    except KeyboardInterrupt:
        print("Thank you for using this maze generator app, goodbye") 
        break
    except ValueError:
        print("Invalid input, 'single' 'text' 'help' 'exit' inputs only")

