
![Logo](https://i.ibb.co/fq7VSQ9/Detect-Bot.png)

A Twitter bot that analyzes an image attached to a tweet and replies if the image is ‘most probably fabricated’ or not

Twitter Bot: [@DetectBott](https://twitter.com/DetectBott)
## Team 

Team Oak Tree (Middle East)
- Omar Abdallah | [@Oabdalah23](https://github.com/Oabdalah23)
- Ashwarye Yadav | [@Ashwarye-Y](https://github.com/Ashwarye-Y)
- Karam Masad


## Problem
- Image Fabrication & Spread of Misinformation
    - As our own technology consistently grows, people are finding more and more enhanced ways in which they are able to fabricate images and make them seem as real as possible, otherwise known as image fabrication. With over 3.2 billion images shared online daily, how does one know which ones are real and which ones are fake? For most people, it is tough to distinguish between real and fake, with the fake being the most potent, and the reason being is these fabricated images allow people to deceive, confuse, or distract viewers, making them uncertain in their own beliefs.  
- Lack of ability to automatically check if an image is fabricated without doing intensive research to find the original image
    - As this calls upon an immensely time-consuming task, most regular users will not go to the lengths of searching if any of the images they are seeing are true or not, in fact during a 2018 study conducted by MIT Sloan professor Sinan Aral and Deb Roy and Soroush Vosoughi of the MIT Media Lab, it was found that falsehoods/misinformation is 70% more likely to be retweeted than the truth, and will reach the first 1500 people six times faster, indicating how the lack of verification tools can allow for this information to rapidly grow and create a false idea regarding various topics within a global social media platform.
 
## Target Audience
- Regular Twitter Users
    - The regular Twitter user uses social media daily and is constantly exposed to fabricated images and information without being aware. Often, images that are fabricated are what may interest the regular Twitter user and, as a result, grab their attention onto misinformation. The large number of people who use Twitter (330 Million monthly active users) should be able to access their favorite social media platform without the constant worry that they are being fed misinformation and illegitimate images.
- Journalists
    - With journalists being critical for the general public as they act as a source of news, it is extremely important that they are able to get access to verified information as quickly as possible, and preferably through a straightforward method; however, as of now many platforms do not offer a fact-checking system that makes it easy for journalists, such that they must have to source external verification tools and thus, (as stated earlier) only about 11-25% of journalists actually verify their information via certain verification tools.  It is essential that they can gain truthful information quickly and efficiently so that they can spread it and allow the general public to gain knowledge about certain topics as quickly as possible. 

## Solution Outcome
- Fast & Easy detection of fabricated images
- Less spread of misinformation/disinformation

## AI Model (ManTraNet)
- ***TensorFlow Backend Utilized***
    - Keras
    - TensorFlow is a library for machine learning tasks and Keras runs on top of it and is defined to be a high-level neural network library, it is usually used as it has built-in python thus making it more user-friendly
    - Keras’s simple framework allows us to build, train, and test our machine learning models quickly and efficiently, an important feature to utilize during short hackathons
- ***Two Sub-Networks***
    - Image Manipulation Trace Feature Extractor
        - This network is sensitive to different manipulation techniques, detecting and encoding the location of image manipulation into a fixed dimension feature vector
    - Local Anamoly Detection Network
        - Compares the dominant feature averaged from a local region to a local feature. Depending on the deviation from the reference feature, values can indicate signs of image manipulation

[ManTraNet Github Repository](https://github.com/ISICV/ManTraNet)

## Video Pitch

####Click Image To Watch
[<img src="https://i.ytimg.com/vi/n-PCkDQ-KmA/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCfj3BbD_jl4T8_a-dpTbIqEsMvBw" width="50%">](https://www.youtube.com/watch?v=n-PCkDQ-KmA "Now in Android: 55")


## Bot Replies (Active)
#### Example One
![One](https://i.ibb.co/X4FPcYZ/Screen-Shot-2022-07-25-at-5-51-23-AM.png)

#### Example Two
![Two](https://i.ibb.co/RTbgHkB/Screen-Shot-2022-07-25-at-5-51-57-AM.png)

#### Example Three
![Three](https://i.ibb.co/604XHXz/Screen-Shot-2022-07-25-at-5-51-34-AM.png)

## Media
![Media](https://i.ibb.co/R3tTKPB/Untitled-1280-1780-px.png)


## Deployment

To deploy the twitter bot run

```bash
  python3 twitterBot.py
```


## Twitter Auth API Reference

#### Get all items

Replace 'XXX' in authCredentials.py with your Twitter Developer App keys


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
| `api_secret_key` | `string` | **Required**. Your API secret key |
| `access_token` | `string` | **Required**. Your access token|
| `access_token_secret` | `string` | **Required**. Your access token secret|



## Acknowledgements

 - [ManTraNet AI Model](https://github.com/ISICV/ManTraNet)
 - [Create Twitter Bot Using Tweepy](https://auth0.com/blog/how-to-make-a-twitter-bot-in-python-using-tweepy/)


## Feedback

If you have any feedback, please reach out to us at detectbottwitter@gmail.com


## License


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


