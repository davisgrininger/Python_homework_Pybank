import os
import csv

csv_path = os.path.join('../Resources/election_data.csv')

candidates = []
number_of_votes = 0
candidate_vote_count = []



with open(csv_path, newline = '') as csvfile:
        csvreader = csv.reader(csvfile, delimiter =',')

        row = next(csvreader, None)

        for row in csvreader:

            number_of_votes = number_of_votes + 1

            candidate = row[2]

            if candidate in candidates:
                candidateindex = candidates.index(candidate)
                candidate_vote_count[candidateindex] = candidate_vote_count[candidateindex] + 1

            else:
                candidates.append(candidate)
                candidate_vote_count.append(1)
        percentofvotes = []
        maxvotes = candidate_vote_count[0]
        maxindex = 0

        for count in range(len(candidates)):
            vote_percentage = candidate_vote_count[count]/number_of_votes*100
            percentofvotes.append(vote_percentage)
            if candidate_vote_count[count] > maxvotes:
                maxvotes = candidate_vote_count[count]
                print(maxvotes)
                maxindex = count
        winner = candidates[maxindex]


        print(number_of_votes)
        for count in range(len(candidates)):
            print(f"{candidates[count]}: {percentofvotes[count]}% ({candidate_vote_count[count]})")
        print("WINNER: " + winner)



        output_path = os.path.join("..","output","election_results.csv")
        with open(output_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(["Results"])
            csvwriter.writerow(["Total Votes: " , number_of_votes])
            for count in range(len(number_of_votes)):
                csvwriter.write([f"{candidates[count]}: {percentofvotes[count]}% ({candidate_vote_count[count]})"])
            csvwriter.writerow(["Winner: " , winner])



       

    

