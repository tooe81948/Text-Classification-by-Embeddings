# Text-Classification-by-Embeddings

It takes text data and converts it into vectors before training it with a machine learning model.

link colab : https://colab.research.google.com/drive/1WfxCi8Vl1DkTb4Evaa30ntdRDHQXZTMI?usp=sharing <br>
kaggle : https://www.kaggle.com/competitions/fake-news/leaderboard <br>
sentence transformers : https://www.sbert.net/ <br>

How to install environment <br>

```
PYTHON VERSION = 3.9.16 
pip install -r requirements.txt
```

Model Embeddings
  
```
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
```

Model Machine Learning <br>
- Sklearn : Multilayer Perceptron Classifier (MLP)
  
```
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
```

