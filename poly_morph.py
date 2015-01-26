class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def tastesLike(self):
        raise NotImplementedError("Subclasses are responsible for creating this method")


class HotDog(Food):
    def tastesLike(self):
        return "%s is type %s \n \t has %s calories \n \t and tastes like Extremely processed meat." \
               % (self.name, type(self), self.calories)


class Hamburger(Food):
    def tastesLike(self):
        return "%s is type %s \n \t has %s calories \n \t and tastes like grilled goodness" \
               % (self.name, type(self), self.calories)


class ChickenPatty(Food):
    def tastesLike(self):
        return "%s is type %s \n \t has %s calories \n \t and tastes like chicken" \
               % (self.name, type(self), self.calories)

dinner = []
dinner.append(HotDog('Beef/Turkey BallPark', 230))
dinner.append(Hamburger('Lowfat Beef Patty', 260))
dinner.append(ChickenPatty('Mickey Mouse shaped Chicken Tenders', 170))

for course in dinner:
    print("%s" % course.tastesLike())


