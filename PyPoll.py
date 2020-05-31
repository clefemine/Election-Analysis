# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
#Challenge county options and county votes
county_names = []
county_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Challenge Track the Largest county voter turnout and its percentage
largest_county_turnout = ""
largest_county_votes = 0
largest_county_percentage = 0

# Read csv and convert to list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read header
    header = next(reader)
    
    # for each row in the csv file
    for row in reader:
        #add to the total votes count
        total_votes = total_votes + 1

        # Get the candidate name from each row
        candidate_name = row[2]

        # Get county name from each row
        county_name = row[1]

        # if the candidate does not match any existing candidate add it into the lis
        if candidate_name not in candidate_options:
            #add candidate name to candidate list
            candidate_options.append(candidate_name)
            # begin tracking candidate voter count
            candidate_votes[candidate_name] = 0
        #add a  vote to that candidate count
        candidate_votes[candidate_name] += 1

       #Challenge add Counties
        if county_name not in county_names:
           # add to the list in running
            county_names.append(county_name)

           #tracking that candidate voter count
            county_votes[county_name] = 0
        # add a vote to the candidate count
        county_votes[county_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as text_file:
    # Print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"\n-------------------------\n"
        f"Total Votes: {total_votes:,}"
        f"\n-------------------------\n\n"
        f"County Votes:\n"
    )
    print(election_results, end="")
    text_file.write(election_results)
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)