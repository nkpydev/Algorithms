# Insertion Sort Info

## Insertion Sort
> This sorting technique will always maintain a sorted sublist in the lower positions of the list.
> Each new item is then "inserted" back into the previous sublist such that the sorted sublist is one item larger in each pass.
> Again here we see that we will require __n-1__ passes to sort __n__ numbers.

### Example:
- (**54**,26,93,17,77,31,44,55,20) # Assume 54 is a sorted list of 1 item
- (**26**,**54**,93,17,77,31,44,55,20) # Inserted 26
- (**26**,**54**,**93**,17,77,31,44,55,20) # Inserted 93
- (**17**,**26**,**54**,**93**,77,31,44,55,20) # Inserted 17
- (**17**,**26**,**54**,**77**,**93**,31,44,55,20) # Inserted 77
- (**17**,**26**,**31**,**54**,**77**,**93**,44,55,20) # Inserted 31
- (**17**,**26**,**31**,**44**,**54**,**77**,**93**,55,20) # Inserted 44
- (**17**,**26**,**31**,**44**,**54**,**55**,**77**,**93**,20) # Inserted 55
- (**17**,**20**,**26**,**31**,**44**,**54**,**55**,**77**,**93**) # Inserted 20