# Shopify to Odoo & Google Sheets Lead Integration

This project integrates a Shopify contact form with Odoo CRM and Google Sheets. When a customer submits the contact form on your Shopify site, the data is sent to:

1. **Odoo CRM** – to create a new lead and customer (if not already existing).
2. **Google Sheets** – to log the submitted data for backup or reporting purposes.

---

## 🔧 How It Works

- The **Shopify form script** captures the form data and sends it via `fetch()` to:
  - A custom **Odoo HTTP controller** (`/shopify/lead`)
  - A **Google Apps Script Web App** that logs the data in a spreadsheet
- Both requests are asynchronous and run before the form is submitted normally to Shopify.

---

## 📁 Components

### 1. Odoo Controller (Python)

Creates a `res.partner` and `crm.lead` in Odoo from incoming Shopify form data.

### 2. Google Apps Script (JavaScript)

Appends the submitted form data to a Google Sheet.

### 3. Shopify Script (JavaScript)

Intercepts the Shopify form submit event and sends the data to both Odoo and Google Sheets endpoints.

---

## 🚀 Usage Instructions

### Step 1: Setup Odoo Endpoint

- Add the provided Odoo controller code to your custom module.
- Ensure the route `/shopify/lead` is publicly accessible.
- Supports CORS for cross-origin requests.

### Step 2: Deploy Google Apps Script

- Create a new Apps Script project linked to a Google Sheet.
- Paste the script code and deploy it as a **Web App** (set access to "Anyone").
- Copy the deployed Web App URL.

### Step 3: Insert Shopify Form Script

- Add the provided JavaScript `<script>` to your Shopify contact page or theme.
- Replace:
  - `'your odoo end point'` with your Odoo `/shopify/lead` URL.
  - `'g sheet script app link'` with your Google Apps Script Web App URL.

---

## ✅ Features

- Automatically creates leads and customers in Odoo CRM
- Stores backup in Google Sheets
- Fully CORS-compliant
- Works without disrupting Shopify's original form submission

---

## 📄 License

MIT License – Free to use, modify, and distribute.

---

## 👤 Author

**Usama Waqar**  
Sydney-based certified HubSpot & Odoo consultant  
Specialized in integrations, automation, and CRM/ERP solutions.
