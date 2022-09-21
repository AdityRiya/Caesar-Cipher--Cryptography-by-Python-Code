import pandas as pd
alphabets = pd.DataFrame({'alphabet':['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],'number':['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']})
print(alphabets)
plain_text=str(input('Enter Your word: '))
shift = int(input('Enter Shift: '))
for i in plain_text:
    if i == alphabets.alphabet():
        alphabets.number = alphabets.number + shift