import csv

samples = ["samples"]
tf_list = ["names"]
points = list()
def ready_up(char = None, tests = None):
    first_names = []
    last_names = []
    countries = []
    colors = []
    objects = []
    foods = []
    with open('esm_famil_data.csv') as words:
        lines_in_words = csv.reader(words)
        lines_in_words = list(lines_in_words)
        for i in range(1, 168):
            first_names.append(lines_in_words[i][0])
            if lines_in_words[i][1] != "":
                last_names.append(lines_in_words[i][1])
            if lines_in_words[i][2] != "":
                countries.append(lines_in_words[i][2])
            if lines_in_words[i][3] != "":
                colors.append(lines_in_words[i][3])
            if lines_in_words[i][4] != "":
                objects.append(lines_in_words[i][4])
            if lines_in_words[i][5] != "":
                foods.append(lines_in_words[i][5])
        # print(first_names)
        # print(last_names)
        # print(countries)
        # print(colors)
        # print(objects)
        # print(foods)
    if char != None:
        valid_first_names = []
        valid_last_names = []
        valid_countries = []
        valid_colors = []
        valid_objects = []
        valid_foods = []
        for i in range(len(first_names)):
            fname = first_names[i]
            if fname[0] == char:
                valid_first_names.append(first_names[i])
        for i in range(len(last_names)):
            last = last_names[i]
            if last[0] == char:
                valid_last_names.append(last_names[i])
        for i in range(len(countries)):
            place = countries[i]
            if place[0] == char:
                valid_countries.append(countries[i])
        for i in range(len(colors)):
            paint = colors[i]
            if paint[0] == char:
                valid_colors.append(colors[i])
        for i in range(len(objects)):
            thing = objects[i]
            if thing[0] == char:
                valid_objects.append(objects[i])
        for i in range(len(foods)):
            eatable = foods[i]
            if eatable[0] == char:
                valid_foods.append(foods[i])
        # print(valid_first_names)
        # print(valid_last_names)
        # print(valid_countries)
        # print(valid_colors)
        # print(valid_objects)
        # print(valid_foods)

        result = [tests[0]]
        name1 = tests[1]
        if name1 in valid_first_names:
            result.append(True)
        elif name1.isalpha() == False:
            result.append(None)
        else:
            result.append(False)
        last1 = tests[2]
        if last1 in valid_last_names:
            result.append(True)
        elif last1.isalpha() == False:
            result.append(None)
        else:
            result.append(False)
        place1 = tests[3]
        if place1 in valid_countries:
            result.append(True)
        elif place1.isalpha() == False:
            result.append(None)
        else:
            result.append(False)
        paint1 = tests[4]
        if paint1 in valid_colors:
            result.append(True)
        elif paint1.isalpha() == False:
            result.append(None)
        else:
            result.append(False)
        thing1 = tests[5]
        if thing1 in valid_objects:
            result.append(True)
        elif thing1.isalpha() == False:
            result.append(False)
        else:
            result.append(False)
        eatable1 = tests[6]
        if eatable1 in valid_foods:
            result.append(True)
        elif eatable1.isalpha() == False:
            result.append(None)
        else:
            result.append(False)
        return result


def add_participant(participant, answers):
    tests = [participant, answers['esm'], answers['famil'], answers['keshvar'], answers['rang'], answers['ashia'], answers['ghaza']]
    character = ""
    samples.append(tests)
    for i in range(1, len(tests)):
        if tests[i].isalpha():
            character = tests[i][0]
    tf_list.append(ready_up(character, tests))


def calculate_all():
    empty_spaces = []
    same_answers = []
    for i in range(1, len(tf_list)):
        for j in range(1, 7):
            if tf_list[i][j] == None:
                empty_spaces.append(j)
            for k in range (1, len(tf_list)):
                if samples[i][j] == samples[k][j] and k != i:
                    same_answers.append(j)
                    same_answers.append(i)
                    same_answers.append(j)
                    same_answers.append(k)

    for i in range(1, len(tf_list)):
        scores = [tf_list[i][0]]
        for j in range(1, 7):
            same_check = [x+1 for x in (0, len(same_answers), 2) if x == j]
            print(same_check)
            if j in empty_spaces:
                if len(same_check) != 0:
                    if tf_list[i][j] == True and samples[i][j] in same_check:
                        scores.append(10)
                    else:
                        scores.append(0)
                elif tf_list[i][j] == True and samples[i][j] not in same_check:
                    scores.append(15)

            elif j not in empty_spaces:
                if len(same_check) != 0:
                    if tf_list[i][j] == True and samples[i][j] in same_check:
                        scores.append(5)
                    else:
                        scores.append(0)
                elif tf_list[i][j] == True and samples[i][j] not in same_check:
                    scores.append(10)
            else:
                scores.append(0)
        points.append(scores)
    return points

add_participant(participant = 'salib', answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
add_participant(participant = 'kianoush', answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
add_participant(participant = 'sajjad', answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
add_participant(participant = 'farhad', answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})
print(tf_list)
print(samples)
print(calculate_all())