<p align="center">
<img src="static/images/logo-no-background.svg" alt="drawing" width="150" height="50"/> 
</p>
<p align="center">
<em>Natural Language Code For Film</em>
</p>
<p align="center">
<strong>Find movies in seconds</strong>
</p>

> Part of the project [Semantic Search AI Hackathon](https://lablab.ai/event/semantic-search-hackathon)



## Tools used

- [Cohere Ai](https://cohere.ai/)
- [PineCone](https://www.pinecone.io/)

### Running Locally

- git clone the repo
- ``pip install -r requirements.txt``
- create [pinecone](https://www.pinecone.io) and [cohere](https://cohere.ai/) account
- create ``.env`` file inside project directory and write
        ``PINECONE_API=<your_pinecone_key>``
       `` COHERE_API=<your_cohore_key>``
- run ``python main.py``


### How we made it
Dataset: [Movies Daily Update Dataset](https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies)


- The vector size is 4096(cohere-large). 
- Only 10k of 700k data being used. 
- No FineTuning!! No Preprocessing!!

<img src="assets/image.png" alt="Making of the model" width = "800" height="400">
