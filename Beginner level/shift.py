def rotate(x,y,z):
	d=[]
	for i in range(x-y,x):
		d.append(z[i])
	for i in range(x-y):
		d.append(z[i])
	print(d)
def main():
	try:
		x=int(input("get number:"))
		y=int(input("shift:"))
		z=[]
		for i in range(x):
			z.append(int(input()))
		rotate(x,y,z)
	except:
		print('invalid')
main()
