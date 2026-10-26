FAIL_MARK = 55
EXCELLENT_MARK = 90

mark = int(input("Enter the mark: "))

is_failed = mark < FAIL_MARK
is_passed = FAIL_MARK <= mark < EXCELLENT_MARK
is_excellent = mark >= EXCELLENT_MARK

msg_failed = "Failed"
msg_passed = "Passed"
msg_excellent = "Excellent"

result = (is_failed * msg_failed) + (is_passed * msg_passed) + (is_excellent * msg_excellent) 

print(f"Result: {result}")
