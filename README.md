# BIL 104 Final Project

This project is a Python program that creates and manipulates different classes of people, such as Insan (Human), Calisan (Employee), MaviYaka (Blue Collar), BeyazYaka (White Collar) and Issiz (Unemployed). The program uses object-oriented programming principles and pandas module to perform various operations on the data.

## Classes

The program defines five classes:

- Insan: This is the base class that represents a human being. It has the following attributes: tc_no (Turkish identity number), ad (name), soyad (surname), yas (age), cinsiyet (gender) and uyruk (nationality). All of these attributes are private and can be accessed and modified by getter and setter methods. The class also has a __str__ method that prints the name and surname of the person.

- Calisan: This is a subclass of Insan that represents an employee. It inherits all the attributes and methods of Insan and adds three more attributes: sektor (sector), tecrube_ay (experience in months) and maas (salary). All of these attributes are private and can be accessed and modified by getter and setter methods. The class also has a zam_hakki method that calculates the raise amount for the employee based on their experience and salary. The class also has a __str__ method that prints the name, surname, experience and new salary of the employee.

- MaviYaka: This is a subclass of Calisan that represents a blue collar worker. It inherits all the attributes and methods of Calisan and adds one more attribute: yipranma_payi (weariness rate). This attribute is private and can be accessed and modified by getter and setter methods. The class also overrides the zam_hakki method to include the weariness rate in the calculation. The class also has a __str__ method that prints the name, surname, experience, new salary and weariness rate of the worker.

- BeyazYaka: This is a subclass of Calisan that represents a white collar worker. It inherits all the attributes and methods of Calisan and adds one more attribute: tesvik_primi (incentive bonus). This attribute is private and can be accessed and modified by getter and setter methods. The class also overrides the zam_hakki method to include the incentive bonus in the calculation. The class also has a __str__ method that prints the name, surname, experience, new salary and incentive bonus of the worker.

- Issiz: This is a subclass of Insan that represents an unemployed person. It inherits all the attributes and methods of Insan and adds one more attribute: statu_tecrube (status experience). This attribute is a dictionary that stores the past experiences of the person in different statuses ("mavi yaka", "beyaz yaka", "yonetici"). The class also has a statu_bul method that calculates the most suitable status for the person based on their experience. The class also has a __str__ method that prints the name, surname and status of the person.

## Main Program

The main program allows the user to create different objects from these classes and perform various operations on them using pandas DataFrame. The program has three functions:

- insan_olustur: This function creates an object from Insan class by taking input from the user. It validates the input values using try/except blocks. It converts the object into a DataFrame and appends it to a global DataFrame called df.

- calisan_olustur: This function creates an object from Calisan or its subclasses by taking input from the user. It validates the input values using try/except blocks. It converts the object into a DataFrame and appends it to df.

- issiz_olustur: This function creates an object from Issiz class by taking input from the user. It validates the input values using try/except blocks. It converts the object into a DataFrame and appends it to df.

The main program uses a while loop to ask the user for their choice of creating an object from one of these classes or exiting the program. For each choice, it calls the corresponding function and prints the information of the created object using __str__ method.

After creating some objects, the main program performs some operations on df using pandas methods:

- It fills any missing values with 0.
- It groups df by calisan_tipi (employee type) column and calculates the mean of tecrube_ay (experience in months) and maas (salary) columns for each group and prints them.
- It counts the number of rows where maas (salary) is greater than 15000 and prints it.
- It sorts df by maas (salary) column in ascending order and prints it.
- It filters df by calisan_tipi (employee type) column where the value is "Beyaz Yaka" and tecrube_ay (experience in months) column where the value is greater than 36 and prints it.
- It slices df by maas (salary) column where the value is greater than 10000 and selects the rows from 2 to 5 and the columns tc_no (Turkish identity number) and maas (salary) and prints it.
- It creates a new DataFrame from df by selecting the columns ad (name), soyad (surname), sektor (sector) and maas (salary) and prints it.

## How to Run

To run this program, you need to have Python 3 and pandas module installed on your system. You can download Python 3 from https://www.python.org/downloads/ and install pandas using pip or conda. You also need to have the five Python files (insan.py, calisan.py, maviyaka.py, beyazyaka.py, issiz.py) and the main.py file in the same folder. Then you can run the main.py file using your preferred IDE or terminal. The program will prompt you for input values and display the output on the screen.
