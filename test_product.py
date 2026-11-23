# Import the function
from product import product_details

# Test the product details function
def test_product_details():

    result = product_details(101, "Laptop", 5, 50000)

    expected = ("Product ID: 101\n"
                "Product Name: Laptop\n"
                "Quantity: 5\n"
                "Price: 50000")

    assert result == expected