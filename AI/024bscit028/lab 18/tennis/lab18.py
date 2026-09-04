import os
os.system("cls")
import math

data = [
    {'outlook':'sunny','temp':'hot','humidity':'high','windy':False,'play':'no'},
    {'outlook':'sunny','temp':'hot','humidity':'high','windy':True,'play':'no'},
    {'outlook':'overcast','temp':'hot','humidity':'high','windy':False,'play':'yes'},
    {'outlook':'rainy','temp':'mild','humidity':'high','windy':False,'play':'yes'},
    {'outlook':'rainy','temp':'cool','humidity':'normal','windy':False,'play':'yes'},
    {'outlook':'rainy','temp':'cool','humidity':'normal','windy':True,'play':'no'},
    {'outlook':'overcast','temp':'cool','humidity':'normal','windy':True,'play':'yes'},
    {'outlook':'sunny','temp':'mild','humidity':'high','windy':False,'play':'no'},
    {'outlook':'sunny','temp':'cool','humidity':'normal','windy':False,'play':'yes'},
    {'outlook':'rainy','temp':'mild','humidity':'normal','windy':False,'play':'yes'},
    {'outlook':'sunny','temp':'mild','humidity':'normal','windy':True,'play':'yes'},
    {'outlook':'overcast','temp':'mild','humidity':'high','windy':True,'play':'yes'},
    {'outlook':'overcast','temp':'hot','humidity':'normal','windy':False,'play':'yes'},
    {'outlook':'rainy','temp':'mild','humidity':'high','windy':True,'play':'no'},
]

train = [data[i] for i in [0,2,3,4,6,7,8,10,11]]
test  = [data[i] for i in [1,5,9,12,13]]
features, target, alpha = ['outlook','temp','humidity','windy'], 'play', 1.0

classes = set(r[target] for r in data)
vocab = {f: set(r[f] for r in data) for f in features}          # possible values per feature
priors = {c: sum(r[target]==c for r in train)/len(train) for c in classes}

def likelihood(f, v, c):
    rows = [r for r in train if r[target] == c]
    count = sum(r[f] == v for r in rows)
    return (count + alpha) / (len(rows) + alpha*len(vocab[f]))   # P(x_i=v | y=c), Laplace-smoothed

def predict(row):
    scores = {c: priors[c] * math.prod(likelihood(f, row[f], c) for f in features) for c in classes}
    return max(scores, key=scores.get)                            # argmax P(y)·∏P(x_i|y)

y_true = [r[target] for r in test]
y_pred = [predict(r) for r in test]
acc = sum(t == p for t, p in zip(y_true, y_pred)) / len(y_true)

print("Accuracy:", acc)
for i, (t, p) in enumerate(zip(y_true, y_pred), 1):
    print(f"Sample {i}: Predicted={p}, Actual={t}")
print("Priors:", priors)