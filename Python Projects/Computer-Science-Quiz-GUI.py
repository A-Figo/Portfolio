import tkinter as tk
from tkinter import ttk, messagebox
import random

# Color Palette (Space Mission Theme)
BG_COLOR = "#0b0d17"  # Deep Navy/Black
FG_COLOR = "#d0d6f9"  # Light Blue/White
ACCENT_COLOR = "#00ffff"  # Cyan Neon
BUTTON_BG = "#151932"  # Dark Blue
BUTTON_FG = "#ffffff"
BUTTON_HOVER = "#3d4c8a"
CORRECT_COLOR = "#00ff00"  # Bright Green
INCORRECT_COLOR = "#ff0000"  # Bright Red
FONT_TITLE = ("Orbitron", 24, "bold")
FONT_HEADER = ("Roboto", 16, "bold")
FONT_TEXT = ("Roboto", 12)
FONT_BUTTON = ("Roboto", 12, "bold")

# Question Data
QUESTIONS_DATA = [
    # Data Representation
    {"q": "What is the binary equivalent of decimal 13?", "options": ["1011", "1101", "1110", "1001"],     "answer": "1101"},
    {"q": "Which hexadecimal value represents decimal 255?", "options": ["FF", "F0", "AA", "1F"],     "answer": "FF"},
    {"q": "How many bits are used to store one ASCII character?", "options": ["6", "7", "8", "16"], "answer": "7"},
    {"q": "Which unit is typically used to measure file size?", "options": ["Hertz", "Bytes", "Pixels", "Volts"], "answer": "Bytes"},
    {"q": "What is the main purpose of data compression?", "options": ["Increase quality", "Reduce file size", "Encrypt data", "Speed up CPU"], "answer": "Reduce file size"},

    # Data Transmission
    {"q": "What is a data packet?", "options": ["A storage device", "A unit of data sent over a network", "A type of software", "A network cable"], "answer": "A unit of data sent over a network"},
    {"q": "Which transmission method sends data in both directions at the same time?", "options": ["Simplex", "Half-duplex", "Full-duplex", "Serial"], "answer": "Full-duplex"},
    {"q": "Which USB standard provides the fastest data transfer rate?", "options": ["USB 1.0", "USB 2.0", "USB 3.0", "USB 1.1"], "answer": "USB 3.0"},
    {"q": "Which technique is used to detect errors in transmitted data?", "options": ["Parity check", "Encryption", "Compression", "Modulation"], "answer": "Parity check"},
    {"q": "What is encryption used for?", "options": ["Reducing file size", "Protecting data from unauthorized access", "Detecting errors", "Speeding up networks"], "answer": "Protecting data from unauthorized access"},

    # Hardware
    {"q": "What does RAM stand for?",
     "options": ["Random Access Memory", "Read Access Memory", "Run Active Memory", "Rapid Action Module"], "answer": "Random Access Memory"},
    {"q": "Which component temporarily stores data currently being processed?", "options": ["RAM", "ROM", "Hard Drive", "GPU"], "answer": "RAM"},
    {"q": "Which device converts digital signals into sounds that humans can hear?", "options": ["Microphone", "Speaker", "Scanner", "Projector"], "answer": "Speaker"},
    {"q": "What is the purpose of ROM?", "options": ["Store permanent instructions", "Temporary storage", "Process graphics", "Connect networks"], "answer": "Store permanent instructions"},
    {"q": "Which hardware component performs calculations?", "options": ["ALU", "Cache", "Motherboard", "NIC"], "answer": "ALU"},

    # Software
    {"q": "What type of software controls the operation of hardware?", "options": ["System software", "Application software", "Utility software", "Programming software"], "answer": "System software"},
    {"q": "Which of the following is an example of utility software?", "options": ["Antivirus", "Spreadsheet", "Web browser", "Game"], "answer": "Antivirus"},
    {"q": "What is open-source software?", "options": ["Software with hidden code", "Software with publicly available source code", "Paid software only", "Illegal software"], "answer": "Software with publicly available source code"},

    # Internet and Its Uses
    {"q": "What is the main purpose of a web browser?", "options": ["Create websites", "Access and display web pages", "Store files", "Protect networks"], "answer": "Access and display web pages"},
    {"q": "Which technology allows secure communication over the internet?", "options": ["HTTPS", "HTTP", "FTP", "SMTP"], "answer": "HTTPS"},
    {"q": "What is cryptocurrency?", "options": ["Digital currency using encryption", "Physical money", "Bank software", "A password"], "answer": "Digital currency using encryption"},
    {"q": "Which is an example of a cybersecurity threat?", "options": ["Malware", "Firewall", "Encryption", "Backup"], "answer": "Malware"},

    # Automated and Emerging Technologies
    {"q": "What is an automated system?", "options": ["System requiring human control", "System operating without human intervention", "Manual process", "Offline computer"], "answer": "System operating without human intervention"},
    {"q": "Which sensor detects changes in temperature?", "options": ["Pressure sensor", "Temperature sensor", "Light sensor", "Motion sensor"], "answer": "Temperature sensor"},
    {"q": "What is robotics?", "options": ["Study of networks", "Design and use of robots", "Programming languages", "Database design"], "answer": "Design and use of robots"},
    {"q": "What is artificial intelligence?", "options": ["Machines simulating human intelligence", "Hardware repairs", "Manual programming", "Network security"], "answer": "Machines simulating human intelligence"},

    # Algorithm Design and Problem Solving
    {"q": "What is an algorithm?", "options": ["Step-by-step solution to a problem", "A programming language", "A hardware device", "A data file"], "answer": "Step-by-step solution to a problem"},
    {"q": "What is a trace table used for?", "options": ["Testing algorithms", "Storing data", "Designing hardware", "Encrypting files"], "answer": "Testing algorithms"},
    {"q": "What does debugging mean?", "options": ["Finding and fixing errors", "Writing code", "Running programs", "Saving files"], "answer": "Finding and fixing errors"},

    # Programming
    {"q": "Which data type stores whole numbers?", "options": ["Integer", "String", "Boolean", "Float"], "answer": "Integer"},
    {"q": "What symbol is commonly used for assignment in programming?", "options": ["=", "==", "+", ":"], "answer": "="},
    {"q": "What is a conditional statement used for?", "options": ["Making decisions", "Repeating code", "Storing data", "Displaying output"], "answer": "Making decisions"},
    {"q": "Which loop repeats while a condition is true?", "options": ["FOR", "WHILE", "IF", "CASE"], "answer": "WHILE"},

    # Databases
    {"q": "What is a database?", "options": ["Organized collection of data", "A program", "A network", "A hardware device"], "answer": "Organized collection of data"},
    {"q": "What is a primary key?", "options": ["Unique identifier for a record", "Duplicate field", "Password", "Relationship"], "answer": "Unique identifier for a record"},
    {"q": "What is a field in a database?", "options": ["Column of data", "Row of data", "Entire table", "Software"], "answer": "Column of data"},

    # Boolean Logic
    {"q": "Which gate outputs true only when both inputs are true?", "options": ["AND", "OR", "NOT", "XOR"], "answer": "AND"},
    {"q": "Which gate outputs the opposite of the input?", "options": ["NOT", "AND", "OR", "NAND"], "answer": "NOT"},
    {"q": "What is the output of OR when inputs are 0 and 1?", "options": ["0", "1", "Error", "Null"], "answer": "1"},
    {"q": "Which gate outputs false only when both inputs are true?", "options": ["NAND", "AND", "OR", "NOR"], "answer": "NAND"}
]

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IGCSE Computer Science Mission")
        self.geometry("900x650")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)

        # Game State
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.user_answers = []  # List of dicts: {'q': question_text, 'correct': correct_ans, 'user': user_ans}

        # Styles
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background=BG_COLOR)
        style.configure("TLabel", background=BG_COLOR, foreground=FG_COLOR, font=FONT_TEXT)
        style.configure("Header.TLabel", font=FONT_HEADER, foreground=ACCENT_COLOR)
        style.configure("Title.TLabel", font=FONT_TITLE, foreground=ACCENT_COLOR)

        # Container for screens
        self.container = tk.Frame(self, bg=BG_COLOR)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

        self.show_title_screen()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def create_styled_button(self, parent, text, command, state="normal", width=20, bg=BUTTON_BG, fg=BUTTON_FG):
        btn = tk.Button(parent, text=text, command=command, state=state, width=width,
                        bg=bg, fg=fg, font=FONT_BUTTON,
                        activebackground=BUTTON_HOVER, activeforeground=ACCENT_COLOR,
                        bd=2, relief="raised", cursor="hand2" if state=="normal" else "")
        # Add hover effect
        def on_enter(e):
            if btn['state'] == 'normal':
                btn['bg'] = BUTTON_HOVER
                btn['fg'] = ACCENT_COLOR
        def on_leave(e):
            if btn['state'] == 'normal':
                btn['bg'] = bg
                btn['fg'] = fg

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    def show_title_screen(self):
        self.clear_container()

        # Decorative top border
        tk.Frame(self.container, bg=ACCENT_COLOR, height=4).pack(fill="x", pady=(0, 20))

        lbl_title = tk.Label(self.container, text="IGCSE Computer Science", font=FONT_TITLE, bg=BG_COLOR, fg=ACCENT_COLOR)
        lbl_title.pack(pady=20)

        lbl_mission = tk.Label(self.container, text="MISSION BRIEFING", font=("Roboto", 18, "bold"), bg=BG_COLOR, fg=FG_COLOR)
        lbl_mission.pack(pady=10)

        desc_text = (
            "Welcome, Cadet. Your mission is to navigate through 40 levels of Computer Science knowledge.\n\n"
            "• You will face 40 multiple-choice questions.\n"
            "• Topics: Data Representation, Data Transmission, Hardware, Software, \nThe Internet and Its Uses, Automated and Emerging Technologies, \nAlgorithm Design and Problem Solving, Programming, Databases, Boolean Logic.\n"
            "• Passing Requirement: 75% accuracy (30/40 correct).\n\n"
            "Prepare for launch."
        )
        lbl_desc = tk.Label(self.container, text=desc_text, font=FONT_TEXT, bg=BG_COLOR, fg=FG_COLOR, justify="center")
        lbl_desc.pack(pady=20)

        btn_start = self.create_styled_button(self.container, "INITIATE MISSION", self.start_quiz, width=25, bg=ACCENT_COLOR, fg=BG_COLOR)
        btn_start.pack(pady=40)

        # Decorative bottom
        tk.Label(self.container, text="SYSTEM READY...", font=("Consolas", 10), bg=BG_COLOR, fg=ACCENT_COLOR).pack(side="bottom", pady=10)

    def start_quiz(self):
        self.questions = random.sample(QUESTIONS_DATA, 40)
        self.current_question_index = 0
        self.score = 0
        self.user_answers = []
        self.show_question_screen()

    def show_question_screen(self):
        self.clear_container()

        q_data = self.questions[self.current_question_index]

        # Level Indicator
        level_text = f"LEVEL {self.current_question_index + 1} / 40"
        lbl_level = tk.Label(self.container, text=level_text, font=("Orbitron", 14), bg=BG_COLOR, fg=ACCENT_COLOR)
        lbl_level.pack(pady=(10, 5))

        # Progress Bar
        progress_frame = tk.Frame(self.container, bg="#333", height=5, width=600)
        progress_frame.pack(pady=(0, 20))
        progress_width = int((self.current_question_index / 40) * 600)
        if progress_width > 0:
            tk.Frame(progress_frame, bg=ACCENT_COLOR, height=5, width=progress_width).place(x=0, y=0)

        # Question Card
        card_frame = tk.Frame(self.container, bg="#1a1d2e", bd=2, relief="flat", padx=20, pady=20)
        card_frame.pack(fill="both", expand=True, padx=50)

        lbl_question = tk.Label(card_frame, text=q_data["q"], font=("Roboto", 16), bg="#1a1d2e", fg="white", wraplength=700, justify="center")
        lbl_question.pack(pady=20)

        # Options
        self.selected_option = tk.StringVar(value="")
        options = q_data["options"].copy()
        random.shuffle(options)

        options_frame = tk.Frame(card_frame, bg="#1a1d2e")
        options_frame.pack(fill="both", expand=True, pady=10)

        self.option_buttons = []

        for idx, option in enumerate(options):
            # Using custom radio-like buttons
            btn = tk.Button(options_frame, text=option, font=FONT_TEXT,
                            bg=BUTTON_BG, fg=BUTTON_FG,
                            activebackground=BUTTON_HOVER, activeforeground="white",
                            bd=1, relief="solid", width=50, pady=10,
                            command=lambda opt=option, b_idx=idx: self.select_option(opt, b_idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

    def select_option(self, option, btn_index):
        self.selected_option.set(option)

        # Update visual selection
        for i, btn in enumerate(self.option_buttons):
            if i == btn_index:
                btn.config(bg=ACCENT_COLOR, fg=BG_COLOR, bd=2)
            else:
                btn.config(bg=BUTTON_BG, fg=BUTTON_FG, bd=1)
            btn.config(state="disabled") # Disable all buttons after selection

        # Automatically proceed to next question after a short delay
        self.after(500, self.next_question)

    def next_question(self):
        user_choice = self.selected_option.get()
        correct_answer = self.questions[self.current_question_index]["answer"]

        # Record Answer
        is_correct = (user_choice == correct_answer)
        if is_correct:
            self.score += 1

        self.user_answers.append({
            "q": self.questions[self.current_question_index]["q"],
            "correct": correct_answer,
            "user": user_choice,
            "is_correct": is_correct
        })

        self.current_question_index += 1

        if self.current_question_index < 40:
            self.show_question_screen()
        else:
            self.show_result_screen()

    def show_result_screen(self):
        self.clear_container()

        percentage = (self.score / 40) * 100
        passed = percentage >= 75

        # Result Header
        result_color = CORRECT_COLOR if passed else INCORRECT_COLOR
        result_title = "MISSION ACCOMPLISHED" if passed else "MISSION FAILED"

        tk.Label(self.container, text=result_title, font=FONT_TITLE, bg=BG_COLOR, fg=result_color).pack(pady=20)

        score_text = f"Final Score: {self.score} / 40 ({percentage:.1f}%)"
        tk.Label(self.container, text=score_text, font=("Orbitron", 18), bg=BG_COLOR, fg="white").pack(pady=10)

        status_msg = "Status: CERTIFIED" if passed else "Status: RETRY REQUIRED"
        tk.Label(self.container, text=status_msg, font=("Roboto", 14), bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)

        # Scrollable Review Area
        review_frame = tk.Frame(self.container, bg=BG_COLOR)
        review_frame.pack(fill="both", expand=True, pady=20, padx=20)

        canvas = tk.Canvas(review_frame, bg=BG_COLOR, highlightthickness=0)
        scrollbar = ttk.Scrollbar(review_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Populate Review
        for idx, ans in enumerate(self.user_answers):
            q_frame = tk.Frame(scrollable_frame, bg="#151932", bd=1, relief="solid", pady=5, padx=5)
            q_frame.pack(fill="x", pady=5, padx=5)

            q_lbl = tk.Label(q_frame, text=f"Q{idx+1}: {ans['q']}", font=("Roboto", 10, "bold"), bg="#151932", fg="white", wraplength=800, justify="left")
            q_lbl.pack(anchor="w")

            user_fg = CORRECT_COLOR if ans['is_correct'] else INCORRECT_COLOR
            user_lbl = tk.Label(q_frame, text=f"Your Answer: {ans['user']}", font=("Roboto", 10), bg="#151932", fg=user_fg, anchor="w")
            user_lbl.pack(anchor="w")

            if not ans['is_correct']:
                corr_lbl = tk.Label(q_frame, text=f"Correct Answer: {ans['correct']}", font=("Roboto", 10), bg="#151932", fg=CORRECT_COLOR, anchor="w")
                corr_lbl.pack(anchor="w")

        # Restart Button
        self.create_styled_button(self.container, "RESTART MISSION", self.show_title_screen, width=20, bg=ACCENT_COLOR, fg=BG_COLOR).pack(pady=20)

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
