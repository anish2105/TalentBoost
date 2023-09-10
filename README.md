
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
  
![image](https://github.com/anish2105/TalentBoost/assets/88924201/60dca96a-50f7-4a37-bdaa-442a00011727)

Login Portal for Organizations to Facilitate Resume Submission and Domain Selection by Candidates

![image](https://github.com/anish2105/TalentBoost/assets/88924201/491069b1-390e-4023-a83b-6392f0b59255)
After a user submits their resume, the system automatically scans and generates a summary of the candidate's key details. Candidates are then provided with an opportunity to review and refine their resumes based on this summary.

![image](https://github.com/anish2105/TalentBoost/assets/88924201/1325c8ce-cf51-4b8f-b9bd-2beb72931ffb)
If the resume is submitted, a pop-up is generated confirming the user's successful submission.

![image](https://github.com/anish2105/TalentBoost/assets/88924201/b7f9fbd2-0578-4569-a7f8-8c9a65955608)
If the resume meets the specified criteria, an automated email is sent to the candidate, containing login credentials and an invitation to participate in the initial assessment round.

![image](https://github.com/anish2105/TalentBoost/assets/88924201/396a4595-2989-41cb-9223-856c3dfbe158)
The login page directs users to enter their password.

![image](https://github.com/anish2105/TalentBoost/assets/88924201/43f707f4-658f-40e0-8c12-810b06e6f1ed)
A questionnaire is dynamically generated from the user's resume to evaluate the candidate's expertise in projects, skills, and other relevant experiences.


![image](https://github.com/anish2105/TalentBoost/assets/88924201/fcaf2e38-2e41-4b14-8e40-c7c429cff0ac)
Depending on the candidate's response, if it doesn't match the expected answer, a lower accuracy score is calculated.


![image](https://github.com/anish2105/TalentBoost/assets/88924201/7d2552e9-14bd-4784-9f93-3158593d065c)
If the response matches the expected answer, a higher accuracy score is assigned. 

![image](https://github.com/anish2105/TalentBoost/assets/88924201/40ce74d0-6fa6-43bc-bc0d-23c905483b6d)
Following the completion of this round, an automated email is sent to the HR or the Manager with the results.
</div>
