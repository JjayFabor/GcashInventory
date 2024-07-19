# Gcash Inventory

## Overview

I created this application because my Mom has a business for Gcash E-Wallet.
This inventory system help my Mother manage the transactions as well as her income.

# Note:
This is a beginner project to practice my skills in using Django. 
I also did not create a user sign up cause I deploy this online and only my Mother have the credentials.

## Live Demo

To see a live demo of the application, watch the video below:

[Watch Live Demo Video](https://drive.google.com/file/d/1OBflgqWBVOOCnXdMyLEmJJ1b3IFDhhk8/view?usp=drive_link)

## Features

- User Authentication (I did not add a registration cause this is for personal use)
  - Feel free to fork the repository and update the code if you want
- Input and View Total Money Invested
- Input Deposit and Withdrawal Amounts with Transaction Fees
- View Transactions (Will add feature to download as PDF)
- Responsive User Interface

## Technologies Used

- Backend: Django, PostgreSQL
- Frontend: HTML, CSS, JavaScript

## Installation

### Prerequisites

- Python 3.x
- PostgreSQL
- Node.js and npm (or yarn)

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/JjayFabor/GcashInventory.git
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Usage

1. Create new user using:
   ```bash
   python manage.py createsuperuser
   ```
2. Use the dashboard to manage your investments and transactions.
3. View your transaction history.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## Contact

For any inquiries, please contact [faborjaylordvhan@gmail.com](mailto:faborjaylordvhan@gmail.com).
