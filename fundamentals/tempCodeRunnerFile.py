
# os.environ['API_KEY'] = os.getenv('API_KEY')
# genai.configure(api_key=os.environ['API_KEY'])
# model = genai.Model('gemini-pro')

# def generate_text(prompt):
#     response = model.generate(prompt=prompt)
#     return response.text

# while True:
#     user_input = input("Enter your prompt: ")
#     if user_input == "quit":
#         break
#     response = generate_text(user_input)
#     print(response)