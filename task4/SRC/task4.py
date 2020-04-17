def check(s1, s2):
    tmp_s1 = s1

    groups = []
    prev_s = None
    for s in s2:
        if s == '*':
            if prev_s:
                groups.append(prev_s)
                prev_s = None
            groups.append(s)
        else:
            if prev_s:
                prev_s += s
            else:
                prev_s = s
    if prev_s:
        groups.append(prev_s)

    for group in groups:
        if group == '*':
            if not tmp_s1:
                return False
            tmp_s1 = tmp_s1[1:]
        elif group in tmp_s1:
            tmp_s1 = tmp_s1[tmp_s1.find(group) + len(group):]
        else:
            return False
    return True


#print("check('12345', '*1*3*5')", check('12345', '*1*3*5'))
#print("check('11113455', '1*3*5')", check('11113455', '1*3*5'))
#print("check('11113455', '*1*5*4')", check('11113455', '*1*5*4'))
#print("check('11113455', '11113455')", check('11113455', '11113455'))
#print("check('qw12e3rt4y', '**12*3**4*')", check('qw12e3rt4y', '**12*3**4*'))
#print("check('qw12e3rt4y', '*12*3**4*')", check('qw12e3rt4y', '*12*3**4*'))
#print("check('1234', '**12*3**4*')", check('1234', '**12*3**4*'))
#print("check('1234', '123*4')", check('1234', '123*4'))
#print("check('1', '**')", check('1', '**'))
#print("check('1', '1*')", check('1', '1*'))
#print("check('', '')", check('', ''))
#print("check('23456', '***56')", check('23456', '***56'))
#print("check('12345', '*******1')", check('12345', '*******1'))
#print("check('1234567', '*234*6*')", check('1234567', '*234*6*'))
#print("check('123456', '*23456*')", check('123456', '*23456*'))
#print("check('Д#₽;(', '18!б')", check('Д#₽;(', '18!б'))
