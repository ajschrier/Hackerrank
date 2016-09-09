englishCount = int(raw_input())
english = set(raw_input().split())
frenchCount = int(raw_input())
french = set(raw_input().split())

print len(english.union(french))
