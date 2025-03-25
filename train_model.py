from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_iris
import joblib

# Загрузка данных
iris = load_iris()
X, y = iris.data, iris.target

# Обучение модели
model = GradientBoostingClassifier()
model.fit(X, y)

# Сохранение модели
joblib.dump(model, 'iris_model.joblib')
