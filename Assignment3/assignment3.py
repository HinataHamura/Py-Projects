import matplotlib.pyplot as plt


class FoodComponent:
    def calculate_weekly_serves(self, daily_intake):
        raise NotImplementedError("Subclasses should implement this!")

    def __str__(self):
        raise NotImplementedError("Subclasses should implement this!")


class FoodItem(FoodComponent):
    def __init__(self, name, recommended_daily_serves, single_serve_size):
        self.name = name
        self.recommended_daily_serves = recommended_daily_serves
        self.single_serve_size = single_serve_size

    def calculate_weekly_serves(self, daily_intake):
        return daily_intake * 7 / self.single_serve_size

    def __str__(self):
        return f"{self.name}: {self.recommended_daily_serves} servings"


class FoodCategory(FoodItem):
    def __init__(self, name, recommended_daily_serves, single_serve_size):
        super().__init__(name, recommended_daily_serves, single_serve_size)
        self.category = name


class FoodDecorator(FoodComponent):
    def __init__(self, decorated_food):
        self.decorated_food = decorated_food

    def calculate_weekly_serves(self, daily_intake):
        return self.decorated_food.calculate_weekly_serves(daily_intake)

    def __str__(self):
        return str(self.decorated_food)


class NutritionalInfoDecorator(FoodDecorator):
    def __init__(self, decorated_food):
        super().__init__(decorated_food)

    def calculate_weekly_serves(self, daily_intake):
        # Example of additional functionality: adding nutritional information
        serves = super().calculate_weekly_serves(daily_intake)
        return serves

    def __str__(self):
        # Example of additional functionality: adding nutritional information
        return f"{super().__str__()} (with nutritional info)"


class UserData:
    def __init__(self, age, gender, weight, height, daily_intake):
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.daily_intake = daily_intake

    def calculate_bmi(self):
        height_meters = self.height / 100
        return self.weight / (height_meters ** 2)


def visualize_bar_chart(user_data, food_categories):
    categories = [category.category for category in food_categories]
    daily_intake_values = [user_data.daily_intake[category] for category in categories]
    recommended_serves_values = [category.recommended_daily_serves for category in food_categories]

    bar_width = 0.35  # Width of each bar
    index = list(range(len(categories)))  # Index for the categories

    plt.figure(figsize=(10, 5))
    plt.bar([i - bar_width / 2 for i in index], daily_intake_values, bar_width, color='blue', label='User Intake')
    plt.bar([i + bar_width / 2 for i in index], recommended_serves_values, bar_width, color=(1.0, 0.5, 0.0, 1.0),
            label='Recommended Intake')
    plt.xlabel('Food Group')
    plt.ylabel('Servings')
    plt.title('Daily Serving Intake')
    plt.xticks(index, categories, rotation=45, ha='right', fontsize=10)  # Set x-ticks to category names
    plt.legend()
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.savefig('visualize_bar_chart.jpg')
    plt.show()


def visualize_pie_charts(user_data, food_categories):
    categories = [category.category for category in food_categories]
    daily_intake_values = [user_data.daily_intake[category] for category in categories]
    recommended_serves_values = [category.recommended_daily_serves for category in food_categories]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    ax1.pie(daily_intake_values, labels=categories, autopct='%1.1f%%')
    ax1.set_title('User Intake')
    ax2.pie(recommended_serves_values, labels=categories, autopct='%1.1f%%')
    ax2.set_title('Recommended Intake')
    fig.suptitle('Daily Serving Intake')
    plt.savefig('visualize_pie_charts.jpg')
    plt.show()


def visualize_line_chart(user_data, food_categories):
    categories = [category.category for category in food_categories]
    daily_intake_values = [user_data.daily_intake[category] for category in categories]
    recommended_serves_values = [category.recommended_daily_serves for category in food_categories]

    plt.figure(figsize=(12, 7))
    plt.plot(categories, daily_intake_values, marker='o', color='blue', label='User Intake')
    plt.plot(categories, recommended_serves_values, marker='s', color='orange', label='Recommended Intake')
    plt.xlabel('Food Group')
    plt.ylabel('Servings')
    plt.title('Daily Serving Intake')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.savefig('visualize_line_chart.jpg')
    plt.show()


def visualize_bubble_chart(user_data, food_categories):
    categories = [category.category for category in food_categories]
    daily_intake_values = [user_data.daily_intake[category] for category in categories]
    recommended_serves_values = [category.recommended_daily_serves for category in food_categories]

    plt.figure(figsize=(12, 7))
    plt.scatter(categories, daily_intake_values, s=[value * 100 for value in daily_intake_values], color='blue',
                alpha=0.5, label='User Intake')
    plt.scatter(categories, recommended_serves_values, s=[(value * 100) for value in recommended_serves_values],
                color='red', alpha=0.5, label='Recommended Intake')
    plt.xlabel('Food Group')
    plt.ylabel('Servings')
    plt.title('Daily Serving Intake')
    plt.xticks(rotation=45, ha='right')
    plt.legend(ncol=1, labelspacing=1, borderpad=1)
    plt.savefig('visualize_bubble_chart.jpg')
    plt.show()


def visualize_bmi_chart(bmi):
    categories = ['Very Underweight', 'Underweight', 'Healthy Weight', 'Overweight', 'Obese']
    boundaries = [0, 15, 18.5, 25, 30, 35]
    y_positions = [-1, 0, 1, 2, 3, 4, 5, 6]

    plt.figure(figsize=(8, 5))

    for i in range(len(boundaries) - 1):
        plt.plot([boundaries[i], boundaries[i + 1]], [y_positions[6 - i], y_positions[6 - i]], 'k-', lw=2)
        plt.text(boundaries[i] + (boundaries[i + 1] - boundaries[i]) / 2, y_positions[6 - i], categories[i],
                 ha='center', va='center', fontsize=10)

    plt.axvline(x=bmi, color='red', linestyle='-', linewidth=2, ymin=0.05, ymax=0.95)
    plt.text(bmi, -1.25, f'Your BMI: {bmi:.2f}', horizontalalignment='center', color='red', fontsize=12,
             fontweight='bold')

    plt.xlabel('BMI')
    plt.ylabel('Weight Category')
    plt.yticks(range(-1, 7), ['6', '5', '4', '3', '2', '1', '0', '-1'])
    plt.ylim(-1.5, 6.5)  # Adjusting y-axis limits
    plt.title('BMI Chart for Adults')
    plt.savefig('visualize_bmi_chart.jpg')
    plt.show()


def main():
    # Initialize food categories
    vegetables = FoodCategory("Vegetables", 6, 20)
    fruits = FoodCategory("Fruits", 2, 20)
    grains = FoodCategory("Grains", 6, 40)
    meats = FoodCategory("Meats", 3, 30)
    dairy = FoodCategory("Dairy", 2.5, 20)

    food_categories = [vegetables, fruits, grains, meats, dairy]

    # Collect user data
    age = int(input("Enter your age (in years): "))
    gender = input("Enter your gender (male or female): ")
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in cm): "))
    daily_intake = {}
    for category in food_categories:
        daily_intake[category.category] = float(
            input(f"Enter your daily intake of {category.category} (in servings): "))

    user_data = UserData(age, gender, weight, height, daily_intake)

    # Calculate BMI
    bmi = user_data.calculate_bmi()
    print(f"Your BMI is: {bmi:.2f}")

    # Save user info
    with open('user_info.txt', 'w') as file:
        file.write(f"Age: {age} years\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Weight: {weight} kg\n")
        file.write(f"Height: {height} cm\n")
        file.write("Daily Serving Intake:\n")
        for category, intake in daily_intake.items():
            file.write(f"{category}: {intake} servings\n")

    # Save BMI chart
    save_bmi_chart = input("Do you want to save the BMI chart? (yes/no): ").lower()
    if save_bmi_chart == "yes":
        visualize_bmi_chart(bmi)
        print("Visualize BMI saved as visualize_bmi_chart.jpg")

    # Save other charts
    save_charts = input("Do you want to save the charts? (yes/no): ").lower()
    if save_charts == "yes":
        visualize_bar_chart(user_data, food_categories)  # Bar chart
        print("Visualize Bar Chart saved as visualize_bar_chart.jpg")
        visualize_pie_charts(user_data, food_categories)  # Pie charts
        print("Visualize Pie Charts saved as visualize_pie_charts.jpg")
        visualize_line_chart(user_data, food_categories)  # Line chart
        print("Visualize Line Chart saved as visualize_line_chart.jpg")
        visualize_bubble_chart(user_data, food_categories)  # Bubble chart
        print("Visualize Bubble Chart saved as visualize_bubble_chart.jpg")

    # Export data
    export_data = input("Do you want to export your data? (yes/no): ").lower()
    if export_data == "yes":
        print("Data exported to user_info.txt")


if __name__ == "__main__":
    main()
