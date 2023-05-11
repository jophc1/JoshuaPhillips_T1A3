from maze_modes import single_play_mode, text_file_mode
# main code loop
while True:
    try:
        mode_selection = input("Which mode to you want to use? ('single', 'text', 'help', 'exit'): ")
        match mode_selection:
            case 'single':
                single_play_mode()
            case 'text':
                text_file_mode()
            case 'help':
                print("'single' = Single maze mode. This mode is where a procedural maze is generated and is played on the terminal")
                print("'text' = Text file mode. This mode is to generate a maze and save it into a .txt file for offline play or printing")
            case 'exit':
                raise KeyboardInterrupt
            case _:
                raise ValueError
    except KeyboardInterrupt:
        print("Thank you for using this maze generator app, goodbye") 
        break
    except ValueError:
        print("Invalid input, 'single' 'text' 'help' 'exit' inputs only")

