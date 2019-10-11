
# list와 string은 밀접
characters = list('abcdef')
print(characters)

# 문자열을 특정 기호를 기준으로 쪼개 리스트화
words = 'Hello World는 프로그래밍을 배우기 아주 좋은 사이트입니다.'
words_list = words.split()
print(words_list)

nowDate = '19:10:11'
nowDate_list = nowDate.split(':')
print(nowDate_list)

# 리스트를 문자열로 만들기
words_str = ' '.join(words_list)
print(words_str)

nowDate_str = ':'.join(nowDate_list)
print(nowDate_str)