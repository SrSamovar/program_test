import pytest


@pytest.mark.parametrize(
    'hare_distances, turtle_distances, expect_result',
    [
        [[3, 4, 5, 6, 7], [1, 2, 3, 4, 5], "заяц"]
    ]
)
def test_race(hare_distances: list, turtle_distances: list, expect_result: str):
    hare_all = sum(hare_distances)
    turtle_all = sum(turtle_distances)
    if hare_all > turtle_all:
        result = "заяц"
    elif turtle_all > hare_all:
        result = "черепаха"
    else:
        result = "одинаково"
    assert result == expect_result


@pytest.mark.parametrize(
    'phrases, expect_result',
    [
        [["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза",
          "а собака боса", "тонет енот", "карман мрак", "пуст суп"],
         ["нажал кабан на баклажан", "рвал дед лавр", "азот калий и лактоза",
          "а собака боса", "тонет енот", "пуст суп"]]
    ]
)
def test_2(phrases, expect_result):
    result = []
    for phrase in phrases:
        new_phrase = phrase.replace(" ", "")
        if new_phrase == new_phrase[::-1]:
            result.append(phrase)
    assert result == expect_result


@pytest.mark.parametrize(
    'receipts, expect_result',
    [
        [[123, 145, 346, 246, 235, 166, 112, 351, 435], [346, 166, 435]]
    ]
)
def test_3(receipts, expect_result):
    result = receipts[2::3]
    assert result == expect_result
