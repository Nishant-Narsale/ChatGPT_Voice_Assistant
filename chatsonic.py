import requests
import re


url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"

def command(question):
    payload = {"input_text": question, "enable_memory": True, "enable_google_results": True}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": ""
    }

    response = requests.post(url, json=payload, headers=headers)

    res = response.json()['message']
    res = res.split('<')
    result = re.sub(r'\[.*?\]', '', res[0])
    return result

if __name__=="__main__":
    print(command("Explain quantum computing in simple terms"))