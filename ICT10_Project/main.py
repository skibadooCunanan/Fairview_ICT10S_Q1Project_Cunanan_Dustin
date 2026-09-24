from pyscript import document, display


def create_order(e):

    # Store the prices of each item
    prices = {
        "item1": 150,
        "item2": 160,
        "item3": 180,
        "item4": 200,
        "item5": 130
    }

    # Store the names of each item
    names = {
        "item1": "Burger",
        "item2": "Cheese Burger",
        "item3": "Vegan Burger",
        "item4": "Burger Supreme",
        "item5": "Burger Fries"
    }

    # Set the starting subtotal and order
    subtotal = 0
    order = []

    # Check each item
    for item in prices:

        checkbox = document.getElementById(item)

        if checkbox.checked:
            subtotal = subtotal + prices[item]
            order.append(names[item])

    # Calculate tax and total
    tax = subtotal * 0.12
    total = subtotal + tax

    # Create the receipt
    receipt = "<div class='receipt-title'>🧾 Order Receipt</div>"

    # Check if no items were selected
    if len(order) == 0:
        receipt = receipt + "No items selected."

    else:

        # Display each selected item
        for item in order:

            receipt = receipt + "<div class='receipt-line'>"
            receipt = receipt + "<span>" + item + "</span>"
            receipt = receipt + "</div>"

        receipt = receipt + "<hr>"

        # Display subtotal
        receipt = receipt + "<div class='receipt-line'>"
        receipt = receipt + "<span>Subtotal</span>"
        receipt = receipt + "<span>₱" + str(subtotal) + "</span>"
        receipt = receipt + "</div>"

        # Display tax
        receipt = receipt + "<div class='receipt-line'>"
        receipt = receipt + "<span>Tax (12%)</span>"
        receipt = receipt + "<span>₱" + str(round(tax, 2)) + "</span>"
        receipt = receipt + "</div>"

        # Display total
        receipt = receipt + "<div class='receipt-line total'>"
        receipt = receipt + "<span>Total</span>"
        receipt = receipt + "<span>₱" + str(round(total, 2)) + "</span>"
        receipt = receipt + "</div>"

    # Display the receipt
    document.getElementById("receipt").innerHTML = receipt