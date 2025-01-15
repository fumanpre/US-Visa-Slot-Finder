# US Tourist Visa Appointment Scraper

## Overview

This project is a **web scraping tool** designed to help individuals find earlier appointments for US tourist visas. Due to overwhelming demand, appointment slots for US tourist visas have become incredibly scarce, with wait times often extending until 2027. This tool automates the process of scanning the official visa appointment website, identifying available slots, and notifying users of any newly available appointments that may open up ahead of the currently selected date.

The primary goal of this project is to simplify and expedite the process for users looking to secure earlier appointments, particularly those who are attempting to "pick and drop" appointment slots when a better one becomes available.

---

## Solution

This tool automates the process of continuously checking for new, earlier appointments. By scraping data from the US Visa Appointment website, the script identifies any newly available slots that may open up due to cancellations or other reasons. Users are then notified when a new appointment becomes available, allowing them to select the optimal time for their visa application.

---

## Features

- **Automatic Slot Checking**: Continuously checks the US Visa Appointment website for available slots.
- **Notifications**: Alerts the user when an earlier slot becomes available via email or other methods.
- **Customizable Search Parameters**: Allows users to set their preferred appointment date range.

---

## Technologies Used

- **Python**: Primary language for the web scraping tool.
- **BeautifulSoup** and **Requests**: Libraries used to scrape and parse the web page.
- **Selenium**: Handles dynamic content or JavaScript-based interactions on the site.
- **Schedule**: Schedules the script to run at set intervals.

