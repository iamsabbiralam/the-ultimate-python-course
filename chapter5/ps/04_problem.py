# what will be the length of following set s:
'''
s = set()
s.add(20)
s.add(20.0)
s.add('20')
'''
s = set()
s.add(20)
s.add(20.0) # 20 and 20.0 are considered the same value
s.add('20')
print(len(s))
