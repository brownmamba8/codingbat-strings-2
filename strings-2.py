## coding bat solutions for string-2

def double_char(str):
  result = '' #empty string
  for i in range(len(str)):
    result = result + str[i] + str[i]
   # result = result + str[i]
  return result 

def count_hi(str):
  return(str.count('hi')) #counts the word
  
def cat_dog(str):
  return(str.count('cat')==str.count('dog')) #will count the occurences of the two words
  
def count_code(str):
    return sum(1 for i in range(len(str) - 3)
        if str[i:i + 2] == 'co' and str[i + 3] == 'e' ) #from index 0 to 2 and 3 see if those chars hold true
    
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (a.endswith(b) or b.endswith(a))
#pro tip if they ask to find some chars at the beginning of a word just use 's1.beginswith(s2)'

def xyz_there(str):
    
    if str.count('.xyz')<0:
        return(True)
    else:
        return False
