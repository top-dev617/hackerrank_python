# Set .intersection()

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = set(input())
eng_news = set(input().split())
b = set(input())
frn_news = set(input().split())
both = eng_news.intersection(frn_news)
print(len(both))
