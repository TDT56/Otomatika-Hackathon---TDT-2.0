*** Settings ***
Documentation     Template robot main suite.
Library           RPA.Browser.Selenium    auto_close=${FALSE}

*** Tasks ***
Download and process online data
    Open the corona worldometer website
    Download the countries table


*** Keywords ***
Open the corona worldometer website
    Open Headless Chrome Browser    https://www.worldometers.info/coronavirus/


Download the countries table
    Wait Until Element Is Visible    id:main_table_countries_today
    ${sales_results_html}=    Get Element Attribute    id:main_table_countries_today    outerHTML