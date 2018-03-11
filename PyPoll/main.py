import pandas as pd
import csv

df = pd.read_csv("election_data_1.csv")

total_votes = sum(pd.value_counts(df['Voter ID']))

winner = df['Candidate'].value_counts().idxmax()

votes_count = df['Candidate'].value_counts()
votes_percentage = (votes_count / total_votes * 100).astype(str) + '%'

summary = pd.concat([votes_percentage, votes_count], axis = 1).to_string(header = False)

# Print results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(summary)
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#Export data to text file
election_results = {
    'Total_Votes:': [total_votes],
    'Summary:': [summary],
    'Winner:': [winner]
    }

election_results = pd.DataFrame(data=election_results).T
election_results.to_csv("election_results.txt", sep = ' ' ,header = False)