import turtle
from random import randint

# Çizim tahtasını ayarla
drawingBoard = turtle.Screen()
drawingBoard.setup(1200,1200,None,None)
drawingBoard.bgcolor('#33FFFF')  # Arka plan rengini ayarla
drawingBoard.title('Turtle Projesi')  # Pencere başlığını ayarla

# Yazı tipi ve başlangıç değerleri
font = ("Verdana", 25, "normal")
score = 0
time_left = 60
durum = "false"

# Puanı göstermek için bir turtle oluştur
turtleScore = turtle.Turtle()
turtleScore.color("white")  # Puan yazısının rengini beyaz yap
turtleScore.hideturtle()  # Yazı turtle'ını gizle
turtleScore.penup()  # Pen uçlarını kaldır
turtleScore.goto(0, 50)  # Puan yazısını yukarıda ortala
turtleScore.write(arg=f"Puan: {score}", move=0, align="center", font=font)

# Süreyi göstermek için bir turtle oluştur
countdown_turtle = turtle.Turtle()
countdown_turtle.color("white")  # Süre yazısının rengini beyaz yap
countdown_turtle.hideturtle()  # Yazı turtle'ını gizle
countdown_turtle.penup()  # Pen uçlarını kaldır
countdown_turtle.goto(0, 0)  # Süre yazısını puanın altına ortala

# Yeniden başlatma mesajını göstermek için yeni bir turtle oluştur
restart_turtle = turtle.Turtle()
restart_turtle.color("white")
restart_turtle.hideturtle()
restart_turtle.penup()
restart_turtle.goto(0, -50)  # Yeniden başlatma mesajını ortada göstermek için

# Rastgele turtle'ı gösterme fonksiyonu
def rastgale():
    global rastgaleTurtle
    if durum == "false":
        rastgaleTurtle = turtle.Turtle()
        rastgaleTurtle.hideturtle()  # Başlangıçta gizle
        rastgaleTurtle.penup()  # Pen uçlarını kaldır
        rastgaleTurtle.color("dark green")  # Turtle rengini koyu yeşil yap
        rastgaleTurtle.shape("turtle")  # Turtle şekli
        rastgaleTurtle.shapesize(3, 2)  # Turtle boyutunu ayarla
        rastgaleTurtle.goto(randint(-drawingBoard.window_width() // 2, drawingBoard.window_width() // 2),
                            randint(-drawingBoard.window_height() // 2, drawingBoard.window_height() // 2))
        rastgaleTurtle.showturtle()  # Turtle'ı göster
        rastgaleTurtle.onclick(handle_click)  # Turtle'a tıklama olayını ekle

        # Turtle'ı 1000 milisaniye (1 saniye) sonra gizle
        def hide_turtle():
            rastgaleTurtle.hideturtle()

        drawingBoard.ontimer(hide_turtle, 1000)  # 1 saniye sonra hide_turtle() fonksiyonunu çağır

    # Rastgele bir süre sonra yeni turtle oluştur
    drawingBoard.ontimer(rastgale, 2000)  # 2 saniye sonra rastgale() fonksiyonunu çağır

# Puanı güncelle
def update_score():
    turtleScore.clear()  # Eski puanı temizle
    turtleScore.write(arg=f"Puan: {score}", move=0, align="center", font=font)  # Yeni puanı yaz

# Süreyi güncelle
def update_time():
    global time_left
    global durum
    countdown_turtle.clear()  # Eski süreyi temizle
    countdown_turtle.write(arg=f"Süre: {time_left} Saniye", move=0, align="center", font=font)  # Yeni süreyi yaz

    if time_left > 0:
        time_left -= 1
        drawingBoard.ontimer(update_time, 1000)  # Her saniye update_time() fonksiyonunu çağır
    else:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Oyun Bitti...Scor: {score}", move=0, align="center", font=font)
        durum = "true"
        show_restart_message()  # Yeniden başlatma mesajını göster

# Fare tıklamasını işleyen fonksiyon
def handle_click(x, y):
    global score
    if durum == "false":
        score += 1
        update_score()  # Puanı güncelle

# Oyun durumunu sıfırlayan fonksiyon
def reset():
    global score
    global time_left
    global durum
    score = 0
    time_left = 60
    durum = "false"
    update_score()
    update_time()
    restart_turtle.hideturtle()  # Yeniden başlatma mesajını gizle

# Yeniden başlatma mesajını göstermek için fonksiyon
def show_restart_message():
    restart_turtle.showturtle()
    restart_turtle.write(arg="Yeniden Başlatmak İçin Tıklayın", move=0, align="center", font=font)
    restart_turtle.onclick(lambda x, y: reset())


# Süreyi başlat
update_time()
# İlk turtle'ı başlat
rastgale()
# İlk puan güncellemesi
update_score()

# Pencerenin açık kalmasını sağla
drawingBoard.mainloop()
