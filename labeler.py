#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:35:07 2021

@author: neo
"""

from simplegmail import Gmail
from simplegmail.query import construct_query

import _pickle as cPickle

# user-defined variables ----------------------------------------------------------------

label_name = "applications"

emails_older_than = 1 # days
emails_newer_than = 10 #days

#----------------------------------------------------------------------------------------

# initiate gmail API
gmail = Gmail(client_secret_file = "gmail_credentials/credentials.json")


# get all labels in your gmail account 

labels = gmail.list_labels()


application_label = list(filter(lambda x: x.name == label_name, labels))[0]


# sample query ---------------

# query_params = {
#     "newer_than": (2, "day"),
#     "unread": True,
#     "labels":[["Work"], ["Homework", "CS"]]
# }

# query to find emails
query_params = {
    "older_than": (emails_older_than, "day"),
    "newer_than": (emails_newer_than, "day")
}

# get emails matching the query
messages = gmail.get_messages(query=construct_query(query_params))

print("Messages Collected...........................................")


path = "pickles/"

# loading vectorizer and feature selector
vectorizer_file = path + "vectorizer.pkl"
vectorizer_file_handler = open(vectorizer_file, "rb")
vectorizer = cPickle.load(vectorizer_file_handler)
vectorizer_file_handler.close()

selector_file = path + "selector.pkl"
selector_file_handler = open(selector_file, "rb")
selector = cPickle.load(selector_file_handler)
selector_file_handler.close()

# load classifier
classifier_file = path + "classifier.pkl"
clf_file_handler = open(classifier_file, "rb")
clf = cPickle.load(clf_file_handler)
clf_file_handler.close()

for m in messages:
    sub = ''.join(e for e in m.subject if e.isalnum() or e == ' ' and e != '-')
    features_test_transformed  = vectorizer.transform([sub])
    features_test  = selector.transform(features_test_transformed).toarray()
    pred = clf.predict(features_test)
    
    if pred[0] == 1:
        # print(clf.predict_proba(features_test))
        m.add_label(application_label)
exit()
    
    





