    # Ingredient to Recipe Generator
    #### Video Demo:
      <URL HERE>
    #### Description:
    This project is meant to be a tool to help you make a meal based on what few ingredients you may already have! Beyond that, it also allows you to add special "filters" to narrow down your search. From there, the program will provide you with a lot of information to navigate such as:
    - Recipe Title
    - Recipe Rating
    - Recipe Description
    - Optional Nutritional Information
    - Cooking Instructions
    - Optional Alternate Recipes For Similar Dishes
    - A Last Resort Meal

    I started this project by scanning through GitHub Public APIs (https://github.com/public-apis/public-apis) and found Tasty (https://rapidapi.com/apidojo/api/tasty). Tasty comes with multiple query formats that were useful throughout this project. The ones that I used were "recipe/list", "tags/list", and "recipe/list-similarities".

    After the user navigates throughout the entire program, if they still have not found a recipe they are enthused about, the program calls upon another API to provide the ultimate back up plan. Using "Restaurants Near Me USA" (https://rapidapi.com/makingdatameaningful/api/restaurants-near-me-usa/playground/apiendpoint_a2840d15-a0ca-42ee-8ff5-750f986ad324), I was able to prompt the user for their state and city to determine whether there is a Taco Bell in their vicinity. If so, the program provides the street address. If not, the program gives up and wishes the user luck.



Additional things I can do:
- Limit number of ingredient and tag inputs
- Implement a back button so you don't have to start over
- Implement input protection if the user types something invalid
- Provide an option to print out all tags
- Star emoji for ratings


1. what each of the files you wrote for the project contains and does

2. if you debated certain design choices and explaining why you made them

3.
