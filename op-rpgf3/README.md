# Description
A script to run some analysis on the RetroPGF Round 3 voting data.

It has been built to make a competitor analysis on Routescan's competitors, but it can be applied on any other project.

The '77,0000' amount is the amount Jesse Pollak, creator of Base, suggested for the Routescan product in his [RetroPGF list published in early November 2023](https://docs.google.com/spreadsheets/d/13_omIPXbvEukklwIVK2lm-lbf1W3BfQEOfRxWp6ij5k/edit?usp=sharing).

The basic goal is to analyse how much Badgeholders were aligned on the amounts proposed in that list, and how lists in general may influence future RetroPGF Rounds.

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
- Sub-25,000 Votes Count: votes whose amount is lower than 25,000
- Zero Votes Percentage
- '77,000' Votes Percentage
- Sub-25,000 Votes Percentage
- Median Deviation from '77,000': deviation from the median vote amount
- Average Deviation from '77,000': deviation from the average vote amount

You can either modify the `keywords_to_filter` array with your keywords (project names) of choice, or remove it entirely to analyse the whole data set of RetroPGF3 recipients.

# Instructions
The script requires `panda` to write the output onto an excel file.

`pip install panda`

`python3 rpgf3-analysis.py`

curl -sX POST --data '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"info.acps",
    "params" :{}
}' -H 'content-type:application/json;' internal-avascan-mainnet-alb-avalanche-776684637.us-east-2.elb.amazonaws.com:9650/ext/info