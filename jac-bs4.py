import requests
from bs4 import BeautifulSoup

# Creating a CSV file
filename = "jac.csv"

# Open the CSV file to write
with open(filename, 'w') as f:
    # Create a header in the file (if needed)

    # Put range of roll numbers
    for i in range(10001, 10302):
        try:
            # Set up the URL
            url = "https://www.jacresults.com/cls-eleven-2023/index.php"

            # Create a session to maintain cookies
            with requests.Session() as session:
                # Make an HTTP GET request
                response = session.get(url)

                # Parse the HTML content with Beautiful Soup
                soup = BeautifulSoup(response.text, 'html.parser')

                # Put roll code using XPath
                rollcode_input = soup.find('input', {'xpath': '/html/body/form/div/div/div/div/div[1]/table/tbody/tr[1]/td[2]/input'})
                rollcode_input['value'] = '32010'

                # Put roll number using XPath
                rollnumber_input = soup.find('input', {'xpath': '/html/body/form/div/div/div/div/div[1]/table/tbody/tr[2]/td[2]/input'})
                rollnumber_input['value'] = str(i)

                # Submit the form using XPath
                submit_button = soup.find('button', {'xpath': '/html/body/form/div/div/div/div/div[2]/div[1]/button'})
                response = session.post(url, data=soup.find('form').attrs)

                # Parse the updated HTML content
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract student name using XPath
                name_element = soup.find('p', {'xpath': '/html/body/div[1]/form/div/div/div[2]/table[1]/tbody/tr[3]/td/p'})
                name = name_element.text if name_element else "Name not found"

                # Extract roll code using XPath
                code_element = soup.find('span', {'xpath': '/html/body/div[1]/form/div/div/div[2]/table[1]/tbody/tr[1]/th[1]/span[2]'})
                code = code_element.text.strip() if code_element else "Code not found"

                # Extract roll number
                roll = str(i)

                # Write all details to the file
                f.write(f"{name},{roll},{code}\n")
                print(f"Scraped: Name={name}, Roll={roll}, Code={code}")

        except Exception as e:
            print(f"Error for Roll {i}: {str(e)}")
            continue
