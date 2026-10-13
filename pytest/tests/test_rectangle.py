def test_area(my_rectangle):
    # rectangle = shapes.Rectangle(10, 20)
    assert my_rectangle.area() == my_rectangle.length * my_rectangle.width


def test_perimeter(my_rectangle):
    # rectangle = shapes.Rectangle(10, 50)
    assert my_rectangle.perimeter() == 2 * (my_rectangle.length + my_rectangle.width)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
