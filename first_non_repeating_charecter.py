import collections

str = "GeekforGeeks"
# str = "GeeksQuiz"
dic = collections.Counter(str)
dic = dict(sorted(dic.items(), key=lambda x: x[0]))
for i in str:
    if dic[i] == 1:
        print(i)
        break
