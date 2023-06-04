# Functions Guide 
#### Created  by ArjanCodes
 
1. Do one thing and do it well.
    - validate_card: too many funcionality. 
    - Split part of them into 'luhn_checksum'.

2. Separate Commands from queries.
    - validate_card: function validate and store computation into object.
    - validate_card only return value based on arguments.

3. Only request information you actually need.
    - validate_card: only need credit card and expired date but received all Customer information. 
    - Create only required arguments for function.
    - Asteriks (*) in validate_card function foreced users to use key-words arguments. 

4. Keep the number of parameters minimal.
    - validate_card: 3 arguments in this example are not so much but it can be done in better way.
    - create class CardInfo. Reduce validate_card arguments to one.
    - Split Customer class into: Customer and Card and seperate data.

5. Don’t create and use an object in the same place.
    - payment_handler created and use in order_food.
    - payment_handler created in main function.

6. Don’t use flag arguments.
    - when boolean exist in arguments its mean that function do two things.
    - take_a_holiday depends on bool value. Firts part did not even need one of parameters.
    - split take_a_holiday into two functions.

7. Remember that functions are objects.
    - Everything in Python are objects. 
    - check partial and callable.

8. Tips for naming functions and parameters.