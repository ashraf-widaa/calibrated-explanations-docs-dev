from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from calibrated_explanations import WrapCalibratedExplainer

# Data: three parts. The model never sees the calibration or test parts.
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
X_proper, X_cal, y_proper, y_cal = train_test_split(
    X_train, y_train, test_size=0.25, stratify=y_train, random_state=42
)

# 1. Wrap and train your model.
explainer = WrapCalibratedExplainer(
    RandomForestClassifier(n_estimators=100, random_state=42)
)
explainer.fit(X_proper, y_proper)

# 2. Calibrate on the held-out calibration set.
explainer.calibrate(X_cal, y_cal, feature_names=list(data.feature_names))

# 3. Calibrated prediction with a range, for one test case.
case = X_test[2:3]
proba, (low, high) = explainer.predict_proba(case, uq_interval=True)
print(f"P(benign) = {proba[0, 1]:.3f}  range [{low[0]:.3f}, {high[0]:.3f}]")

# 4. Explanations of the same case.
factual = explainer.explain_factual(case)
alternatives = explainer.explore_alternatives(case)
print(type(factual).__name__, "with", len(factual), "explanation")
print(type(alternatives).__name__, "with", len(alternatives), "explanation")
