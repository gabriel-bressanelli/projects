
# Setting lists and variables (list needed for the assignment)
names = ["Rennan", "Pedro A", "Julia", "Peter", "Andres", "Alyssa"]
bmi_list = []
underweight_count = []  # float
normal_weight_count = []  # float
overweight_count = [] # float



# Defining a function that calculates the BMI and append each bmi to a different list
def bmi_calc(weight,height):
    BMI = weight * 703 / (height * height) #float
    bmi_list.append(BMI)
    if BMI < 18.5:
       underweight_count.append(BMI)
    elif 18.5 <= BMI < 24.9:
        normal_weight_count.append(BMI)
    elif BMI > 24.9:
        overweight_count.append(BMI)

# Using a loop to input data and calculate BMI for each individual
for name in names:
    print(f"Enter data for {name}") 
    weight = input("Enter weight in pounds: ")
    weight = float(weight) # converting user input to float 
    height = input("Enter height in inches: ")
    height = float(height) # converting user input to float
    bmi_calc(weight,height)
    # print(underweight_count)
    # print(normal_weight_count)
    # print(overweight_count)



# Displaing the results
print("BMI Categories:")
print(f"Underweight:", len(underweight_count),  "individuals")
print(f"Normal Weight:", len(normal_weight_count), "individuals")
print(f"Overweight:", len(overweight_count), "individuals")
	
