🏦 Bank Chatbot Project

A simple banking chatbot web application built using Flask and PostgreSQL.
This project allows users to log in and interact with a chatbot for basic banking queries.

🚀 How to Run This Project (Step-by-Step Guide)

📌 Follow these steps carefully — even if you are a beginner with no coding experience.

🧰 1️⃣ Install Required Software

Before running the project, install:

🐍 Python (3.x)

🗄️ PostgreSQL

🌐 Git (optional but recommended)

📥 2️⃣ Download the Project
🔹 Option 1: Download ZIP (Easy)

Click Code → Download ZIP

Extract the ZIP file

🔹 Option 2: Using Git (Recommended)
git clone https://github.com/yourusername/bank-chatbot.git
📂 3️⃣ Navigate to Project Folder

After extraction, you may see:

Bank-ChatBot-main/
   └── Bank-ChatBot-main/

👉 This is normal!

✅ Go inside the inner folder:
cd Bank-ChatBot-main
cd Bank-ChatBot-main
⚠️ Common Problem Faced

❌ Error:

can't open file 'app.py'

✔️ Solution:
👉 You were in the wrong folder
👉 Move inside the correct folder where app.py exists

📁 4️⃣ Folder Structure (VERY IMPORTANT)

Make sure your project looks like this:

bank-chatbot/
 ├── app.py
 ├── templates/
 │     ├── login.html
 │     ├── chatbot.html
 │     ├── admin.html
 │     ├── dashboard.html

❗ If templates folder is missing → app will NOT run

📦 5️⃣ Install Python Libraries

Open Command Prompt in project folder and run:

pip install flask psycopg2-binary
🗄️ 6️⃣ Setup PostgreSQL Database

Open pgAdmin and run the following:

✅ Create Database
CREATE DATABASE bankdb;
✅ Create Table
CREATE TABLE users(
id SERIAL PRIMARY KEY,
username TEXT,
password TEXT
);
✅ Insert Test User
INSERT INTO users(username,password)
VALUES('admin','admin');
⚠️ Important Note

In app.py, check this:

password="postgres"

👉 If your PostgreSQL password is different, change it accordingly.

▶️ 7️⃣ Run the Application

In terminal:

python app.py

You will see:

Running on http://127.0.0.1:5000
🌐 8️⃣ Open in Browser

Go to:

http://127.0.0.1:5000
🔐 Login Credentials
Username: admin
Password: admin
💬 9️⃣ How to Use

After login:

Click 💬 chatbot button

Try typing:

hello

balance

loan

credit card

⚠️ Common Errors & Solutions
❌ Template Not Found

✔️ Make sure HTML files are inside templates folder

❌ Database Connection Error

✔️ Check:

PostgreSQL is running

Database name = bankdb

Password is correct

❌ psycopg2 Error

✔️ Run:

pip install psycopg2-binary
🧠 Project Notes

This chatbot is rule-based (not AI)

Uses Flask for backend

Uses PostgreSQL for database

Frontend built using HTML + CSS

🚀 Future Improvements

🤖 Add AI chatbot (OpenAI API)

🗄️ Replace PostgreSQL with SQLite (easier setup)

🎨 Improve UI design

🌍 Deploy online
