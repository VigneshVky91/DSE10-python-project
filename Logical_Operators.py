is_age_gt_18 = False
has_no_criminal_rec = False


# and op will return true if both the conditions are true
if is_age_gt_18 and has_no_criminal_rec:
    print("You are eligible for this job")
else:
    print("Sorry you are not eligible for this job")

# or op will return true atleast if one condition is true
if is_age_gt_18 or has_no_criminal_rec:
    print("You are eligible for this job")
else:
    print("Sorry you are not eligible for this job")