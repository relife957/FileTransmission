import jieba # jieba中文分词库
# 从文件读入小说
with open('three_kingdoms.txt', 'r', encoding='UTF-8') as novelFile:
    novel = novelFile.read()
novel = novel.replace(u'\u3000',' ')
# 将小说中的特殊符号过滤
with open('punctuation.txt', 'r', encoding='UTF-8') as punctuationFile:
    for punctuation in punctuationFile.readlines():
        novel = novel.replace(punctuation[0], ' ')

# 添加特定词到词库
jieba.add_word('刘备')
jieba.add_word('张飞')
jieba.add_word('关羽')
jieba.add_word('曹操')
jieba.add_word('孔明')
jieba.add_word('玄德')
jieba.add_word('孟德')

# 从文件独处无意义词
with open('meanless.txt', 'r', encoding='UTF-8') as meaninglessFile:
    mLessSet = set(meaninglessFile.read().split('\n'))
mLessSet.add(' ')

novelList = list(jieba.cut(novel))
novelSet = set(novelList) - mLessSet # 将无意义词从词语集合中删除
novelDict = {}
# 统计出词频字典
for word in novelSet:
    novelDict[word] = novelList.count(word)

# 对词频进行排序
novelListSorted = list(novelDict.items())
novelListSorted.sort(key=lambda e: e[1], reverse=True)

# 打印前20词频
topWordNum = 0
for topWordTup in novelListSorted:
    if topWordNum == 20:
        break
    print(topWordTup)
    topWordNum += 1
