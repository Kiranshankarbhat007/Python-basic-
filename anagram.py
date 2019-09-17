def anagram():
    s1 = raw_input("Enter your first string :")
    s2 = raw_input("Enter ypur second string :")
    s1 = list (s1)
    s2 = list (s2)
    ana = []
    if len(s1) == len (s2):
        for x in s1:
            if x in s2:
                ana.append(x)
            else:
                pass
        
        if ana == s1:
            print ("it is a anagram")
        else:
            print ("it is not a anagram")

    else:
        print ("the length of strings are not equal")
anagram()
