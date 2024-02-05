from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from itertools import permutations

app = Flask(__name__)
CORS(app)

# Global variables
word_set = set()


@app.route('/letters', methods=['GET'])
def get_words():
    data = request.get_data()
    print(data)
    data_string = data.decode('utf-8')

    forged_words = []


    for perm in permutations(data_string):
        for i in range(len(perm)):
            for j in range(i + 1, len(perm) + 1):
                if j-i > 2:
                    possible_word = ''.join(perm[i:j])
                    #print(''.join(perm[i:j]))
                    if possible_word in word_set:
                        forged_words.append(possible_word)



    sorted_data = sorted(forged_words, key=lambda x: len(x), reverse=True)
    return_data = {'data': sorted_data}

    return jsonify(return_data)






@app.route('/howdy', methods=['GET'])
def test_hello():
    return jsonify({'howdy': "Hello World!"})



if __name__ == "__main__":
    file = open("english_words_full.txt", "r")
    for line in file:
        word_set.add(line.strip())
    file.close()

    app.run(debug=True)