## Introduction: -
Nowadays, real time communication is increasingly rapidly. The popularity of this communication is mostly seen through messages and chats, whether be it personal messages or confidential emails. Thus, there is a need of some protection system which could prevent other party from intruding the privacy of the users. Encrypted Chatbot is such project where two or more authorized users can have chats and messages with no invasion of external party. The chats are encrypted end to end with use of different encryption methods and keys. This is done so as to protect the privacy of people and their messages. For securing of information, it is encrypted before it leaves a user's device and can only be decrypted by the intended recipient. The encrypted message is called as cipher text. For encryption and decryption both the users will require a Key, which might be public or private. The key needs to be created, stored, and offered robust end-to-end secure encryption. Therefore, this project will create texts and keys taking plain texts as input. The algorithm used for encryption is taking number series as a mathematical conversion and storing the secret word in a generated string. Have a safe space for your chats!

## Research: -
https://www.scientificamerican.com/article/crack-the-code-make-a-caesar-cipher/

## Swot Analysis: -

<p align="center">
  <img 
    width="500"
    height="500"
  src="https://github.com/Madhushreevp/OOPs-Python/blob/dfbf75b1646c4fd0f6f4015050372efdd7b7c255/1_Requirements/SWOT.PNG"
  >
</p>

## Requirements: -
| ID | Description | Input | Category | 
| --- | --- | --- | --- | 
| 01 | Number to be encoded | Integer | Logical | 
| 02 | Binary Array to be generated | Integer   | Logical | 
| 03 | Limit for the series to be set |Integer  | Mathematical | 
| 04 | Number Series to be generated | Integer | Mathematical | 
| 05 | Index to be appended at end of code  | Integer | Technical |  

## FLOW CHART: -

<p align="center">
  <img 
    width="600"
    height="600"
  src="https://github.com/Madhushreevp/OOPs-Python/blob/bb71a3e26ca723b38b0396b9c70d6c7f158eca6f/2_Architecture/flow_chart.png"
  >
</p>

## Implementation: -
* Download the code.
* Run the program in any python compiler.
* Give number as input.
* Encoded binary string will be generated. 

## Test plan and Output

### HIGH LEVEL TEST PLAN and LOW LEVEL TEST PLAN

| Test ID | Description | Input | Expected output | Actual Output | Passed or not |
| --- | --- | --- | --- | --- | --- |
| 01 | Limit | Integer | Boundary  | Boundary defined  |  ✅ |
| 02 | Limit | Integer   | Negative Number not acceptable | Negative Number stops system |   ✅ |
| 03 | Limit | Integer  | Number less than 10 not acceptable | Number less than 10 stops system | ✅ |
| 04 | Binary Array | Integer | Number to be encoded | Number is transcripted | ✅ |
| 05 | Binary Array | Integer | Number compared with Index  |  Number appended with Index  |    ✅ |  
| 06 | Binary Array | Integer | Number  series estimated   | Number  series calculated    |    ✅ |  
| 07 |Binary Array | Integer | Number generates usage bits  | Binary string stores encoded number    |    ✅ |  
| 08 | Index | Integer | Index used for secret word    | Index used for traversing    |    ✅ |  
| 09 | Length | Integer | Length of secret word      | Length calculated using Index             |    ✅ |  
| 10 | End of secret word  | Integer | Number appended in the end  | Digit 1 appended in the last   |    ✅ |  



## Outputs

### PyLint Score
<p align="center">
  <img 
    width="600"
    height="150"
src="https://github.com/Madhushreevp/OOPs-Python/blob/cae2b686aac6d84d5956f1676f6440b387dde919/4_TestPlan&Output/PyLint%20Score.PNG"
       >
</p>

### Different Output 
<p align="center">
  <img 
    width="600"
    height="300"
src="https://github.com/Madhushreevp/OOPs-Python/blob/cae2b686aac6d84d5956f1676f6440b387dde919/4_TestPlan&Output/output1.PNG"      
       >
</p>

<p align="center">
  <img 
    width="600"
    height="300"
src="https://github.com/Madhushreevp/OOPs-Python/blob/cae2b686aac6d84d5956f1676f6440b387dde919/4_TestPlan&Output/output2.PNG"      
       >
</p>

<p align="center">
  <img 
    width="600"
    height="300"
src="https://github.com/Madhushreevp/OOPs-Python/blob/cae2b686aac6d84d5956f1676f6440b387dde919/4_TestPlan&Output/output3.PNG"      
       >
</p>



