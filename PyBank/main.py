# The total number of months included in the dataset 
# The total amount of revenue gained over the entire period
# The average change in revenue between months over the entire period
# The greatest increase in revenue (date and amount) over the entire period
# The greatest decrease in revenue (date and amount) over the entire period

# Print results 
# Export into CSV

import pandas as pd


df = pd.read_csv("budget_data_2.csv")
df['MoM'] = df['Revenue'] - df['Revenue'].shift(+1)

total_months = sum(pd.value_counts(df['Date']))
total_revenue = '${:.0f}'.format(df['Revenue'].sum())
average_revenue_change = '${:.0f}'.format(df['MoM'].mean())
greatest_revenue_increase = '${:.0f}'.format(df['MoM'].max())
greatest_revenue_decrease = '${:.0f}'.format(df['MoM'].min())

greatest_revenue_increase_month = df[['Date']][df.MoM == df.MoM.max()].to_string(header = False, index = False)
greatest_revenue_decrease_month = df[['Date']][df.MoM == df.MoM.min()].to_string(header = False, index = False)

# Print output directly
print("Financial Analysis")
print("------------------------------------------------")
print("Total months: " + str(total_months))
print("Total revenue: " + str(total_revenue))
print("Average revenue change: " + str(average_revenue_change))
print("Greatest increase in revenue: " + greatest_revenue_increase_month + " (" + str(greatest_revenue_increase) + ")")
print("Greatest decrease in revenue: " + greatest_revenue_decrease_month + " (" + str(greatest_revenue_decrease) + ")")

# Export data to text file
df_analysis = {
    "Total_months:": [total_months, ""], 
    "Total_revenue:": [total_revenue, ""], 
    "Average_revenue_change:": [average_revenue_change, ""],
    "Greatest_increase_in_revenue:": [greatest_revenue_increase_month, greatest_revenue_increase],
    "Greatest_decrease_in_revenue:": [greatest_revenue_decrease_month, greatest_revenue_decrease]
    }

df_analysis = pd.DataFrame(data=df_analysis).T
df_analysis.to_csv("financial_analysis.txt", sep=' ', header = False)