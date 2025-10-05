import pytest
from project import check_ingredient
from project import check_tag
from project import get_recipe
from project import get_similar_recipes


def test_check_ingredient():
    with pytest.raises(TypeError):
        check_ingredient(1)
    with pytest.raises(ValueError):
        check_ingredient("0")
    with pytest.raises(ValueError):
        check_ingredient("123")
    with pytest.raises(ValueError):
        check_ingredient("")
    assert check_ingredient("chicken") == "chicken"
    assert check_ingredient("rice") == "rice"
    # Cannot check if the ingredient is in the API
    # Cannot check that the ingredient is not a Tag


def test_check_tag():
    with pytest.raises(TypeError):
        check_tag(1)
    with pytest.raises(ValueError):
        check_tag("")
    assert check_tag("italian") == "italian"
    assert check_tag("dairy-free") == "dairy-free"
    assert check_tag("under 15 minutes") == "under 15 minutes"


def test_get_recipe():
    with pytest.raises(TypeError):
        get_recipe("chicken", "italian")
    with pytest.raises(TypeError):
        get_recipe(1, "italian")
    with pytest.raises(TypeError):
        get_recipe(1, ["italian"])
    with pytest.raises(TypeError):
        get_recipe(["chicken", "rice"], {})


def test_get_similar_recipes():
    with pytest.raises(TypeError):
        get_similar_recipes("0")
    with pytest.raises(TypeError):
        get_similar_recipes("8138")
    with pytest.raises(TypeError):
        get_similar_recipes("cat")
    with pytest.raises(ValueError):
        get_similar_recipes(-1)


# For more thorough testing in the future, I can explore
## Isolating API connection functions
## Isolating a nutrition function
## Isolating a description function
## Isolating a rating function

# The challenge with this is that the API database may change over time and
#  so will the hardcoded "correct" answers to these values.
