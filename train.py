import pickle
import cProfile
import pstats
import io
import os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def train_model():
    iris = load_iris()
    clf = RandomForestClassifier(random_state=42)
    clf.fit(iris.data, iris.target)

    os.makedirs("model", exist_ok=True)
    with open("model/my_model.pkl", "wb") as f:
        pickle.dump(clf, f)
    print("✅ Model trained and saved to model/my_model.pkl")

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    train_model()

    profiler.disable()

    # Save profiling results
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats("cumtime")
    ps.print_stats()

    with open("model/profile.txt", "w") as f:
        f.write(s.getvalue())

    print("✅ Profiling report saved to model/profile.txt")
