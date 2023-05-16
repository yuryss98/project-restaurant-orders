from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


def test_ingredient():
    ovo = Ingredient("ovo")
    assert ovo.name == "ovo"
    assert ovo.__repr__() == "Ingredient('ovo')"
    assert hash(ovo) == hash(Ingredient("ovo"))

    farinha = Ingredient("farinha")
    assert farinha == Ingredient('farinha')
    assert farinha != ovo
    assert hash(farinha) != hash(ovo)
    assert farinha.restrictions == {Restriction.GLUTEN}
