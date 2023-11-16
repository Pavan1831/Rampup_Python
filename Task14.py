from collections import defaultdict

def topKStudents(positive_feedback, negative_feedback, report, student_id, k):
    points = defaultdict(int)

    positive_words = set(positive_feedback)
    negative_words = set(negative_feedback)

    for i in range(len(report)):
        words = report[i].split()
        student = student_id[i]
        for word in words:
            if word in positive_words:
                points[student] += 3
            elif word in negative_words:
                points[student] -= 1

    # Sort students by points in non-increasing order and by student ID in case of ties
    sorted_students = sorted(points.keys(), key=lambda x: (-points[x], x))

    return sorted_students[:k]

# Example
positive_feedback = ["smart", "brilliant", "studious"]
negative_feedback = ["not"]
report = ["this student is studious", "the student is smart"]
student_id = [1, 2]
k = 2

result = topKStudents(positive_feedback, negative_feedback, report, student_id, k)
print(result)  # Output: [1, 2]
