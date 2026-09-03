import customtkinter as ctk

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class StoryApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("The Last Light in Dorm 3")
        self.geometry("800x600")
        self.minsize(600, 400)
        
        # Grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.discovered_endings = set()
        self.total_endings = 12
        
        self.current_frame = None
        self.show_home_screen()

    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

    def show_home_screen(self):
        self.clear_frame()
        self.current_frame = ctk.CTkFrame(self)
        self.current_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.current_frame.grid_rowconfigure(0, weight=1)
        self.current_frame.grid_rowconfigure(1, weight=1)
        self.current_frame.grid_rowconfigure(2, weight=1)
        self.current_frame.grid_rowconfigure(3, weight=1)
        self.current_frame.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            self.current_frame,
            text="The Last Light in Dorm 3",
            font=ctk.CTkFont(family="Courier", size=40, weight="bold"),
            text_color="#ff4444"
        )
        title_label.grid(row=0, column=0, pady=(50, 20))

        desc_text = (
            "A mysterious midnight blackout hits your dorm.\n"
            "Only the emergency lights remain.\n"
            "Then, you hear the knocking.\n\n"
            "Will you survive the night? Every choice matters."
        )
        desc_label = ctk.CTkLabel(
            self.current_frame,
            text=desc_text,
            font=ctk.CTkFont(size=18),
            justify="center"
        )
        desc_label.grid(row=1, column=0, pady=20)

        start_btn = ctk.CTkButton(
            self.current_frame,
            text="Start Game",
            font=ctk.CTkFont(size=24, weight="bold"),
            fg_color="#8b0000",
            hover_color="#5c0000",
            height=60,
            width=200,
            command=self.start_game
        )
        start_btn.grid(row=2, column=0, pady=(20, 50))
        
        if self.discovered_endings:
            stats_label = ctk.CTkLabel(
                self.current_frame,
                text=f"Endings Discovered: {len(self.discovered_endings)} / {self.total_endings}",
                font=ctk.CTkFont(size=16)
            )
            stats_label.grid(row=3, column=0, pady=10)

    def start_game(self):
        self.show_node("start")

    def show_node(self, node_id):
        self.clear_frame()
        self.current_frame = ctk.CTkFrame(self)
        self.current_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.current_frame.grid_rowconfigure(0, weight=3)
        self.current_frame.grid_rowconfigure(1, weight=1)
        self.current_frame.grid_columnconfigure(0, weight=1)

        node = STORY_NODES[node_id]

        text_box = ctk.CTkTextbox(
            self.current_frame,
            font=ctk.CTkFont(size=20),
            wrap="word",
            state="normal"
        )
        text_box.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        text_box.insert("0.0", node["text"])
        text_box.configure(state="disabled")

        choices_frame = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        choices_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        
        for i in range(3):
            choices_frame.grid_columnconfigure(i, weight=1)

        for idx, choice in enumerate(node["choices"]):
            btn = ctk.CTkButton(
                choices_frame,
                text=choice["text"],
                font=ctk.CTkFont(size=16),
                height=50,
                command=lambda target=choice["target"]: self.handle_choice(target)
            )
            btn.grid(row=idx//2, column=idx%2, padx=10, pady=10, sticky="ew")

    def handle_choice(self, target):
        if target.startswith("ending_"):
            self.show_ending(target)
        else:
            self.show_node(target)

    def show_ending(self, ending_id):
        self.clear_frame()
        ending = ENDINGS[ending_id]
        self.discovered_endings.add(ending_id)

        self.current_frame = ctk.CTkFrame(self)
        self.current_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.current_frame.grid_rowconfigure(0, weight=1)
        self.current_frame.grid_rowconfigure(1, weight=1)
        self.current_frame.grid_rowconfigure(2, weight=1)
        self.current_frame.grid_rowconfigure(3, weight=1)
        self.current_frame.grid_rowconfigure(4, weight=1)
        self.current_frame.grid_columnconfigure(0, weight=1)

        category_label = ctk.CTkLabel(
            self.current_frame,
            text=ending["category"],
            font=ctk.CTkFont(family="Courier", size=32, weight="bold"),
            text_color="#ffaa00"
        )
        category_label.grid(row=0, column=0, pady=(40, 5))

        name_label = ctk.CTkLabel(
            self.current_frame,
            text=ending["name"],
            font=ctk.CTkFont(size=24, weight="bold")
        )
        name_label.grid(row=1, column=0, pady=5)

        result_label = ctk.CTkLabel(
            self.current_frame,
            text=ending["result_text"],
            font=ctk.CTkFont(size=18, slant="italic"),
            wraplength=600,
            justify="center"
        )
        result_label.grid(row=2, column=0, pady=15)

        stats_label = ctk.CTkLabel(
            self.current_frame,
            text=f"You discovered Ending {len(self.discovered_endings)} of {self.total_endings}.\nKeep playing to find them all!",
            font=ctk.CTkFont(size=16),
            justify="center"
        )
        stats_label.grid(row=3, column=0, pady=10)

        replay_btn = ctk.CTkButton(
            self.current_frame,
            text="Replay",
            font=ctk.CTkFont(size=20, weight="bold"),
            height=50,
            width=200,
            command=self.show_home_screen
        )
        replay_btn.grid(row=4, column=0, pady=(20, 40))


STORY_NODES = {
    "start": {
        "text": "You wake up in Dorm 3. The power is out. Only the faint red glow of emergency lights illuminates your room. Suddenly, you hear a slow, rhythmic knocking on your door.\n\nKnock... Knock... Knock...",
        "choices": [
            {"text": "Open the door.", "target": "open_door"},
            {"text": "Look through the peephole.", "target": "peephole"},
            {"text": "Ignore it and go back to sleep.", "target": "ignore"}
        ]
    },
    "ignore": {
        "text": "You pull the covers over your head. The knocking stops. Then, you hear your closet door creak open from the inside. A cold hand grabs your ankle...",
        "choices": [
            {"text": "Accept your fate.", "target": "ending_1"}
        ]
    },
    "open_door": {
        "text": "You swing the door open. The hallway is empty, but the temperature drops drastically. You see wet footprints leading towards the stairwell.",
        "choices": [
            {"text": "Follow the footprints.", "target": "follow_prints"},
            {"text": "Lock the door and stay inside.", "target": "lock_door"},
            {"text": "Check the bathroom across the hall.", "target": "bathroom"}
        ]
    },
    "peephole": {
        "text": "You peer through the peephole. You see yourself staring back, but the 'you' outside has completely black eyes and a twisted smile.",
        "choices": [
            {"text": "Back away slowly.", "target": "back_away"},
            {"text": "Yell 'Who are you?!'", "target": "yell"}
        ]
    },
    "back_away": {
        "text": "You back away from the door. The knocking gets louder, turning into violent banging. The wood begins to splinter.",
        "choices": [
            {"text": "Hide under the bed.", "target": "hide_bed"},
            {"text": "Climb out the window.", "target": "window"}
        ]
    },
    "lock_door": {
        "text": "You quickly lock the door. You feel safe for a moment. But then you realize the wet footprints didn't start outside... they started at your bed and led out.",
        "choices": [
            {"text": "Turn around slowly.", "target": "ending_2"}
        ]
    },
    "follow_prints": {
        "text": "You follow the wet footprints to the stairwell. The lights are completely off here. You can either go down to the basement, or up to the roof.",
        "choices": [
            {"text": "Go down to the basement.", "target": "basement"},
            {"text": "Go up to the roof.", "target": "roof"}
        ]
    },
    "bathroom": {
        "text": "You enter the communal bathroom. The mirrors reflect nothing. Not even you. You touch your face, but you feel nothing. You've become one of them.",
        "choices": [
            {"text": "Stare into the void.", "target": "ending_12"}
        ]
    },
    "yell": {
        "text": "You yell through the door. The thing outside mimics your voice perfectly: 'Who are you?!' Then it laughs. The door unlocks itself with a click.",
        "choices": [
            {"text": "Hold the door shut.", "target": "hold_door"},
            {"text": "Run to the closet to hide.", "target": "hide_closet"}
        ]
    },
    "hide_bed": {
        "text": "You slide under your bed. The door bursts open. Two pale, bare feet walk slowly into your room. They stop right next to your bed. A face drops down to look at you.",
        "choices": [
            {"text": "Scream.", "target": "ending_3"}
        ]
    },
    "window": {
        "text": "You pry the window open and jump. It's a rough landing, but you survive. You run away from Dorm 3, never looking back. But you left your friends behind...",
        "choices": [
            {"text": "Keep running.", "target": "ending_4"}
        ]
    },
    "hold_door": {
        "text": "You throw your weight against the door. The force on the other side is immense. Suddenly, it stops. You wait until morning, too terrified to move.",
        "choices": [
            {"text": "Wait for sunrise.", "target": "ending_5"}
        ]
    },
    "hide_closet": {
        "text": "You dash into the closet and shut the door. You hear footsteps enter the room. They search around, then leave. You stay in the closet until sunrise.",
        "choices": [
            {"text": "Stay quiet.", "target": "ending_6"}
        ]
    },
    "basement": {
        "text": "You slowly descend into the pitch-black basement. The generator is here. You also see a strange figure hunched over it.",
        "choices": [
            {"text": "Try to turn on the generator.", "target": "generator"},
            {"text": "Sneak past the figure.", "target": "maintenance"},
            {"text": "Speak to the figure.", "target": "speak_figure"}
        ]
    },
    "roof": {
        "text": "You climb to the roof. The cold night air hits you. You see a helicopter in the distance, but also shadowy figures crawling up the sides of the building.",
        "choices": [
            {"text": "Signal the helicopter.", "target": "signal"},
            {"text": "Fight the shadows.", "target": "fight_shadows"}
        ]
    },
    "generator": {
        "text": "You rush the generator and pull the lever. The lights blind the figure, which shrieks and disintegrates. The dorm is safe once again.",
        "choices": [
            {"text": "Breathe a sigh of relief.", "target": "ending_7"}
        ]
    },
    "maintenance": {
        "text": "You sneak into the maintenance room and find an old journal. It details dark experiments done in Dorm 3 fifty years ago. You found the truth, but the figure blocks your exit.",
        "choices": [
            {"text": "Read the final page.", "target": "ending_8"}
        ]
    },
    "speak_figure": {
        "text": "You ask the figure what it wants. It turns around, revealing the face of the dorm RA. 'Just fixing the fuse,' he says. The knocking was just the wind. You feel very silly.",
        "choices": [
            {"text": "Apologize.", "target": "ending_11"}
        ]
    },
    "signal": {
        "text": "You wave your phone flashlight. The helicopter spotlights you... and the horde of shadows behind you. They swarm you before help arrives.",
        "choices": [
            {"text": "It's too late.", "target": "ending_9"}
        ]
    },
    "fight_shadows": {
        "text": "You grab a metal pipe from the roof debris and swing at the shadows. You fight valiantly until sunrise, when the shadows melt away. You are battered but victorious.",
        "choices": [
            {"text": "Watch the sunrise.", "target": "ending_10"}
        ]
    }
}

ENDINGS = {
    "ending_1": {
        "category": "Bad Ending", 
        "name": "The Closet Dweller",
        "result_text": "By choosing to ignore the knocking, you left yourself vulnerable. The entity already inside claimed you before you could even scream."
    },
    "ending_2": {
        "category": "Strange Ending", 
        "name": "The Thing Under The Bed",
        "result_text": "Locking the door was a mistake. You focused on the threat outside, completely unaware that the horror had been waiting under your bed all along."
    },
    "ending_3": {
        "category": "Bad Ending", 
        "name": "Found",
        "result_text": "Hiding under the bed provided no safety. The creature's twisted face was the last thing you saw as it dragged you into the darkness."
    },
    "ending_4": {
        "category": "Survival Ending", 
        "name": "Coward's Escape",
        "result_text": "You chose self-preservation over your friends. You survived the night, but the silence from Dorm 3 will haunt your dreams forever."
    },
    "ending_5": {
        "category": "Survival Ending", 
        "name": "The Long Night",
        "result_text": "Through sheer willpower and strength, you held the door shut. The sun finally rose, and the scratching on the other side faded into nothingness."
    },
    "ending_6": {
        "category": "Safe Ending", 
        "name": "Closet Survivor",
        "result_text": "Staying perfectly still in the closet saved your life. The entity roamed your room for hours, eventually leaving when it couldn't find its prey."
    },
    "ending_7": {
        "category": "True Ending", 
        "name": "Bringer of Light",
        "result_text": "Activating the generator flooded the dorm with light, incinerating the shadow creature instantly. You've restored safety to Dorm 3."
    },
    "ending_8": {
        "category": "Mystery Ending", 
        "name": "The Dark History",
        "result_text": "You discovered the truth behind the experiments, but knowledge is a dangerous burden. The figure has trapped you here to ensure the secret dies with you."
    },
    "ending_9": {
        "category": "Bad Ending", 
        "name": "So Close, Yet So Far",
        "result_text": "Your signal for help only served as a beacon for the shadows. Help arrived just in time to find an empty rooftop."
    },
    "ending_10": {
        "category": "Survival Ending", 
        "name": "Shadow Slayer",
        "result_text": "You fought the shadows with everything you had. As the first rays of dawn touched the roof, the creatures vanished, leaving you alone and alive."
    },
    "ending_11": {
        "category": "Strange Ending", 
        "name": "Anti-Climax",
        "result_text": "Your fear was your greatest enemy. The 'monster' was just your RA working late, leaving you to explain your terrified behavior in the morning light."
    },
    "ending_12": {
        "category": "Bad Ending", 
        "name": "The Mirror Realm",
        "result_text": "Checking the bathroom led you into a trap of reflections. You are now a shadow in the glass, watching others live their lives from the other side."
    }
}

if __name__ == "__main__":
    app = StoryApp()
    app.mainloop()
