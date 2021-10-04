H, M = map(int, input().split())
if(H <= 23 and M >= 45):
    M -= 45
    print(str(H) + " " + str(M))
elif(H <= 23 and H == 0 and M < 45):
    H = 23
    M = M+60-45
    print(str(H) + " " + str(M))
elif(H <= 23 and H > 0 and M < 45):
    H -= 1
    M = M+60-45
    print(str(H) + " " + str(M))
