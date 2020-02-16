import numpy as np

def check_for_array(H,A,B,J,C,D):
    '''This function will find the user input array J(small 2-D array)
    inside big array H(2-D array).if it found the array J inside H, function wil return True 
    else False'''
    
    counter = 0
    
    ''' We have initialized this counter with Zero, it will be incremented by one when array 
        is present in it'''
    
    for i in range(0,(A-C)+1):
        for j in range (0,(B-D)+1):
            ''' here A-C and B-D logic is used to limit the range of i and j until the value 
            where slicing of H with respect to J will not exceed array index'''
            
            row = np.arange(C) + i
            col = np.arange(D)[:,np.newaxis] + j
            ''' row and column being calculated to slice the array H, using array broad casting,
            in this case both row and col array will broadcast to meet each other's dimension, and 
            H will be sliced with the same dimensions'''
            
            if np.sum(H[row,col].transpose() == J) == C*D:
                '''here we need to calculate the Transpose of array since, both row and col are
                being broad casted and resulting in the transpose of array of what we want exactly'''
                counter = counter + 1
                break
            
    if counter > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    np.random.seed(0)
    H= np.random.randint(15, size = (4,4))
    J = np.array([[7,9],[2,4]])
    print(check_for_array(H,4,4,J,2,2))



  

            