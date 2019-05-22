age = int(input("나이를 입력하십쇼.\n"))

if age < 1:
    print("어디서 사기를 칩니까?");
    exit();
elif age <= 5:
    print("5이상이군요 아이입니다.");
    exit();
elif age <= 8:
    print("8이상이군요 초등학생입니다.")
    exit()
