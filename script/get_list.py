import os
import glob
import pickle

f1 = open('train.txt', 'w')
f2 = open('test.txt', 'w')
thershold = 15
thedir = '/n/whiskey/xy/vis/peterwg/dataset/indian_bird/'
partion_of_test = 0.8

dirs = [ name for name in os.listdir(thedir) if os.path.isdir(os.path.join(thedir, name)) ]
dic = {}
for curdir in dirs:
    included_extensions = ['jpg','JPG', 'bmp', 'png', 'gif']
    file_names = [fn for fn in os.listdir(str(thedir)+(curdir))
                  if any(fn.endswith(ext) for ext in included_extensions)]
    dic[curdir] = file_names
#print dic

## elimitation
for label in dic.keys():
    if len(dic[label]) <= thershold:
        del dic[label]
#print dic
#print len(dic.keys())
def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
save_obj(dic, "nzdict")

count = 0
for label in dic.keys():
    TH = len(dic[label])*partion_of_test
    count2 = 0
    for spec in dic[label]:
        if count2<= TH:
            f1.write(thedir+label+"/"+spec+" "+str(count)+"\n")
        else:
            f2.write(thedir+label+"/"+spec+" "+str(count)+"\n")
        count2 += 1
    count += 1

f1.close()
f2.close()
