
print("Istalgan sonni kvadratini hisoblaydi")
#birinchi calculator haqida ma'lumot beradi
savol = "Istalgan son kiriting "
#salov o'zgaruvchisiga calculator ga son kiritishini so'raydi

savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#savol o'zgaruvchisiga += shu belgini yozilsa dasturni to'xtatish uchun exit deb yozishni so'raydi va savol o'zgaruvchisiga qo'shib qo'yadi

qiymat = ""
#qiymat o'zgaruvchisiga bo'sh qiymat beriladi chunki dastur boshlanishi bilan qiymat kiritilmaydi

while qiymat != "exit":
#qiymat o'zgaruvchisiga exit deb yozilganda dastur to'xtaydi
    
    qiymat = input(savol)
    #qiymat o'zgaruvchisiga savol o'zgaruvchisiga kiritilgan qiymat beriladi
    
    if qiymat != "exit":
        #qiymat o'zgaruvchisiga exit deb yozilganda dastur to'xtaydi
        #agar qiymat o'zgaruvchisiga exit deb yozilmasa dastur davom etadi
        
        print(f"{qiymat} ning kubi {int(qiymat)**2} ga teng")
    #print deb kiritilgan qiymatning kubini hisoblaydi va ekranga chiqaradi


