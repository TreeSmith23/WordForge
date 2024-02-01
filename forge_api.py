from flask import Flask, request, jsonify, make_response
from flask_cors import CORS




def main():
    #Code here
    with open("new_english_words_full.txt", 'w') as wfile:
        with open("english_words_full.txt", 'r') as file:
                for line in file:
                    if len(line.strip()) > 2:
                         wfile.write(line)
                     
                
    return 0

if __name__ == "__main__":
    main()