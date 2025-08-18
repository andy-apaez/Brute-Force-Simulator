from flask import Flask, render_template, request, Response
import itertools
import string
import time

app = Flask(__name__)

# ---------- Mutation function ----------
def mutate_word(word):
    return [
        word,
        word.capitalize(),
        word + "1",
        word + "123",
        word + "2025",
        word.replace("a", "@").replace("s", "$")
    ]

# ---------- Dictionary attack streaming ----------
def dictionary_stream(password, wordlist="wordlist.txt"):
    attempts = 0
    try:
        with open(wordlist, "r", encoding="latin-1") as f:
            for word in f:
                attempts += 1
                word = word.strip()

                # yield current guess
                yield f"data: {{\"status\":\"progress\",\"guess\":\"{word}\",\"attempts\":{attempts},\"method\":\"dictionary\"}}\n\n"

                if word == password:
                    yield f"data: {{\"status\":\"done\",\"password\":\"{word}\",\"attempts\":{attempts},\"time\":0,\"method\":\"dictionary\"}}\n\n"
                    return

                # check mutated variations
                for variation in mutate_word(word):
                    attempts += 1
                    yield f"data: {{\"status\":\"progress\",\"guess\":\"{variation}\",\"attempts\":{attempts},\"method\":\"dictionary\"}}\n\n"
                    if variation == password:
                        yield f"data: {{\"status\":\"done\",\"password\":\"{variation}\",\"attempts\":{attempts},\"time\":0,\"method\":\"dictionary+mutations\"}}\n\n"
                        return
    except FileNotFoundError:
        pass

# ---------- Brute force attack streaming ----------
def brute_force_stream(password, charset, max_length=5):
    attempts = 0
    start_time = time.time()
    total = sum(len(charset)**i for i in range(1, max_length+1))

    for length in range(1, max_length+1):
        for guess_tuple in itertools.product(charset, repeat=length):
            attempts += 1
            guess = ''.join(guess_tuple)
            progress = int((attempts / total) * 100 * 0.9)  # 90% reserved for brute force
            yield f"data: {{\"status\":\"progress\",\"guess\":\"{guess}\",\"attempts\":{attempts},\"progress\":{progress},\"method\":\"brute force\"}}\n\n"

            if guess == password:
                elapsed = round(time.time() - start_time, 2)
                yield f"data: {{\"status\":\"done\",\"password\":\"{guess}\",\"attempts\":{attempts},\"time\":{elapsed},\"method\":\"brute force\"}}\n\n"
                return

    elapsed = round(time.time() - start_time, 2)
    yield f"data: {{\"status\":\"done\",\"password\":null,\"attempts\":{attempts},\"time\":{elapsed}}}\n\n"

# ---------- Combined attack streaming ----------
def combined_attack_stream(password, charset, max_length=5):
    # Try dictionary first
    yield from dictionary_stream(password)
    # Then brute force fallback
    yield from brute_force_stream(password, charset, max_length)

# ---------- Routes ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_attack")
def start_attack():
    password = request.args.get("password", "")
    charset = string.ascii_lowercase + string.digits
    max_length = int(request.args.get("maxLength", 5))
    return Response(combined_attack_stream(password, charset, max_length), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

