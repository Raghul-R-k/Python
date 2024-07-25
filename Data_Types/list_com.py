#using list comprehension creating a list of square numbers

#new_list = [expression for member in iterable]

#new_list = [expression for member in iterable if(option)]

new_list = [i for i in range(1,11)]
print('List Compregension : ',new_list)


new_list = [i for i in range(1,11) if(i%2 == 0)]
print('List Compregension : ',new_list)


vowels = 'aeiou'
my_name = 'Raghul Kumar'
non_vowels_list = [i for i in my_name if i not in vowels]
print(non_vowels_list)
