import unittest
from assignment2 import DietRecommendation

class TestDietRecommendation(unittest.TestCase):
    def test_get_recommendations(self):
        # Test case 1: Male, age > 19, not pregnant, not breastfeeding
        recommendation1 = DietRecommendation(35, "male", pregnant=False, breastfeeding=False)
        expected_recommendations1 = {
            "vegetables": 6,
            "fruits": 2,
            "grains": 6,
            "meats": 3,
            "dairy": 2.5
        }
        self.assertEqual(recommendation1.get_recommendations(), expected_recommendations1)

        # Test case 2: Female, age < 19, not pregnant, not breastfeeding
        recommendation2 = DietRecommendation(17, "female", pregnant=False, breastfeeding=False)
        expected_recommendations2 = {
            "vegetables": 5,
            "fruits": 2,
            "grains": 7,
            "meats": 2.5,
            "dairy": 3.5
        }
        self.assertEqual(recommendation2.get_recommendations(), expected_recommendations2)
        #Test case 2: Male, age>19 , pregnant ,breastfeeding
        try:
            DietRecommendation(34, "male", pregnant=True, breastfeeding=True).get_recommendations()
        except ValueError as e:
            self.assertEqual(str(e), "Men cannot be pregnant and breastfeeding at the same time.")


if __name__ == '__main__':
    unittest.main()
