
def checkR(arr,n):
    if len(arr)==0 or n==0:
        return 
	
    if n in arr:
        print("true")
        return
    print("false")
    return
        
    
	
arr=[int(ele) for ele in input().split()]
n=int(input())
checkR(arr,n)
