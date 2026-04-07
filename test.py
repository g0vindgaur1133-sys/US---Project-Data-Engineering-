import requests

url = "https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_2021_5.zip"
response = requests.get(url, stream=True)

print( response)
print( response.headers)


with open("test.zip", mode="wb") as file:
    for chunk in response.iter_content(chunk_size=1024 * 1024):
        file.write(chunk)