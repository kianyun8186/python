1) Ensure the directory of the stored files are correct in the code. (Line 349)

Code example:

def sides_files():
    startfile("X:/........./sides.txt")

def mains_files():
    startfile("X:/........./mains.txt")

def beverages_files():
    startfile("X:/........./beverages.txt")

def member_files():
    startfile("X:/........./members.txt")

2) When editing dishes in the files, follow the same format as previous dishes.
Example:
fruit salad:$4.00

3)When deleting dishes, ensure to delete the whole line completely. 
When line is deleted completely, the insertion point (the blinking line that indicates where text 
is inserted when you type)should not shift down when 'arrown down' key is pressed

If empty line not deleted, will caused 'ValueError: not enough values to unpack (expected 2, got 1)'

4) If more dishes are added into menu, can increase window geometry. Lookout for the code is below

def main_window():
    global window
    window = tk.Tk()
    window.geometry("400x680")


