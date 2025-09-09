# North Remembers: A Game of Thrones Data Exploration
I may have arrived late to **Westeros**, but I have journeyed through Game of Thrones—HBO’s epic saga inspired by A Song of Ice and Fire by George R. R. Martin.This project dives into the scripts of the show, seeking to uncover the shifting voices of its characters and the rise and fall of its great houses not through prophecy but through the lens of data and visualization.....



![GoT](./visuals/GoT.jpeg)


## Datasets
This project is based on two datasets, First One **Character Dataset**. This file constitute information about the main characters in the show, including: 
- *Character name*
- *Actor/actress portraying them*
- *Number of episodes they appeared in*
- *Year of first appearance*
- *Year of last appearance*

This dataset helps analyze character presence across the series and compare how long different roles lasted.


**Dataset Source:** [Game of Thrones Character Dataset on Kaggle](https://www.kaggle.com/datasets/rezaghari/game-of-thrones) 

Second One **Script Dataset**. This file contains dialogue transcripts from every episode, with metadata about where and when each line was spoken. The main columns include: 
- *Release date*
- *Season and episode number*
- *Episode title*
- *Character name* 
- *Dialogue line (sentence spoken)*

This dataset allows for dialogue frequency analysis, tracking who spoke the most, and observing character presence across seasons.

**Dataset Source:** [Game of Thrones Script – All Seasons on Kaggle](https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons)
  
Together, these datasets reveal patterns such as Tyrion Lannister’s dominance in dialogue, Jon Snow’s gradual rise, and the shifting balance of power between Starks, Lannisters, Targaryens, and beyond.

## Analysis and Finfings
### 1. The Voices of the Seven Kingdoms
Ever wondered who truly dominates the story of Game of Thrones? Is it Jon Snow, Daenerys Targaryen, or someone else? This analysis examines the top characters by episodes appeared in Game of Thrones, providing insight into who dominated the screen time across Westeros and Essos. One simple way to measure this is by screen presence—the number of episodes a character appears in. 

Let’s take a look at the top 10 characters by episodes appeared.
![GoT](./visuals/top_10_got_characters.png)


**Key Findings**

- *Tyrion Lannister*  – Frequently appearing across many episodes, his wit and schemes make him a central figure in the story.
- *Cersei Lannister*  – A major player in the political games of Westeros, her influence grows as her appearances accumulate over the seasons.
- *Jon Snow* – Steadfast and consistently present, his journey from the Wall to the heart of political intrigue makes him a narrative anchor.
- *Daenerys Targaryen*  – From Essos to Westeros, her dramatic rise is pivotal, though slightly less frequent than the Lannisters or Jon.
- *Other Supporting Characters*  – While appearing less often, they contribute meaningfully to key plot developments and interactions.


By analyzing episode appearances, we see how screen presence is distributed among the characters. Tyrion and the Lannisters (Cersei included) dominate the spotlight, Jon Snow provides a steady narrative backbone, and Daenerys’ appearances highlight her rising influence. Together, the mix of central and supporting characters shapes the rich tapestry of Westeros and Essos.
