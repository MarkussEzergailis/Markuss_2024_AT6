from InputValidator import UserInputValidator

list1 = [1,2,4,-1,-2,-3,4,5,-6,1,-2]
list2 = [1,9,-3,-1,-2,-3,4,5,2,7,-2]

instance1 = UserInputValidator(list1)
instance2 = UserInputValidator(list2)

instance1.validate_positive_integer()
instance2.validate_positive_integer()