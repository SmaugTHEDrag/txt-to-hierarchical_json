# Import thư viện openai
import openai

# Thiết lập khóa API của OpenAI của bạn
openai.api_key = ""

# Khởi tạo khách hàng OpenAI với khóa API
client = openai.OpenAI(api_key=openai.api_key)

# Hàm để đọc nội dung từ một tệp văn bản 
def read_text_file(filename): 
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    return content + "RESPONSE: " 
        
# Hàm để ghi nội dung vào một tệp văn bản
def write_text_file(filename, content):
    content = content.strip("```")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content + "\n")

# Đọc nội dung ban đầu từ text.txt
text_content = read_text_file("text.txt")

# Khởi tạo một danh sách các tin nhắn với nội dung ban đầu từ text.txt
messages = [{"role": "assistant", "content": text_content}]

# Nhận đầu vào từ người dùng
user_input = text_content

# Thêm đầu vào của người dùng vào lịch sử cuộc trò chuyện
messages.append({"role": "user", "content": user_input})

# Gửi tin nhắn đến OpenAI và nhận phản hồi
response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-1106:personal::9GojMIMF:ckpt-step-90",
    messages=messages,
    temperature=0,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Trích xuất câu trả lời từ phản hồi
reply = response.choices[0].message.content

# In ra câu trả lời của Bot
print(reply)

# Lưu câu trả lời của Bot vào output.json dưới dạng JSON
write_text_file("output.json", reply)
