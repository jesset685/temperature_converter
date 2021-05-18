# quick component to convert degrees C to F.
# Function takes in value, does conversion and puts answer into a list.


def to_fahrenheit(from_celsius):
    fahrenheit = (from_celsius * 9 / 5) + 32
    return fahrenheit

# Main routine
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_fahrenheit(item)
    ans_statement = "{} degrees Celsius is {} degrees F".format(item, answer)
    converted.append(ans_statement)

print(converted)
