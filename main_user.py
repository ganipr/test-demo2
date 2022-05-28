from user import User
from post import Post

user_one = User("Raju", "abc@g.com", "123456", "DevOps Engineer")
user_one.get_user_details()
user_two = User("XX", "abc@g.com", "123456", "DevOps Engineer")
user_two.get_user_details()
user_three = User("YY", "abc@g.com", "123456", "DevOps Engineer")
user_three.get_user_details()

user_post = Post("This is a test message!!!", user_one.name)
user_post.get_author_info()
