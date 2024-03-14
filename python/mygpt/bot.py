import google.generativeai as gpt

file = open("C:\\Users\\amera\\OneDrive\\Desktop\\python\\mygpt\\answer.txt","w")

prompt = input("question please")

gpt.configure(api_key='AIzaSyBpwknLrtL2QOGaXm5K4i1j4xSHfgY1bFU')
geminipro = gpt.GenerativeModel('gemini-pro')
response = geminipro.generate_content(prompt)

# print(response.text)
try:
    file.writelines(response.text)
    print("got the answer")
except FileNotFoundError:
    print("Data not found ")

file.close()