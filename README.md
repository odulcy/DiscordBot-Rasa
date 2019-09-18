## Discord Bot working with Rasa

You need to create a file `my_token` with the variable `TOKEN` inside.

# How does it work ?

It is based on RASA NLU. You need to launch a rasa server to enable the api to use the interpreter.

To do this, you need to execute `rasa run --enable-api -m models/XXXXXX.tar.gz` in the folder `rasa_files`.
