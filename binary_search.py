def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low <= high :
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item :
            print(item)
            return item
        elif guess > item :
            high = mid - 1
        else :
            low = mid + 1
    return None

the_list = [1,2,3,4,5,6,7,8,9,10]
num = int(input("type the chosen number : "))
binary_search(the_list,num)