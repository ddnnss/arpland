

import random
def check_profile(request):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    if request.user.is_authenticated:
        currentUser = request.user

    return locals()

