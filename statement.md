
## Problem Statement

Manually tracking warehouse inventory and shipment details is prone to errors, time-consuming, and inefficient, especially as stocks and shipments grow. There is a need for a simple, reliable tool that allows users to manage products and shipments directly from their device without complex setup or technical help.

## Scope of the Project

This project provides a command-line based solution for storing, managing, and updating goods and shipping records in a warehouse. The entire solution uses Python and SQLite, ensuring platform independence and minimal software requirements. The system can easily be adapted for educational projects, small businesses, or personal warehouse tracking needs. It covers basic CRUD (Create, Read, Update, Delete) operations for two core areas: inventory (goods) management and shipment (shipping details) management.

## Target Users

- Small business owners and staff who need an offline inventory/shipment tracker.
- Students wanting to learn about database-driven applications using Python.
- Beginners interested in managing and organizing data with simple, no-cost tools.

## High-Level Features

- Menu-driven interface for managing goods and shipments.
- Add, edit, delete, view, and list all goods or shipping records.
- Persistent data storage using a local SQLite `.db` file.
- Easy setup—requires only Python (with sqlite3 module) and no extra installations.
- Modular code structure for future extensions, such as more tables, search capabilities, or reporting.
- Clear prompts and error handling for a user-friendly experience.