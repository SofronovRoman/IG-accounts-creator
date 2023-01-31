
import requests
import time

# the class for work with email for registration
class Tenminutesemail:
    def __init__(self):
        self.data = None
        self.content = None

    def get_email_address(self):
        self.data = requests.Session()
        self.content = self.data.get('https://10minutemail.net')
        content_text = self.content.text
        index_start = content_text.find('data-clipboard-text="') + 21
        index_end = content_text.find('"', index_start)
        return content_text[index_start:index_end]

    def get_instagram_code(self):
        start_time = time.time()
        while (time.time() - start_time < 180):
            time.sleep(5)
            content_text = self.data.get(self.content.url).text
            index_end = content_text.find(' is your Instagram code')
            if index_end > 0:
                return content_text[index_end - 6:index_end]

    def close_session(self):
        self.data.close()





