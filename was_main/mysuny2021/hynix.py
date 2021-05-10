from sklearn.metrics import confusion_matrix
import pandas as pd


sample = pd.read_csv('submission_hynix.csv',delimiter = ',')
answer = pd.read_csv('answer_hynix.csv',delimiter = ',')

def score(hw, answer) : 
    
    dt = pd.merge(answer[['Index', 'PF']], hw[['Index', 'PF']], how = 'left', on = ['Index'])
    
    include_dt = dt[(dt['PF_y'] == 1) | (dt['PF_y'] == 0)]
    exclude_dt = dt[~dt.index.isin(include_dt.index)]
    

    s00 = dt[(dt['PF_x'] == 0) & (dt['PF_y'] == 0)]
    s01 = dt[(dt['PF_x'] == 0) & (dt['PF_y'] == 1)]
    s10 = dt[(dt['PF_x'] == 1) & (dt['PF_y'] == 0)]
    s11 = dt[(dt['PF_x'] == 1) & (dt['PF_y'] == 1)]
    san = dt[~((dt['PF_y'] == 1) | (dt['PF_y'] == 0))]
    s1n = san[san['PF_x']== 1] 
    s0n = san[san['PF_x']== 0]
    
    
    acc = (len(s00) + len(s01)) / len(dt) * 100
    acc1 = len(s11) / (len(s10) + len(s11) + len(s1n)) * 100
    recall = len(s00) / (len(s00) + len(s10))  * 100
    precision = len(s00) / (len(s00) + len(s01) + len(s0n)) * 100
    
    #print(acc, acc1, recall, precision)
    
    return acc, acc1, recall, precision
    
      
acc, acc1, recall, precision = score(sample, answer)
print(acc, acc1, recall, precision)