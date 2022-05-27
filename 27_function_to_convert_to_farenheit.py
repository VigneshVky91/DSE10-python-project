def celcius_to_farenheit():
    celcius = int(input("Input the weather in celcius: "))
    farenheit = celcius * 9/5 + 32
    print(f"Weather in Farenheit: {farenheit} ")

def farenheit_to_celcius():
    farenheit = float(input("Input weather in farenheit: "))
    celcius = (farenheit - 32) * 5/9
    print(f"Weather in Celcius: {celcius} ")

# celcius_to_farenheit()
farenheit_to_celcius()