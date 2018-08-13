# GoatVentures
Python implementation for the GoatVentures word puzzle generator/search problem exercise
the implementation has two stages:
stage 1: (a) Generating a 2D square grid of an arbitrary size.
         (b-1) Generating k engligh words with different length witout repetition to fill (x = word_fill_percentage)% of the grid word                density.
         or
         (b-2) Reading k engligh words with different length witout repetition to fill (x = word_fill_percentage)% of the grid word density              from a text file.
         (c) Placing word horizontally/vertically/diagonally into the grid with the placement probabilities (e.g. pv = 0.5, ph = 0.3,
            pd = 0.2) 
         (d) and Finally printing the grid in the output.
         
 stage 2: (a) Setting the direction of search in a namedtuple data structure
          (b) searching for the words (in word_list) that are placed into the grid.
          (c) Printing the result according the required format (e.g. 'CAT' Found at (0, 0) in Horizontal direction)
          
all the implementation constraints has been met.

In the Bounus points all ther crietria was met except the object ogiented design was missed. (implementation hasn't finished yet)

My Comments:
    for the search problem (brute force search) the complexity of search for 1D is O(n)
                                                        2D is O(n^2) and so on.
    using the dictionary "dict" type for storing and searching the grid could have improve the search time to O(nln)
Suggestion: 
    It could be more challenging if words that are placed into the grid had one character in common.
    
      

