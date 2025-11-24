              
# Warehouse Management System using Python and SQLite:
This Python program gives you an easy way to track warehouse goods and shipping details with simple menus. You can add, edit, delete, and view inventory or shipments, all stored in a reliable, serverless SQLite database for quick access and management.

## Overview of the Project

This project is a command-line warehouse management tool developed in Python. It allows users to manage goods inventory and shipment details through an interactive menu. Users can add, update, delete, and search for goods and shipping records in a local SQLite database.

## Features

- Add, edit, delete, display, and search goods entries (product inventory)
- Add, edit, delete, display, and search shipment details (shipping records)
- Interactive text-based menu for ease of use
- Data is persistently stored in a SQLite (`.db`) database file

## Technologies/Tools Used

- Python 
- SQLite (via `sqlite3` Python library)
- Terminal or Command Prompt

## Steps to Install & Run the Project

1. **Clone or Download** the project code to your local system.
2. **Ensure Python is installed** on your machine.
3. Place the script and, if not already present, create the SQLite database `data_warehouse.db` with tables `goods` and `shipping_date`.
4. **Run the script** in your terminal:
python warehouse_management.py
5. Follow the on-screen prompts to manage goods and shipping data.
