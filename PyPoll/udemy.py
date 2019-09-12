import os, csv
header = "id,title,url,isPaid,price,numSubscribers,numReviews,numPublishedLectures,instructionalLevel,contentInfo,publishedTime"
headerslist = header.split(",")

file1 = os.path.join('..','Resources','web_starter.csv')

Title = []
Price = []
Subscriber_Count = []
Number_of_Reviews = []
Course_Length = []

with open(file1, 'r', newline='', encoding="utf8") as MyFile:
    Data = csv.reader(MyFile, delimiter=',')
   
    for row in Data:
        Title.append(row[1])
        Price.append(row[4])
        Subscriber_Count.append(row[5])
        Number_of_Reviews.append(row[6])
        row_course_length = row[9].split(" ")
        Course_Length.append(int(row_course_length[0]))
    
    Header = zip()
    Everything = zip(Title, Price, Subscriber_Count, Number_of_Reviews, Course_Length)

with open("NewUdemy.csv", "w", newline='') as UdemyFile:
    Organized = csv.writer(UdemyFile, delimiter=',')

    Organized.writerow(["Title", "Price", "Subscriber Count", "Number of Reviews", "Course Length"])
    Organized.writerows(Everything)
    