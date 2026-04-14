import pytest

from calculator import add


def test_add():
    assert add(2, 2) == 4
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

    # Большие числа
    assert add(10**15, 10**15) == 2 * 10**15

    # Числа с плавающей точкой
    assert add(0.1, 0.2) == pytest.approx(0.3)

    # Работа с бесконечностью
    assert add(float('inf'), 1) == float('inf')
    assert add(float('-inf'), float('inf')) is not float('inf')

    # Проверка на обработку некорректных типов
    with pytest.raises(TypeError):
        add(1, "2")
