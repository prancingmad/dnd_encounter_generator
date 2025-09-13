from .config import *
from .gui_functions import *
from .show_error import show_error

bestiary_flag = "archive"

from .config import *

class Monster():
    def __init__(self, name, challenge_rating):
        self.name = name
        self.challenge_rating = challenge_rating

    def to_dict(self):
        enemy_dict = {}
        enemy_dict["name"] = self.name
        enemy_dict["challenge_rating"] = self.challenge_rating
        return enemy_dict

    def save_to_file(self):
        global bestiary_flag
        if bestiary_flag == "archive":
            file_path = ARCHIVE_FILE_PATH
        monster_list = []
        if os.path.exists(PARTY_FILE_PATH):
            with open(PARTY_FILE_PATH, "r") as f:
                content = f.read().strip()
                if content:
                    players_list = json.loads(content)
        player_dict = self.to_dict()
        players_list.append(player_dict)
        with open(PARTY_FILE_PATH, "w") as f:
            json.dump(players_list, f, indent=4)

def archive_page(root, left_frame, right_frame):
    clear_widgets(left_frame)
    clear_widgets(right_frame)
    global bestiary_flag
    bestiary_flag = "archive"

    scroll_frame = create_scrollable_frame(left_frame)
    with open(ARCHIVE_FILE_PATH, "r") as f:
        content = f.read().strip()
        if content:
            f.seek(0)
            archive_data = json.load(f)

            for creature in archive_data:
                creature_text = f"{creature['name']} - Challenge Rating: {creature['challenge_rating']}"
                label = tk.Label(scroll_frame, text=creature_text, anchor="w", justify="left")
                label.pack(fill="x", pady=2)
        else:
            placeholder_label = tk.Label(left_frame, text="", anchor="nw", justify="left")
            placeholder_label.pack(fill=tk.BOTH, expand=True)

    button_frame = tk.Frame(right_frame)
    button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    for label in ARCHIVE_BUTTON_LABELS:
        btn = tk.Button(button_frame, text=label, command=lambda l=label: on_button_click(l, root, left_frame, right_frame))
        btn.pack(**BUTTON_PACK_OPTIONS)

def add_monster(root, left_frame=None, right_frame=None):
    global bestiary_flag
    if bestiary_flag == "archive":
        add_monster_flag = ARCHIVE_FILE_PATH

    popup = tk.Toplevel(root)
    popup.title(f"Add New Monster to {bestiary_flag}")

    result = {"data": None}

    instr_label = tk.Label(popup, text="Adding a monster.")
    instr_label.pack(pady=10)

    def on_submit():
        name_val = name_entry.get()
        cr_val = cr_entry.get()

        for key, value in [("Name", name_val), ("Challenge Rating", cr_val)]:
            if value.strip() == "":
                show_error("Missing a Value.", root)
                return

        monster_list = []
        if os.path.exists(add_monster_flag):
            with open(add_monster_flag, "r") as f:
                content = f.read().strip()
                if content:
                    monster_list = json.loads(content)

        for mon in monster_list:
            if mon["name"] == name_val:
                show_error(f"Monster already exists in {bestiary_flag}", root)
                return

        new_monster = Monster(name_val, cr_val)

