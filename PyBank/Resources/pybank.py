import os
import csv

csv_path = os.path.join('../Resources/budget_data.csv')



with open(csv_path, newline = '') as csvfile:
        csvreader = csv.reader(csvfile, delimiter =',')
        
        
        Months = 0
        revenue_change = 0
        sum_revenue = 0
        previous_revenue = 0
        total_change = 0
        change_min = 0
        min_month = ""
        max_month = ""
        change_max = 0
        sum_revenue_change = 0
    
        
        row = next(csvreader, None)
        for row in csvreader:



                
                Months = Months + 1
                revenue = float(row[1])
                sum_revenue = sum_revenue + revenue
                revenue_change = revenue - previous_revenue
                sum_revenue_change = sum_revenue_change + revenue_change


                if revenue_change > change_max:
                    max_month = row[0]
                    change_max = revenue_change
                
                if revenue_change < change_min:
                    min_month = row[0]
                    change_min = revenue_change
            
                previous_revenue = revenue 

            
        avg_revenue = sum_revenue/Months
        avg_revenue_change = sum_revenue_change/Months 




        print("Total Months: " , Months)
        print("Total Revenue($): " , sum_revenue)
        print("Average Change($): " , int(avg_revenue_change) )
        print("Greatest Increase in Profits($): " ,max_month, "", change_max)
        print("Greatest Decrease in Profits($): ", min_month, "", change_min)

        output_path = os.path.join("..","output","budget_results.csv")
        with open(output_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(["Results"])
            csvwriter.writerow(["Total Months: " , Months])
            csvwriter.writerow(["Total Revenue ($): " , sum_revenue])
            csvwriter.writerow(["Average change: " , int(avg_revenue_change)])
            csvwriter.writerow(["Greatest Increase in Profits($): " ,max_month, "", change_max])
            csvwriter.writerow(["Greatest Decrease in Profits($): ", min_month, "", change_min])



       