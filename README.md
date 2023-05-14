# Aqua-Password-Manager

A secure password manager with end-to-end encryption. More on that later

Features:

- Cloud saving: Saves every password to the cloud.
- Secure encryption: Even if our server gets hacked your passwords are safe
- Secure Database: We use a key-value database called Redis, wich isn't vulnerable to database attacks
- If you want to use your own Redis database, we have a tutorial at the bottom
- Open-Source
- Comes with a secure password generator


# Encryption

Our program uses AES-256 encryption which is the most secure algorithm in the world
You will get a key during registration, write down to a paper or somewhere (DONT SAVE IT ON THE COMPUTER BECAUSE IF IT GET HACKED THEY CAN DECRYPT EVERY PASSWORD)
Or, theres a half-secure option, to save it to the cloud (Not reccomended)

# Database
We use a key-value database called Redis![kép](https://github.com/RedStone45789/Aqua-Password-Manager/assets/127690373/d56f3e72-7657-4e07-bc8c-cbf905c28afa)

# Offline-mode

If you dont trust our servers you can save it to your local pc or your own database (Redis)

# 
