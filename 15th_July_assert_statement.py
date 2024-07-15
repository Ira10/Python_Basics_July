def percent(marks, MaxMarks):
    perc = (marks /MaxMarks) * 100
    return perc 

def main():
    MaxMarks = float(input("Enter maximun marks "))
    assert MaxMarks >=0 and MaxMarks <= 500

    marks = float(input("Enter marks "))
    assert marks >=0 and marks <= MaxMarks

    percentage = percent(marks, MaxMarks)
    # return percentage -- it is not working here
    print("percentage is ", percentage)

if __name__ == "__main__":
    main()
