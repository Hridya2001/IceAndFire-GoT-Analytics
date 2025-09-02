import pandas as pd
import matplotlib.pyplot as plt
import os

# ------------------------------
# Step 1: Load the dataset
# ------------------------------
df = pd.read_csv("/home/hridya/AwsTasks/TASK15/archive/Game_of_Thrones_Script.csv")

# Clean character names
df['Name'] = df['Name'].str.strip().str.title()

# ------------------------------
# Step 2: Map characters to houses
# ------------------------------
house_mapping = {
    "Stark": ["Eddard Stark", "Arya Stark", "Sansa Stark", "Jon Snow", "Robb Stark", "Bran Stark", "Catelyn Stark"],
    "Lannister": ["Tyrion Lannister", "Cersei Lannister", "Jaime Lannister", "Tywin Lannister", "Joffrey Baratheon"],
    "Targaryen": ["Daenerys Targaryen", "Viserys Targaryen"],
    "Baratheon": ["Robert Baratheon", "Stannis Baratheon", "Renly Baratheon"],
    "Bolton": ["Roose Bolton", "Ramsay Bolton"],
    "Greyjoy": ["Balon Greyjoy", "Theon Greyjoy", "Yara Greyjoy", "Euron Greyjoy"]
}

# ------------------------------
# Step 3: Assign house to characters
# ------------------------------
def get_house(name):
    for house, members in house_mapping.items():
        if name in members:
            return house
    return None

df['House'] = df['Name'].apply(get_house)

# Keep only known houses
df = df[df['House'].notnull()]

# ------------------------------
# Step 4: Count dialogues per house per season
# ------------------------------
house_season_count = df.groupby(['Season', 'House']).size().reset_index(name='Dialogue_Count')

# ------------------------------
# Step 5: Define house colors
# ------------------------------
colors = {
    "Stark": "#1E90FF",      # Blue
    "Lannister": "#B22222",  # Red
    "Targaryen": "#FF0000",  # Bright red
    "Baratheon": "#FFD700",  # Golden yellow
    "Bolton": "#800000",     # Dark blood red
    "Greyjoy": "#DAA520",    # Goldenrod
}

# ------------------------------
# Step 6: Plot trends
# ------------------------------
plt.style.use("dark_background")
plt.figure(figsize=(12,7))

for house in house_mapping.keys():
    data = house_season_count[house_season_count['House'] == house]
    plt.plot(
        data['Season'],
        data['Dialogue_Count'],
        marker='o',
        linewidth=2.5,
        markersize=8,
        label=house,
        color=colors.get(house, "white")  # FIXED
    )

# Title and labels
plt.title("Game of Thrones – Dialogue Trends of Noble Houses",
          fontsize=18, fontweight="bold", color="gold", family="serif")
plt.xlabel("Season", fontsize=14, fontweight="bold", color="w", family="serif")
plt.ylabel("Dialogue Count", fontsize=14, fontweight="bold", color="w", family="serif")

plt.xticks(fontsize=10, family="serif")
plt.yticks(fontsize=10, family="serif")

# Grid
plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)

# Legend
plt.legend(
    facecolor="black",
    edgecolor="gold",
    fontsize=12,
    title="Houses",
    title_fontsize=13
)

# Save and show
output_file = os.path.join(os.getcwd(), "got_house_trends_dark.png")
plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.show()
