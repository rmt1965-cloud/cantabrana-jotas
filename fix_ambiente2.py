c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    """  ambiente: [
    'audio/ambiente/ambiente10.mp3',
    'audio/ambiente/ambiente11.mp3',
    'audio/ambiente/ambiente14.mp3',
    'audio/ambiente/ambiente15.mp3',
    'audio/ambiente/ambiente17.mp3',
  ],""",
    """  ambiente: [
    'audio/ambiente/ambiente1.mp3',
    'audio/ambiente/ambiente2.mp3',
    'audio/ambiente/ambiente3.mp3',
    'audio/ambiente/ambiente4.mp3',
    'audio/ambiente/ambiente5.mp3',
    'audio/ambiente/ambiente6.mp3',
    'audio/ambiente/ambiente7.mp3',
    'audio/ambiente/ambiente8.mp3',
    'audio/ambiente/ambiente9.mp3',
    'audio/ambiente/ambiente10.mp3',
    'audio/ambiente/ambiente11.mp3',
    'audio/ambiente/ambiente12.mp3',
    'audio/ambiente/ambiente13.mp3',
    'audio/ambiente/ambiente14.mp3',
    'audio/ambiente/ambiente15.mp3',
    'audio/ambiente/ambiente16.mp3',
    'audio/ambiente/ambiente17.mp3',
    'audio/ambiente/ambiente18.mp3',
  ],"""
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')