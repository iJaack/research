# Description
A script to run some analysis on the RetroPGF Round 3 voting data.

It has been built to make a competitor analysis on Routescan's competitors, but it can be applied on any other project.

The '77,0000' amount is the amount Jesse Pollak, creator of Base, suggested for the Routescan product in his RetroPGF list published in early November 2023.

The basic goal is to analyse how much Badgeholders were aligned on the amounts proposed in that list, and how that may influence future RetroPGF Rounds.

Current data points produced:
- Project name
- Votes: the complete array of votes
- Total votes: the sum of votes in the **Votes** array
- Average Vote
- Max Vote
- Min Vote
- Median Vote
- Number of votes
- Zero Votes Count
- '77,000' Votes count: number of votes with the 77,000 amount
- Sub-25,000 Votes Count
- Zero Votes Percentage
- '77,000' Votes Percentage
- Sub-25,000 Votes Percentage
- Median Deviation from '77,000'
- Average Deviation from '77,000'

You can either modify the `keywords_to_filter` array with 

# Instructions
The script requires `panda` to write the output onto an excel file.

`pip install panda`

`python3 rpgf3-analysis.py`