#Даны два числа:
#num1 = 12345
#num2 = 12321
#Проверьте, что все цифры второго числа есть в первом числе.

num1 = 12345
num2 = 12321


nums1 = (str(num1))
nums2 = (str(num2))
resto = nums2 in nums1

print(resto)