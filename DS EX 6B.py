from collections import deque
def is_palindrome(string):
    dq = deque()
    for ch in string:
        if ch.isalnum():
            dq.append(ch.lower())
    while len(dq)>1:
        front = dq.popleft()
        rear = dq.pop()
        if front != rear:
            return False
    return True
if __name__=="__main__":
    text = input("Enter a string:")
    if is_palindrome(text):
        print("The given string is a palindrome.")
    else:
        print("The given string is NOT a Palindrome.")
