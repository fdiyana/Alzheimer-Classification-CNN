import numpy as np
from scipy.stats import mode


# models is a list of model objects
def EnsemblePrediction(models, x_test, y_test):
    # collect predictions from all models
    labels = []
    for model in models:
        preds = model.predict(x_test)
        label_preds = np.argmax(preds, axis=1)
        labels.append(label_preds)
    # find the majority vote
    all_labels = np.stack(labels, axis=1)
    majority_vote = mode(all_labels, axis=1)[0].reshape(len(all_labels))
    acc = np.sum(y_test[:, 1] == majority_vote) / len(y_test)
    print(f'Ensemble accuracy: {acc}')
    return majority_vote
