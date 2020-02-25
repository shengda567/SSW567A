"""
classify the trianngle is valid and print the result
"""
# classify the trianngle is valid and print the result
def clsfy_triangle(side1, side2, side3):
    """
    :param side1: int
    :param side2: int
    :param side3: int
    :return: string
    """
    if isinstance(side1, int) and isinstance(side2, int) and isinstance(side3, int) and \
            side1 > 0 and side2 > 0 and side3 > 0:
        if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
            if side1 == side2 == side3:
                return "Equilateral"
            elif side1 == side2 or side1 == side3 or side2 == side3:
                return "Isosceles"
            elif side1*side1 + side2*side2 == side3*side3 \
                    or side1*side1 + side3*side3 == side2*side2 \
                    or side2*side2 + side3*side3 == side1*side1:
                return "Right"
            else:
                return "Scalene"
        else:
            return "NotATriangle"

    return "InvalidInput"


if __name__ == '__main__':
    print("classify_triangle(side1, side2, side3)=", clsfy_triangle(5, 7, 7), sep=" ")
