*** Settings ***
Resource  resource.robot
Suite Setup    Open And Configure Browser
Suite Teardown    Close Browser
Test Setup    Reset Application Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  newuser
    Set Password  newpassword123
    Set Password Confirmation  newpassword123
    Click Button  Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  validpassword123
    Set Password Confirmation  validpassword123
    Click Button  Register
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  validuser
    Set Password  ab
    Set Password Confirmation  ab
    Click Button  Register
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username and Invalid Password
    Set Username  validuser
    Set Password  password
    Set Password Confirmation  password
    Click Button  Register
    Registration Should Fail With Message  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  anotheruser
    Set Password  validpassword123
    Set Password Confirmation  differentpassword123
    Click Button  Register
    Registration Should Fail With Message  Passwords do not match

Register With Username That Is Already In User
    Set Username  kalle
    Set Password  anotherpassword123
    Set Password Confirmation  anotherpassword123
    Click Button  Register
    Registration Should Fail With Message  Username is already taken



*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Set Username
    [Arguments]    ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]    ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]    ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}  

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page