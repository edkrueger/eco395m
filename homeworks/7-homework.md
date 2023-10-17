## Homework 7

You must have a _private_ repository with the name specified. You must also add me (edkrueger) and the TAs ([Click here for TA GitHub usernames](/ta-githubs.txt)) as collaborators.  

In this assignment, you'll build a zero-shot classifier using OpenAI's "gpt-3.5-turbo" model through the [chat completions API](https://platform.openai.com/docs/guides/gpt/chat-completions-api). You'll ultimately use the [OpenAI Python Library](https://github.com/openai/openai-python), but it's a thin wrapper around the API, so you should read the API docs first.

Though I've written this assignment and picked and subsetted the dataset to minimize costs, you should also look at the pricing for this API, which you can find [here](https://openai.com/pricing).

You'll apply your classifier to a small labeled text message spam dataset in order to validate it.

## Problem 0 - (0 points)

You'll clone a repo with some starter code.  

a) Go to the repo: https://github.com/edkrueger/eco395m-homework-gptzs

b) Select "Use this template" and create a _private_ repository with the name "eco395m-homework-gptzs".  

c) Select "Settings>Collaborators>" and add "edkrueger" and the TAs as collaborators.

## Problem 1 - (100 points)
You'll write a program that reads in a CSV with the following schema.

| Field | Type | Example |
| - | - | - |
| "label" | str, either "ham" or "spam" | "spam" |
| "text" | str | "Boltblue tones for 150p Reply POLY# or MONO# eg POLY3 1. Cha Cha Slide 2. Yeah 3. Slow Jamz 6. Toxic 8. Come With Me or STOP 4 more tones txt MORE" |

Your program will apply a zero-shot classifier to the "text" column in order to predict labels resulting in a CSV with the following schema.

| Field | Type | Example |
| - | - | - |
| "label" | str, either "ham" or "spam" | "spam" |
| "text" | str | "Boltblue tones for 150p Reply POLY# or MONO# eg POLY3 1. Cha Cha Slide 2. Yeah 3. Slow Jamz 6. Toxic 8. Come With Me or STOP 4 more tones txt MORE" |
|"predicted_label"| str, either "ham" or "spam"|"spam"|

This dataset will allow you to evaluate the quality of your classifier.

For this assignment, you _will_ submit your `.env` file along with your code. This is not normally a good practice, but it will allow me to grade your problem using your account. In the unlikely event that there is an error in your code that causes excessive requests or excessive tokens to be sent to the API, you will bear the costs.

When grading this problem, we'll execute the code by cloning your repo, running `cd eco395m-homework-groundwater` to open your repository and running `python code/classify.py data/holdout.csv artifacts/holdout.csv`, where `holdout.csv` is a file that we intentionally do not distribute. You can instead run `python code/classify.py data/eval.csv artifacts/eval.csv` to check that your solution works on the evaluation set.

Your code will be executed in a Python environment containing only the Standard Library and the packages specified in `requirements.txt`. Install them with `pip install -r requirements.txt`.   

If your code does not execute properly with this command, it will be considered incomplete and you will receive a 0.  

After running your code, we'll check for a CSV file called `holdout.csv` at the location, relative to the top level of the repo, of `artifacts/holdout.csv`.

The expectation is that your code generates the output when we run it, not just that the file exists. This means that if the code does not run, you will receive a 0.  

We also expect that your code executes in under 5 minutes; if it does not, you will receive a 0. For context, my code executes in approximately 2 minutes.  

You'll get 20 points if the generated CSV follows the format specified in `artifacts/holdout.csv`. In particular, the CSV must have the same header as the example. If it does not, you will receive a 0 for this part.  

You'll get 80 points if your classifier has a weighted average F1 of .9 or greater AND your accuracy is greater than .9 when evaluated against the holdout set. If your classifier works but does not meet this threshold, you'll get 60 points.

_You are required to use the starter code. If you don't we will not help you. You don't necessarily need to complete the steps in the order below, but you should follow all of the steps._

a) Use ChatGPT's web interface to design a prompt.

b) Make an OpenAI developers account, obtain an API key, and put that key into your `.env` file with the environmental variable name `OPENAI_API_KEY`. __This time, and this time only, you will submit your `.env` in the repo. Therefore, it's extra important that you keep your repo private. It's highly recommended that you roll your key after the homework is graded.__ 

c) Look at `prompt_classifier.py` and notice that I've left in tests for many of the functions under `if __name__ == "__main__"`. You can run them by running `python code/prompt_classifier.py`. You can also use the sample data in this section to understand what the raw data looks like and what is expected for each function's output.

d) Write the string `PROMPT` according to the prompt you used in step (a) and write `classify_text_message`. Make sure that `classify_text_message` can only return "ham" or "spam".

(_Note that `classify_text_message` is decorated with a cache, this will save you from making the same request multiple times, however, if you modify your prompt, you'll have to remove the cache with `rm -rf .cachedir` to make requests with the new prompt._)

e) In `classify.py`, write `load_data` which loads a CSV given a path. Note that in this homework, the paths are not hard coded into the code base, but passed by the user as an argument to Python. For example, to run the code on a valid CSV at `data/eval.csv`, you'll run `python code/classify.py data/eval.csv artifacts/eval.csv`. This will cause the program to write the output CSV to `artifacts/eval.csv`.

f) Write `classify_all`. There are many ways to do this, but the intended way is to pass `classify_text_message` as an argument to `progress_apply`. To be able to use a progress bar with pd.DataFrame, tqdm can modify pd.DataFrame's methods to include `progress_apply` which works like apply, but adds a progress bar.

g) Check your classification metrics in the classification report from the evaluation dataset by running `python code/classify.py data/eval.csv artifacts/eval.csv` if you are happy with them, then you are done. Otherwise, try modifying your prompt until they improve. Remember that you'll have to clear the cache to modify the prompt. Remove the cache with `rm -rf .cachedir`.
