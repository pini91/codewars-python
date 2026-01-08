# You need to write regex that will validate a password to make sure it meets the following criteria:

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a digit
# only contains alphanumeric characters (note that '_' is not alphanumeric)

import re

str='fjd3IR9'

result = re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$', str)

if result:
    print(True)
else:
    print(False)