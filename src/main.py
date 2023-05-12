from maze_modes import single_play_mode, text_file_mode
from sys import argv
# main code loop

try:
    print("\n")
    match argv[1]:
        case 'single':
            single_play_mode()
        case 'text':
            text_file_mode()
        case 'help' | '':
            print("./mazescript.sh single --> Single maze mode. This mode is where a procedural maze is generated and is played on the terminal")
            print("./mazescript.sh text --> Text file mode. This mode is to generate a maze and save it into a .txt file for offline play or printing")
        case _:
            raise ValueError
except KeyboardInterrupt:
    print("Thank you for using this maze generator app, goodbye") 
except ValueError:
    print("Invalid input, 'single' 'text' 'help' inputs only")
except IndexError:
    print("No mode provided, after './mazescript.sh' enter in 'single' 'text' or 'help' e.g ./mazescript help")

