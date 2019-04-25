import requests
import random
import time

requests.packages.urllib3.disable_warnings()

user_agent_list = [
	#Chrome
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	#Firefox
	'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
	'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
	'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

proxy_list = [
	'182.253.67.42:8080',
	'89.186.1.215:53281',
	'69.130.120.228:46439',
	'213.6.7.51:80',
	'178.20.231.218:80',
	'190.184.144.146:46456'
	'103.254.126.182:34324',
	'116.212.109.42:63141',
	'91.225.109.186:37271',
	'103.111.134.85:31194',
	'4.34.50.189:55656',
	'27.147.167.98:60510',
	'186.224.94.6:48957',
	'103.254.185.219:41968',
	'157.230.244.41:3128',
	'178.128.153.253:3128',
	'104.248.159.30:8080',
	'157.230.33.25:8080',
	'157.230.240.140:8080',
	'157.230.33.168:8080',
	'167.99.74.148:8080',
	'167.99.148.235:3128',
	'138.197.108.5:3128',
	'82.114.78.82:45449',
	'202.52.114.67:35066',
	'95.181.37.114:54244'
	
]


def sneakyRequest(url):
	#Pick a random user agent
	user_agent = random.choice(user_agent_list)
	#Set the headers 
	headers = {'User-Agent': user_agent}
 	#pick a random proxy
	proxy = random.choice(proxy_list)
	
	try:
		print("attempting sneaky request to %s via proxy %s" % (url, proxy))
		r = requests.get(url, verify = False, headers = headers, proxies = {'http':proxy, 'https':proxy})

		if 'Buffy' in r.text:
			print (r.text)
			return r.text
		else:
			delay = random.randint(2,5)
			print("Page returned doesn't mention buffy. We're being blocked? Dumping to blocked.hml; Will delay %i secs and try again." % delay)
			with open('blocked.html', 'w+') as f:
				f.write(r.text)

			time.sleep(delay)
			sneakyRequest(url)
		
		
	except requests.exceptions.ProxyError:
		print("Proxy %s not working right now. Trying again..." % proxy)
		sneakyRequest(url)
	except urllib3:
		print("Proxy %s not working right now. Trying again..." % proxy)
	except:
		print("some other error?  Trying again...")

