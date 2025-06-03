# Frequently Asked Questions

## What is Ansari? 

Ansari is an AI assistant to help increase understanding of the Islamic faith and help Muslims practise their faith more effectively. 

## Who wrote Ansari? 

Waleed Kadous ([site](http://walee.dk/home), [LinkedIn](https://www.linkedin.com/in/waleedkadous/)) is the primary author of Ansari. EndeavorPal has been helping with the web frontend and mobile applications. 

## Where do I send my thoughts, errors, feedback about Ansari? 

Please send to [feedback@ansari.chat]("mailto:feedback@ansari.chat"). It is checked daily. 

## Is there a particular Large Language Model Ansari uses? 

Ansari 2.0 and below use GPT-4-Turbo from [OpenAI](https://openai.com). We have also tried GPT-3.5-Turbo, but the accuracy really suffers. In one test, GPT-4-Turbo running Ansari got 97% accuracy; GPT-3.5-Turbo with identical prompts, tools etc, only got 77% accuracy. 

Ansari 3.0 use Claude 3.7 Sonnet from [Anthropic](https://anthropic.com). 
Sonnet was selected because of its better results over GPT-4.0 and in particular
its ability to make citations and references. 

## How is it different to GPT-4-Turbo or Sonnet, then? 

It differs in the following ways: 

- Carefully crafted system prompts to ensure information is presented from an Islamic perspective. 
- Tools specifically to retrieve Qur'an and Sunnah for retrieval augmented generation. This helps significantly reduce hallucination. 
- Has been validated on multiple Islamic data sets. 
- Is constrained to focus and answer questions primarily on topics related to Islam. 

## Is Ansari Open Source? 

Yes it is. Here is the source code for the [backend](https://github.com/ansari-project/ansari-backend) and the [frontend](https://github.com/ansari-project/ansari-frontend). 

## Does Ansari cost money? 

Users do not have to pay anything to use Ansari. However, LLMs are very expensive to use (especially high end ones like GPT-4-Turbo and Claude Sonnet). So each request and response costs about 5c or so.

