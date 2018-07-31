with open('filter.txt') as f:
    content = f.read()
    content = content.split(',')
    user_input = input("请输入一段字符：")
    for word in content[:-1]:
        word = word.strip('\n')
        if word in user_input:
            user_input = user_input.replace(word, '**')
print(user_input)
