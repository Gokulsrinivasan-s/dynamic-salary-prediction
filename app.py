from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# ---------------- Load Saved Files ----------------
model = joblib.load("salary_model.pkl")
le = joblib.load("education_encoder.pkl")
mlb = joblib.load("skills_mlb.pkl")
model_columns = list(joblib.load("model_columns.pkl"))

# ---------------- Home Route ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- Prediction Route ----------------
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # -------- Collect Form Data --------
        data = {
            "Experience_Years": float(request.form["Experience_Years"]),
            "Education": request.form["Education"],
            "Job_Role": request.form["Job_Role"],
            "Location": request.form["Location"],
            "Industry": request.form["Industry"],
            "Company_Size": request.form["Company_Size"]
        }

        df = pd.DataFrame([data])

        # -------- Encode Education --------
        df["Education"] = le.transform(df["Education"])

        # -------- Multi-Select Skills --------
        user_skills = request.form.getlist("Skills")
        user_skills = [s for s in user_skills if s in mlb.classes_]

        skills_encoded = mlb.transform([user_skills])
        skills_df = pd.DataFrame(skills_encoded, columns=mlb.classes_)

        df = pd.concat([df, skills_df], axis=1)

        # -------- One Hot Encoding --------
        df = pd.get_dummies(
            df,
            columns=["Job_Role", "Location", "Industry", "Company_Size"],
            drop_first=True
        )

        # -------- Add Missing Columns --------
        for col in model_columns:
            if col not in df.columns:
                df[col] = 0

        df = df[model_columns]

        # -------- Prediction --------
        prediction = model.predict(df)[0]

        # -------- Smart Suggestion --------
        suggestion = ""

        if prediction < 3:
            suggestion = "Improve skills like AWS, Azure, ML and gain more experience."
        elif prediction < 6:
            suggestion = "Add advanced skills like Deep Learning, Kubernetes to boost salary."
        else:
            suggestion = "Strong profile! Focus on leadership & system architecture for growth."

        return render_template(
            "index.html",
            prediction_text=f"{round(prediction,2)} LPA",
            suggestion_text=suggestion
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


# ---------------- Run Server ----------------
if __name__ == "__main__":
    app.run(debug=True)