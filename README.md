# Presenting Karlos - your AI sales agent

## Overview

Karlos is an AI assistant powered by OpenAI's infrastructured, it is developed using [Asssitants API](https://platform.openai.com/docs/assistants/overview).
It is deployed as a whatsapp assistant using [twilio conversations API](https://www.twilio.com/docs/conversations/api) 

Karlos comes with 2 main features, one of them is to provide customers with the availability of vehicles, its pricing and other relevant data for any interested customer.
![image](https://github.com/user-attachments/assets/0b54cd08-5754-4e6a-bd6d-a54e803843ba)

It is also capable of generating financing estimations out of the box!
![image](https://github.com/user-attachments/assets/ae1f356a-411f-4ee4-8298-3ed1fd4ca372)


## Getting Started

To get started with testing your very own Karlos, follow the next steps.

### 1. Clone project
```
git clone https://github.com/aleiruiz/chatbot.git
```

### 2. Install required dependencies
```
pip install -r requirements.txt
```

### 3. Get openAI keys
Go to [OpenAI's API platform](https://openai.com/es-ES/api/) create an account and get your [`api keys`](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).

### 4. Get twilio
Go to [Twilio](https://www.twilio.com/) create an account and navigate to [twilio console](https://console.twilio.com/), once there, you should be able to see your `Account SID` and your `Auth Token`.

### 5. Get access to conversations API
On Twilio console, go to explore products, look for Messagging, you should see something like this
![image](https://github.com/user-attachments/assets/01c4bbfd-c39c-41d9-8d79-587926166053)

after that, click on send whatsapp message and then on that page click on sandbox settings, you should see something like this now 

![image](https://github.com/user-attachments/assets/74180e6f-d0c1-4c04-bcbf-3bea5bef675e)

For now, we dont need to care about `When a message comes in` but save it for later as we will need to configure this later.

scroll down a bit and you will be able to see your sandbox number, send it the message on screen so that it gets activated.


### 6. Get Redis
There are multiple providers for redis, you can even setup your own local environment if you like, here is a [good guide to do that](https://medium.com/@ishara11rathnayake/setup-a-redis-in-a-local-machine-redis-clustering-120289f71df5).

### 7. Set up your local env
We are almost there! now all you need to do is open the project folder, look for the `.env.example` file, copy that file and rename the copy to just `.env`

You will see something like this

```
OPENAI_API_KEY=OPENAI_API_KEY_PLACEHOLDER
ASSISTANT_NAME=Karlos  # You can name karlos however you like! he does not mind

# Redis configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=
REDIS_SSL=true

#Twilio Configuration
TWILIO_ACCOUNT_SID=SID_PLACEHOLDER
TWILIO_AUTH_TOKEN=TOKEN_PLACEHOLDER
TWILIO_WHATSAPP_NUMBER=whatsapp:+NUMBER_PLACEHOLDER
```

Change the data with the information we gathered on previous steps.

### 8 Start the application
Run the following command on root to start the project
```
 Flask run
```

### 9 Set up Twilio webhook
now get back to the Message page we saw on step 5, if we are working on a server, we simply need to write our endpoint directly on the `When a message comes in` box.

![image](https://github.com/user-attachments/assets/74180e6f-d0c1-4c04-bcbf-3bea5bef675e)

To connect your local env to the webhook, you can use ngrok.

### 9.1 Install ngrok
```
 sudo snap install ngrok
```
or go into ngrok's official guide https://ngrok.com/docs/getting-started/

### 9.2 Point ngrok to our local env

```
ngrok http <your-app-port>
```
you need to point it to the port you are using, normally the app will be using port `5000`.

### 9.3 Open ngrok url
You will get something like this on your terminal

![image](https://github.com/user-attachments/assets/c3f6551c-5542-4982-8c17-9d86993de06e)

you should open the URL once before passing it to twilio as it will first ask you to manually turn it on

![image](https://github.com/user-attachments/assets/7fdc16d3-d1e4-4eb8-8729-b177e739237a)

### 9.4 Point twilio to ngrok

To finish it off, paste your ngrok URL into the `When a message comes in` box on twilio sandbox configuration, remember to include the endpoint `/api/twilio/inbound` to the URL.

![image](https://github.com/user-attachments/assets/7dff20c3-4955-4fe2-a649-59b3b72289f8)


### 10 Send a whatsapp message
After the configuration is done, simply send a message to you whatsapp sandbox and start chatting!


