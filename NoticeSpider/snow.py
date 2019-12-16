from snownlp import SnowNLP

with open('data.txt', 'r', encoding='utf-8') as f:
    content = str(f.read().splitlines())


s = SnowNLP(content)
print(s.summary(3))
