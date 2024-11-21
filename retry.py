
def calculate_total_cost(cost, tip=15):
    total = cost*(1+(tip/100))
    return total
def main():
    while True:
        try:
            cost = float(input("Meal cost: "))
            tip = int(input("Tip percentage: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for meal cost and tip percentage")
            continue
        if tip < 0:
            print("Invalid tip percentage! Using default value of 15%")
            total2 = calculate_total_cost(cost,15)
            rounded2 = round(total2,2)
            print(rounded2)
            break

        total = calculate_total_cost(cost,tip)
        rounded = round(total,2)
        print(f"The total cost of the meal is: ${rounded}")
        break

main()
