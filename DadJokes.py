import figlet as fig, requests as req
from random import choice

def dadJokeSearch(searchterm):
    url = "https://icanhazdadjoke.com/search"
    res = req.get(
            url,
            headers={"Accept": "application/json"},
            params={"term": searchterm}
    )
    data = res.json()
    jokes = [elem["joke"] for elem in data["results"]]
    output = "Found {} jokes on {}".format(len(jokes), searchterm)
    if len(jokes) > 0:
        output += " here is one: \n{}".format(choice(jokes))
    return output
    

if __name__ == "__main__":
    fig.printfig("Dad Jokes 5000")
    while True:
        topic = input("Enter a topic > ")
        if topic == "stop" or len(topic) == 0:
            break
        print(dadJokeSearch(topic))