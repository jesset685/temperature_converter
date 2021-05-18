# quick component to convert degrees C to F.
# Function takes in value, does conversion and puts answer into a list.


def to_celsius(from_fahrenheit):
    celsius = (from_fahrenheit -32) * 5/9
    return celsius

# Main routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_celsius(item)
    ans_statement = "{} degrees Fahrenheit is {} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)
