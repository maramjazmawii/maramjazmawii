SINGLE_TRACK_MIN_CREDITS = 30
DOUBLE_TRACK_MIN_CREDITS = 16

degree = input("Degree (bachelor/etgar/master): ")
year = int(input("Year of study: "))
track = input("Track (single/double): ")
credits_earned = int(input("Creadits (nz) earned last year: "))

is_master_or_etgar = (degree == "master") or (degree == "etgar")
is_bachelor_valid_year = (degree == "bachelor") and (year == 2) or (year == 3)
eligible_program_and_year = is_master_or_etgar or is_bachelor_valid_year

is_single_track = (track == "single")
is_double_track = (track == "double")
minimum_credits = (is_single_track * SINGLE_TRACK_MIN_CREDITS) + (is_double_track * DOUBLE_TRACK_MIN_CREDITS)

enough_credits = credits_earned >= minimum_credits

meets_requirements = eligible_program_and_year and enough_credits

print(f"Eligible program and year: {eligible_program_and_year}")
print(f"Minimum credits: {minimum_credits}")
print(f"Enough credits: {enough_credits}")
print(f"Meets the scholaship requirements: {meets_requirements}")

