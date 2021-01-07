*** Settings ***
Library    OperatingSystem
Library    ../Library/pylib


*** Keywords ***
Validate File Exists And Copy
    [Arguments]    ${filepath}