*** Settings ***
Resource  resource.robot
Suite Setup    Open And Configure Browser
Suite Teardown    Close Browser
Test Setup    Reset Application Create User And Go To Login Page

*** Test Cases ***
Click Login Link
    Click Link   Login
    Login Page Should Be Open

Click Register Link
    Click Link   Register new user
    Register Page Should Be Open

*** Keywords ***

Reset Application Create User And Go To Login Page
    Reset Application
    Go To Starting Page