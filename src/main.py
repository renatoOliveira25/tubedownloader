from pytubefix import YouTube

# Solicita a URL do vídeo ao usuário
url = input("Digite a URL do vídeo do YouTube que deseja baixar:\n")

try:
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("✅ Download concluído com sucesso!")
except Exception as e:
    print(f"❌ Erro ao baixar: {e}")