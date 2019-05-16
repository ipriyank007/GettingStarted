def health_Calculator(age, apples_Ate, ciggs_Smoked):
    answer = (100-age) + (apples_Ate * 1.5) - (ciggs_Smoked * 2.5)
    print(answer)
    
priyank_Data = [23, 1, 0]

# health_Calculator(priyank_Data[0], priyank_Data[1], priyank_Data[2])
health_Calculator(*priyank_Data)
# saqueeb_Data = [23.5, 0, 50] 
# health_Calculator(*saqueeb_Data)