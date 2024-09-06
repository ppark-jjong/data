def is_vps(ps):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # 스택이 비어 있는데 ')'가 온 경우
                return "NO"
            stack.pop()  # '('와 짝을 맞추기 위해 pop
    
    if not stack:  # 모든 괄호가 짝이 맞아 스택이 비어 있으면 VPS
        return "YES"
    else:
        return "NO"

def main():
    T = int(input())  # 테스트 케이스의 수
    for _ in range(T):
        ps = input().strip()  # 한 줄의 괄호 문자열
        print(is_vps(ps))  # VPS 여부 출력

if __name__ == "__main__":
    main()
