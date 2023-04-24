# https://www.acmicpc.net/problem/10808

s = input()
# A : 65, a : 97
result = [0]*26
for i in s:
    result[ord(i)-97] += 1
# join 시에 값이 숫자인 경우 for문 & 값 str 처리
print(' '.join(str(ch) for ch in result))