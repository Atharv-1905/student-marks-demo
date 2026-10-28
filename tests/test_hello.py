from hello import analyze_marks


def test_student_pass():
    average, result = analyze_marks([75, 80, 65])

    assert average == 220 / 3
    assert result == "Pass"
