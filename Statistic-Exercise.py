##### Question 1: Compute Mean   #########

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def compute_mean(X):
    n = len(X)
    total = sum(X)
    mean = total/n
    return mean

# X = [2,0,2,2,7,4,-2,5,-1,-1]
# print("Mean : ", compute_mean(X))

######  Question 2: Compute Median

def compute_median(X):
    size = len(X)
    X = np.sort(X)
    print(X)
    if size % 2 == 0:
        return (X[size // 2 - 1] + X[size // 2]) / 2
    else:
        return X[size + 1 // 2]
# X = [1, 5, 4, 4, 9, 13]
# print (" Median : ", compute_median (X))

###### Question 3: Compute_std

def compute_std(X):
    mean = compute_mean(X)
    variance = 0
    for x in X:
        variance = variance + ((x-mean)**2)
    variance = variance / len(X)
    return np.sqrt(variance)


# X = [171, 176, 155, 167, 169, 182]
# print ( compute_std (X))


#####   Question 4: compute_correlation_cofficient (X, Y):

def compute_correlation_cofficient (X, Y):
    N = len(X)
    numerator = N * X.dot(Y) - np.sum(X)*np.sum(Y)
    denominator = np.sqrt(N * np.sum(np.square(X)) - np.square(np.sum(X))) * np.sqrt(N * np.sum(np.square(Y)) - np.square(np.sum(Y)))
    return np.round(numerator / denominator, 2)

# X = np. asarray ([-2, -5, -11, 6, 4, 15, 9])
# Y = np. asarray ([4 , 25, 121 , 36, 16, 225 , 81])
# print (" Correlation : ", compute_correlation_cofficient (X,Y))

########   Question 5: compute correlation for real data

data = pd. read_csv("advertisingg.csv")

def correlation(x,y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = np.sum((x-x_mean)*(y-y_mean))
    denominator = np.sqrt(np.sum((x-x_mean)**2) * np.sum((y-y_mean)**2))
    if denominator == 0:
        return 0
    else:
        return numerator / denominator

# x = data['Radio']
# y = data['Newspaper']
#
# result = correlation(x, y)
# print(round(result, 2))

######### Question 6
# features = ['TV', 'Radio', 'Newspaper']
#
# for feature_1 in features:
#   for feature_2 in features:
#       correlation_value = correlation(data[feature_1], data[feature_2])
#       print(f"{feature_1} and {feature_2}: {round(correlation_value, 2)}")


####### Question 7
# x = data['Radio']
# y = data['Newspaper']
# result = np.corrcoef(x,y)
# print ( result )


#########   Question 8
data_corr = data.corr()
# print(data_corr)

############  Question 9

plt . figure ( figsize =(10 ,8) )
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
# plt . show ()

###### Question 10
vi_data_df = pd. read_csv ("./ vi_text_retrieval .csv")
context = vi_data_df ['text ']
context = [doc. lower () for doc in context ]

tfidf_vectorizer = TfidfVectorizer ()
context_embedded = tfidf_vectorizer.fit_transform(context)
print(context_embedded.toarray()[7][0])

def tfidf_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(context_embedded, query_embedded).reshape((-1,))
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'cosine_score':cosine_scores[idx]
        }
        results.append(doc)
    return results
question = vi_data_df . iloc [0][ 'question ']
results = tfidf_search ( question , tfidf_vectorizer , top_d =5)
print(results [0][ 'cosine_score '])

def corr_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    corr_scores = np.corrcoef(
        query_embedded.toarray()[0],
        context_embedded.toarray()
    )
    corr_scores = corr_scores[0][1:]
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score':corr_scores[idx]
        }
        results.append(doc)
    return results

question = vi_data_df . iloc [0][ 'question ']
results = corr_search ( question , tfidf_vectorizer , top_d =5)
print(results [1][ 'corr_score '])