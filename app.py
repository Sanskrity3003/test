from flask import Flask, render_template, request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    # Collaborative filtering recommendation
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    collaborative_rec = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        collaborative_rec.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))

    # Popularity-based recommendation
    popular_rec = popular_df['Book-Title'].tolist()

    # Hybridize recommendations
    hybrid_rec = list(set(collaborative_rec + popular_rec))[:10]  # Combine and get top 10 unique recommendations

    # Fetch details of recommended books
    data = []
    for title in hybrid_rec:
        temp_df = books[books['Book-Title'] == title]
        data.append([title, temp_df['Book-Author'].iloc[0], temp_df['Image-URL-M'].iloc[0]])

    return render_template('recommend.html', data=data)

