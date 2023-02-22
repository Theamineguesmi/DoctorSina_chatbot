
# DoctorSina
Doctor Sina, a Web &amp; Mobile App, that provides its users with Artificial Intelligence "AI" based functions aiming Healthcare assistance and Distant Medical Support.
=======
<p align="center"><img src="./assets/bot.png" width="10%"></p>
<h1 align="center">Customer Care Bot</h1>
<p align="center">Customer care bot for E-Health company which can solve faq and chitchat with users, can contact directly to team.</p>

<p align="center">
  <img src="https://img.shields.io/github/pipenv/locked/python-version/horizon733/customer-care-chatbot">
  <img src="https://img.shields.io/github/pipenv/locked/dependency-version/horizon733/customer-care-chatbot/rasa?color=blueviolet&label=Rasa">
</p>



## 🛠 Features
- [x] FAQ
- [x] chitchats
- [x] Out of Scope
- [x] Contact us form
- [x] Send Emails
- [x] chat GPT api

## ⚡ Quick Setup
- Initialize a virtual environment via:
- Conda:
```bash
conda create --name rasaenv python=3.7
```
- virtualenv
```bash
virtualenv -p python3.7 rasaenv
```
- use pipenv
```
cd /customer-care-chatbot
pipenv install
```

## 🧪 Testing
- Train bot
```
rasa train
```
- Test bot on shell
```
rasa shell
```
- start `rasa` server
```bash
rasa run --enable-api --cors "*" --debug[Optional] -p {PORT}[optional]
```
- start `actions` server
```
rasa run actions -p {PORT}[Optional]
```

>>>>>>> fbd4695 (deploy chatbot)
