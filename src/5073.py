# 삼각형과 세 변

while (1):
	a, b, c = map(int, input().split())
	if a == 0 and b == 0 and c == 0:
		break
	maxi = max(a, b, c)
	if maxi >= a + b + c - maxi:
		print("Invalid")
		continue
	if a == b == c:
		print("Equilateral")
	elif a != b and a != c and b != c:
		print("Scalene")
	else:
		print("Isosceles")
