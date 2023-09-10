
# TalentBoost

## Abstract:
**"TalentBoost"**  is a dynamic web application aimed at simplifying and optimizing the candidate evaluation process during recruitment. Leveraging the power of modern web technologies, this application allows candidates to submit their resumes for evaluation against predefined suitability criteria. Recruiters can  review and assess these submissions, receiving instant feedback on each candidate's qualifications, skills, and experience. The application not only automates the assessment process but also facilitates efficient communication with candidates, notifying them of their evaluation outcomes. Built with a user-friendly interface and incorporating advanced natural language processing techniques, TalentBoost represents a significant advancement in modern talent acquisition, promoting speed, efficiency, and objectivity in candidate selection. With the ability to scale, adapt, and integrate with other recruitment systems, TalentBoost promises to revolutionize the way organizations identify and engage top talent.

--

## Tools and Technologies:
**FRONT-END** HTML, CSS, JAVASCRIPT

**BACK-END**  FLASK, PYTHON OPENAI
--

## Run Locally

Clone the project

```bash
  git clone https://github.com/anish2105/TalentBoost.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```


## Authors

- [@Anish Vantagodi](https://www.github.com/anish2105)


# Screenshots

## Screenshots of the Flask app for intended questions.
<div align="center">
<img src="https://imgur.com/tklOMNc" alt="Login Portal" width="50%" text-align="center">
Login Portal for Organizations to Facilitate Resume Submission and Domain Selection by Candidates

<img src="https://imgur.com/5heujXC" alt="Resume Summary" width="50%" text-align="center">
After a user submits their resume, the system automatically scans and generates a summary of the candidate's key details. Candidates are then provided with an opportunity to review and refine their resumes based on this summary.

<img src="https://imgur.com/VuDAYpi" alt="Form Submition" width="50%" text-align="center">
If the resume is submitted, a pop-up is generated confirming the user's successful submission.

<img src="https://imgur.com/4evrhyQ" alt="Clearing First round" width="50%" text-align="center">
If the resume meets the specified criteria, an automated email is sent to the candidate, containing login credentials and an invitation to participate in the initial assessment round.

<img src="https://imgur.com/eoxbOHi" alt="Login" width="50%" text-align="center">
The login page directs users to enter their password.

<img src="https://imgur.com/fY49gEB" alt="Questionaire" width="50%" text-align="center">
A questionnaire is dynamically generated from the user's resume to evaluate the candidate's expertise in projects, skills, and other relevant experiences.


<img src="https://imgur.com/H7La2nx" alt="Accuracy low" width="50%" text-align="center">
Depending on the candidate's response, if it doesn't match the expected answer, a lower accuracy score is calculated.


<img src="https://imgur.com/TaA6my0" alt="High Accuracy " width="50%" text-align="center">
If the response matches the expected answer, a higher accuracy score is assigned. 

<img src="https://imgur.com/57122IC" alt="Final results" width="50%" text-align="center">
Following the completion of this round, an automated email is sent to the candidate with the results.

</div>
