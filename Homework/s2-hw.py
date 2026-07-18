# [=================| Welcome message |=================]
print(
  """
                          $$\                                             
                        $$ |                                            
$$\  $$\  $$\  $$$$$$\  $$ | $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$ | $$ | $$ |$$  __$$\ $$ |$$  _____|$$  __$$\ $$  _$$  _$$\ $$  __$$\ 
$$ | $$ | $$ |$$$$$$$$ |$$ |$$ /      $$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |
$$ | $$ | $$ |$$   ____|$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$   ____|
\$$$$$\$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$  |$$ | $$ | $$ |\$$$$$$$\ 
 \_____\____/  \_______|\__| \_______| \______/ \__| \__| \__| \_______|
  """
)

# [=================| Get Information |=================]
firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")
age = int(input("Enter your : age"))
nationalID = input("Enter your nationalID: ")

# [=================| Show Information |=================]
print(
  """
  [================== YOUR INFORMATION ==================]
  |---- Firstname: {firstname}                           |
  |---- Lastname: {lastname}                             |
  |---- Age: {age}                                       |
  |---- National ID: {nationalID}                        |
  [======================================================]
  """
)

# [=================| Do math on user age |=================]
# jam
print("age + 2: ", ( age + 2 ))
# tafrigh
print("age - 10: ", ( age - 10 ))
# zarb
print("age × 3: ", (age * 10))
# taghsim
print("age ÷ 6: ", (age / 6))
# kharej ghesmat
print("kharej ghesmat age bar 6: ", (age // 6))
# baghimande
print("baghimande age bar 6: ", (age % 6))
# tavan
print("tavan 2 age: ", (age ** 2))