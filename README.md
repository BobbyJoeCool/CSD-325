# CSD-325
Advanced Python

## Module 1
10/20/2025 - 10/26/2025

In this module, we will review the basic elements of programming that were covered in one of your previous courses: CSD205 or CIS245.

You'll be creating a program that includes a function, looping, a sentinel value, an if/else statement and getting input from the user before the program is run. For each programming assignment, you'll also need to create a flowchart using standard shapes and notation. I've placed a tutorial in the reading section in case you need a little refresh on how to contruct flowcharts. You may use any app you'd like to create the charts as long as the result is copied/pasted into a Word doc, or saved as a .pdf. You'll also need to have Python installed. If you do not, there is a link in the reading to installation instructions.

### Deliverables

1) Module 1.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CT.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CT.
3) Module 1.2 Assignment: GitHub Repository Setup - Due by Sunday 11:59 p.m., CT.
4) Module 1.3 Assignment: On the Wall + Flowchart - Due by Sunday 11:59 p.m., CT.

### Discussion Board Topics
In this module's discussion board assignment, answer the following questions:

1) Which IDE did you use for the last Python course? Will you use it again? Why or why not?
2) What resource did/will you use the most for programming issues? Why this one?
3) Using the Pragmatic Programmer reading assignment, select one (1) topic and complete the following:
    - Why did you select this topic?
    - Summarize the main points (in your own words) of that topic in three or four sentences.
    - Find at least one additional resource (video, book, article, website, etc.) that supports your summary. Write an additional 1-2 sentences. Include a link to that resource.

### Assignments
#### Assignment 1.2
For this assignment, you will be creating a GitHub repository using git and the CLI. The repository you create in this assignment will be used throughout the course to host the coding assignments and flowcharts. If you have not already installed Git, please do so before continuing. Make sure that you complete the steps to set the global username and global email address.

There are resources available in the Git/GitHub Resources menu item to the left on installing and configuring Git.

**Instructions:**

1) Click on each instruction box below to expand the instructions.
2) Complete the setup instructions and save the following items into a single Word document that includes your name and assignment number at the top of the document:
    - Link to your GitHub repository
    - Screenshot of your GitHub repository
    - Screenshot of your local directory, following the structure format provided in the instructions below.

**Deliverables:**
1) Link to your GitHub repository.
2) Screenshot of your GitHub repository.
3) Screenshot of your local directory (properly formatted).
4) Combine all 3 items into a single Word document, place your name and assignment number on the first page, and title it <your-last-name>-<assignment-name> .docx.

#### Assignment 1.3
For this assignment, you have two tasks. The first is to create a flowchart (or flowcharts) for the following requirements, then to write a Python program that produces the required results:

If you are not familiar with the reverse counting song "100 bottles of beer on the wall", you'll need to do a little research to familiarize yourself with it.

- Ask the user how many bottles of beer are on the wall.
- Pass that input to a function that manages the countdown.
- The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
- Once the count is down to 1, change lyrics to show "1 bottle of beer..."
- At the end of the countdown, get back to the main program and remind the user to buy more beer.

**Deliverables:**
1) Open up a drawing application. Use a text element to include your name and assignment number at the top of the drawing. Before continuing, you might view the Flowchart and Structures video listed in the Module Reading area. Then, create a flowchart that models the above process.  Copy/paste the diagram into a Word document and save to your module-1 directory.
2) Create a Python program that addresses the requirements of the process above. Save the file to your module-1 directory.

## Module 2
10/20/2025 - 10/26/2025

In this module, we will be working on debugging, something that we all must do at some point!

You'll be stepping through a provided tutorial for debugging using an IDE, but the same steps can be used with the pdb module from the Python standard library. Breakpoints, stepping in, stepping over, stepping out, and continuing are some of the more common actions to take when debugging. Many IDEs do aid when searching for syntax errors, but finding logic errors are a little more problematic.

### Deliverables
1) Module 2.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CT.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CT.
3) Module 2.2 Assignment: Documented Debugging - Due by Sunday 11:59 p.m., CT.

### Discussion Board
In this module's discussion board assignment, answer the following questions:

- Using the Pragmatic Programmer reading assignment, select one (1) topic and complete the following:
    - Why did you select this topic?
    - Summarize the main points (in your own words) of that topic in three or four sentences.
    - Find at least one additional resource (video, book, article, website, etc.) that supports your summary. Write an additional 1-2 sentences. Include a link to that resource.

### Assignments
#### Assignment 2.2
For this assignment, you have three tasks. The first is find a program that you've written, or find an example online that contains at least one function, you'll then need to create a flowchart (or flowcharts) for the program, then capture debugging activity on the program.

1) Create (if you haven't already) a directory in CSD-325 named module-2.
2) Look through programs you've created from previous classes, (or do a little research and find an example of a program) that contains a least one function.
3) Open up a drawing application. Use a text element to include your name and assignment number at the top of the drawing. Create a flowchart that models the program you selected.  Copy/paste the diagram into a Word document and save to your module-2 directory.
4) Open the Debugging Guide from the reading material for this module and follow through the steps. You might want to practice them first..
5) Open your program in an IDE and use the debugging tools, **OR** read through the tutorial at [Debugging in Python](https://www.codementor.io/@gbozee/debugging-in-python-9ia7lof32) (Abiola, codementor.io, 2017) and use the Python module for debugging.
6) Create a Word document and put your name and assignment number on the first page.
7) Back in the IDE, create a break point, and start the debugging process, take a screenshot of your progress and paste into the Word document.
8) Step into the function, and take a screenshot of the current location and paste it into the Word document.
9) Use at least one more action in the code, either adding errors, or moving through the program and take a screenshot of the progress and paste into the Word document.
10) Save the Word document, with at least three screenshots, into the CSD/CSD-325/module-2 directory.
11) Save the Python program into the CSD/CSD-325/module-2 directory.

## Module 3
10/27/2025 - 11/3/2025

In this module, we'll be focusing on brownfield development, which you may not have done before. The term is usually used to compare development types; brownfield and greenfield, either in construction or program development. Basically a greenfield development means you are starting from scratch, constructing a building or a program from the ground up. A brownfield development means that you are taking some existing infrastructure and modifying it to suit a specific purpose. There are definitely advantages and disadvantages to each. You can read a little more about these by reading through the article Brownfield vs. Greenfield: Netkodo in the Reading list below.

For this module you'll be doing a brownfield development on an existing program written to mimic a Cho-han game. The source code is provided...have fun!

**Module Deliverables**

1) Module 3.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CT.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CT.
3) Module 3.2 Assignment: Brownfield + Flowchart - Due by Sunday 11:59 p.m., CT.

### Discussion Board

In this module's discussion board assignment, answer the following questions:

- Using the Pragmatic Programmer reading assignment, select one (1) topic and complete the following:
    - Why did you select this topic?
    - Summarize the main points (in your own words) of that topic in three or four sentences.
    - Find at least one additional resource (video, book, article, website, etc.) that supports your summary. Write an additional 1-2 sentences. Include a link to that resource.

### Assignments
#### Assignment 3.2
For this assignment, you have two tasks. The first is to create a flowchart (or flowcharts) for the following requirements, then to write a Python program that produces the required results:

1) Create (if you haven't already) a directory in CSD-325 named module-3.
2) Download the attached file: chohan.py
3) Examine the code and figure out the flow of execution.
4) Open up a drawing application. Use a text element to include your name and assignment number at the top of the drawing. Create a flowchart that models the above program.  Copy/paste the diagram into a Word document and save to your module-3 directory.
5) Make the following changes to the chohan.py program:
    - Change the input prompt to your initials and a colon. Ex. mss:
    - Change the percentage that goes to the house to 12 percent instead of 10 percent.
    - In the program introduction, include a notice that if the user gets a 2 or a 7 on a dice roll, they get a 10 mon bonus.
    - If the dice roll is equal to a 2 or a 7, output a message to the user what the total of roll was and that they got a 10 mon bonus. Then add that bonus to the purse.
    - Document all your changes, and save as chohan_"your initials".py. Ex. chohan_mss.py to your module-3 directory.

## Module 4
11/3/2025 - 11/9/2025

In this module, we'll be focusing again on brownfield development, just to give you more practice. You'll also be working with additional modules; one that you'll need to install, and one that is ready to be imported.

Read more on importing csv and installing matplotlib using the resources in the Reading list. For this module you'll be doing a brownfield development on an existing program written to display high temperatures in Sitka, Alaska. The data used for temperatures was saved as a .csv file. The source code is provided...have fun!

### Deliverables
1) Module 4.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CT.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CT.
3) Module 4.2 Assignment: High/Low Temperatures - Due by Sunday 11:59 p.m., CT.

### Discussion Board
- Using the Pragmatic Programmer reading assignment, select one (1) topic and complete the following:
    - Why did you select this topic?
    - Summarize the main points (in your own words) of that topic in three or four sentences.
    - Find at least one additional resource (video, book, article, website, etc.) that supports your summary. Include a link to that resource.

### Assignment
#### Assignment 4.2
For this assignment, you have three tasks. The first is to create a flowchart (or flowcharts) for the following requirements, the second is to write a Python program that produces the required results, and the third is to revise your flowchart to reflect the changes.

1) Create (if you haven't already) a directory in CSD-325 named module-4.
2) Download the attached file: sitka_weather.zip
3) Examine the code and figure out the flow of execution.
4) Open up a drawing application. Use a text element to include your name and assignment number at the top of the drawing. Create a flowchart that models the above program. Copy/paste the diagram into a Word document and save to your module-4 directory.
5) Before you can make changes, you'll need to install mathplotlib, see the instructions in the Reading List above.
6) Make the following changes to the sitka_highs.py program:
    - Open the program with instructions on how to use the menu; Highs, Lows, or Exit.
    - When the program starts, allow the user to select whether they want to see the high temperatures or the low temperatures, or to exit.
    - When the user selects 'lows', they should see a graph, in blue, that reflects the lows for those dates.
    - Allow the program to loop until the user selects exit.
    - When the user exits, provide an exit message.
    - Use what elements you can from previous programs, perhaps including sys to help the exit process.
    - Document all your changes, and save as sitka_high_low_"your initials".py. Ex. sitka_high_low_mss.py to your module-4 directory.
7) Open up your initial flowchart and revise it to reflect the changes made to the program. Take a screenshot and add it to your Word document, and save to your module-4 directory.

## Module 5
11/3/2025 - 11/9/2025

In this module, we'll be focusing again on brownfield development, just to give you even more practice. The project for this module will result in an example of emergent behavior, which is best described as the interaction between simple parts in a system creating complicated patterns. Read more in the article listed below. You'll be working in small teams with 2-3 students. This small project will include both Module 5 and Module 6 assignments. You'll need at least one additional module for Python: Bext. Read more on installing Bext with the resources in the Reading list.

For this project you'll be doing the modeling, both before and after modifications for a brownfield development on a current program modified from a previous program, based on an original program, all of which are forest fire simulations (who wrote what is documented in the code). The latest source code is provided...have fun!

### Deliverables
1) Module 5.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CT.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CT.
3) Module 5.2 Assignment: Forest Fire Simulation: Flowchart - Due by Sunday 11:59 p.m., CT.

### Discussion Board
In this module's discussion board assignment, answer the following questions:

- Using the Pragmatic Programmer reading assignment, select one (1) topic and complete the following:
  - Why did you select this topic?
  - Summarize the main points (in your own words) of that topic in three or four sentences.
  - Find at least one additional resource (video, book, article, website, etc.) that supports your summary. Write an additional 1-2 sentences. Include a link to that resource.

### Assignments
#### Assignment 5.2
For this assignment, you have two tasks. The first is to click on "Groups/Teams" in the left-side menu and introduce yourself by providing information on when you are available to communicate with team members. The second task is to create a flowchart (or flowcharts) for the code provided. Once the team decides on a final version of the flowchart, you need to submit that to Blackboard. Once that is submitted, the modifications required can be viewed in the next module. Why the wait? I want the team to have a firm understanding of how this program works, step by step. It's not a long program, but it is a little complicated. You'll be creating the program and the modified flowchart during the next module.

One additional step you might take is to write down the rules regarding assignment of pixels. In this program, pixels are initially populated with either trees, fire, or remain empty based on growth rates and lightning chance. Each time the program is run, you'll see different patterns emerging due to the random placement.

1) Create (if you haven't already) a directory in CSD-325 named module-5.
2) Download the attached file: forestfiresim.py.
3) Examine the code and figure out the flow of execution.
4) Install Bext per instructions in Bext article in Reading List.
5) Run the code in a command line interface to see the colors.
6) Open up a drawing application. Use a text element to include each team member's name and assignment number at the top of the drawing. Create a flowchart that models the above program. Copy/paste the diagram into a Word document and save to your module-5 directory.

## Module 6
11/10/2025 - 11/16/2025

In this module, you'll be continuing the forest fire simulation project.

For this module you'll be making modifications for a brownfield development on a current program modified from a previous program, based on an original program, all of which are forest fire simulations. You'll also need to revise your original flowchart to reflect those changes. The latest source code is provided...have fun!

### Discussion Board

In this module's discussion board assignment, answer the following questions:

- Using the Pragmatic Programmer reading assignment, select one (1) topic and complete the following:
  - Why did you select this topic?
  - Summarize the main points (in your own words) of that topic in three or four sentences.
  - Find at least one additional resource (video, book, article, website, etc.) that supports your summary. Write an additional 1-2 sentences. Include a link to that resource.

### Assignments
#### Assignment 6.2
**Forest Fire Simulation: Program and Revised Flowchart**

For this assignment, you have two tasks. The first is make the modifications listed below to the forestfiresim.py program. The second is to revise the teams' original flowchart to reflect those modifications. The team needs to work together on the program and the flowchart.   **hint.. to see maximum color, I ran this through the command line, not an IDE.

1) Create (if you haven't already) a directory in CSD-325 named module-6.
2) Download (if you haven't already) the attached file in Module 5: forestfiresim.py.
3) Make the following modifications to the program:
    - Add a lake roughly in the center of the display. You might want to take a look at the video above titled Mod5 Cartesian for a brief explanation of how elements are placed in a display.
    - The water feature should use a different character (not A or @) and be blue.
    - The water feature cannot be modified once it is in place, the water feature acts as a firebreak that flames cannot cross.

4) Document all your code changes, and save as forestfiresim_325.py to your module-6 directory.
5) Open up a drawing application. Use a text element to include each team member's name and assignment number at the top of the drawing. Create a flowchart that depicts the revisions. Copy/paste the diagram into a Word document and save to your module-6 directory.

## Module 7
11/17/2025 - 11/24/2025

In this module, we'll be working with a Python module called unittest, which allows you to create test cases both at the function level and at a class level to make sure your code is behaving as you thought it would. You'll be using a chapter out of the Python Crash Course text, which is available from the Bellevue University Library. I've included a short .pdf file in the reading area that depicts how to access the text. Have fun with it!

**Deliverables**
1) Module 7.1 Discussion Board Initial Post - Due by Thursday 11:59 p.m., CT.
2) Discussion Board Responses - Due by Sunday 11:59 p.m., CT.
3) Module 7.2 Assignment: Test Cases - Due by Sunday 11:59 p.m., CT.

### Discussion Board

In this module's discussion board assignment, answer the following questions:

- Using the Pragmatic Programmer reading assignment, select one (1) topic and complete the following:
  - Why did you select this topic?
  - Summarize the main points (in your own words) of that topic in three or four sentences.
  - Find at least one additional resource (video, book, article, website, etc.) that supports your summary. Write an additional 1-2 sentences. Include a link to that resource.

### Assignments
#### Assignment 7.2
For this assignment, you have two tasks. The first is to write a Python program that produces the required results. Document those results, then add unit tests to test whether functions work as required.
1) Create (if you haven't already) a directory in CSD-325 named module-7.
2) Open a Word document and put your name and assignment number at the top.
3) Read through Chapter 11 in the Python Crash Course text. Link on how to access is in the 'Select Text from Library.pdf' file listed in the Reading area.
4) Create a program that includes the following:
    - Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form City, Country, such as Santiago, Chile. Store the function in a file named city_functions.py. In the same file, call the function at least three times using a City, Country values. Excecute city_functions.py and take a screenshot of the result. Paste that screenshot into your Word document.
    - Create a file called test_cities.py that tests the function you just wrote (remember that you need to import unittest and the function you want to test). Write a method called test_city_country() to verify that calling your function with values such as santiago and chile results in the correct string. Run test_cities.py, and make sure test_city_country() passes. When it passes, take a screenshot of the result and paste in into your Word document.
    - Modify your city_country function in city_functions.py so it requires a third parameter, population. It should now return a single string of the form City, Country - population xxx, such as Santiago, Chile - population 5000000.
    - Run test_cities.py again. It should fail. Take a screenshot of the result and paste into your Word document.
    - Now modify your city_country function in city_functions.py so that the population parameter is optional.
    - Run test_cities.py again. It should pass. Take a screenshot of the result and paste into your Word document.
    - Modify your city_country function in city_functions.py so it requires a fourth parameter, language. It should now return a single string of the form City, Country - population xxx, Language, such as Santiago, Chile - population 5000000, Spanish.
    - Run test_cities.py again. It should fail. Take a screenshot of the result and paste into your Word document.
    - Now modify your city_country function in city_functions.py so that the language argument is optional.
    - Run test_cities.py again. It should pass. Take a screenshot of the result and paste into your Word document.
    - Run city_functions.py. Call the function at least three times using a City, Country for one, City, Country, Population for the next and City, Country, Population, Language for the last. Excecute city_functions.py and take a screenshot of the result. Paste that screenshot into your Word document.
5) Save your Word document to your module-7 directory.
6) Save the city_functions.py and final test_cities.py to your module-7 directory.

Zip your module-7 directory and submit by clicking on the Assignment Link above, then scroll down to the Upload Files section and click on Browse Local Files. Select your zipped folder, add any comments as appropriate, and then click on Submit.  
