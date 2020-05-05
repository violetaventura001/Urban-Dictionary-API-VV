import requests, os, sys

# Retrieve your API credentials from the .env file
if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)

# Get credentials from the .env file
API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")

# continue with your application here
def sync_word(_word,_permission):
    text_file = open("./src/"+ _word + ".txt",_permission)
    if _permission =="w+": 
        text_file.write(body["list"][0]["definition"])
    else:
        return text_file.read()
    text_file.close()

word = ""

if len(sys.argv) ==1:
    word = input("What term do you want to look for?")
else:
    word = sys.argv[1]

if os.path.isfile("./src/"+ word + ".txt"):
    print("fetching")
    print(sync_word(word,"r"))
else:
    
querystring = {"term":"wat"}

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "8c88dd91bcmsh459684562c9ed27p1f7bd8jsn98ac2e72f8d9"
}

response = requests.get(API_HOST, headers=headers, params=querystring)
body = response.json()

print(body["list"][0]["definition"])