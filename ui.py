import tkinter as tk

cli_header = """
__        __         _                                       _              
\ \      / /   ___  | |   ___    ___    _ __ ___     ___    | |_    ___     
 \ \ /\ / /   / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \   | __|  / _ \    
  \ V  V /   |  __/ | | | (__  | (_) | | | | | | | |  __/   | |_  | (_) |   
   \_/\_/     \___| |_|  \___|  \___/  |_| |_| |_|  \___|    \__|  \___/    
                                                                            
           _     _                 ___    _   _   ___   _____  _            
          | |_  | |__     ___     / _ \  | | | | |_ _| |__  / | |           
          | __| | '_ \   / _ \   | | | | | | | |  | |    / /  | |           
          | |_  | | | | |  __/   | |_| | | |_| |  | |   / /_  |_|           
           \__| |_| |_|  \___|    \__\_\  \___/  |___| /____| (_)           
"""
cli_game_over = """
  ____    _    __  __ _____    _____     _______ ____    _ 
 / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \  | |
| |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) | | |
| |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ <  |_|
 \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\ (_)
"""

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 500

class QuizUi:

    def __init__(self):
        self.window = tk.Tk()
        # WINDOW SETUP
        blank_space = " "
        self.window.title(60*blank_space+"THE QUIZ!")
        self.center_window()
        self.window.resizable(False, False)

        # HEADER
        self.header = tk.Label(
            self.window, 
            text="Welcome to the Quiz!",
            font=("Times", 20, "bold"))
        self.header.grid(row=0, column=0)

        self.window.mainloop()

    def center_window(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_cordinate = (screen_width//2) - (WINDOW_WIDTH//2)
        y_cordinate = (screen_height//2) - (WINDOW_HEIGHT//2)
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_cordinate}+{y_cordinate}")