import pandas as pd
import os
from sklearn.metrics import f1_score

score = 0.0
answer_df = pd.read_csv('answer_skc.csv')
submission_df = pd.read_csv('submission_skc.csv')

submission_dict = dict(zip(list(submission_df['img_name']), list(submission_df['defect'])))  # make dictionary 
answer_df['submission'] = answer_df['img_name'].map(submission_dict)

answer_df.head()

score = f1_score(answer_df['defect'], answer_df['submission'], average='weighted')

print(score)