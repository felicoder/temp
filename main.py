import requests
import threading
import time


image_paths = ['fetlife-pics/1.jpg', 'fetlife-pics/2.jpg', 'fetlife-pics/3.jpg', 'fetlife-pics/4.jpg', 'fetlife-pics/5.jpg', 'fetlife-pics/6.jpg']
def fetch_data():
    while True:
        try:
            response = requests.get("https://fetbotpro.pythonanywhere.com/get_fetusers")
            data = response.json()
            if data:  # Check if data is not empty
                # Pass the first item of the array to the thread
                threading.Thread(target=process_data, args=(data[0],)).start()
            else:
                print("No data received.")
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        time.sleep(30)  # Wait for 10 seconds before the next fetch

def process_data(item):
    # Process the first item here
    # For demonstration, we'll just print it
    print(f"Processing: {item}")
    username = item['username']
    email = item['email'] 

    # Now, delete the user
    try:
        
        delete_url = f"https://fetbotpro.pythonanywhere.com//delete_fetuser?usr={username}"
        delete_response = requests.get(delete_url)  # Make the delete request
        # Check if the delete operation was successful
        if delete_response.status_code == 200:
            print(f"Successfully deleted user: {username}")
        else:
            print(f"Failed to delete user: {username}, Status code: {delete_response.status_code}")
    except requests.RequestException as e:
        print(f"Request to delete user failed: {e}")
    for i in range(3):
        time.sleep(7200)
        img_num = 0
        def send_img_4(email):
            image_paths = ['fetlife-pics/1.jpg', 'fetlife-pics/2.jpg', 'fetlife-pics/3.jpg', 'fetlife-pics/4.jpg', 'fetlife-pics/5.jpg', 'fetlife-pics/6.jpg']
            api_key = '07998EE152D27336815DDEFA5715671D303881059E5660C8BC31789C6F9B924295439372A4AFFF515B5C3BA807358D01'  # Replace with your actual API key
            from_email = 'fetbotpro@gmail.com'  # Replace with your verified from address
            to_email = email
            subject = 'Avatar: I love making people look at my photos and watch while their dick gets bigger, its kind of an obsession i have <3. pss remember to check my bio so that we can chat'
            body_text = 'Please find the attached images.'
            body_html = '<html><body><p>Please find the attached images.</p></body></html>'
            image_paths = [image_paths[img_num], image_paths[img_num+1]] # Replace with the actual paths to your images

            # Elastic Email URL for sending email
            url = 'https://api.elasticemail.com/v2/email/send'

            # Payload with the data to be sent
            payload = {
                'apikey': api_key,
                'from': from_email,
                'fromName': 'Your Name',  # Replace with your name or your company's name
                'to': to_email,
                'subject': subject,
                'bodyText': body_text,
                'bodyHtml': body_html,
                'isTransactional': True,
            }

            # Files to be sent
            files = {}
            for i, image_path in enumerate(image_paths, start=1):
                file_key = f'file_{i}'
                with open(image_path, "rb") as image_file:
                    files[file_key] = (f'{i}.jpg', image_file.read(), 'image/jpeg')

            # Sending the request
            try:
                response = requests.post(url, data=payload, files=files)
                if response.status_code == 200:
                    print('Email sent successfully with attachments!')
                    print(response.text)  # This will print Elastic Email's response
                else:
                    print(f"Failed to send email, status code: {response.status_code}")
                    print(response.text)  # This will print Elastic Email's response, including any errors
            except Exception as e:
                print(f"An error occurred: {e}")
        send_img_4(email)
        img_num += 2
        
    

if __name__ == "__main__":
    threading.Thread(target=fetch_data).start()
