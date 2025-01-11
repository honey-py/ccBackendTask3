from requests import Session

username = input("Username: ")

password = input("Password: ")

url = "https://fw.bits-pilani.ac.in:8090/"
logout_magic = "010c020f0a040801"  # every previously used keepalive magic id apparently works again and can be used to logout

# curl_output = str(run(["curl", "http://detectportal.firefox.com/canonical.html"], capture_output=True))
# magic = curl_output[206:222]

session = Session()
response = session.get("http://detectportal.firefox.com/canonical.html")

magic = response.text[101:117]
# print(magic)
data = {
    "magic": magic,
    "username": username,
    "password": password
}

if "fw.bits-pilani.ac.in" in response.text:
    print("Login unsuccessful")
    # run(["curl", "https://fw.bits-pilani.ac.in:8090/", "-X", "POST", "--data-raw",
    #      f"4Tredir=http%3A%2F%2Fdetectportal.firefox.com%2F&magic={magic}&username={username}&password={password}"])
    post_response = session.post(url, data=data)
    print(post_response.text)
else:
    print("Login successful")
