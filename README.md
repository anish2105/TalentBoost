
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

![image](https://github.com/anish2105/TalentBoost/assets/88924201/cb378ac6-4eae-4fb7-a47a-f0ab23d973e3)


Login Portal for Organizations to Facilitate Resume Submission and Domain Selection by Candidates



  
![image](https://github.com/anish2105/TalentBoost/assets/88924201/5efe3d57-b505-4638-be6f-f4bcffdd16a4)


Once the user submits a resume, the brief details about the candidate is scanned, a Summary of the resume is generated and gives the candidates a chance to refine the resume



![image](https://github.com/anish2105/TalentBoost/assets/88924201/56038b7e-b410-41b4-b7b7-5428c20afef4)


After a user submits their resume, the system automatically scans and generates a summary of the candidate's key details. Candidates are then provided with an opportunity to review and refine their resumes based on this summary.



![image](https://github.com/anish2105/TalentBoost/assets/88924201/e207e948-ac9c-494d-8441-ff6a10801743)

If the resume is submitted, a pop-up is generated confirming the user's successful submission.



![image](https://github.com/anish2105/TalentBoost/assets/88924201/b93fe165-6ecf-46e5-b6a8-68b4989e6a0c)


If the resume meets the specified criteria, an automated email is sent to the candidate, containing login credentials and an invitation to participate in the initial assessment round.



![image](https://github.com/anish2105/TalentBoost/assets/88924201/e6a1ea7c-8bc7-44e6-8020-46f4906a5ee8)

A questionnaire is dynamically generated from the user's resume to evaluate the candidate's expertise in projects, skills, and other relevant experiences.



![image](https://github.com/anish2105/TalentBoost/assets/88924201/7a1fd61b-4af3-424b-83c3-783dfa8230cd)

Depending on the candidate's response, if it doesn't match the expected answer, a lower accuracy score is calculated.



![image](https://github.com/anish2105/TalentBoost/assets/88924201/adb72337-3d87-4e53-89e6-591866220a1f)

If the response matches the expected answer, a higher accuracy score is assigned. 
Following the completion of this round, an automated email is sent to the candidate with the results.

![image](https://github.com/anish2105/TalentBoost/assets/88924201/06b226c5-eb97-43c0-967a-d96d4a764ef8)

