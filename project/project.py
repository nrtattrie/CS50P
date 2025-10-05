#####
# Project Title: Ingredient to Recipe Generator
# Author: Nathan Renn Tattrie (GitHub: nrtattrie)
# This project was created to satisfy the edX CS50P final project requirements
#####
import requests
import emoji  # type: ignore
import sys


# Main function: Greets and runs other functions
def main():
    print(
        "\nHello and welcome to the 'Ingredient to Recipe Generator'!\nI hope to help you combine ingredients you already have on hand into a recipe that you may not have been able to come up with on your own!"
    )
    ingredients = read_ingredients()
    tags = read_tags()
    get_recipe(ingredients, tags)
    # In the case that no recipes are found, or all presented options are
    #  rejected
    print(
        "\n\nAlright, well, you've exhausted all the options I could come up with. Try new filters in your next search! Thank you and goodbye!"
    )


# Read in the ingredients from the user
def read_ingredients():
    # Gathers a list of ingredients to use in the get_recipe() function
    print(
        "\nTo begin, please provide 1-3 ingredients for me to cross reference recipes with.\nIf you wish to enter fewer than 3 ingredients, say 'Done' after your 1 to 2 entries."
    )
    print("\nINGREDIENTS")
    ingredients = []
    count_ingredients = 0
    while True:
        # If the user enters 'done' before 3 ingredients have been entered,
        #  exit the loop
        item = input("Ingredient: ").strip().lower()
        if item == "done":
            break
        # Check if it is a non-string type
        if item in ingredients:
            print(
                "That item has already been added to your ingredient list! Please try another!"
            )
        else:
            count_ingredients += 1
            ingredients.append(check_ingredient(item))
        # If 3 ingredients have been entered, exit the loop
        if count_ingredients > 2:
            break
    return ingredients


# Checks that the ingredient input is valid
def check_ingredient(item):
    if type(item) != str:
        raise TypeError("The ingredient you input is not of type 'str'")
    if not item.isalpha():
        raise ValueError(
            "The ingredient you entered contains characters that are not letters and cannot be used."
        )
    if item == "":
        raise ValueError("You did not enter an ingredient.")
    return item


# Read in Tags from the user
def read_tags():
    answer = (
        input(
            "\n\nBefore we begin using tags to filter the search, would you like to see an exhaustive list of tag options? Caution, it is a long list! \nYes or no? "
        )
        .strip()
        .lower()
    )
    if answer == "yes":
        print_tag_options()

    print("\n\nPlease provide 1-3 tags for me to cross reference recipes with.")
    print(
        "Here are examples of possible tags: 'Italian, Christmas, Dairy-Free, Appetizers, Tongs, and so on!"
    )
    print("When you are done entering tags, input 'Done'")

    print("\nTAGS")
    tags = []
    count_tags = 0
    while True:
        try:
            # If 3 tags have been entered, exit the loop
            if count_tags > 2:
                break
            tag = input("Tag: ").strip().lower()
            # If the user enters 'done' before 3 tags have been entered, exit the loop
            if tag == "done":
                break
            if check_tag(tag) != tag:
                raise Exception()
            if tag in tags:
                print(
                    "You have already entered that tag! Please try another or enter 'Done'"
                )
            else:
                count_tags += 1
                tags.append(tag)
        except Exception:
            print(
                f"I'm sorry, the Tag '{tag}', is not in the database! Please try another."
            )
    return tags


# Prints an exhaustive list of tags that can be used during the filtering step
def print_tag_options():
    headers = {
        "x-rapidapi-key": "4e6e1cddd9mshda2c9866c14b313p1b1b08jsne1dd626ed979",
        "x-rapidapi-host": "tasty.p.rapidapi.com",
    }
    response = requests.request(
        "GET", "https://tasty.p.rapidapi.com/tags/list", headers=headers
    )
    if response.status_code != 200:
        raise ValueError(
            f"Tasty's 'tag/list' has an API status code of '{response.status_code}'"
        )

    o = response.json()
    for i in range(len(o["results"])):
        print(o["results"][i]["display_name"])


# After taking in a tag as input, this function checks whether or not the Tag
#  is valid within the API's database.
#  This function also checks whether or not they syntax or input type is valid.
def check_tag(tag):
    if type(tag) != str:
        raise TypeError("The tag you input is not of type 'str'")
    if tag == "":
        raise ValueError("You did not enter an tag.")

    headers = {
        "x-rapidapi-key": "4e6e1cddd9mshda2c9866c14b313p1b1b08jsne1dd626ed979",
        "x-rapidapi-host": "tasty.p.rapidapi.com",
    }
    response = requests.request(
        "GET", "https://tasty.p.rapidapi.com/tags/list", headers=headers
    )
    if response.status_code != 200:
        raise ValueError(
            f"Tasty's 'tag/list' has an API status code of '{response.status_code}'"
        )

    o = response.json()
    for i in range(len(o["results"])):
        if tag == str(o["results"][i]["display_name"]).lower():
            return tag

    return "-1"


# Returns a list of recipes with more input specifiers than resipes autocomplete
def get_recipe(items, tags):
    if not isinstance(items, list):
        raise TypeError(
            f"The entry for the items list is not of variable type 'list', but rather is of type {type(items)}."
        )
    if not isinstance(tags, list):
        raise TypeError(
            f"The entry for the tags list is not of variable type 'list', but rather is of type {type(tags)}"
        )

    # Gaining access to the Tasty "recipes/list" API
    id = 0
    headers = {
        "x-rapidapi-key": "4e6e1cddd9mshda2c9866c14b313p1b1b08jsne1dd626ed979",
        "x-rapidapi-host": "tasty.p.rapidapi.com",
    }

    # Note that I set the maximum number of results to 10
    url = f"https://tasty.p.rapidapi.com/recipes/list?from=0&size=10&tags="

    for tag in tags:
        url = url + f"{tag}%2C%20"
    url = url.rstrip("%2C%20")

    url = url + "&q="
    for ingredient in items:
        url = url + f"{ingredient}%2C%20"
    url = url.rstrip("%2C%20")

    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise ValueError(
            f"Tasty's 'recipes/list' has an API status code of '{response.status_code}'"
        )

    o = response.json()
    # Begin interfacing with the program user to find recipes
    # I could fine tune this print statement with regular expressions.
    print(f"\nThere are {len(o["results"])} result(s) using those filters!\n")
    if len(o["results"]) == 0:
        print(
            "I'm sorry, but the program could not find a recipe with the filters you have entered."
        )
        print(
            "Please try new search criteria with fewer tags or ingredients. Good luck!\n"
        )
        sys.exit()

    # Iterate through all (<=20) filter-based results for a rating and
    #  description
    for i in range(len(o["results"])):
        # Recipe number, title, and rating
        print(
            f"\nRECIPE {i+1}\n{o["results"][i]["name"]} ({(5.0 * o["results"][i]["user_ratings"]["score"]):.2f} out of 5 {emoji.emojize(":star:")}s)"
        )
        # Recipe prep time, cook time, and description
        print(
            f"DESCRIPTION: {o["results"][i]["yields"]}, takes {o["results"][i]["prep_time_minutes"]} minutes to prep, and {o["results"][i]["total_time_minutes"]} minutes to cook!\n{o["results"][i]["description"]}\n"
        )

        # Begin Nutrition fact section
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

        # Determine whether or not the suggested recipe is accepted or if
        #  another option is desired
        answer = input("\nDo you wish to get the recipe for this dish? Yes or no? ")
        if answer.lower() == "yes":
            id = o["results"][i]["id"]
            print(f"\nCongratulations! You have found a recipe!\n\n INSTRUCTIONS:")
            j = 0
            for j in range(len(o["results"][i]["instructions"][j])):
                print(
                    f"    {j+1}. {o["results"][i]["instructions"][j]["display_text"]}"
                )
            break

    if id != 0:
        alternate = input(
            "\nIf you like the sound of the dish, but do not love the instructions, want me to provide you with some alternate options with similar ingredients and styles? Yes or no? "
        )
        if alternate.strip().lower() == "yes":
            get_similar_recipes(id)
            print(
                "\n\nEnjoy this alternate option! I hope it is delicious! Come back any time. Goodbye!\n"
            )
            sys.exit()  # Concludes program by design
        else:
            print(
                "\n\nEnjoy your meal! I hope it is delicious! Come back anytime. Goodbye!\n"
            )
            sys.exit()  # Concludes program by design


# Returns a list of recipes that are similar to the specified rcipe and accepts #  a numeric parameter called id obtained from recipes/list.
def get_similar_recipes(id):

    if type(id) != int:
        raise TypeError(
            f"'id' has been incorrectly passed in as type {type(id)} instead of type 'int'"
        )
    if id < 0:
        raise ValueError("The value of 'id' cannot be negative")

    headers = {
        "x-rapidapi-key": "4e6e1cddd9mshda2c9866c14b313p1b1b08jsne1dd626ed979",
        "x-rapidapi-host": "tasty.p.rapidapi.com",
    }
    response = requests.request(
        "GET",
        f"https://tasty.p.rapidapi.com//recipes/list-similarities?recipe_id={id}",
        headers=headers,
    )
    if response.status_code != 200:
        raise ValueError(
            f"Tasty's 'recipes/list-similarities' has an API status code of '{response.status_code}'"
        )

    o = response.json()

    if (len(o["results"])) == 0:
        print("I'm sorry to get your hopes up, but it turns out there are not any similar recipes to the one you just viewed! Please go with that recipe or start a new search.")

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


# END OF USED FUNCTIONS
## The functions below are for potential add on functions for future development
## The functions below have now function and are not called
## One main reason why "get_tacobell" is not fully implemented is that I would ##  quickly reach my allowable API use with the current strategy


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
