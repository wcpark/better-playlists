from flask import Flask, request, jsonify
from time import time
from mergesort import mergeSort
from quicksort import quickSort
import ast

app = Flask(__name__)


@app.route("/sort", methods=["POST"])
def sort():
    data = request.json
    input_list = data["list"]

    # Convert input string to list of tuples
    input_list = ast.literal_eval(input_list)

    # Merge sort
    merge_sorted_list = (
        input_list.copy()
    )  # Creating a copy to avoid modifying the original

    start_time = time()
    mergeSort(merge_sorted_list, 0, len(input_list) - 1)
    end_time = time()
    merge_sort_time = end_time - start_time

    # Quick sort
    quick_sorted_list = (
        input_list.copy()
    )  # Creating a copy to avoid modifying the original

    start_time = time()
    quickSort(quick_sorted_list, 0, len(input_list) - 1)
    end_time = time()
    quick_sort_time = end_time - start_time

    return jsonify(
        {
            "mergeSortTime": merge_sort_time,
            "quickSortTime": quick_sort_time,
            "mergeSortedArray": merge_sorted_list,
            "quickSortedArray": quick_sorted_list,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)


# Members API Route
# @app.route("/members")
# def members():
#     return {"members": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":
    app.run(debug=True)
