import warnings, numpy as np
warnings.simplefilter("ignore")
import calibrated_explanations as ce
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from calibrated_explanations import WrapCalibratedExplainer
X, y = load_diabetes(return_X_y=True)
Xt, Xte, yt, yte = train_test_split(X, y, test_size=0.2, random_state=42)
Xp, Xc, yp, yc = train_test_split(Xt, yt, test_size=0.25, random_state=42)
w = WrapCalibratedExplainer(RandomForestRegressor(n_estimators=50, random_state=42))
w.fit(Xp, yp); w.calibrate(Xc, yc)
for lh in ((-np.inf, 90), (10, np.inf)):
    pred, (low, high) = w.predict(Xte[:2], uq_interval=True, low_high_percentiles=lh)
    print(ce.__version__, lh, "low", np.round(low, 1), "high", np.round(high, 1), "| cal y min/max", yc.min(), yc.max())
