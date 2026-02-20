# 🚀 Dynamic Salary Prediction System

A Machine Learning web application that predicts salary (LPA) based on user inputs like experience, education, job role, industry, location, company size, and multiple skills.

---

## 📌 Problem Statement

Many job seekers do not know:
- What salary they should expect
- Whether their skills justify higher pay
- How experience impacts salary

This system helps estimate salary using a trained ML model.

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML & CSS
- One Hot Encoding
- MultiLabelBinarizer

---

## ⚙️ Features

- Multiple skills selection
- Real-time salary prediction
- Interactive UI
- ML Model Deployment using Flask

---

## 📂 Project Structure
dynamic-salary-prediction/
│
├── app.py
├── salary_model.pkl
├── education_encoder.pkl
├── skills_mlb.pkl
├── model_columns.pkl
│
├── templates/
│ └── index.html
│
└── README.md


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py

Open browser:

http://127.0.0.1:5000
👨‍💻 Author

Gokul Kul


---

After creating README:

```bash
git add README.md
git commit -m "Added README file"
git push
💡 Pro Tip (Very Important)

Before pushing, create .gitignore file and add:

__pycache__/
*.pkl
*.pyc
.env

⚠️ Don’t upload large model files unless necessary.
