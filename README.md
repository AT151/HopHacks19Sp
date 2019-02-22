# Get in the Frame
Machine-learning system to provide real-time feedback from input received from webcam.

To run, open main.ipynb and webcam.html.

## Inspiration
We are all members of the Johns Hopkins Sport Taekwondo Club on campus! Most of us are beginners and have had trouble practicing proper form outside of practice. It's difficult to improve without feedback from experienced people, so we wanted to create a website that could analyze and correct technique (especially when starting out with good form builds great habits!) 

## What it does
This web-application uses machine learning to provide live feedback on taekwondo punches through a webcam stream. Captured frames were fed into a neural network, which outputs a classification that is converted into text feedback. The corrective information is displayed in real time on the website.

## How we built it
The site takes live feed from the webcam and converts it into image files to be analyzed with machine learning in order to provide feedback on how to improve form. The website in which the application is hosted was built with HTML/CSS for the front end and JavaScript for the back end.

## Challenges we ran into
Pytorch's DataLoader was difficult to use on our dataset because of our inexperience with using data outside Pytorch's defaults. Because of how we collected our data, we had limited diversity in our training set. We had to run everything locally without GPUs due to having to demo without using GCP. None of us had prior experience with programming in JavaScript, so developing the back end of the site was a struggle. There were some creative workarounds to read in and write out files due to our lack of experience with server-side programming.

## Accomplishments that we're proud of
This was the first end-to-end machine learning project that we've worked on, and we're proud of how quickly setting up the environment, in terms of packages and libraries, occurred. We also think that for a group with limited experience in HTML/CSS/JavaScript, we were able to figure out most of the major issues successfully, with enough work. We're also proud of our graphic design, such as with our blue jay banner!

## What we learned
We learned how to set up the machine learning environment from scratch, and we learned how to create a website running scripts for streaming video and recording media.

## What's next for Get in the Frame
The concept for Get in the Frame could be expanded to other activities that require proper form, such as weightlifting, CPR training, and more!