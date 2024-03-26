encoder = {'%':'A', ' ':'B', '\n':'C'}
decoder = {'A':'%', 'B':' ', 'C':'\n'}

def encodeString(stringVal):
    myList = []
    chara = stringVal[0] #store first character
    count = 1
    for character in stringVal:
        if character in encoder:
            if chara not in encoder:
                chara = character
            if chara == character:
                count += 1
            else:
                myList.append((encoder[chara],count))
                chara = character
                count = 1
    return myList


def decodeString(encodedList):
    myString = ""
    for packet in encodedList:
        if packet[0] in decoder:
            for i in range(packet[1]):
                myString += decoder[packet[0]]
    return myString
art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''

encodedString = encodeString(art)

#print(encodedString)

print(decodeString(encodedString))