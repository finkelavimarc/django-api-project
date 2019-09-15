from postings.models import BlogPost
import csv

wine_csv = open('wine.csv', 'r', encoding = "utf-8") 
reader = csv.reader(wine_csv)
headers = next(reader, None)[:]
print ("---------",headers)
for row in reader:  
   wine_dict = {}
   for h, val in zip(headers, row[:]):
      wine_dict[h] = val
   wine = BlogPost.objects.create(**wine_dict)

wine_csv.close()

