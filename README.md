# Campus Management System Suite

A unified Python command-line suite that integrates 10 business logic, inventory, payroll, financial analysis, and point-of-sale modules tailored for a campus cafe or small business environment.

---

## Overview

The **Campus Management System Suite** combines multiple utility programs into a single interactive CLI application. It allows users to run individual modules or navigate through dedicated sub-menus for operations, finances, inventory control, and customer management.

### Key Features

* **Budget & Expense Tracking:** Monitor departmental costs and flag budget cap overruns.
* **Inventory Control & POS Terminal:** Search menu stock, generate itemized bills with promo code support, and apply custom discounts and taxes.
* **Payroll & Financial Summaries:** Calculate student/staff payroll with tax reserves and estimate real-time Net Profit/Loss across campus operations.
* **Loyalty & Vendor Management:** Manage multi-tier customer rewards programs and issue vendor purchase orders with stock status tracking.
* **Analytics & Dynamic Pricing:** Analyze projected promo revenues and simulate price adjustments (surge/discount) based on demand and stock levels.
* **Multi-Currency Converter:** Convert international currencies and compute cross-border transaction fees.

---

## Program Structure

| Module # | Module Name | Description |
| :--- | :--- | :--- |
| **1** | **Budget Tracker** | Calculates total operational costs against soft and hard budget limits. |
| **2** | **Inventory Threshold Checker** | Looks up specific menu items, displays stock levels, and flags reorder triggers. |
| **3** | **Campus Cafe POS Terminal** | Processes itemized customer orders, checks promo codes, and generates receipts. |
| **4** | **Employee Payroll Calculator** | Computes gross pay, overtime, tax reserves, and net payouts for staff. |
| **5** | **Financial Performance Summary** | Synthesizes revenue, COGS, and overhead expenses to project Net Profit/Loss. |
| **6** | **Customer Loyalty Management** | Interactive sub-menu to register users, track points, and manage Bronze/Silver/Gold tiers. |
| **7** | **Vendor Purchase Order** | Formats and validates vendor-specific purchase requests and stock statuses. |
| **8** | **Business Analytics Report** | Sorts products by base price and projects promotional sales and savings. |
| **9** | **Currency Conversion System** | Sub-menu for currency conversions, exchange rate tables, and cross-border fee checks. |
| **10** | **Dynamic Pricing Simulation** | Adjusts base prices using automated surge and discount rules based on demand metrics. |

---

## Requirements

* **Python:** 3.6 or higher
* **Dependencies:** Standard library only (`sys` module). No external pip packages required.

---

## Usage

1. **Clone or Download the Repository:**
```bash
    git clone https://github.com/Jeanne-of-the-night/BUV-Programming-Fundamentals.git
    cd BUV-Programming-Fundamentals
```
2. **Run the Script:**
```bash
	python main.py
```
3. **Navigate the Application:**
 * Enter numbers **1–10** from the main menu to execute a specific module.
 * Follow the on-screen terminal prompts for interactive modules (e.g., POS ordering, loyalty points redemption, currency conversions).
 * Enter **0** to safely exit the system.

---

## Sample Execution

```text
==========================================
      CAMPUS MANAGEMENT SYSTEM SUITE     
==========================================
 1. Budget Tracker
 2. Inventory Threshold Checker
 3. Campus Cafe POS Terminal
 4. Employee Payroll Calculator
 5. Financial Performance Summary
 6. Customer Loyalty Management
 7. Vendor Purchase Order
 8. Business Analytics Report
 9. Currency Conversion System
10. Dynamic Pricing Simulation
 0. Exit System
==========================================
Select a program to execute (0-10): 3

Enter items to order (Exp: Coffee 2, Tea 1, Sandwich 1): Coffee 2, Sandwich 1
Order received. Processing your order...
Enter a promo code (if applicable): STUDENT90
```

---

## License

This project is open-source and available under the MIT License.
