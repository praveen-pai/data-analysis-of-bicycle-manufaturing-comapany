# Import necessary Python libraries
import pyodbc                          # For connecting to a SQL Server database
import pandas as pd                    # For working with data in tabular format (DataFrames)
import matplotlib.pyplot as plt        # For creating graphs and visualizations
import numpy as np                     # For numerical operations like correlation and linear regression

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')  # Trusted connection uses Windows credentials

# Read the SQL query from the file into a string
query = open('SQL Queries/Q6 - Store Size Num Employees and Revenue.sql').read()

# Run the SQL query and store the result in a Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Get the unique AnnualRevenue values and sort them
categories = list(set(df['AnnualRevenue']))
categories.sort()

### GRAPH 1: Annual Revenue by Store Size ###
for x in categories:
    # Filter data for each revenue category
    df_1 = df[df['AnnualRevenue'] == x]
    # Plot a scatter point for Store Size vs Revenue
    plt.scatter(df_1['SquareFeet'], df_1['AnnualRevenue'])

# Fit a linear regression line (best fit line)
a, b = np.polyfit(df['SquareFeet'], df['AnnualRevenue'], 1)
# Calculate the correlation coefficient (how strongly related size and revenue are)
c = round(np.corrcoef([df['SquareFeet'], df['AnnualRevenue']])[0, 1], 3)

# Plot the line of best fit in grey
plt.plot(df['SquareFeet'], a * df['SquareFeet'] + b, c='grey', label=f'line of best fit (c = {c}', linestyle='--')

# Customize x-axis ticks with square footage and labels
plt.xticks(ticks=[0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000], 
           labels=['0', '10 000 ft$^{2}$', '20 000 ft$^{2}$', '30 000 ft$^{2}$', '40 000 ft$^{2}$', 
                   '50 000 ft$^{2}$', '60 000 ft$^{2}$', '70 000 ft$^{2}$', '80 000 ft$^{2}$'],
           rotation=20)

# Customize y-axis revenue ticks
plt.yticks(ticks=[0, 50000, 100000, 150000, 200000, 250000, 300000], 
           labels=['$0K', '$50K', '$100K', '$150K', '$200K', '$250K', '$300K'])

plt.xlabel('Store Size')                  # Label x-axis
plt.ylabel('Annual Revenue')              # Label y-axis
plt.title("Annual Revenue by Store Size") # Title of graph
plt.grid(linestyle='--', linewidth=0.5)   # Add a grid
plt.legend()                              # Show legend
plt.tight_layout()                        # Automatically adjusts layout
plt.show()                                # Show the graph
plt.clf()                                 # Clear the figure for next plot

### GRAPH 2: Annual Revenue by Number of Employees ###
for x in categories:
    df_1 = df[df['AnnualRevenue'] == x]
    plt.scatter(df_1['NumberEmployees'], df_1['AnnualRevenue'])

# Calculate correlation and best fit line between employees and revenue
c = round(np.corrcoef([df['NumberEmployees'], df['AnnualRevenue']])[0, 1], 3)
a, b = np.polyfit(df['NumberEmployees'], df['AnnualRevenue'], 1)

# Plot best fit line
plt.plot(df['NumberEmployees'], a * df['NumberEmployees'] + b, c='grey', label=f'line of best fit (c = {c}', linestyle='--')

# Customize y-axis revenue ticks
plt.yticks(ticks=[0, 50000, 100000, 150000, 200000, 250000, 300000], 
           labels=['$0K', '$50K', '$100K', '$150K', '$200K', '$250K', '$300K'])

plt.xlabel('Number of Employees')              # Label x-axis
plt.ylabel('Annual Revenue')                   # Label y-axis
plt.title("Annual Revenue by Number of Employees")  # Title
plt.grid(linestyle='--', linewidth=0.5)        # Grid lines
plt.legend()                                   # Show legend
plt.tight_layout()                             # Adjust layout
plt.show()                                     # Show the plot
plt.clf()                                      # Clear figure

### GRAPH 3: Number of Employees by Store Size ###
for x in categories:
    df_1 = df[df['AnnualRevenue'] == x]
    plt.scatter(df_1['SquareFeet'], df_1['NumberEmployees'], label=f'${round(x/1000)}K')  # Add label by revenue

# Customize x-axis ticks
plt.xticks(ticks=[0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000], 
           labels=['0', '10 000 ft$^{2}$', '20 000 ft$^{2}$', '30 000 ft$^{2}$', '40 000 ft$^{2}$', 
                   '50 000 ft$^{2}$', '60 000 ft$^{2}$', '70 000 ft$^{2}$', '80 000 ft$^{2}$'],
           rotation=20)

plt.xlabel('Store Size')                         # Label x-axis
plt.ylabel('Number of Employees')                # Label y-axis
plt.title("Number of Employees by Store Size")   # Graph title
plt.grid(linestyle='--', linewidth=0.5)          # Add grid
plt.legend(title='Colours = Yearly Revenue')     # Add legend with title

# Add manual annotations (text) to specific points
plt.text(x=5000.5, y=12, s='$30K', c='tab:blue')
plt.text(x=15000.5, y=3, s='$80K', c='tab:orange')
plt.text(x=22000.5, y=32, s='$100K', c='tab:green')
plt.text(x=33000.5, y=24, s='$150K', c='tab:red')
plt.text(x=64000, y=90, s='$300K', c='tab:purple')

plt.tight_layout()    # Automatically adjust spacing
plt.show()            # Show the final graph
