def front_x(words):
  b = []
  for word in words:
    if(word[0] == 'x'):
      b.append(word)
  print words
  words = [x for x in words if x[0] != 'x']
  print words
  b = sorted(b)
  words = sorted(words)
  print b + words
  return b + words
front_x(['Srikanth','Kashyap','xzs','xae','Pulipaka','xdff'])