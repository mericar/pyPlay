import math


#calculates after tax amount in some progressive tax system, where
#			- No taxation occurs before 10,000 units
#			- Each subsequent 10,000 units is taxed an extra 3.5%
#				eg. level 1 = 15%, level 2 = 18.5%, ... up to no 
#				more than 50%.
#
# integer -> float
def calc(total):
	if total <= 10000:
		return total
	else:
		base = 10000
		rem = total % base
		levels = math.floor(total/base)
		final_mutable = base
		incr = 1
		tax = 0.15
		print(final_mutable)
		while incr <= levels:
			print("tax as a ratio at level " + str(incr) + " is a whopping " + str(tax) )
			if incr == levels:
				r = rem*tax
				final_mutable += rem - r
				break;
			else:
				prcnt = base*tax
				final_mutable += 10000 - prcnt
				if tax < 0.5:
					tax += 0.035
				incr += 1
				print(final_mutable)

		return  final_mutable

#example calc computation test cases:
print(calc(12))
print(calc(502))
print(calc(10000))
print(calc(10001))
print(calc(20000))
print(calc(20001))
print(calc(175000))


			
