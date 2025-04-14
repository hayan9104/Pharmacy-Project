Pharmacy Management System
The Pharmacy Management System is a comprehensive web application designed to streamline the operations of a pharmacy. It facilitates efficient management of inventory, sales, and customer interactions, ensuring optimal pharmaceutical services.
Features
• Inventory Management: Track and manage medicine stock levels, including details like expiration dates and batch numbers.
• Sales Processing: Handle sales transactions, generate invoices, and maintain sales records.
• Customer Management: Store and manage customer information, including purchase history.
• Reporting: Generate reports on sales, inventory status, and customer interactions.
Technologies Used
Frontend:
- HTML5, CSS3, JavaScript
Backend:
- Python with Django framework
Database:
- SQLite
Installation
• Clone the Repository:
  git clone https://github.com/hayan9104/Pharmacy-Project.git
• Navigate to the Project Directory:
  cd Pharmacy-Project
• Set Up a Virtual Environment (optional but recommended):
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
• Install Required Dependencies:
  pip install -r requirements.txt
• Set Up the Database:
  flask db init
  flask db migrate -m 'Initial migration.'
  flask db upgrade
• Run the Application:
  flask run
  Access the application at http://127.0.0.1:5000/.
Usage
• Dashboard: View an overview of inventory status, recent sales, and notifications.
• Inventory: Add new medicines, update existing stock, and monitor inventory levels.
• Sales: Process new sales, print invoices, and review past transactions.
• Customers: Manage customer information and view their purchase histories.
• Reports: Generate and view reports on sales performance and inventory turnover.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes.
License
This project is licensed under the MIT License.
