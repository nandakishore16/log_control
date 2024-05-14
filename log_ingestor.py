import json
import requests
from configparser import ConfigParser

class LogIngestor:
    def __init__(self, config_file):
        self.config = ConfigParser()
        self.config.read(config_file)

    def ingest_log(self, api_url, log_data):
        response = requests.post(api_url, json=log_data)
        if response.status_code == 200:
            print(f"Log from {api_url} ingested successfully!")
        else:
            print(f"Error ingesting log: {response.text}")

    def run(self):
        apis = self.config.sections()
        for api_name in apis:
            api_url = self.config[api_name].get('url')
            source_file = self.config[api_name].get('source_file')

            # Simulate reading log data from each API
            log_data = {
                "level": "info",
                "log_string": f"Sample log message from {api_name}",
                "timestamp": "2024-05-17T00:00:00Z",
                "metadata": {
                    "source": source_file
                }
            }

            # Write log data to the corresponding file
            with open(source_file, "a") as log_file:
                json.dump(log_data, log_file)

            # Simulate sending log to external system (optional)
            self.ingest_log(api_url, log_data) # Replace with actual API call if needed

if __name__ == "__main__":
    config_file = "config.ini"
    ingestor = LogIngestor(config_file)
    ingestor.run()



def search_logs(filename):
    search_term = input("Enter your search term: ")
    logs = read_logs(filename) # Function from step 4

    matching_logs = []
    for log in logs:
        if search_term.lower() in log["log_string"].lower():
            matching_logs.append(log)

    if matching_logs:
        for log in matching_logs:
            print(json.dumps(log, indent=2)) # Pretty-print JSON output
    else:
        print("No matching logs found.")


if __name__ == '__main__':
    filename = 'log1.log' # Modify as needed
    search_logs(filename)
