from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction
import pytest


def test_dish():
    strogonoff = Dish("Strogonoff", 22.09)
    frango = Ingredient("frango")
    strogonoff.add_ingredient_dependency(frango, 10)
    assert strogonoff.name == "Strogonoff"
    assert strogonoff == Dish("Strogonoff", 22.09)
    assert strogonoff != Dish("Lasanha", 22.09)
    assert hash(strogonoff) != hash(Dish("Lasanha", 22.09))
    assert hash(strogonoff) == hash(Dish("Strogonoff", 22.09))
    assert repr(strogonoff) == f"Dish('{'Strogonoff'}', R${22.09})"
    assert strogonoff.recipe == {Ingredient("frango"): 10}
    assert strogonoff.get_ingredients() == {frango}
    assert strogonoff.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Strogonoff", "Vinte dois")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Strogonoff", 0)
