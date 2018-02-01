from fake_useragent import UserAgent
import requests

lines = [line.rstrip('\n') for line in open('tt.txt')]
ua = UserAgent()
a='ea78570b2a48693a6c6ba26455cf263f1ac00e21edb7c70fbc86e3cc6c4931061df20f67ad96a232580ebe8d6714f4bfde5455074b10d4396d92ace15a99238e3078132467042812543259b34f862f48c7422e608bdde8bc92bdbaad8079b484be07606476491a2a246480d8b6de50c3144740ac388a12d12c2120b2a6226aa9'

cookie = {'uid': a}
header = {'User-Agent':str(ua.chrome)}

url = "http://pin.ctf.tamu.edu/login/"

r = requests.post(url,data={"pin": '111'}, headers=header)
print(r.text)