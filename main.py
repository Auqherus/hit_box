class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        pass


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        self.__hit_box = Rectangle(pos_x - width/2, 
                          pos_y - height/2, 
                          pos_x + width/2, 
                          pos_y + height/2)
        
    def in_area(self, x1, y1, x2, y2):
        self.rect = Rectangle(x1, y1, x2, y2)
        return self.rect.overlaps(self.__hit_box)
        


# Don't touch below this line


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

def main():
    
    unit_1 = Unit("Black Dragon", 3, 2)
    dragon_1 = Dragon(Unit, 2, 1, 2, 1,2)
    unit_2 = Unit("Gold Dragon", 2, 1)
    dragon_2 = Dragon(Unit, 3, 2, 1, 2,3)
    dragon_3 = Dragon(Unit, 4, 3, 1, 3,2)
    print(f"Is {unit_1.name} in hit box =  {dragon_1.in_area(2, 1, 3, 2)}")
    print(f"Is {unit_2.name} in hit box =  {dragon_2.in_area(1, 2, 1, 3)}")
    print(f"Is {unit_1.name} in hit box =  {dragon_3.in_area(2, 3, 2, 1)}")

main()
