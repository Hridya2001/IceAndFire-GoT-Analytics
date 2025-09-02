import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Step 1: Load and process data
# ------------------------------
df = pd.read_csv("/home/hridya/AwsTasks/TASK15/archive/Game_of_Thrones_Script.csv")

# Clean character names
df['Name'] = df['Name'].str.strip().str.title()

# Remove rows with missing values
df = df.dropna(subset=['Season', 'Name', 'Sentence'])

# Remove duplicates
df = df.drop_duplicates()

# Convert Season to numeric
df['Season_Num'] = df['Season'].str.extract('(\d+)').astype(int)

# ------------------------------
# Step 1a: Select top 11 characters overall
# ------------------------------
top_characters_overall = df.groupby('Name')['Sentence'].count().nlargest(11).index
plot_data = df[df['Name'].isin(top_characters_overall)]

# Count dialogues per character per season
plot_data = plot_data.groupby(['Season_Num', 'Name']).size().unstack(fill_value=0)

# ------------------------------
# Step 2: Visualization
# ------------------------------
plt.style.use('dark_background')
plt.figure(figsize=(12,6))

# Use distinct colors
# Use a colormap with more colors
colors = plt.cm.tab20.colors  # 20 distinct colors

for i, character in enumerate(plot_data.columns):
    plt.plot(
        plot_data.index, 
        plot_data[character], 
        marker='o', 
        linewidth=2, 
        alpha=0.8, 
        label=character, 
        color=colors[i]  # no need for modulo since tab20 has 20 colors
    )

# Styling
plt.xlabel('Season', fontsize=14, fontname='Garamond', color='#F5F5F5')
plt.ylabel('Number of Dialogues', fontsize=14, fontname='Garamond', color='#F5F5F5')
plt.title('Season-wise Character Presence', fontsize=18, fontweight='bold', fontname='Garamond', color='#F5F5F5')

# Move legend outside
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.grid(True, color='gray', linestyle='--', alpha=0.3)
plt.tight_layout()

# Save and show plot
plt.savefig("season_wise_top11_characters.png", dpi=300, bbox_inches='tight')
plt.show()
