import naive_bayes as nb
import nltk
import random

#get negative comment data as hash, assign val = 1 in hash
bad_training_raw = nb.get_comment_data('bad.txt', 1)

#get the features for the negative comment data
bad_training_features = [(nb.get_features(comment), val) for (comment, val) in bad_training_raw.items()]


#get positibe comment data as hash, assign val = -1 in hash
good_training_raw = nb.get_comment_data('good.txt', -1)

#get the features for the positive comment data
good_training_features = [(nb.get_features(comment), val) for (comment, val) in good_training_raw.items()]

#combine the features, and then shuffle/randomize
combined_feature_sets = bad_training_features +  good_training_features
random.shuffle(combined_feature_sets)

#split the data into train and test
size = int(len(combined_feature_sets) * 0.9)
train_set, test_set = combined_feature_sets[size:], combined_feature_sets[:size]

#train the classifier using the training data
classifier = nltk.NaiveBayesClassifier.train(train_set)

#checking the accuracy of the training data.
print "current accuracy: %s" % nltk.classify.accuracy(classifier, test_set)

def classify_with_NB(comment):
    #Given a string of comment
    #@return 1 if comment needs to be flagged
    #@returns -1 if comment is fine.
    comment_feature = (nb.get_features(comment))
    return classifier.classify(comment_feature)
    
