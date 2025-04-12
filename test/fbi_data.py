import requests

def get_fbi_data(api_key):
    # Base URL for the FBI Crime Data API
    base_url = "https://api.usa.gov/crime/fbi/cde"
    
    # Here’s one endpoint example:
    # Summarized data for a specific agency (e.g., "CO0131300") from 2010 to 2019.
    # You can adjust these parameters to whatever endpoint you need.
    endpoint = "summarized/agencies/CO0131300/offenses/2010/2019"
    
    # Construct the full URL by combining base URL and endpoint
    url = f"{base_url}/{endpoint}"
    url = "https://api.usa.gov/crime/fbi/cde/arrest/state/IN/60?type=counts&from=04-2000&to=03-2025&API_KEY=2g5gsqeOnHbldYcsmM9Wf1dSARMa5s9DRQYgJw78"
    
    # Some APIs require an 'API_KEY' query parameter; 
    # The FBI Crime Data API supports passing the key either as a query param (?API_KEY=xxxx)
    # or in the request headers as well. For simplicity, we’ll use a query param:
    params = {
        'API_KEY': api_key
    }
    
    try:
        response = requests.get(url)
        # Raise HTTPError if the response status code is 4xx or 5xx
        response.raise_for_status()
        
        data = response.json()
        print("Successfully fetched data!")
        print(data)
        return data
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Replace 'YOUR_API_KEY' with your actual key from https://api.data.gov/signup.
my_api_key = "2g5gsqeOnHbldYcsmM9Wf1dSARMa5s9DRQYgJw78"
get_fbi_data(my_api_key)
