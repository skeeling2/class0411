#Two ways to create dictionary
actors = {}

actors_x = dict()

actors = {"name": "Clint Eastwood"}
print(actors) #print whole dictionary
print(actors["name"]) #print by name

actors["name"] = "Frank Sinatra" #replace Clint with Frank
print(actors["name"])

actors["name"] = [
    "Tom Cruise"
    "Angelina Jolie"
    "Kristen Stewart"]
print(actors["name"]) #print dictionary

print(actors["name"][2]) #print Krsiten Stewart

actress = {"name": "Angie",
            "genre": "Action"} #multiple keys in dictionary

    #can mix strings, integers, booleans, etc in dictionary

film = {
    "title": "Interstellar",
    "revenues": {
    "United States": 360,
    "China": 250,
    "UK": 73}
}

print(film["revenues"]["United States"]) #get US revenue value