words = ['cat', 'spider', 'alligator']
for w in words[:]:
	print (w, len(w))
	if len(w) > 6:
		words.insert(0, w)

print words
