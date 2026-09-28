print("====shop====")
print("1.sword 10 bath")
print("2.bow 10 bath")
print("exit for exit")
choose=int(input("เลือกเลขสินค้าที่ต้องการซื้อ"))
money=20
play=True
while play:
    if choose==1 and money>=10:
        money=money-10
        print("you get sword")
    elif choose==1 and money<10:
        print("เงินไม่พอครับน้อง")
        break
    else:
        print("exit")
    print(f"you have monney={money}")
print("helloword")
