f = open('StudentsPerformance.csv')

keys = []


def do_list_from_line(line):
    return [x.replace('"', '', 2).replace('\n', '') for x in line.split(',')]


def add_group_value(line):
    result = {}
    data = do_list_from_line(line)
    for order, name in enumerate(keys):
        if name not in ['gender', 'race/ethnicity']:
            result[name] = data[order]
    return result


gender_dict = {}


for line in f.readlines():
    if line.split(',')[0] == '"gender"':
        keys = do_list_from_line(line)
    else:
        data = do_list_from_line(line)

        if data[0] in gender_dict:
            if data[1] in gender_dict[data[0]]:
                gender_dict[data[0]][data[1]].append(add_group_value(line))
            else:
                gender_dict[data[0]][data[1]] = [add_group_value(line)]

        else:
            gender_dict[data[0]] = {data[1]: [add_group_value(line)]}


male_lunch_standard = 0

for i in gender_dict['male']:
    for j in gender_dict['male'][i]:
       if j['lunch'] == 'standard':
           male_lunch_standard += 1

print(male_lunch_standard)

male_test_preparation_course_completed = 0
for i in gender_dict['male']:
    for j in gender_dict['male'][i]:
        if j['test preparation course'] == 'completed':
            male_test_preparation_course_completed += 1

print(male_test_preparation_course_completed)

femail_parental_level_of_education = 0
for i in gender_dict['female']:
    for j in gender_dict['female'][i]:
        if j['parental level of education'] == 'master\'s degree':
            femail_parental_level_of_education += 1
print(femail_parental_level_of_education)


group_c_test_preparation_course_completed = 0

for i in gender_dict.values():
    for j in i['group C']:
        if j['test preparation course'] == 'completed':
            group_c_test_preparation_course_completed += 1

print(group_c_test_preparation_course_completed)

female_parental_level_of_education_master_and_math_score_more_90 = 0
for i in gender_dict['female']:
    for j in gender_dict['female'][i]:
        if j['parental level of education'] == 'master\'s degree' and int(j['math score']) > 90:
            female_parental_level_of_education_master_and_math_score_more_90 += 1

print(female_parental_level_of_education_master_and_math_score_more_90)


test_reading_score_course_total = 0
counter = 0
for i in gender_dict['male']:
    for j in gender_dict['male'][i]:
        test_reading_score_course_total += int(j['reading score'])
        counter += 1

print(round(test_reading_score_course_total / counter, 3))

f.close()


f = open('StudentsPerformance.csv')

max_math_score_total = 0
counter = 0
for line in f.readlines()[1:]:
    if do_list_from_line(line)[3] == 'free/reduced':
        max_math_score_total += int(do_list_from_line(line)[7])
        counter += 1

print(round(max_math_score_total / counter, 3))


def get_median(list):
    list = sorted(list)
    if len(list) % 2 == 0:
        return (list[int(len(list) / 2)] + list[int(len(list) / 2) - 1]) / 2
    return list[int(len(list) / 2)]



def normalize(numbers, std=1, mean=0):
    return list(map(lambda x: (x - mean) / std, numbers))

print(normalize([10, 20], mean=15))

def sum_args(*args):
    return sum(args)

def show_keys(**kwargs):
    print(' '.join(kwargs.keys()))


def count_letters(sentence, average=False):
    each_word_len = map(lambda x: len(x), sentence.split(" "))
    if average:
        return round(sum(each_word_len) / len(sentence.split(" ")), 3)
    return sum(each_word_len)

print(count_letters("I will build my own theme park", average=True))



def always(n):
    return lambda: n

five = always(5)
print(five()) # должно вернуть 5
