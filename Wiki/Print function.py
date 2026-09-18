""""Hacker Rank Projects """""


"""Python Print Function

number = int(input(""))
for i in range(1, number + 1):
    print(i, end="")
"""""

"""Python Filtered, list, map function

n = int(input())  # Read the number of scores
arr = list(map(int, input().split()))  # Read and store the scores as a list
max_score = max(arr)  # Find the highest score
# Create a new list excluding all occurrences of the highest score
filtered_scores = [score for score in arr if score != max_score]
runner_up = max(filtered_scores)  # Find the highest score in the filtered list
print(runner_up)  # Print the runner-up score
"""""

