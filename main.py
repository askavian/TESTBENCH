admin = True
update_required = True

if admin:
    if update_required:
        print("You are authorized to update")
    else:
        print("No update required")
else:
    print("You need admin privileges to do this")