<h1 align="center">Copy-Catcher</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/54114888/124520794-27487a80-de0b-11eb-9c1b-8e0767524f0d.png" width="180" height="180">
</p>

## 📜 Description:
The project **"Copy-Catcher"** is a simple plagiarism detection tool in python code, the basic idea is to normalize python representation and use `difflib` to get the modification from referenced code to candidate code. The plagiarism defined is how many referenced code is plagiarized by candidate code, which means swap referenced code and candidate code will get different result. The Similarity of the two files are being compared here.

## 📽 Sample Demo:
https://user-images.githubusercontent.com/54114888/124520699-ce78e200-de0a-11eb-857a-6a9104e2b639.mp4

## 👀 The above demonstration Shows the working in 3 scenarios:
- 1st scenario shows `100.00 %` Plagiarism between the 2 files.
- 2nd scenario shows few lines removed, and `18.89 %` Plagiarism between the files.
- 3rd scenario shows all the lines of the file removed and `0.00 %` Plagiarism between the files.

## 🏗 Built With:
- Python.
- difflib.
- SequenceMatcher.
- PyCharm.

## 📝 Feedback Form:
https://forms.gle/mxpiGKb1oqEQJYsM6

## 🧪 Steps to Build locally:
- Clone the Repository with: 
```bash 
git clone https://github.com/Akash-Ramjyothi/Copy-Catcher 
```
- Install required dependencies with: 
```bash
pip install difflib
```
- Run the Script, type: 
```bash
python3 main.py
```

## 💥 How to Contribute?

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) 

- Take a look at the Existing [Issues](https://github.com/Akash-Ramjyothi/Copy-Catcher/issues) or create your own Issues!
- Wait for the Issue to be assigned to you after which you can start working on it.
- Fork the Repo and create a Branch for any Issue that you are working upon.
- Create a Pull Request which will be promptly reviewed and suggestions would be added to improve it.
- Add Screenshots to help me know what this Code is all about.

## 👦 Developed By:
<h2 align="center">Akash Ramjyothi</h2>
<p align="center">
  <a href="https://github.com/Akash-Ramjyothi"><img src="https://avatars.githubusercontent.com/u/54114888?v=4" width=150px height=150px /></a> 
    
<p align="center">
  <a target="_blank"href="https://www.linkedin.com/in/akash-ramjyothi/"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="mailto:akash.ramjyothi@gmail.com?subject=Hello%20Akash,%20From%20Github"><img src="https://img.shields.io/badge/gmail-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.instagram.com/akash.ramjyothi/"><img src="https://img.shields.io/badge/instagram-%23D14836.svg?&style=for-the-badge&logo=instagram&logoColor=pink" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  ☎️ PH:+91 8939928002.
</p>

## 🌐 References Used:
- https://github.com/Akash-Ramjyothi/Sherlock-Checker
- https://stackoverflow.com/questions/5312982/can-difflib-be-used-to-make-a-plagiarism-detection-program
- https://pypi.org/project/cdifflib/
