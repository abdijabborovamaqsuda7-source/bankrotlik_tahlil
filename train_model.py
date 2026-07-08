import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# CSV yuklash
df = pd.read_csv("bankrotlik_data.csv")
print(df.columns.tolist())
df.columns = df.columns.str.strip()

# Ustunlarni o'zbekcha qilish
df.rename(columns={
    "Bankrupt?":"Bankrotlik",
    "Current Ratio":"Joriy likvidlik",
    "Debt ratio %":"Qarz koeffitsienti",
    "Operating Gross Margin":"Operatsion foyda",
    "ROA(C) before interest and depreciation before interest":
    "Aktivlar rentabelligi"
}, inplace=True)

# Kerakli ustunlar
X = df[
    [
        "Joriy_likvidlik_koeffitsienti",
        "Qarz_darajasi_foizi",
        "AKR_C_foiz_va_amortizatsiyagacha",
        "Operatsion_foyda_darajasi"
    ]
]
y = df["Bankrot_holati"]

# Train/Test
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = LogisticRegression(max_iter=1000)

model.fit(X, y)

# Saqlash
joblib.dump(model,"bankrot_model.pkl")

print("Model muvaffaqiyatli saqlandi!")
