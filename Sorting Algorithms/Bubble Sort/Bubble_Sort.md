# Bubble Sort Info

**Bubble Sort**
> Bubble Sort is the simplest sorting algorithm.
> This sort makes multiple passes through the list.
> It will compare adjacent items and exchange them if they are out of order.
> It takes __n-1__ passes to sort n __numbers__.

### Example:

- (**54**,**26**,93,17,77,31,44,55,20) --> (**26**,**54**,93,17,77,31,44,55,20) # Exchanged 26,54
- (26,**54**,**93**,17,77,31,44,55,20) --> (26,**54**,**93**,17,77,31,44,55,20) # No Exchange required
- (26,54,**93**,**17**,77,31,44,55,20) --> (26,54,**17**,**93**,77,31,44,55,20)  #Exchanged 17,93
- (26,54,17,**93**,**77**,31,44,55,20) --> (26,54,17,**77**,**93**,31,44,55,20) # Exchanaged 77,93
- (26,54,17,77,**93**,**31**,44,55,20) --> (26,54,17,77,**31**,**93**,44,55,20) # Exchanged 31,93
- (26,54,17,77,31,**93**,**44**,55,20) --> (26,54,17,77,31,**44**,**93**,55,20) # Exchanged 44,93
- (26,54,17,77,31,44,**93**,**55**,20) --> (26,54,17,77,31,44,**55**,**93**,20) # Exchanged 55,93
- (26,54,17,77,31,44,55,**93**,**20**) --> (26,54,17,77,31,44,55,**20**,**93**) # Exchanged 20,93 - Note 93 the largest of them all, comes to its                                                                                                       final position after 1st pass
Subsequently after all passes [8], we will get all the numbers at their proper sorted places.