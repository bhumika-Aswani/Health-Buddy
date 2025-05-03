import pandas as pd
from datetime import datetime
import os

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def diabetes_risk(glucose, bmi_cat):
    if glucose < 90 and bmi_cat == "Normal":
        return "Low"
    elif 90 <= glucose <= 130 or bmi_cat in ["Overweight", "Underweight"]:
        return "Moderate"
    else:
        return "High"

def save_record(name, age, weight, height, glucose, bmi, bmi_cat, risk):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "Name": name,
        "Age": age,
        "Weight": weight,
        "Height": height,
        "Glucose": glucose,
        "BMI": bmi,
        "BMI Category": bmi_cat,
        "Diabetes Risk": risk,
        "Date": time
    }

    df = pd.DataFrame([data])

    file_exists = os.path.isfile("records.csv") and os.path.getsize("records.csv") > 0
    df.to_csv("records.csv", mode="a", header=not file_exists, index=False)
    print("\n✅ Record saved successfully!")

def view_records():
    if os.path.exists("records.csv") and os.path.getsize("records.csv") > 0:
        df = pd.read_csv("records.csv")
        print("\n📋 All Saved Records:\n")
        print(df.to_string(index=False))
    else:
        print("\n❌ No records found yet. Please add one first.")

def main():
    print(" Welcome to Health Buddy 🔹")
    while True:
        print("\n1. Enter New Health Record")
        print("2. View All Records")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            weight = float(input("Enter Weight (kg): "))
            height = float(input("Enter Height (m): "))
            glucose = float(input("Enter Glucose Level (mg/dL): "))

            bmi = calculate_bmi(weight, height)
            bmi_cat = bmi_category(bmi)
            risk = diabetes_risk(glucose, bmi_cat)

            print(f"\n📊 BMI: {bmi} ({bmi_cat})")
            print(f"🩺 Diabetes Risk Level: {risk}")

            save_record(name, age, weight, height, glucose, bmi, bmi_cat, risk)

        elif choice == "2":
            view_records()

        elif choice == "3":
            print("\n👋 Thank you for using Health Buddy. Stay healthy!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
