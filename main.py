import requests
import json


cookies = {
    'autologin_trustie': '769ccb0b779f1aaed62d50285254937b9d0f8a66',
    '_educoder_session': 'bda0f486d46b4c2c6d79bbd3226606c6',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=utf-8',
    # 'Cookie': 'autologin_trustie=32b5eb46affa9938767e1df78a4d7eed9f45ec8c; _educoder_session=c2c66ba1be4598db29b094306a7914ca',
    'If-None-Match': 'W/"fed76e8f489a7314b892a5e2b12d0104"',
    'Origin': 'https://www.educoder.net',
    'Pc-Authorization': 'bda0f486d46b4c2c6d79bbd3226606c6',
    'Referer': 'https://www.educoder.net/classrooms/FO4WQPAR/exercise/99351/users/p2ifxpo5f?check=true',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'X-EDU-Signature': '38240b9dcace8dedbc12bc1fa5efc8a6',
    'X-EDU-Timestamp': '1718372975606',
    'X-EDU-Type': 'pc',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    # 'coursesId': 'c5lq4tef',
    # 'categoryId': '52638',
    # 'login': 'm74arxswq',
    # 'exerciseId': '52638',
    # 'zzud': 'm74arxswq',
}

response = requests.get(
    'https://data.educoder.net/api/exercises/99350/user_exercise_detail.json',
    params=params,
    cookies=cookies,
    headers=headers,
)

#打印结果
print(response.text)

# 假设response.text包含了从API获取的JSON数据
json_data = response.text

# 将JSON字符串解析为Python字典
data = json.loads(json_data)

# 提取练习的基本信息
exercise_id = data['exercise']['id']
exercise_name = data['exercise']['exercise_name']
exercise_description = data['exercise']['exercise_description']

print(f"练习ID: {exercise_id}")
print(f"练习名称: {exercise_name}")
print(f"练习描述: {exercise_description}")

# 提取题目类型和数量
question_types = data['exercise_question_types']
for question_type in question_types:
    type_name = question_type['name']
    type_count = question_type['count']
    print(f"题目类型: {type_name}, 数量: {type_count}")

# 定义选项
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
letters_index = 0

#定义题目编号
question_index = 1

# 提取单选题信息
single_choice_questions = [q for q in question_types if q['question_type'] == 0]
if single_choice_questions:
    single_choice_count = single_choice_questions[0]['count']
    print(f"单选题数量: {single_choice_count}")
    for item in single_choice_questions[0]['items']:
        question_title = item['question_title']
        standard_answer_show = item['standard_answer_show']
        print(f"{question_index}. {question_title}")
        question_index+=1
        print(f"答案: {standard_answer_show}")
        for choice in item['question_choices']:
            current_letter = letters[letters_index]
            letters_index+=1
            choice_text = choice['choice_text']
            print(current_letter + f". {choice_text}")
        letters_index = 0 #初始化
    question_index = 1 #初始化

multiple_choice_questions = [q for q in question_types if q['question_type'] == 1]
if multiple_choice_questions:
    multiple_choice_count = multiple_choice_questions[0]['count']
    print(f"多选题数量: {multiple_choice_count}")
    for item in multiple_choice_questions[0]['items']:
        question_title = item['question_title']
        standard_answer_show = item['standard_answer_show']
        print(f"{question_index}. {question_title}")
        question_index+=1
        print(f"答案: {standard_answer_show}")
        for choice in item['question_choices']:
            current_letter = letters[letters_index]
            letters_index+=1
            choice_text = choice['choice_text']
            print(current_letter + f". {choice_text}")
        letters_index = 0 #初始化
    question_index = 1 #初始化


# 提取判断题信息
true_false_questions = [q for q in question_types if q['question_type'] == 2]
if true_false_questions:
    true_false_count = true_false_questions[0]['count']
    print(f"判断题数量: {true_false_count}")
    for item in true_false_questions[0]['items']:
        question_title = item['question_title']
        standard_answer_show = item['standard_answer_show']
        print(f"题目: {question_title}")
        print(f"答案: {standard_answer_show}")

# 提取填空题信息
fill_blank_questions = [q for q in question_types if q['question_type'] == 3]
if fill_blank_questions:
    fill_blank_count = fill_blank_questions[0]['count']
    print(f"填空题数量: {fill_blank_count}")
    for item in fill_blank_questions[0]['items']:
        question_title = item['question_title']
        standard_answer = item['standard_answer']
        answer_text = [item['answer_text'] for item in standard_answer]
        print(f"题目: {question_title}")
        print(f"答案: {answer_text}\n")