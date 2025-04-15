import requests
import json
import sys


# Main function: Greets and runs other functions
def main():

    # Gathers a list of ingredients to use in the get_recipe() function
    print(
        "Please provide 1-3 ingredients for me to cross reference recipes with.\nWhen you are done entering ingredients, input 'Done'"
    )
    ingredients = []
    while True:
        item = input("Ingredient: ").strip().lower()
        if item == "done":
            break
        ingredients.append(item)

    # Checks whether a tag exists for cross referencing in the get_recipe() function
    print(
        "Please provide 1-3 tags for me to cross reference recipes with.\nWhen you are done entering tags, input 'Done'"
    )
    tags = []
    while True:
        tag = input("Tag: ").strip().lower()
        if tag == "done":
            break
        tags.append(get_tags(tag))

    get_recipe(ingredients, tags)

    print(
        "Alright, well, you've exhausted all the options I could come up with. Try new filters in your next search! Goodbye!"
    )
    # print("Alright, well, you've exhausted all the options I could come up with. I only see one other course of action to take...")
    # get_tacobell() #API IS MAXED OUT FOR MARCH


# Returns a list of recipes with more input specifiers than resipes autocomplete
def get_recipe(items, tags):
    id = 0
    headers = {
        "x-rapidapi-key": "4e6e1cddd9mshda2c9866c14b313p1b1b08jsne1dd626ed979",
        "x-rapidapi-host": "tasty.p.rapidapi.com",
    }

    # Note that I set the maximum number of results to 20
    url = f"https://tasty.p.rapidapi.com/recipes/list?from=0&size=20&tags="

    for tag in tags:
        url = url + f"{tag}%2C%20"
    url = url.rstrip("%2C%20")

    url = url + "&q="
    for ingredient in items:
        url = url + f"{ingredient}%2C%20"
    url = url.rstrip("%2C%20")

    response = requests.request("GET", url, headers=headers)

    o = response.json()

    print(f"\nThere are {len(o["results"])} results using those filters!\n")

    for i in range(len(o["results"])):
        print(
            f"Recipe {i+1} - {o["results"][i]["name"]} ({(5.0 * o["results"][i]["user_ratings"]["score"]):.2f} out of 5 stars)"
        )  # Add an emoji instead of the word "stars"
        print(
            f"Description: {o["results"][i]["yields"]}, takes {o["results"][i]["prep_time_minutes"]} minutes to prep, and {o["results"][i]["total_time_minutes"]} minutes to cook!\n{o["results"][i]["description"]}\n"
        )

        # Extra feature
        # print(f"Watch a short video on this recipe here: {o["results"][i]["original_video_url"]}\n")

        nutrition = input("Do you want to know the nutrition information? Yes or no: ")
        if nutrition.strip().lower() == "yes":
            print(f"- {o["results"][i]["nutrition"]["calories"]} calories")
            print(
                f"- {o["results"][i]["nutrition"]["carbohydrates"]} grams of carbohydrates"
            )
            print(f"- {o["results"][i]["nutrition"]["fat"]} grams of fat")
            print(f"- {o["results"][i]["nutrition"]["fiber"]} grams of fiber")
            print(f"- {o["results"][i]["nutrition"]["protein"]} grams of protein")
            print(f"- {o["results"][i]["nutrition"]["sugar"]} grams of sugar\n")

        answer = input("\nDo you wish to make this dish? Yes or no? ")
        if answer.lower() == "yes":
            id = o["results"][i]["id"]
            print(f"\nThe instructions are:")
            j = 0
            for j in range(len(o["results"][i]["instructions"][j])):
                print(
                    f"    {j+1}. {o["results"][i]["instructions"][j]["display_text"]}"
                )
            break

    if id != 0:
        alternate = input(
            "\nIf you like the sound of the dish, but do not love the instructions, want me to provide you with alternate versions of the same dish? Yes or no? "
        )
        if alternate.strip().lower() == "yes":
            get_similar_recipes(id)
            print("Enjoy the alternate recipe for this dish!")
            sys.exit()
        else:
            print("Enjoy your meal!")
            sys.exit()


# Returns a list of tags that can be used in your search.
def get_tags(tag):

    headers = {
        "x-rapidapi-key": "4e6e1cddd9mshda2c9866c14b313p1b1b08jsne1dd626ed979",
        "x-rapidapi-host": "tasty.p.rapidapi.com",
    }

    response = requests.request(
        "GET", "https://tasty.p.rapidapi.com/tags/list", headers=headers
    )

    o = response.json()

    for i in range(len(o["results"])):
        if tag.title() == o["results"][i]["display_name"]:
            return tag

    print("I'm sorry, that tag is not in the database! Exiting program.")
    sys.exit()  # MAKE THIS A TRY EXCEPT LOOP UNTIL I GET CORRECT INPUT


# Returns a list of recipes that are similar to the specified rcipe and accepts a numeric parameter called id obtained from recipes/list.
def get_similar_recipes(id):

    headers = {
        "x-rapidapi-key": "4e6e1cddd9mshda2c9866c14b313p1b1b08jsne1dd626ed979",
        "x-rapidapi-host": "tasty.p.rapidapi.com",
    }

    response = requests.request(
        "GET",
        f"https://tasty.p.rapidapi.com//recipes/list-similarities?recipe_id={id}",
        headers=headers,
    )

    o = response.json()

    for i in range(len(o["results"])):
        print(
            f"\nHow about the dish '{o["results"][i]["name"]}'?\nIts description is:\n{o["results"][i]["description"]}\n"
        )
        print("The instructions are as follows:")
        j = 0
        for j in range(len(o["results"][i]["instructions"])):
            print(f"    {j+1}. {o["results"][i]["instructions"][j]["display_text"]}")
        done = input("\nDoes this sound good? Yes or no? ")
        if done.strip().lower() == "yes":
            break


# Give up and get fast food
def get_tacobell():

    state = input("What state are you in? ")
    state = full_to_abbrev(state.strip().lower())

    city = input(f"And what city in {state} are you in? ")
    page = 0
    count = 0

    headers = {
        "x-rapidapi-key": "4e6e1cddd9mshda2c9866c14b313p1b1b08jsne1dd626ed979",
        "x-rapidapi-host": "restaurants-near-me-usa.p.rapidapi.com",
    }

    while True:
        if page > count:
            print(
                "Unfortunately I could not find a Taco Bell near you. You will have to starve!! Good luck and goodbye!"
            )
            sys.exit()

        response = requests.request(
            "GET",
            f"https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/state/{state}/city/{city}/{page}",
            headers=headers,
        )

        o = response.json()

        for i in range(len(o["restaurants"])):
            if o["restaurants"][i]["restaurantName"] == "Taco Bell":
                print(
                    f"You should just go to {o["restaurants"][i]["restaurantName"]} instead. It is at {o["restaurants"][i]["address"]}. Enjoy!"
                )
                sys.exit()
        if page == 0:
            count = (o["matching_results"] / 10) + 1
        page += 1


# Take a the full name of a state and return the two letter abbreviation
def full_to_abbrev(state):
    states = {
        "alabama": "AL",
        "alaska": "AK",
        "arizona": "AZ",
        "arkansas": "AR",
        "california": "CA",
        "colorado": "CO",
        "connecticut": "CT",
        "delaware": "DE",
        "florida": "FL",
        "georgia": "GA",
        "hawaii": "HI",
        "idaho": "ID",
        "illinois": "IL",
        "indiana": "IN",
        "iowa": "IA",
        "kansas": "KS",
        "kentucky": "KY",
        "louisiana": "LA",
        "maine": "ME",
        "maryland": "MD",
        "massachusetts": "MA",
        "michigan": "MI",
        "minnesota": "MN",
        "mississippi": "MS",
        "missouri": "MO",
        "montana": "MT",
        "nebraska": "NE",
        "nevada": "NV",
        "new Hampshire": "NH",
        "new Jersey": "NJ",
        "new Mexico": "NM",
        "new York": "NY",
        "north Carolina": "NC",
        "north Dakota": "ND",
        "ohio": "OH",
        "oklahoma": "OK",
        "oregon": "OR",
        "pennsylvania": "PA",
        "rhode Island": "RI",
        "south Carolina": "SC",
        "south Dakota": "SD",
        "tennessee": "TN",
        "texas": "TX",
        "utah": "UT",
        "vermont": "VT",
        "virginia": "VA",
        "washington": "WA",
        "west Virginia": "WV",
        "wisconsin": "WI",
        "wyoming": "WY",
    }
    return states[state]


if __name__ == "__main__":
    main()
