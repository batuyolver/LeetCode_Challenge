def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0
    
    counter = 0
    for x in string:
        if x in ["A","E","I","O","U"]:
            kevin += (len(string)-counter)
            counter +=1
        else:
            stuart += (len(string)-counter)
            counter +=1
    
            
    
    if stuart > kevin:
        print("Stuart {}".format(stuart))
    elif kevin > stuart:
        print("Kevin {}".format(kevin))
    else:
        print("Draw")
        
        

if __name__ == '__main__':