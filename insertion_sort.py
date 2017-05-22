cdnsajnv
Myfinal_arr = []

Addbikerun_arr = [34,44,19,50,11,27]

for i in range(len(Addbikerun_arr)):
 
    if not Myfinal_arr:
        Myfinal_arr.insert(0, i)
    else:
        if (Addbikerun_arr[Myfinal_arr[0]] < Addbikerun_arr[i]):
            m = Myfinal_arr[0]
            Myfinal_arr[0] = i
                    
        else:
            m = i
         
        for p in range(len(Myfinal_arr)):
           
            if(Addbikerun_arr[m] > Addbikerun_arr[Myfinal_arr[p]]):
                Myfinal_arr.insert(p, m)
                break
            elif (p+1 == len(Myfinal_arr)):
                Myfinal_arr.append(m)
                break
           
                
print(Myfinal_arr)
