#plain text

txt = "안녕하세요 저는 오유라입니다. 잘 부탁드립니다.\n"
print(txt)


# 인코딩 -> 문자처리방식
# 127개 문자로 문자 처리 -> 127개의 문자를 모아놓은 것 (문자표. 캐릭터셋) -> ascii // 1바이트
# 중국이나 한국같은 경우 2바이트 이용해서 처리
# 네트워크 발전-> 웹 : 전세계 데이터가 공유.
# 유니코드로 문자표 통합. 유니코드를 처리하는 방식(utf-8)


# 1. 파일 저장
# open 함수 이용해서 파일모드 'w'로 저장
f = open('day2/file_exam/exam1_data/test.txt', 'w', encoding='utf-8-sig')

# 문자열 저장
f.write(txt)

# 문자열 여러개 저장
f.writelines(['aaa\n', 'bbb\n', 'cccc\n'])

# 파일 닫기
f.close()

# 쓰기할 때 파일모드 'w'는 덮어쓰기, 'a'는 삽입하기
f2 = open('day2/file_exam/exam1_data/test.txt', 'a', encoding='utf-8-sig')
f2.write('새로운 내용')

f2.close()

# 2. 파일 읽기
# 파일모드 'r'로 읽어옴
f3 = open('day2/file_exam/exam1_data/test.txt', 'r', encoding='utf-8-sig')

txt1 = f3.read() # 전체 읽어오기
print(txt1)

f3.seek(0)# 커서 초기화

txt2 = f3.readline() # 한줄 읽어오기
print(txt2)

f3.seek(0) 

txt3 = f3.readlines() # 한줄식 리스트로 읽어오기
print(txt3)

f3.close()

# with 구문을 사용하면 파일 사용이 끝난 후 close()를 하지 않아도 된다.
with open('day2/file_exam/exam1_data/test.txt', 'r', encoding='utf-8-sig') as f4 :
    print(f4.read())