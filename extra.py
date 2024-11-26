from InputValidator import UserInputValidator

list2 = [1,2,11,-1,-2,-4,4,-33,6,11,-2]
list1 = [1,2,22,-1,-66,-3,4,5,6,7,-2]

validator1 = UserInputValidator(list1)
validator2 = UserInputValidator(list2)

validator1.validate_positive_integer()
validator2.validate_positive_integer()