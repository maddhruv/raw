while True:
	try:
		n=int(input("Enter:"))
		print(1/n)
		break
	#python 3	
	except ValueError:
		print("Error\n")
	#python 2.7	
	except NameError:
		print("Name error\n")
	except ZeroDivisionError:
		print("ZeroDivisionError\n")
	except:
		break
	finally:
		print("Done\n")