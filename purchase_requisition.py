requisition_counter = 10000


class Requisition:

    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name

        global requisition_counter
        requisition_counter += 1

        self.requisition_id = requisition_counter
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = ""

    def add_requisition(self, item_name, item_price):
        item = {
            "name": item_name,
            "price": item_price
        }

        self.items.append(item)
        self.total += item_price

        print("Item added:", item_name)
        print(f"Current Total: ${self.total:.2f}")

        return self.total

    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            last_three = str(self.requisition_id)[-3:]
            self.approval_reference = self.staff_id + last_three
        else:
            self.status = "Pending"
            self.approval_reference = ""

        return self.status

    def respond_requisition(self, decision):
        if self.status != "Pending":
            print("This requisition is already processed.")
            return self.status

        if decision == "Approved":
            self.status = "Approved"
            last_three = str(self.requisition_id)[-3:]
            self.approval_reference = self.staff_id + last_three

        elif decision == "Not approved":
            self.status = "Not approved"
            self.approval_reference = ""

        else:
            print("Invalid decision. Requisition remains pending.")

        return self.status

    def display_requisitions(self):
        print("\n-----------------------------")
        print("PURCHASE REQUISITION DETAILS")
        print("-----------------------------")

        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Items:")
        for item in self.items:
            print(f"  - {item['name']}: ${item['price']:.2f}")
        print(f"Total: ${self.total:.2f}")
        print("Status:", self.status)

        if self.approval_reference:
            print(
                "Approval Reference Number:",
                self.approval_reference
            )
        else:
            print("Approval Reference Number: Not available")

        print("-----------------------------")

    def requisition_statistics(self, requisitions):
        total = len(requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for requisition in requisitions:
            if requisition.status == "Approved":
                approved += 1
            elif requisition.status == "Pending":
                pending += 1
            elif requisition.status == "Not approved":
                not_approved += 1

        print("\nREQUISITION STATISTICS")
        print("Total Requisitions:", total)
        print("Approved:", approved)
        print("Pending:", pending)
        print("Not Approved:", not_approved)

        return total, approved, pending, not_approved


all_requisitions = []

while True:

    print("\nENTER REQUISITION DETAILS")

    date = input("Enter Date: ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")

    request = Requisition(date, staff_id, staff_name)

    print("Requisition ID:", request.requisition_id)

    while True:

        item_name = input("Enter Item Name: ")

        while True:
            try:
                item_price = float(input("Enter Item Price: $"))
                if item_price < 0:
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid price.")

        request.add_requisition(item_name, item_price)

        another_item = input(
            "Do you want to add another item? (yes/no): "
        ).strip().lower()

        if another_item != "yes":
            break

    print("\nFinal Total:", request.total)
    print("Staff Name:", request.staff_name)
    print("Staff ID:", request.staff_id)
    print("Status:", request.status)

    request.approve_requisition()

    print("Requisition ID:", request.requisition_id)
    print("Approval Status:", request.status)
    print("Approval Reference:", request.approval_reference)

    all_requisitions.append(request)

    another_request = input(
        "\nDo you want to create another requisition? (yes/no): "
    ).strip().lower()

    if another_request != "yes":
        break


print("\nMANAGER RESPONSE SECTION")

for request in all_requisitions:

    if request.status == "Pending":

        print("\nRequisition ID:", request.requisition_id)
        print("Staff Name:", request.staff_name)
        print(f"Total: ${request.total:.2f}")

        decision = input(
            "Enter Manager Decision "
            "(Approved/Not approved/Pending): "
        ).strip().lower()

        if decision == "approved":
            request.respond_requisition("Approved")

        elif decision == "not approved":
            request.respond_requisition("Not approved")

        elif decision == "pending":
            print("Requisition remains pending.")

        else:
            print("Invalid decision. Requisition remains pending.")


print("\nFINAL REQUISITION RESULTS")

for request in all_requisitions:
    request.display_requisitions()


print("\nFINAL STATISTICS")

if all_requisitions:
    all_requisitions[0].requisition_statistics(all_requisitions)


print("\nCHECKING REQUISITION IDS")

for request in all_requisitions:
    print(request.requisition_id)


print("\nCHECKING APPROVAL REFERENCES")

for request in all_requisitions:
    print(
        request.requisition_id,
        request.status,
        request.approval_reference
    )


if all_requisitions:
    all_requisitions[0].requisition_statistics(all_requisitions)