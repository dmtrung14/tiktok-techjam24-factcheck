# tiktok-techjam24-factcheck
## TL;DR
Please like our project on [devpost](https://devpost.com/software/tiktok-factcheck) and [Youtube](https://www.youtube.com/watch?v=Q88AerLjSpM). This project is a part of [TikTok TechJam 2024](https://tiktoktechjam2024.devpost.com/)

![logo](/assets/logo.png)


## Inspiration
Every day, millions of users spend hours browsing TikTok videos. The attention to short content is unequivocally high. Nonetheless, this also poses a challenge: how do _news, science, and information show_ compete with music covers and comedy sketches to find a place in a world of short-form entertainment? **FactCheck** solves this problem by gamifying information videos to capture user attention. Through the short pop quiz, we hope to introduce a novel form of _"TL;DR"_ for media files and deliver information in 10-15 seconds.

## What it does
- **State-of-the-art**: We adapted a state-of-the-art Generative AI model to extract the content of uploaded videos and provide a small pop quiz for users.  
- **Extensive**:  The model is extensively trained to cover a wide range of topics, including but not limited to Science & Technology, Finance, Sports, Healthcare, and Politics. 
- **Personalized**:  Additionally, the quiz will be provided in the user's preferred language to promote equal access to the tool.

## How we built it
We used the [Qwen2](https://huggingface.co/docs/transformers/en/model_doc/qwen2) model with 1.5 billion parameters to generate the quiz for the video.  The model can adapt its response to a specified conversation history, enabling tailored responses and ensuring ethical constraints to generated questions.

Our application is developed using _Flutter_ and made available on iOS 14+ operations systems, with a _fastapi_ backend. Our model is preloaded, and generated quizzes are also cached in a _Firestore (Firebase)_ database to enable quick access for other users. 

## Challenges we ran into
- **Ethics of AI**: How to tune the model to fit with the ethical values of AI: accuracy of information, denial of service for prohibited contents, and respect for users' privacy.
- **Data & Privacy**: Collecting users' preferences without encroaching on their privacy.
- **Balancing Human & AI Expertise**: How to use AI efficiently but still stay consistent with the educational intentions of the creators. 

## Accomplishments that we're proud of
- Devised a new way to access information for TikTok users
- Enabled fast generation for content creators using state-of-the-art Generative AI and fast access for users using streamlined backend protocols
- Bridged the gap between short-form content and educational channels.

## What we learned
- How to apply Generative AI to solving a real-world pressing problem
- TikTok FactCheck requires continuous development to match the trends and needs of the online world. 
- Balancing the use of AI with ethical constraints.

## What's next for TikTok FactCheck
Applications are generally more useful when people can interact with each other. Some possible features are:
- Build leaderboards and scoring systems for users to share.
- Sharing quizzes/videos they find interesting and "challenge" their friends.

## About Us
We are:
- [Trung Dang](https://github.com/dmtrung14), Senior at University of Massachusetts Amherst
- [Giap Nguyen](https://github.com/giaphoang), Junior at University of Massachusetts Amherst
- [Hung Nguyen](https://github.com/HungNT1st), Senior at University of Massachusetts Amherst
