import mainExample

print("This is the main script")

# Call the helper function from mainExample
mainExample.helper_function()

# Call the main function from mainExample
mainExample.main()

print("--------------------")
print(f"Module2's name is: {__name__}")
print(f"mainExample's name is: {mainExample.__name__}")