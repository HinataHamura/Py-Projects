class DietRecommendation:
    def __init__(self, age, gender, pregnant=False, breastfeeding=False):
        self.age = age
        self.gender = gender
        self.pregnant = pregnant
        self.breastfeeding = breastfeeding

    def get_recommendations(self):
        recommendations = {
            "vegetables": self.get_vegetable_serving_size(),
            "fruits": self.get_fruit_serving_size(),
            "grains": self.get_grain_serving_size(),
            "meats": self.get_meat_serving_size(),
            "dairy": self.get_dairy_serving_size()
        }

        return recommendations

    def get_vegetable_serving_size(self):
        serving_size = 0
        if self.age in range(2, 4):
            serving_size = 2.5
        elif self.age in range(4, 9):
            serving_size = 4.5
        elif self.age in range(9, 12):
            serving_size = 5
        elif self.age in range(12, 14):
            if self.gender == 'male':
                serving_size = 5.5
            elif self.gender == 'female':
                serving_size = 5
        elif self.age in range(14, 19):
            if self.gender == 'male':
                serving_size = 5.5
            elif self.gender == 'female':
                serving_size = 5
        elif self.age in range(19, 51):
            if self.gender == "male":
                serving_size = 6
            if self.gender == "female":
                serving_size = 5
            if self.pregnant and self.gender=='female':
                serving_size = 5
            if self.breastfeeding and self.gender=='female':
                serving_size = 7.5
        elif self.age in range(51, 71):
            if self.gender == "male":
                serving_size = 5.5
            elif self.gender == "female":
                serving_size = 5
        elif self.age >= 71:
            serving_size = 5
        return serving_size

    def get_fruit_serving_size(self):
        serving_size = 0
        if self.age in range(2, 4):
            serving_size = 1
        elif self.age in range(4, 9):
            serving_size = 1.5
        elif self.age in range(9, 12):
            serving_size = 2
        elif self.age in range(12, 14):
            serving_size = 2
        elif self.age in range(14, 19):
            serving_size = 2
        elif self.age in range(19, 51):
            serving_size = 2
        elif self.age in range(51, 71):
            serving_size = 2
        elif self.age >= 71:
            serving_size = 2
        return serving_size

    def get_grain_serving_size(self):
        serving_size = 0
        if self.age in range(2, 4):
            serving_size = 4
        elif self.age in range(4, 9):
            serving_size = 4
        elif self.age in range(9, 12):
            if self.gender == 'male':
                serving_size = 5
            elif self.gender == 'female':
                serving_size = 4
        elif self.age in range(12, 14):
            if self.gender == 'male':
                serving_size = 6
            elif self.gender == 'female':
                serving_size = 5
        elif self.age in range(14, 19):
            serving_size = 7
        elif self.age in range(19, 51):
            if self.gender == "male":
                serving_size = 6
            if self.gender == "female":
                serving_size = 6
            if self.pregnant:
                serving_size = 8.5
            if self.breastfeeding:
                serving_size = 9
        elif self.age in range(51, 71):
            if self.gender == "male":
                serving_size = 6
            if self.gender == "female":
                serving_size = 4
        elif self.age >= 71:
            if self.gender == 'male':
                serving_size = 4.5
            elif self.gender == 'female':
                serving_size = 3
        return serving_size

    def get_meat_serving_size(self):
        serving_size = 0
        if self.age in range(2, 4):
            serving_size = 1
        elif self.age in range(4, 9):
            serving_size = 1.5
        elif self.age in range(9, 12):
            serving_size = 2.5
        elif self.age in range(12, 14):
            serving_size = 2.5
        elif self.age in range(14, 19):
            serving_size = 2.5
        elif self.age in range(19, 51):
            if self.gender == "male":
                serving_size = 3
            if self.gender == "female":
                serving_size = 2.5
            if self.pregnant:
                serving_size = 3.5
            if self.breastfeeding:
                serving_size = 2.5
        elif self.age in range(51, 71):
            if self.gender == "male":
                serving_size = 2.5
            if self.gender == "female":
                serving_size = 2
        elif self.age >= 71:
            if self.gender == 'male':
                serving_size = 2.5
            elif self.gender == 'female':
                serving_size = 2
        return serving_size

    def get_dairy_serving_size(self):
        serving_size = 0
        if self.age in range(2, 4):
            serving_size = 1.5
        elif self.age in range(4, 9):
            if self.gender == 'male':
                serving_size = 2
            else:
                serving_size = 1.5
        elif self.age in range(9, 12):
            if self.gender == 'male':
                serving_size = 2.5
            elif self.gender == 'female':
                serving_size = 3
        elif self.age in range(12, 14):
            serving_size = 3.5
        elif self.age in range(14, 19):
            serving_size = 3.5
        elif self.age in range(19, 51):
            serving_size = 2.5
        elif self.age in range(51, 71):
            if self.gender == "male":
                serving_size = 2.5
            if self.gender == "female":
                serving_size = 4
        elif self.age >= 71:
            if self.gender == 'male':
                serving_size = 3.5
            elif self.gender == 'female':
                serving_size = 4
        return serving_size


def print_food_descriptions():
    print("\nAdditionally, here are detailed descriptions of what constitutes a single serving for each food category:")
    print(
        "\nVEGETABLES\nSingle serve of vegetable is 75g (100-350kJ). Here are some examples of single serve of Vegetable:")
    print("• 0.5 cup of cooked green or orange vegetables (like broccoli, spinach, carrots, or pumpkin)")
    print("• 0.5 cup of cooked dried or canned beans, peas, or lentils")
    print("• 1 cup of green leafy or raw salad vegetables")
    print("• 0.5 cup of sweet corn")
    print("• 0.5 of a medium potato or other starchy vegetables (such as sweet potato, taro, or cassava)")
    print("• 1 medium tomato")

    print("\nFRUITS\nSingle serve of fruit is 150g (350kJ). Here are some examples of single serve of fruit:")
    print("• 1 medium apple, banana, orange, or pear")
    print("• 2 small apricots, kiwi fruits, or plums")
    print("• 1 cup of diced or canned fruit (with no added sugar)")

    print("\nGRAINS\nSingle serve of grain is (500kJ). Here are some examples of single serve of grain:")
    print("• 1 slice (40g) of bread")
    print("• 0.5 medium (40g) roll or flat bread")
    print("• 0.5 cup (75-120g) of cooked rice, pasta, noodles, barley, buckwheat, semolina, polenta, bulgur or quinoa")
    print("• 0.5 cup (120g) of cooked porridge")
    print("• 0.66 cup (30g) of wheat cereal flakes")
    print("• 0.75 cup (30g) of muesli")
    print("• 3 (35g) crispbreads")
    print("• 1 (60g) crumpet")
    print("• 1 small (35g) English muffin or scone")

    print("\nMEAT\nSingle serve of meat is (500-600kJ). Here are some examples of single serve of meat:")
    print("• 65g cooked lean red meats such as beef, lamb, veal, pork, goat, or kangaroo (about 90-100g raw)")
    print("• 80g cooked lean poultry such as chicken or turkey (100g raw)")
    print("• 100g cooked fish fillet (about 115g raw) or one small can of fish")
    print("• 2 large (120g) eggs")
    print("• 1 cup (150g) cooked or canned legumes/beans such as lentils, chickpeas, or split peas")
    print("• 170g tofu")
    print("• 30g nuts, seeds, peanut or almond butter, tahini, or other nut or seed paste")

    print("\nDAIRY\nSingle serve of dairy is (500-600kJ). Here are some examples of single serve of dairy:")
    print("• 1 cup (250ml) of fresh, UHT long life, reconstituted powdered milk or buttermilk")
    print("• 0.5 cup (120ml) of evaporated milk")
    print("• 2 slices (40g) or a 4 x 3 x 2 cm cube (40g) of hard cheese, such as cheddar")
    print("• 0.5 cup (120g) of ricotta cheese")
    print("• 0.25 cup (200g) of yoghurt")
    print("• 1 cup (250ml) of soy, rice or other cereal drink with at least 100mg of added calcium per 100ml")


def main():
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age must be a positive integer.")

        if age>120:
            raise ValueError("This can't be a human's age!")

        gender = input("Enter your gender (male/female): ").lower()
        if gender not in ['male', 'female']:
            raise ValueError("Gender must be 'male' or 'female'.")

        pregnant_input = input("Are you pregnant? (yes/no): ").lower()
        if pregnant_input not in ['yes', 'no']:
            raise ValueError("Please enter 'yes' or 'no'.")
        pregnant = pregnant_input == "yes"

        breastfeeding_input = input("Are you breastfeeding? (yes/no): ").lower()
        if breastfeeding_input not in ['yes', 'no']:
            raise ValueError("Please enter 'yes' or 'no'.")
        breastfeeding = breastfeeding_input == "yes"

        if gender == "male" and (pregnant or breastfeeding):
            raise ValueError("Men cannot be pregnant and breastfeeding at the same time.")

        if age>=51 and age<=70  and (pregnant or breastfeeding):
            raise ValueError("This is not normal to be pregnant in this age")

        if age<19 and (pregnant or breastfeeding):
            raise ValueError("Too young to be pregnant!")

        recommendation = DietRecommendation(age, gender, pregnant, breastfeeding)
        recommendations = recommendation.get_recommendations()

        print("\nBased on your inputs, the minimum recommended servings are:")
        for food_group, serving_size in recommendations.items():
            print(f"{food_group.capitalize()}: {serving_size} servings per day")

        print_food_descriptions()

        export = input("\nWould you like to export these recommendations and serving sizes? (yes/no): ").lower()
        if export == "yes":
            filename = input("Enter a filename for the export (leave blank for 'DietaryRecommendations.txt'): ").strip()
            if filename and not filename.endswith(".txt"):
                raise ValueError("Filename must end with '.txt'.")
            filename = filename if filename else "DietaryRecommendations.txt"
            with open(filename, "w") as file:
                file.write("Dietary Recommendations\n\n")
                for food_group, serving_size in recommendations.items():
                    file.write(f"{food_group.capitalize()}: {serving_size} servings per day\n")
                file.write(
                    "\nAdditionally, here are detailed descriptions of what constitutes a single serving for each food category:\n")
                file.write(
                    "\nVEGETABLES\nSingle serve of vegetable is 75g (100-350kJ). Here are some examples of single serve of Vegetable:\n")
                file.write("• 0.5 cup of cooked green or orange vegetables (like broccoli, spinach, carrots, or pumpkin)\n")
                file.write("• 0.5 cup of cooked dried or canned beans, peas, or lentils\n")
                file.write("• 1 cup of green leafy or raw salad vegetables\n")
                file.write("• 0.5 cup of sweet corn\n")
                file.write(
                    "• 0.5 of a medium potato or other starchy vegetables (such as sweet potato, taro, or cassava)\n")
                file.write("• 1 medium tomato\n")

                file.write(
                    "\nFRUITS\nSingle serve of fruit is 150g (350kJ). Here are some examples of single serve of fruit:\n")
                file.write("• 1 medium apple, banana, orange, or pear\n")
                file.write("• 2 small apricots, kiwi fruits, or plums\n")
                file.write("• 1 cup of diced or canned fruit (with no added sugar)\n")

                file.write("\nGRAINS\nSingle serve of grain is (500kJ). Here are some examples of single serve of grain:\n")
                file.write("• 1 slice (40g) of bread\n")
                file.write("• 0.5 medium (40g) roll or flat bread\n")
                file.write(
                    "• 0.5 cup (75-120g) of cooked rice, pasta, noodles, barley, buckwheat, semolina, polenta, bulgur or quinoa\n")
                file.write("• 0.5 cup (120g) of cooked porridge\n")
                file.write("• 0.66 cup (30g) of wheat cereal flakes\n")
                file.write("• 0.75 cup (30g) of muesli\n")
                file.write("• 3 (35g) crispbreads\n")
                file.write("• 1 (60g) crumpet\n")
                file.write("• 1 small (35g) English muffin or scone\n")

                file.write("\nMEAT\nSingle serve of meat is (500-600kJ). Here are some examples of single serve of meat:\n")
                file.write(
                    "• 65g cooked lean red meats such as beef, lamb, veal, pork, goat, or kangaroo (about 90-100g raw)\n")
                file.write("• 80g cooked lean poultry such as chicken or turkey (100g raw)\n")
                file.write("• 100g cooked fish fillet (about 115g raw) or one small can of fish\n")
                file.write("• 2 large (120g) eggs\n")
                file.write("• 1 cup (150g) cooked or canned legumes/beans such as lentils, chickpeas, or split peas\n")
                file.write("• 170g tofu\n")
                file.write("• 30g nuts, seeds, peanut or almond butter, tahini, or other nut or seed paste\n")

                file.write(
                    "\nDAIRY\nSingle serve of dairy is (500-600kJ). Here are some examples of single serve of dairy:\n")
                file.write("• 1 cup (250ml) of fresh, UHT long life, reconstituted powdered milk or buttermilk\n")
                file.write("• 0.5 cup (120ml) of evaporated milk\n")
                file.write("• 2 slices (40g) or a 4 x 3 x 2 cm cube (40g) of hard cheese, such as cheddar\n")
                file.write("• 0.5 cup (120g) of ricotta cheese\n")
                file.write("• 0.25 cup (200g) of yoghurt\n")
                file.write(
                    "• 1 cup (250ml) of soy, rice or other cereal drink with at least 100mg of added calcium per 100ml\n")

            print(f"Recommendations and serving sizes have been exported to {filename}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
