import csv
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import sklearn.tree as st
import sklearn.ensemble as se

def transfer_feature(split):
    map = {"No" : 0, "Yes" : 1}
    split[3] = map.get(split[3])
    split[4] = map.get(split[4])
    num = 0
    for ch in split[0]:
        num = num*100+ord(ch)-ord('A')
    split[0] = num
    return split

def predict(model,target_name):
    f = open("test")
    data = []
    for row in f.readlines()[1:]:
        split = row.replace("\n","").split("\t")
        split = transfer_feature(split)
        data.append(split)
    f.close()

    list = open("test").readlines()
    result = []
    for index, pred in enumerate(model.predict(data).tolist()):
        result.append(list[index].replace('\n','').split('\t'))
        result[index].append(pred)
    f = open(target_name,'w+')
    writer = csv.writer(f)
    writer.writerows(result)

f = open("train")
feature = []
target = []
for row in f.readlines()[1:]:
    split = row.replace("\n","").split("\t")
    split = transfer_feature(split)
    feature.append(split[:19])
    target.append(split[19])
X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state=0)

#单一决策树
model = st.DecisionTreeClassifier(criterion="entropy")
model.fit(X_train,y_train)
scores = cross_val_score(model, feature, target, cv=10)
print('10-kfold scores(单一决策树):',scores.mean())
#AdaBoost
model = se.AdaBoostClassifier(model,n_estimators=100,random_state=7)
model.fit(X_train,y_train)
scores = cross_val_score(model, feature, target, cv=10)
print('10-kfold scores(AdaBoost):',scores.mean())
# predict(model,'result-AdaBoost.csv')
#Bagging
model = st.DecisionTreeClassifier(criterion="entropy")
model = se.BaggingClassifier(model,n_jobs=4,n_estimators=100,random_state=7)
model.fit(X_train,y_train)
scores = cross_val_score(model, feature, target, cv=10)
print('10-kfold scores(Bagging):',scores.mean())
predict(model,'result-Bagging.csv')






