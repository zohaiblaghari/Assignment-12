def calculate_grade(scores):
    total_score = sum(scores)
    max_total_score = len(scores) * 100
    percentage = (total_score / max_total_score) * 100

    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
def main():
    subjects = {"Math","science","History","English"}
    scores = []

    for subject in subjects:
        score = float(input(f"Enter score for {subject}:"))
        scores.append(score)
    
    overall_grade = calculate_grade(scores)
    print(f"Overall grade: {overall_grade}")

if __name__=="__main__":
    main()
    