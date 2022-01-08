#Q1
def calculate(min,max):
    sum = 0
    for i in range(min,max+1,1):
        sum = sum + i
    print(sum)

calculate(1,3)
calculate(4,8)

#Q2
def avg(data):
    sum = 0
    for element in data['employees']:
        sum += element['salary']
    print(sum/data['count'])


avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})


#Q3
def maxProduct(nums):
    number = 0
    maxnumber = 0
    if(len(nums) == 2):
        maxnumber = nums[0] * nums[1]
    else:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                number = nums[i] * nums[j]
                if(number > maxnumber):
                    maxnumber = number
    print(maxnumber)

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])


#Q4
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i] + nums[j] == target):
                return [i,j]

result = twoSum([2,11,7,15],9)
print(result)





