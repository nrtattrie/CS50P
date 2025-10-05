    # Ingredient to Recipe Generator
    #### Video Demo:
    https://youtu.be/48r8MmSh0Jc

    #### Description:
    Do you ever go into your fridge and pantry and find ingredients you simply do not know what to do with? Perhaps you don't have the time or energy to go to the store and scrounge for a sad, disjointed meal. Fortunately for you, this Ingredient to Recipe Generator is just the tool you need for taking ingredients you have in your kitchen, regardless of how random or loosely connected they may seem. Now you can use these lonely ingredients in new, fun, and convenient ways.

    Provide up to three ingredients you wish to make into a tasty dish, and this program will quickly provide several possible recipes to try. To further hone your search, you have the option to further filter your recipe search through the use of "tags". These tags cover anything from cuisine origin, cookware, dietary restrictions, to utensils, and more! The program will let you know if your search is too restrictive or if your tag is not in the database it cross-references.

    Not only does the program provide you with step-by-step instructions, but it also includes the following:
    - Recipe Rating
    - Recipe Description
    - Optional Nutritional Information
    - Cooking Instructions

    Once the step-by-step instructions are provided, you may notice that a step involves a utensil or piece of kitchen equipment that you may not have. I thought that this would be a bad place for the program to dead end and commit you to a recipe that is incompatible with your kitchen’s capabilities or force you to make something work. Therefore, if you want to pivot, the program is designed to help you do so. From here, you will be asked if you wish to explore similar recipes based on your initial search.

    Upon successfully pivoting and finding a recipe that sounds tasty with the ingredients and equipment available to you, the program will wish you a happy meal and conclude. In the off chance the filtering is too restrictive, or you say you are uninterested in all of the options presented, the program will inform you that there are no more options and then instruct you to restart your search.

    I started this project by scanning through [GitHub Public APIs] (https://github.com/public-apis/public-apis) and found [Tasty] (https://rapidapi.com/apidojo/api/tasty). Tasty comes with multiple query formats that were useful throughout this project. The ones that I used were "recipe/list", "tags/list", and "recipe/list-similarities".

    The foundation of the project uses the “recipe/list” portion of the API. This query takes in tags and ingredients and then returns all the data necessary to help the user make their decision.

    The “tags/list” portion of the API was a very useful and informative part of this program. “Filters” can be ambiguous, but this API enables the user to see and select them from an exhaustive list. Also, in the case the user tries to use a filter that isn’t in the database, the program can query against this API to ensure the search is corrected.

    Each recipe provided from the “recipe/list” API has a unique ID. The “recipe/list-similarities” takes in a unique ID and then returns multiple similar recipes that are already linked together within the database.

    Within this API, one flaw I wish that could be mitigated is the inclusion of an “ingredients/list” query. With it, I could ensure the user inputs valid ingredients and ensure the search returns relevant and correct information.


    Future implementation to further build out the project:
    - Cross reference ingredients in the API before conducting the search
    - Add a "list all tags" option so the user can perform more rigorous searches
    - Implement input protection if the user types something invalid
    - Implement a "I give up" function that points the user to the nearest Taco Bell
