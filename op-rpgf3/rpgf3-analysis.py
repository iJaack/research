import csv
import ast
import pandas as pd

def analyze_votes_from_csv(file_path, keywords, output_excel_path):
    data_list = []
    total_votes_list = []
    total_zero_votes = 0
    total_77000_votes = 0
    total_sub_25000_votes = 0
    
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # Check if the row has enough columns
            if len(row) >= 3:
                try:
                    project_name = row[0]
                    
                    # Check if project_name contains any of the specified keywords
                    if any(keyword.lower() in project_name.lower() for keyword in keywords):
                        votes_str = row[1]
                        num_votes = int(row[2])

                        # Convert the string representation of the votes array to a Python list
                        votes_list = ast.literal_eval(votes_str)

                        # Calculate various statistics on the votes
                        total_votes = sum(votes_list)
                        average_vote = total_votes / num_votes
                        max_vote = max(votes_list)
                        min_vote = min(votes_list)

                        # Count the number of 0 votes
                        zero_votes_count = votes_list.count(0)

                        # Count the number of 77000 votes
                        votes_77000_count = votes_list.count(77000)

                        # Count the number of sub-25000 votes
                        sub_25000_count = sum(1 for vote in votes_list if vote < 25000)

                        # Update total counts
                        total_zero_votes += zero_votes_count
                        total_77000_votes += votes_77000_count
                        total_sub_25000_votes += sub_25000_count

                        # Append data to the list
                        data_list.append({
                            'Project': project_name.strip(),
                            'Votes': votes_list,
                            'Total Votes': total_votes,
                            'Average Vote': average_vote,
                            'Max Vote': max_vote,
                            'Min Vote': min_vote,
                            'Median Vote': pd.Series(votes_list).median(),
                            'Number of Votes': num_votes,
                            'Zero Votes Count': zero_votes_count,
                            '77000 Votes Count': votes_77000_count,
                            'Sub-25000 Votes Count': sub_25000_count
                        })

                except (ValueError, SyntaxError) as e:
                    print(f"Error processing row: {row}. {e}")
            else:
                print("Invalid row format: ", row)

    # Calculate percentages
    total_projects = len(data_list)
    percentage_zero_votes_total = (total_zero_votes / sum(total_votes_list)) * 100 if sum(total_votes_list) > 0 else 0

    # Add new columns for percentages
    for data in data_list:
        data['Percentage Zero Votes'] = (data['Zero Votes Count'] / data['Number of Votes']) * 100 if data['Number of Votes'] > 0 else 0
        data['Percentage 77000 Votes'] = (data['77000 Votes Count'] / data['Number of Votes']) * 100 if data['Number of Votes'] > 0 else 0
        data['Percentage Sub-25000 Votes'] = (data['Sub-25000 Votes Count'] / data['Number of Votes']) * 100 if data['Number of Votes'] > 0 else 0
        data['Median Deviation from 77000'] = data['Median Vote'] - 77000
        data['Average Deviation from 77000'] = data['Average Vote'] - 77000

    # Create a DataFrame from the list of data
    df = pd.DataFrame(data_list)

    # Write the DataFrame to an Excel file
    df.to_excel(output_excel_path, index=False)
    print(f"Data written to {output_excel_path}")

# Specify the keywords to filter projects
keywords_to_filter = [
    'Conduit', 'Ethereum Attestation Service', 'Gelato',
    'L2BEAT', 'OPChainList', 'OpTracker', 'Otterscan',
    'Revoke.cash', 'Superscan', 'Tenderly', 'beaconcha.in', 
    'Blockscout', 'DefiLlama', 'Optimistic Indexer'
]

# Example usage with a CSV file named 'votes_data.csv' and output Excel file 'output_data.xlsx'
file_path = 'votes_data.csv'
output_excel_path = 'output_data.xlsx'
analyze_votes_from_csv(file_path, keywords_to_filter, output_excel_path)
