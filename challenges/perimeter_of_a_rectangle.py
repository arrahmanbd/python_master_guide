'''
Find the Perimeter of a Rectangle
Create a function that takes length and width and finds the perimeter of a rectangle.

Examples
find_perimeter(6, 7) ➞ 26

find_perimeter(20, 10) ➞ 60

find_perimeter(2, 9) ➞ 22
Notes
Don't forget to return the result.
If you're stuck, find help in the Resources tab.
If you're really stuck, find solutions in the Solutions tab.

'''
# solution
def find_perimeter(length, width):
	# perimter of the rectangle formula P=2(l+w)
	perimeter = 2 * (length + width)
	return perimeter
	
print(find_perimeter(6, 7))
	
	
