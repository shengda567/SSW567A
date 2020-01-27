def classfiy_triangle(a, b, c):

    if (isinstance(a, int)) and isinstance(b, int) and isinstance(c, int) and a > 0 and b > 0 and c >0:
        if (a + b > c and b + c > a and a + c > b):
            if (a == b == c):
                return "Equilateral"
            elif a == b or a == c or b == c:
                return "Isosceles"
            elif a*a + b*b == c*c or  a*a + c*c == b*b or b*b + c*c == a*a:
                return "Right"
            else:
                return "Scalene"

        else:
            return "NotATriangle"

    return "InvalidInput"


if __name__ == '__main__':
    print("classify_triangle(a, b, c)=", classfiy_triangle(5,7,7), sep=" ")