def generate(n):
    import random
    import string
    charset = string.ascii_uppercase + string.ascii_lowercase + '0123456789'    
    code = ''
    for i in range(n):
        code+=random.choice(charset)
    return code
