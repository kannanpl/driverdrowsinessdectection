from tkinter import *
import cv2
import os
import argparse

# import filedialog module
from tkinter import filedialog


# Function for opening the
# file explorer window



def browseFiles():
    filename = filedialog.askopenfilename( initialdir = "/",
                                           title = "Select a File",)
    print("Preprocessed Data")



    #filename = filedialog.askopenfilename( initialdir = "/",
                                          # title = "Select a File",
                                           #filetypes = (("Text files",
                                                        # "*.txt*"),
                                                       # ("all files",
                                                        # "*.*")) )

    # Change label contents
    label_file_explorer.configure( text = "File Opened: " + filename )
    print( "Getting Selected Input File" )

    ref_point = []
    crop = False

    def shape_selection(event, x, y, flags, param):
        # grab references to the global variables
        global ref_point, crop

        # if the left mouse button was clicked, record the starting
        # (x, y) coordinates and indicate that cropping is being performed
        if event == cv2.EVENT_LBUTTONDOWN:
            ref_point = [(x, y)]

        # check to see if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates and indicate that
            # the cropping operation is finished
            ref_point.append( (x, y) )

            # draw a rectangle around the region of interest
            cv2.rectangle( img, ref_point[0], ref_point[1], (0, 255, 0), 2 )
            cv2.imshow( "img", img )

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    #ap.add_argument( "-i", "--img", required = True, help = "Path to the image" )
    args = vars( ap.parse_args() )

    # load the image, clone it, and setup the mouse callback function
    img = cv2.imread( filename )

    dirname, basename = os.path.split( filename )
   # print( basename )
    index_of_dot = basename.index( '.' )
    file_name_without_extension = basename[:index_of_dot]
    print( file_name_without_extension )
    print (file_name_without_extension.rsplit( '-', -1 )[1])

    index_of_dot1 = file_name_without_extension.rsplit( '-', -1 )[1]






    text = file_name_without_extension
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (00, 185)
    fontScale = 1
    color = (0, 0, 255)
    thickness = 2
    ######img = Image.open(filename)
    net = cv2.dnn.readNet( 'yolov3.weights', 'yolov3.cfg' )
    #clone = image.copy()
    cv2.namedWindow( "Training Image" )
    cv2.setMouseCallback( "Training Image", shape_selection )
    cv2.imshow( "Resized-Image", img )
    cv2.imshow( 'Accept', img )

    image = cv2.putText( img, text, org, font, fontScale,
                         color, thickness, cv2.LINE_AA, False )




    start_point = (150, 150)
    end_point = (420, 420)



    # Line thickness of 2 px


    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    image = cv2.rectangle( img, start_point, end_point, color, thickness )

    #if index_of_dot1 == "cs":
      #  print( "Another-Department Student Security Not Access" )
       # print( "Not-Accept" )
   # else:
      #  print( "IT-Department Student Security  Access" )
       # print("Accept")




    # cv2.imshow( "crop_img", crop_img )
    cv2.waitKey( 0 )


    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
       # cv2.imshow( "Resized-Image", img )
        key = cv2.waitKey( 1 ) & 0xFF


        # press 'r' to reset the window


        # if the 'c' key is pressed, break from the loop
        if key == ord( "c" ):
            break






    # Destroying present windows on screen
    cv2.destroyAllWindows()


# Create the root window
window = Tk()

# Set window title
window.title( 'File Explorer' )

# Set window size
window.geometry( "500x500" )

# Set window background color
window.config( background = "white" )

# Create a File Explorer label
label_file_explorer = Label( window,
                             text = "FACE DETECTION ",
                             width = 100, height = 4,
                             fg = "blue" )

button_explore = Button( window,
                         text = "Browse Files",
                         command = browseFiles )


button_exit = Button( window,
                      text = "Exit",
                      command = exit )

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid( column = 1, row = 1 )

button_explore.grid( column = 1, row = 2 )


button_exit.grid( column = 1, row = 3 )



# Let the window wait for any events
window.mainloop()
