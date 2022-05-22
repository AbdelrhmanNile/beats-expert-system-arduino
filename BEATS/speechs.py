import pyttsx3

speech = pyttsx3.init()
speech.setProperty("rate", 135)

welcoming_speech = "Welcome to BEATS, BEATS is an Expert System that analyzes your health based on your BPM and other parameters like your age and habits, BEATS has a BPM sensor that will read your BPM, BEATS only understands Binary values for Yes or No questions, 1 for Yes, 0 for No"

ready_speech = "Are you ready?"
age_speech = "How old are you?"
smoke_speech = "Do you smoke?"
bpm_speech = "Your BPM is "

finger_speech = "Please, Place your finger on the sensor an hold ir still for 30 seconds"

wait_speech = "Reading your BPM, please wait"

rate10_speech = "Great job!,You are very healthy!,Keep on working out and taking care of yourself"
new_smoker_speech = "you must be new to smoking, it has not affected you health yet, you need to stop smoking before it is to late"

rate7_speech = "Your health is Okay, But, it could be better, You might need to workout"
rate5_speech = "Your health is below average, You need to watch your diet and workout"
rate2_speech = "Your health is very poor!, Please visit a doctor as soon as possible to discuss your health issues"

smoker_speech = "Smoking has affected your health, it will get worse if you did not stop"

goodbye_speech = "Okay, GoodBye!"
