from PIL import Image


img = Image.open(r"C:\Users\gabri\OneDrive\Imagens\pinterest\reizinha.jpeg")

imagename = "reizinha.jpeg"

img = img.resize((32, 32))

img.save(f"{imagename.split('.')[0]}favicon.ico", format="ICO")

print("Conversão concluída! O arquivo 'favicon.ico' foi criado.")
