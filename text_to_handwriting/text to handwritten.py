import pywhatkit as pw
txt="You can perform a Google search using the following simple command. It opens your browser and searches for the topic you have given in your code."

pw.text_to_handwriting(txt,"text1.png",[0,0,138])
print("END")
