from pyscript import document, display


def generate_sku(e):

    # Clear the previous SKU
    document.getElementById("sku_result").innerHTML = ""

    # Get the category
    category = document.getElementById("category").value

    # Get the product name
    product_name = document.getElementById("product_name").value

    # Get the stock quantity
    stock_qty = document.getElementById("stock_qty").value

    # Create the SKU
    sku = (category[:3].upper()+ "-"+ product_name[:4].upper() + "-"+ str(stock_qty) )

    # Display the SKU
    display("SKU: " + sku, target="sku_result")