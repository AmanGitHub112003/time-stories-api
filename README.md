# 📰 Time Stories API

This project is a simple API service that fetches the **latest 6 stories** from [Time.com](https://time.com) using only Python’s built-in libraries.

It was built as part of a programming assignment with the following constraints:
- ❌ No external libraries or packages.
- ✅ Basic parsing of feed (RSS/XML) data.
- ✅ Expose a simple GET API that returns results in JSON.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AmanGitHub112003/time-stories-api.git
   cd time-stories-api
   ```
   
2. **Run the Python application:**
  ```bash
  python app.py
  ```

3. **Access the API in your browser or Postman:**
  ```bash
  http://localhost:8000/getTimeStories
  ```

---

## 📌 API Response Format

The endpoint returns a JSON array with the latest 6 stories:

[
  {
    "title": "Story headline here",
    "link": "https://time.com/story-link"
  },
  {
    "title": "Another headline",
    "link": "https://time.com/story-link-2"
  }
]

---

## 🛠 Built With

Python Standard Library
  - urllib – fetch the Time.com RSS feed
  - xml.etree.ElementTree – parse XML data
  - json – format API response
  - http.server – create a simple API endpoint

---

## 📷 Screenshot / Demo

Here’s an example of the API response in your browser after running the server:

![API Response Screenshot](Screenshot (5122).png)

---

## ✨ Author

Amandeep Kaur
📌 https://github.com/AmanGitHub112003
📌 https://www.linkedin.com/in/amandeep-kaur-4313a9259/
