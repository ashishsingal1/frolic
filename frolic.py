import sys, os, datetime, pandas as pd, numpy as np, time, pickle

########################################################################
# STATIC
########################################################################

sys.path.insert(1, os.path.join(sys.path[0], '..'))
dir_path = os.path.dirname(os.path.realpath(__file__))

model_path = dir_path + '/out/basic_model.pkl'
bm_features = ['title_len', 'body_len', 'answer_count', 'comment_count', 'score']

########################################################################
# UTILITIES
########################################################################

def read_pickle(path): return pickle.load(open(path, 'rb'))

def write_pickle(file, path): return pickle.dump(file, open(path,'wb'), protocol=4)

########################################################################
# MACHINE LEARNING
########################################################################

def predict(ls_predict):
    model = read_pickle(model_path)
    result = model.predict(pd.DataFrame(ls_predict)[bm_features])[0]
    return result