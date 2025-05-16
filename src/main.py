import csv
import os
from datetime import datetime

PRODUCTS_FILE = 'products.csv'
SUPPLIERS_FILE = 'suppliers.csv'
USERS_FILE = 'users.csv'

# User authentication
def authenticate(username, password):
    try:
        with open(USERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
    except Exception as e:
        print(f"An error occurred during authentication: {e}")
    return False

# Product management
def add_product(product):
    try:
        with open(PRODUCTS_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(product)
    except Exception as e:
        print(f"An error occurred while adding the product: {e}")

def update_product(product_id, updated_product):
    try:
        products = []
        with open(PRODUCTS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == product_id:
                    products.append(updated_product)
                else:
                    products.append(row)
        with open(PRODUCTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(products)
    except Exception as e:
        print(f"An error occurred while updating the product: {e}")

def delete_product(product_id):
    try:
        products = []
        with open(PRODUCTS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != product_id:
                    products.append(row)
        with open(PRODUCTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(products)
    except Exception as e:
        print(f"An error occurred while deleting the product: {e}")

def search_product(search_term):
    results = []
    try:
        with open(PRODUCTS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if search_term.lower() in row[1].lower():  # Search by product name
                    results.append(row)
    except Exception as e:
        print(f"An error occurred while searching for the product: {e}")
    return results

# Supplier management
def add_supplier(supplier):
    try:
        with open(SUPPLIERS_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(supplier)
    except Exception as e:
        print(f"An error occurred while adding the supplier: {e}")

def update_supplier(supplier_id, updated_supplier):
    try:
        suppliers = []
        with open(SUPPLIERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == supplier_id:
                    suppliers.append(updated_supplier)
                else:
                    suppliers.append(row)
        with open(SUPPLIERS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(suppliers)
    except Exception as e:
        print(f"An error occurred while updating the supplier: {e}")

def delete_supplier(supplier_id):
    try:
        suppliers = []
        with open(SUPPLIERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != supplier_id:
                    suppliers.append(row)
        with open(SUPPLIERS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(suppliers)
    except Exception as e:
        print(f"An error occurred while deleting the supplier: {e}")

def search_supplier(search_term):
    results = []
    try:
        with open(SUPPLIERS_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if search_term.lower() in row[1].lower():  # Search by supplier name
                    results.append(row)
    except Exception as e:
        print(f"An error occurred while searching for the supplier: {e}")
    return results


# Main program
def main():
    if not os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Description', 'Price', 'Quantity'])

    if not os.path.exists(SUPPLIERS_FILE):
        with open(SUPPLIERS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Contact'])

    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Password'])
            # Add a default admin user
            writer.writerow(['admin', 'admin123'])

    print("Welcome to the Stock Management System")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not authenticate(username, password):
        print("Authentication failed!")
        return

while True:
    print("\n1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Add Supplier")
    print("6. Update Supplier")
    print("7. Delete Supplier")
    print("8. Exit")  # Add an exit option
    choice = input("Select an option: ")
    
    if choice == '1':
        product = input("Enter product details (ID, Name, Description, Price, Quantity) separated by commas: ").split(',')
        add_product(product)
        print("Product added successfully.")
        
    elif choice == '2':
        product_id = input("Enter the product ID to update: ")
        updated_product = input("Enter updated product details (ID, Name, Description, Price, Quantity) separated by commas: ").split(',')
        update_product(product_id, updated_product)
        print("Product updated successfully.")
        
    elif choice == '3':
        product_id = input("Enter the product ID to delete: ")
        delete_product(product_id)
        print("Product deleted successfully.")
        
    elif choice == '4':
        search_term = input("Enter the product name to search: ")
        results = search_product(search_term)
        if results:
            print("Search Results:")
            for row in results:
                print(row)
        else:
            print("No products found.")
        
    elif choice == '5':
        supplier = input("Enter supplier details (ID, Name, Contact) separated by commas: ").split(',')
        add_supplier(supplier)
        print("Supplier added successfully.")
        
    elif choice == '6':
        supplier_id = input("Enter the supplier ID to update: ")
        updated_supplier = input("Enter updated supplier details (ID, Name, Contact) separated by commas: ").split(',')
        update_supplier(supplier_id, updated_supplier)
        print("Supplier updated successfully.")
        
    elif choice == '7':
        supplier_id = input("Enter the supplier ID to delete: ")
        delete_supplier(supplier_id)
        print("Supplier deleted successfully.")
        
    elif choice == '8':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid option. Please try again.")



