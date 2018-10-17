from sklearn import svm

from persistence import db_manager
from util import Result, ColorDataset

clf = svm.SVC(gamma=0.001, C=100., probability=True)

colors = ['red-ish', 'yellow-ish', 'green-ish',
          'purple-ish', 'brown-ish', 'blue-ish',
          'pink-ish', 'orange-ish', 'black-ish', 'white-ish']


# preparing the dataset
def prepare_model():
    dataset = ColorDataset(db_manager.get_data_set())
    score = clf.fit(dataset.data[:200], dataset.target[:200]).score(dataset.data[-200:], dataset.target[-200:])
    clf.fit(dataset.data, dataset.target)
    return score, dataset.length


def predict_color(rgb_values):
    result = Result('success', '', {})
    prediction = clf.predict(rgb_values)
    probability = clf.predict_proba(rgb_values).max()
    result.message = f"I think its {colors[prediction[0]]}. Im {probability * 100}% sure."
    return result
