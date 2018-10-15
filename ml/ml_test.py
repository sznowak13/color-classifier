from persistence import db_manager
from sklearn import svm

COLOR_LABELS = {
    'red-ish': 0,
    'yellow-ish': 1,
    'green-ish': 2, 
    'purple-ish': 3, 
    'brown-ish': 4, 
    'blue-ish': 5, 
    'pink-ish': 6, 
    'orange-ish': 7, 
    'black-ish': 8, 
    'white-ish': 9
}


class ColorDataset:
    def __init__(self, rawdata):
        self.data = [[row['red'], row['green'], row['blue']] for row in rawdata]
        self.target = [COLOR_LABELS[row['color_guess']] for row in rawdata]

    def __repr__(self):
        return (f"Color dataset with {len(self.data)} entries.")

# preparing the dataset
dataset = ColorDataset(db_manager.get_data_set())
clf = svm.SVC(gamma=0.001, C=100., probability=True)
score = clf.fit(dataset.data[:200], dataset.target[:200]).score(dataset.data[-200:], dataset.target[-200:])
clf.fit(dataset.data, dataset.target)

