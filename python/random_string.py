import random
import string

def ranCode(size=14, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

print(ranCode())