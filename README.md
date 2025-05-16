Inventory Management System (IMS)

Overview:

Inventory Management System (IMS) is a Python-based command-line application designed to help businesses efficiently manage their stock inventory. This system allows authorized users to manage products, suppliers, track stock levels, handle purchase orders, and keep the inventory data organized using CSV files.

Features:

Authentication System
- Secure login for authorized users (administrators/managers).
- Username and password authentication to restrict access.

Product Management
- Add new products including details such as name, description, price, and quantity.
- Update existing product details.
- Delete products from the inventory.
- Search for products by name.

Stock Tracking
- Track current stock levels.
- Record new stock receipts to update inventory.
- Record sales and automatically deduct stock quantities.

Supplier Management
- Add new suppliers with details like name and contact information.
- Update supplier information.
- Remove suppliers from the system.
- Search for suppliers by name.

Purchase Orders
- Generate purchase orders for items with low stock.
- Record purchase orders and update stock upon receipt.

Data Storage
- All inventory, supplier, and user data is stored in CSV files located in the `data/` directory.
- Products (`products.csv`), Suppliers (`suppliers.csv`), and Users (`users.csv`) data are maintained in separate files for easy management.

Technologies Used
- Python 3.x
- Standard Python libraries: `csv`, `datetime`, `os`
- Command-line interface for user interaction


Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ProlificTMontana/inventorymanagement.git
   cd inventorymanagement
   
2. Ensure you have Python installed (version 3.6 or higher recommended).

3. Run the application:

  ```bash
   python src/main.py
   
4. Initial Login:

    The default administrator account is:
        Username: admin
        Password: admin123

    You can modify or add users by editing the data/users.csv file.

Usage

  - Run the program in a terminal or command prompt.
  - Follow the on-screen menu options to manage products, suppliers, stock levels, and purchase orders.
  - Use the search functionalities to find specific products or suppliers by name.

Notes and Best Practices

  - Make sure to backup the data/ directory regularly to prevent data loss.
  - Update user credentials in data/users.csv with strong passwords.
  - When adding products or suppliers, ensure unique IDs to maintain data integrity.
  - The system uses CSV files for simplicity; for larger scale or more robust applications, consider using a database system.

Contributing

Contributions are welcome! Please feel free to submit issues or pull requests for improvements or bug fixes.
  
