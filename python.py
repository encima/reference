#map - calls the command (1st arg), for each item in the 2nd arg (DOES NOT ADD SEPARATOR TO LAST ELEMENT)
';'.join(map(str,range(10)))
#filter - similar to map, uses the 1st arg as a condition and loops through for every element in the 2nd arg
map( lambda b:b.draw(), filter( lambda b: b.area() > 150, blobs ) )


