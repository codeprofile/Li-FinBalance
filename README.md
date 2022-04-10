# Li-FinBalance
Balancing a Financial Life settlement is very important because it decides the choices we make in life . Financial Life decides the quality of Life . 

<b>Li-FinBalance</b> :-  An Web Application that manages your Financial life and prompts you with necessary actions and taxes exempt applicable on your Finance.


<b> Architecture Diagram </b>

<img src =https://user-images.githubusercontent.com/94001814/162633562-34f4d8d9-4c68-4236-99f8-282626d66dc9.JPG width=75% height=75%>

<b> To Use Application there are 3 steps: </b>
  <ul>
  <li><b> Create User Profile</b><li>
    
   <img src=https://user-images.githubusercontent.com/94001814/162634383-14dca74a-da80-4309-bdc2-38ab7c2eea7b.png width=75% height=75%>
    </br>
    <p>Questionaries on the Create User Page are Important for Multi-label Model to Classify the tax deduction or exemption section accordingly</p>
    <b> All questionaries generates a `Feature matrix` such is then given as a input to a multi-label Classifier Model </b>
    
  <b> Feature List for the Model:</b> `['TAX_SAVING_FD', 'AGE_GTE_60', 'EPF_VPF_CONTRIBUTION','TUTION_FEE_2_CHILDREN', 'INTEREST_ON_SAVINGS_ACCOUNT_BELOW_10K','NPS_CONTRIBUTION', 'PPF', 'DISABILITY_STATUS', 'SPECIFIC_ILLNESS','LIFE_INSURANCE_PREMIUM', 'EDUCATION_LOAN','EDUCATION_LOAN_PERIOD_LTE_8', 'PROPERTY_LOAN', 'FIRST_PROPERTY','MEDICAL_EXPENSE']`
  
 <b> Target List of the Model :</b> `['80D', '80DD', '80DDB', '80E', '80EE', '80EEA','80TTB', '80TTA', '80CCD', '80C']`
       
 <li><b> Set Goal </b></li>
 
 
 <img src=https://user-images.githubusercontent.com/94001814/162634815-e4468cb0-c7b7-486c-a774-13852fa9bafd.png width=75% height=75%>
 
 
<li> <b> Goal Plan </b></li>


<P> Goal Plan are categories into : 1. Eligible Plan according to tax Slab  2. Not Eligible Plan </p>

<img src=https://user-images.githubusercontent.com/94001814/162634839-d6a19eb5-365c-46c8-a712-676645ff8642.png width=75% height=75%>
     
     
     
<b> All the Necessary Action Steps are listed in the roadmap to follow </b>


<img src=https://user-images.githubusercontent.com/94001814/162634870-df51efb5-5b5e-4435-acad-b668410b2c7f.png width=75% height=75%>

  </ul>
  
  
 <b> Steps to run the Project </b>
 <ul>
  <li> git clone `https://github.com/codeprofile/Li-FinBalance`
  <li> Cd into the project still `Li-FinBalance` </li>
  <li> run `pip install -r requirements.txt`</li>
  <li> run `flask run </li>
  </ul>
  
  

