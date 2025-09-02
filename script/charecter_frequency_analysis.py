import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("/home/hridya/AwsTasks/TASK15/archive/characters.csv")

# Show first 5 rows
# print(df.head())
# print(df.info())      # check datatypes and null counts
# print(df.isnull().sum())  # check missing values

# From the output: I dataset has 832 rows. Character column has 13 missing values, all other columns are complete. 
# The other columns (Actor/ess, Episodes_appeared, First_appearance, Last_appearance) are fine.


# cleaning
# --------
# Fill missing Character names with 'Unknown'
df['Character'] = df['Character'].fillna('Unknown')

# Remove leading/trailing spaces
df['Character'] = df['Character'].str.strip()

# Standardize capitalization (Title Case)
df['Character'] = df['Character'].str.title()

# Similarly, clean Actor/ess column just in case
df['Actor/ess'] = df['Actor/ess'].str.strip().str.title()

# Check again
print(df.head())
print(df.isnull().sum())



# Sort characters by Episodes_appeared in descending order
top_characters = df.sort_values(by='Episodes_appeared', ascending=False)
# Take top 10 characters
top_10 = top_characters.head(10)


# Plotting
# --------
# Set dark background style
plt.style.use('dark_background')

# Create figure with dark facecolor
fig, ax = plt.subplots(figsize=(12,6))
fig.patch.set_facecolor('#1C1C1C')  # dark background

# Bar colors: top character in gold, others in dark red
colors = ['#FFD700'] + ['#8B0000'] * (len(top_10)-1)

# Plot bars with edge color
bars = ax.bar(top_10['Character'], top_10['Episodes_appeared'], 
              color=colors, edgecolor='#DAA520')

# Labels and title
ax.set_xlabel('Character', fontsize=14, fontname='Garamond', color='#F5F5F5')
ax.set_ylabel('Episodes Appeared', fontsize=14, fontname='Garamond', color='#F5F5F5')
ax.set_title('Top 10 Game of Thrones Characters by Episodes Appeared', 
             fontsize=18, fontweight='bold', fontname='Garamond', color='#F5F5F5')

# Rotate x-axis labels for readability
plt.xticks(rotation=45, fontsize=12, fontname='Garamond', color='#F5F5F5')

# Grid for subtle reference
ax.grid(True, color='gray', linestyle='--', alpha=0.3)


# Save the figure
plt.tight_layout()  # Adjust layout so labels don't get cut off
plt.savefig('top_10_got_characters.png', dpi=300)  # Save as PNG with high resolution
plt.show()
