# 📄 Question:
# Create a class MathUtils with a @staticmethod called multiply(a, b) that returns the product of two numbers.

# Day 4 OOPs - Q2: Static method utility class

class MathUtils(object):
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers and return the result"""
        return a * b

# Test
result = MathUtils.multiply(4, 5)
print("Multiplication Result:", result)  # Output: 20
