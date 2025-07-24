# 🛠️ FastAPI Product Configurator

A backend API built with **FastAPI** to create and validate customizable product templates, option categories, option choices, and compatibility rules.

---

## 🚀 Features

- 📦 Create product templates
- 🧩 Add option categories and choices
- 🔒 Define compatibility rules (e.g., incompatible or required options)
- ✅ Validate product configurations
- 💰 Calculate total price of a configured product

---

## 📁 Project Structure

```
main.py              # FastAPI app with all endpoints
requirements.txt     # Python dependencies
README.md            # Project documentation
```

---

## 🔧 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- In-memory data storage (dictionaries)

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-product-configurator.git
cd fastapi-product-configurator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Server

```bash
uvicorn main:app --reload
```

Open your browser at:  
🔗 `http://127.0.0.1:8000/docs` for Swagger UI  
📘 `http://127.0.0.1:8000/redoc` for ReDoc

---

## 📘 API Overview

- `POST /product-templates` — Create a product template
- `POST /product-templates/{template_id}/option-categories` — Add category to product
- `POST /option-categories/{category_id}/choices` — Add choices to category
- `POST /product-templates/{template_id}/compatibility-rules` — Add rules
- `POST /product-templates/{template_id}/available-options/{target_category_id}` — Get available choices based on current selection
- `POST /product-templates/{template_id}/validate-configuration` — Validate a user’s selection

---

## 🧪 Example Request

```json
POST /product-templates
{
  "template_str_id": "laptop_x",
  "name": "Laptop X",
  "base_price": 500
}
```

---

## 📌 Improvements to Add

- Database integration (SQLite/PostgreSQL)
- User authentication
- Frontend integration (React/Vue)
- Docker support

---

## 👨‍💻 Author

**Jeevana Priya Aitham**  
📧 jeevanapriyaaitham@gmail.com

---
