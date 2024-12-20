class ExampleClass:
    # Constructor (__init__)
    def __init__(self, instance_value):
        self.instance_value = instance_value  # Instance attribute
        print(f"Instance created with value: {self.instance_value}")

    # Instance method
    def instance_method(self, increment):
        self.instance_value += increment
        print(f"Instance value updated to: {self.instance_value}")

    # Class method
    @classmethod
    def class_method(cls, new_value):
        cls.class_attribute = new_value  # Class attribute
        print(f"Class attribute set to: {cls.class_attribute}")

    # Static method
    @staticmethod
    def static_method():
        print("Static method called. Does not use instance or class.")

# Using the class
# Create an instance of the class
instance = ExampleClass(10)  # Calls the constructor (__init__)

# Call instance method
instance.instance_method(5)  # Updates instance_value to 15

# Call class method
ExampleClass.class_method(100)  # Sets class_attribute to 100

# Access class attribute directly (added by class_method)
print(f"Class attribute: {ExampleClass.class_attribute}")

# Call static method
ExampleClass.static_method()

#Example of a way to use the os module
import os

# Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# Access an environment variable
home_dir = os.environ.get('HOME')
print("Home directory:", home_dir)

#example of what the getpass module is used for
#The getpass module provides a way to securely handle password inputs from users.
# The primary function is getpass.getpass(), which prompts the user for a password without echoing what they type to the console. This is useful for sensitive information like passwords, ensuring they are not displayed on the screen.
# Example usage:
import getpass

password = getpass.getpass("Enter your password: ")

#Use Cmd + / to comment blocks of code