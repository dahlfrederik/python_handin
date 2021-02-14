import utils as utils

# Testing the get file by names and adding to output.txt
utils.get_file_names(
    "/")

# Testing the get all file names and adds to output2.txt
utils.get_all_file_names(
    "/", "output2.txt")

print("#### Testing the print first line of files ")
# Testing the print first line of files
utils.print_line_one("output.txt")


print("#### Testing the print emails ")
# Testing the print emails
utils.print_emails("emails.txt")

# Testing the write_headlines from MD files
utils.write_headlines("mdfile.md", "output3.txt")
