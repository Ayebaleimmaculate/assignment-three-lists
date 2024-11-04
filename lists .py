# student_names = ['Sandra',  'Patricia', 'Phiona', 'Anita']
# student_marks = [80, 56, 78, 90]

#  print Patricia, Faith, Phionah and Anitah
# Add Masha at the forth position.
# Update the name Phionah to Phionah Aladina
# Display the length of the student list.
# Print all the students names using a for loop.
# Calculate the total marks for the student marks variable

# SOLUTION



# student names and marks
student_names = ['Sandra', 'Patricia', 'Phiona', 'Anita']
student_marks = [80, 56, 78, 90]

print("Patricia, Faith, Phionah and Anitah")

# Adding 'Masha' at the fourth position
student_names.insert(3, 'Masha')
print("Updated list after adding Masha:", student_names)

# Updating the name 'Phiona' to 'Phionah Aladina'
index_phiona = student_names.index('Phiona')
student_names[index_phiona] = 'Phionah Aladina'
print("Updated list after renaming Phiona:", student_names)

# length of the student list
print("Length of the student list:", len(student_names))

# students names using a for loop
print("Student names:")
for name in student_names:
    print(name)

#  total marks _marks variable
total_marks = sum(student_marks)
print("Total marks for the students is:", total_marks)


