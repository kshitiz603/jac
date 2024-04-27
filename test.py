import requests
import csv
from bs4 import BeautifulSoup

filename = "new.csv"
f = open(filename, 'w')

# Define the URL and payload
url = "https://www.jacresults.com/sec-all/show_result.php"
for i in range(32001, 32200):
    for x in range(1,202):
        payload = {
        "rollcode": i,
        "rollno": "000"+str(x),
        "B1": "Submit"
        }

        # Send the POST request with allow_redirects=True to follow redirects
        response = requests.post(url, data=payload, allow_redirects=True)
    

        # Check if the request was successful
        if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table containing the data you want
            table = soup.find("table")
        
            if table:
            # Iterate through rows in the table
                for row in table.find_all("tr"):
                # Initialize an empty list to store column data
                    column_data = []
                
                # Iterate through columns in each row
                    columns = row.find_all("td")
                
                # Extract and append the data in each column to column_data
                    for column in columns:
                        column_text = column.text.strip() if column.text else ""  # Handle None values
                        column_data.append(column_text)
                
                # Print the row's data as a comma-separated string
                    row_data = ",".join(column_data)
                    f.write(row_data + " \n")
                    print(row_data +" \n")
            
                
            else:
                print("Table not found on the page." + str(i))
        else:
            print("Failed to retrieve data. Status code:", response.status_code)
