from hashlib import sha256

secret_phrase = "bolognese"

def get_hash_with_secret_phrase(input_data, secret_phrase):
    combined_data = input_data + secret_phrase
    return sha256(combined_data.encode()).hexdigest()
    
email_body = "Hello, I hope you are doing well. I am writing to you to inform you that I have received the package. The package number is 1.23454.Thank you."

print(get_hash_with_secret_phrase(email_body, secret_phrase))