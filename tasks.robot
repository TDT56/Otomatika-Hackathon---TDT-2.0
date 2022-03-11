*** Settings ***
Documentation     Template robot main suite.

Library           RPA.Browser.Selenium    auto_close=${FALSE}

*** Tasks ***
Download and process online data
    Open the corona worldometer website


*** Keywords ***
Open the corona worldometer website
    Open Available Browser    https://www.worldometers.info/coronavirus/