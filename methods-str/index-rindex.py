s = 'foo bar foo baz foo qux'
print(s.find('foo'))
print(s.find('bar'))
print(s.find('qu'))
print(s.find('python'))

#Методы find() и rfind() являются более безопасными чем index() и rindex(),
#так как не приводят к возникновению ошибки во время выполнения программы.