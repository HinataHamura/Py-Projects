import unittest
from assignment3 import FoodItem, FoodCategory, UserData, FoodDecorator, NutritionalInfoDecorator,FoodComponent


class TestFoodComponent(unittest.TestCase):
    def test_method_not_implemented_error(self):
        # Attempt to call a method of FoodComponent
        food_component = FoodComponent()
        # Test that NotImplementedError is raised
        with self.assertRaises(NotImplementedError):
            food_component.calculate_weekly_serves(4)


class TestFoodItem(unittest.TestCase):
    def test_calculate_weekly_serves(self):
        # Create a FoodItem object
        food_item = FoodItem("Test Food", 3, 25)
        # Test the calculate_weekly_serves method
        self.assertEqual(food_item.calculate_weekly_serves(4), 4 * 7 / 25)

    def test_str(self):
        # Create a FoodItem object
        food_item = FoodItem("Test Food", 3, 25)
        # Test the __str__ method
        self.assertEqual(str(food_item), "Test Food: 3 servings")

class TestFoodCategory(unittest.TestCase):
    def test_init(self):
        # Create a FoodCategory object
        food_category = FoodCategory("Test Category", 4, 30)
        # Test the __init__ method
        self.assertEqual(food_category.category, "Test Category")

class TestUserData(unittest.TestCase):
    def test_calculate_bmi(self):
        # Create a UserData object
        user_data = UserData(25, "Male", 70, 175, {"Vegetables": 3, "Fruits": 2, "Grains": 4})
        # Test the calculate_bmi method
        self.assertAlmostEqual(user_data.calculate_bmi(), 22.86, places=2)
class TestFoodDecorator(unittest.TestCase):
    def test_calculate_weekly_serves(self):
        # Create a FoodItem object
        food_item = FoodItem("Test Food", 3, 25)
        # Create a FoodDecorator object
        decorated_food = FoodDecorator(food_item)
        # Test the calculate_weekly_serves method
        self.assertEqual(decorated_food.calculate_weekly_serves(4), 4 * 7 / 25)

    def test_str(self):
        # Create a FoodItem object
        food_item = FoodItem("Test Food", 3, 25)
        # Create a FoodDecorator object
        decorated_food = FoodDecorator(food_item)
        # Test the __str__ method
        self.assertEqual(str(decorated_food), "Test Food: 3 servings")

class TestNutritionalInfoDecorator(unittest.TestCase):
    def test_calculate_weekly_serves(self):
        # Create a FoodItem object
        food_item = FoodItem("Test Food", 3, 25)
        # Create a NutritionalInfoDecorator object
        decorated_food = NutritionalInfoDecorator(food_item)
        # Test the calculate_weekly_serves method
        self.assertEqual(decorated_food.calculate_weekly_serves(4), 4 * 7 / 25)

    def test_str(self):
        # Create a FoodItem object
        food_item = FoodItem("Test Food", 3, 25)
        # Create a NutritionalInfoDecorator object
        decorated_food = NutritionalInfoDecorator(food_item)
        # Test the __str__ method
        self.assertEqual(str(decorated_food), "Test Food: 3 servings (with nutritional info)")

if __name__ == '__main__':
    unittest.main()
