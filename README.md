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


## Architecture

Karlos is an AI assistant powered by AI and as such, a lot of its complexity lays on the prompt structure, assistant logic and assistant tools, this initial schema however, is purely representative of the data flow.

![image](https://github.com/user-attachments/assets/644c8d72-3936-482b-a766-09a3f201acad)

### User input
Every interaction with the API starts with a user conversation, we do not initiate conversation with customers.

### Twilio
Twilio works as a bridge between our business logic and the agent's AI, its primary function is to pass information into a dedicated API.

### API
As Restful API's are inherently stateless, we needed another way to handle small and temporary state data, as such, the API works in a way where it will first check for existing cache, if there is no cache available for the user, it will then create an openAI thread, fetch its ID value, then create a mapping into redis where the key is the user's whatsapp identifier and the value is the id of the thread they are on, since we dont handle data directly on the API, the is no need to save anything else.

### Redis
its a small single schema db that stores openai thread ids using user's whatsapp identifier as key values, this data is alive for 30 minutes after its last update.

### OpenAI
We will get into more depth about the prompt architecture on a following section.

### Twilio 
When everything is set and done, we will not respond to the webhook twilio sends as it is likely to fail due to the extended wait times we can expect from openAI's assistant tools, so what we do is call a send api request to send a message directly after the process is completed.

## Prompt Architecture

The prompt architecture is quite simple, but it is worth explaining a little bit about it.

![image](https://github.com/user-attachments/assets/41df51e4-33e3-46bd-ba17-f96abb8acd03)

### Agent Upsert
The first check our API will do, is check if an agent exist on the openAI account, and if it doesnt,  then create it. this is done to allow the user to provide different configuration keys without needing to manually configure the assistant on openAI's UI.

### Thread Upsert
As explained on the previous section, if a thread exists on cache, we will use the existing thread Id, if it doesnt, then we are going to create a new thread, and save that data into redis for future use.

### Create message
We will pass the user's message into the assistant's thread

### Create and Poll
This step will make the assistant, poll the new message and respond to it depending on context, sometimes, an assistant will need to use one of the tools it was configured to work with in order to perform a task, in that case, we will execute that functionality in the API, add the tool response onto the thread and poll again, we shall repeat this until no further tool is needed.

### Return last message
After a thread has been polled and no other tool is required, we will fetch the response from the model, and return this to the API to handle.

## Open AI Assistant API vs regular ChatGPT
You might have notice by now that we are using open AI's Assistant API rather than the regular chatGPT endpoints.

There are a couple of reasons for this decision, namely, we wanted to provide the customer with a very specific functionality, ChatGPT can be manipulated to ignore its instructions and function as any ChatGPT instance, this can cause alucinations, irrelevant info dump, or even innapropiate behavior.

ChatGPT also opens the door to malicios actors who might try to abuse the agent to get access to a free of restrictions OpenAI key, with assistants we have more tools to prevent such things from happening.

### Response times
A huge disadvantage on using Assistants instead of ChatGPT, is the waiting, Assistants are quite slower than the regular ChatGPT APi, which can be frustating for some users, but the more reliable responses compensates for the wait time most of the time.

### Tools
Karlos uses 2 tools for the time beign. `fetch_vehicles_data` and `fetch_credit_estimate`.

### fetch_vehicles_data
This function reads a csv file containing data of available vehicles, it uses this information to make suggestions to the customers and to fetch the stock Id, which is needed for the next function.

### fetch_credit_estimate
This functions creates a credit estimate using the user's prefered vehicle, the price of it, the downpayment on a 10% interest rate


 

