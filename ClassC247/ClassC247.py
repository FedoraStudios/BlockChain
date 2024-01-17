for nonce in range(1, 20):
    equation = 20+4-nonce

    if equation == 18:
       print('After calculation we have obtained the result that the number is 18 at a number:', nonce, ' Hence the nonce is: ', nonce)
       break

    else:
        print('At number: ', nonce, "We didn't get the result as 18")