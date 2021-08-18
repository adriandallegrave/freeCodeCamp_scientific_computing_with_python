class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        pic = ""
        side = "*" * int(self.width)
        for x in range(self.height):
            pic += side + "\n"

        return pic

    def __str__(self):
        print = "Rectangle(width={}, height={})"
        print = print.format(self.width, self.height)
        return print

    def get_amount_inside(self, poly):
        side = self.width / poly.width
        top = self.height / poly.height
        answer = int(side) * int(top)
        return answer


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        txt = "Square(side={})"
        txt = txt.format(self.side)
        return txt

    def set_height(self, side):
        self.side = side

    def set_width(self, side):
        self.side = side
