
def ifEven(length, array):
	quo = round(length/2)
	if(length%2 == 0):

		ave = (array[quo]+array[quo-1])/2
	else:
		return array[quo-1]
	return ave


def median(array1,array2):
	len_arr1 = len(array1)
	len_arr2 = len(array2)

	med1 = ifEven(len_arr1,array1)
	med2 = ifEven(len_arr2,array2)
	
	ave = (med1+med2)/2

	return ave

def main():

	arr1 = [1,3,5]
	arr2 = [2,4,6]

	answer = median(arr1,arr2)
	print(answer)

main()