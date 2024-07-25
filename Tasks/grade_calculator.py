def grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    elif marks >= 50:
        return 'E'
    else:
        return 'Fail'

def main():
    marks = {
        'Python': int(input('Enter your Python Marks: ')),
        'Java': int(input('Enter your Java Marks: ')),
        'React': int(input('Enter your React Marks: ')),
        'Angular': int(input('Enter your Angular Marks: ')),
        'MySQL': int(input('Enter your MySQL Marks: '))
    }
    for subject,mark in marks.items():
        print(f'Your grade for {subject}: {grade(mark)}')

if __name__ == '__main__':
    main()
