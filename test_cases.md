```markdown
# Agentic CRM Application - Test Cases

This document outlines comprehensive test cases for the Agentic CRM application based on the provided requirements, user stories, and code artifacts.

## 1. Functional Tests

These tests verify the core functionality of the application, ensuring that each feature works as expected.

### Lead Management

**Test ID:** FT-LM-001
**Title:** Create a New Lead - Valid Data
**Description:** Verify that a new lead can be created with valid data.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Navigate to the "Create Lead" page.
2.  Enter valid data for all required fields (firstName, lastName, email, phone).
3.  Optionally, enter valid data for travelPreferences and source.
4.  Click the "Save" button.
**Expected Results:**
1.  A new lead is created in the database.
2.  The application displays a success message.
3.  The newly created lead is displayed with the correct information.
4.  The leadScore is 0.
**Postconditions:** None

**Test ID:** FT-LM-002
**Title:** Create a New Lead - Invalid Email Format
**Description:** Verify that the system rejects a lead creation attempt with an invalid email format.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Navigate to the "Create Lead" page.
2.  Enter valid data for firstName, lastName, and phone.
3.  Enter an invalid email address (e.g., "invalid-email").
4.  Enter data for travelPreferences and source.
5.  Click the "Save" button.
**Expected Results:**
1.  The system displays an error message indicating an invalid email format.
2.  The lead is not created in the database.
**Postconditions:** None

**Test ID:** FT-LM-003
**Title:** Read Lead by ID - Valid ID
**Description:** Verify that a lead can be retrieved by a valid ID.
**Preconditions:** At least one lead exists in the database.
**Test Steps:**
1.  Retrieve the ID of an existing lead from the database or UI.
2.  Navigate to the "Read Lead" endpoint using the retrieved ID.
**Expected Results:**
1.  The application displays the lead information corresponding to the provided ID.
**Postconditions:** None

**Test ID:** FT-LM-004
**Title:** Read Lead by ID - Invalid ID
**Description:** Verify that the system returns an error when trying to retrieve a lead with an invalid ID.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Navigate to the "Read Lead" endpoint using an invalid UUID.
**Expected Results:**
1.  The system returns a 404 Not Found error with the message "Lead not found".
**Postconditions:** None

**Test ID:** FT-LM-005
**Title:** Update Lead - Valid Data
**Description:** Verify that an existing lead can be updated with valid data.
**Preconditions:** At least one lead exists in the database.
**Test Steps:**
1.  Retrieve the ID of an existing lead from the database or UI.
2.  Navigate to the "Update Lead" endpoint using the retrieved ID.
3.  Modify the lead information with valid data.
4.  Click the "Save" button.
**Expected Results:**
1.  The lead in the database is updated with the new information.
2.  The application displays a success message.
3.  The updated lead is displayed with the correct information, including updated `updatedAt` field.
**Postconditions:** None

**Test ID:** FT-LM-006
**Title:** Update Lead - Non-Existent Lead
**Description:** Verify that the system returns an error when attempting to update a non-existent lead.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Attempt to update a lead using an ID that does not exist in the database.
**Expected Results:**
1.  The system returns a 404 Not Found error with the message "Lead not found".
**Postconditions:** None

**Test ID:** FT-LM-007
**Title:** Delete Lead - Valid ID
**Description:** Verify that a lead can be deleted by a valid ID.
**Preconditions:** At least one lead exists in the database.
**Test Steps:**
1.  Retrieve the ID of an existing lead from the database or UI.
2.  Navigate to the "Delete Lead" endpoint using the retrieved ID.
3.  Confirm the deletion (if prompted).
**Expected Results:**
1.  The lead is removed from the database.
2.  The application displays a success message.
3.  Attempting to retrieve the deleted lead by ID results in a 404 error.
**Postconditions:** None

**Test ID:** FT-LM-008
**Title:** Delete Lead - Non-Existent Lead
**Description:** Verify that the system returns an error when attempting to delete a non-existent lead.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Attempt to delete a lead using an ID that does not exist in the database.
**Expected Results:**
1.  The system returns a 404 Not Found error with the message "Lead not found".
**Postconditions:** None

**Test ID:** FT-LM-009
**Title:** Import Leads - Valid CSV File
**Description:** Verify that leads can be imported from a valid CSV file.
**Preconditions:** A valid CSV file with lead data is available.
**Test Steps:**
1.  Navigate to the "Import Leads" page.
2.  Upload the valid CSV file.
3.  Click the "Import" button.
**Expected Results:**
1.  The leads from the CSV file are created in the database.
2.  The application displays a success message with the number of leads imported.
**Postconditions:** None

**Test ID:** FT-LM-010
**Title:** Import Leads - Invalid CSV File (Incorrect Format)
**Description:** Verify that the system handles an invalid CSV file (e.g., missing required columns).
**Preconditions:** An invalid CSV file with missing required columns is available.
**Test Steps:**
1.  Navigate to the "Import Leads" page.
2.  Upload the invalid CSV file.
3.  Click the "Import" button.
**Expected Results:**
1.  The system displays an error message indicating the invalid CSV format and specific error encountered.
2.  No leads are imported from the CSV file.
**Postconditions:** None

**Test ID:** FT-LM-011
**Title:** Import Leads - Invalid CSV File (Invalid Data)
**Description:** Verify that the system handles an invalid CSV file (e.g., invalid email format).
**Preconditions:** An invalid CSV file with data that violates validation rules is available.
**Test Steps:**
1.  Navigate to the "Import Leads" page.
2.  Upload the invalid CSV file.
3.  Click the "Import" button.
**Expected Results:**
1.  The system attempts to import leads.
2.  The system displays an error message indicating the invalid data.
3.  No leads with the invalid data are imported. Leads with valid data are imported successfully.
**Postconditions:** None

**Test ID:** FT-LM-012
**Title:** Import Leads - Empty CSV File
**Description:** Verify that the system handles an empty CSV file.
**Preconditions:** An empty CSV file is available.
**Test Steps:**
1.  Navigate to the "Import Leads" page.
2.  Upload the empty CSV file.
3.  Click the "Import" button.
**Expected Results:**
1.  The system displays a message indicating that no leads were imported.
2.  No leads are imported from the CSV file.
**Postconditions:** None

**Test ID:** FT-LM-013
**Title:** Convert Lead to Customer - Valid Lead ID
**Description:** Verify that a lead can be converted to a customer.
**Preconditions:** A lead exists in the database.
**Test Steps:**
1.  Retrieve the ID of an existing lead from the database or UI.
2.  Navigate to the "Convert Lead" endpoint using the retrieved ID.
**Expected Results:**
1.  A new customer is created in the database with the lead's information.
2.  The original lead is deleted from the database.
3.  The application returns the created customer details.
**Postconditions:** None

**Test ID:** FT-LM-014
**Title:** Convert Lead to Customer - Invalid Lead ID
**Description:** Verify that the system returns an error when converting a non-existent lead.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Attempt to convert a lead using an ID that does not exist in the database.
**Expected Results:**
1.  The system returns a 404 Not Found error with the message "Lead not found".
**Postconditions:** None

### Customer Management

**Test ID:** FT-CM-001
**Title:** Create a New Customer - Valid Data
**Description:** Verify that a new customer can be created with valid data.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Navigate to the "Create Customer" page.
2.  Enter valid data for all required fields (firstName, lastName, email, phone).
3.  Optionally, enter valid data for preferences.
4.  Click the "Save" button.
**Expected Results:**
1.  A new customer is created in the database.
2.  The application displays a success message.
3.  The newly created customer is displayed with the correct information.
**Postconditions:** None

**Test ID:** FT-CM-002
**Title:** Read Customer by ID - Valid ID
**Description:** Verify that a customer can be retrieved by a valid ID.
**Preconditions:** At least one customer exists in the database.
**Test Steps:**
1.  Retrieve the ID of an existing customer from the database or UI.
2.  Navigate to the "Read Customer" endpoint using the retrieved ID.
**Expected Results:**
1.  The application displays the customer information corresponding to the provided ID.
**Postconditions:** None

**Test ID:** FT-CM-003
**Title:** Read Customer by ID - Invalid ID
**Description:** Verify that the system returns an error when trying to retrieve a customer with an invalid ID.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Navigate to the "Read Customer" endpoint using an invalid UUID.
**Expected Results:**
1.  The system returns a 404 Not Found error with the message "Customer not found".
**Postconditions:** None

### Communication Management

**Test ID:** FT-CC-001
**Title:** Send Email - Valid Data
**Description:** Verify that an email can be sent with valid data.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Navigate to the "Send Email" page.
2.  Enter valid data for all required fields (recipient, subject, body).
3.  Click the "Send" button.
**Expected Results:**
1.  An email record is created in the database with the provided information.
2.  The email status is set to "sent". (This assumes a mock email sending)
3.  The application displays a success message.
**Postconditions:** None

**Test ID:** FT-CC-002
**Title:** Send SMS - Valid Data
**Description:** Verify that an SMS can be sent with valid data.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Navigate to the "Send SMS" page.
2.  Enter valid data for all required fields (recipient, body).
3.  Click the "Send" button.
**Expected Results:**
1.  An SMS record is created in the database with the provided information.
2.  The SMS status is set to "sent". (This assumes a mock SMS sending)
3.  The application displays a success message.
**Postconditions:** None

**Test ID:** FT-CC-003
**Title:** Get Communication Suggestions - Valid Lead ID
**Description:** Verify that the system returns communication suggestions for a valid lead ID.
**Preconditions:** A lead exists in the database.
**Test Steps:**
1.  Retrieve the ID of an existing lead from the database or UI.
2.  Navigate to the "Get Communication Suggestions" endpoint using the retrieved ID.
**Expected Results:**
1.  The system returns a dictionary containing lists of email templates and call scripts.
2.  The lists contain the expected dummy data.
**Postconditions:** None

**Test ID:** FT-CC-004
**Title:** Get Communication Suggestions - Invalid Lead ID
**Description:** Verify that the system handles an invalid lead ID when requesting communication suggestions.  Although this currently returns static data, we should test it anyway, anticipating future functionality.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Navigate to the "Get Communication Suggestions" endpoint using an invalid UUID.
**Expected Results:**
1.  The system returns a dictionary containing lists of email templates and call scripts.
2.  The lists contain the expected dummy data.  (Currently returns static data, future implementation should return an error if ID is invalid)
**Postconditions:** None

## 2. Integration Tests

These tests verify the interaction between different components of the application.

**Test ID:** IT-LM-CM-001
**Title:** Lead Creation and Conversion to Customer
**Description:** Verify that a lead can be created and successfully converted to a customer, and the customer data is accurate.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Create a new lead using the "Create Lead" endpoint.
2.  Retrieve the ID of the newly created lead.
3.  Convert the lead to a customer using the "Convert Lead" endpoint.
4.  Retrieve the customer using the customer ID.
**Expected Results:**
1.  A new lead is created in the database.
2.  The lead is successfully converted to a customer.
3.  The customer data matches the lead data.
4.  The lead is deleted after conversion.

**Test ID:** IT-CC-LM-001
**Title:** Send Email to Newly Created Lead
**Description:** Verify that an email can be sent to a newly created lead.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1. Create a new lead using the "Create Lead" endpoint.
2. Retrieve the email of the newly created lead.
3. Send an email to the lead's email address using the "Send Email" endpoint.
**Expected Results:**
1. A new lead is created in the database.
2. An email record is created in the database with the lead's email.
3. The email status is set to "sent". (This assumes a mock email sending)

## 3. Edge Case Tests

These tests verify the application's behavior under unusual or boundary conditions.

**Test ID:** EC-LM-001
**Title:** Create Lead - Long String Fields
**Description:** Verify that the system handles extremely long strings for text fields (firstName, lastName, travelPreferences).
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Navigate to the "Create Lead" page.
2.  Enter a very long string (e.g., 1000+ characters) for firstName, lastName, and travelPreferences.
3.  Enter valid data for other required fields.
4.  Click the "Save" button.
**Expected Results:**
1.  The system either:
    *   Successfully creates the lead with the truncated string (if truncation is implemented).
    *   Returns an error message indicating the maximum allowed length for the fields.

**Test ID:** EC-LM-002
**Title:** Import Leads - Large CSV File
**Description:** Verify that the system can handle importing a very large CSV file (e.g., 10,000+ leads).
**Preconditions:** A large CSV file with lead data is available.
**Test Steps:**
1.  Navigate to the "Import Leads" page.
2.  Upload the large CSV file.
3.  Click the "Import" button.
**Expected Results:**
1.  The system imports the leads from the CSV file.
2.  The application displays a success message with the number of leads imported.
3.  The import process does not time out or crash the application.

**Test ID:** EC-CC-001
**Title:** Send SMS - Long SMS Body
**Description:** Verify that the system handles an SMS body that exceeds the maximum allowed length.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Navigate to the "Send SMS" page.
2.  Enter a very long string (e.g., 200+ characters) for the SMS body.
3.  Enter a valid phone number.
4.  Click the "Send" button.
**Expected Results:**
1. The system either:
    * Successfully sends the truncated SMS message.
    * Return an error message indicating the maximum allowed length for the SMS body.

## 4. Performance Tests

These tests evaluate the application's performance under various load conditions.  These tests require more infrastructure and tools that are not provided in the initial prompt, so they will only be outlined.

**Test ID:** PT-LM-001
**Title:** Concurrent Lead Creation
**Description:** Measure the application's response time when multiple users simultaneously create leads.
**Preconditions:** The application is running and accessible. A performance testing tool is available (e.g., JMeter, Locust).
**Test Steps:**
1.  Configure the performance testing tool to simulate multiple concurrent users creating leads (e.g., 50 users).
2.  Run the test for a specified duration (e.g., 10 minutes).
**Expected Results:**
1.  The average response time for lead creation remains within acceptable limits (e.g., < 2 seconds).
2.  The application does not experience any errors or crashes.
3.  Resource utilization (CPU, memory) remains within acceptable limits.

**Test ID:** PT-LM-002
**Title:** Lead Import Performance
**Description:** Measure the time taken to import a large CSV file with leads.
**Preconditions:** The application is running and accessible. A large CSV file with lead data is available.
**Test Steps:**
1.  Navigate to the "Import Leads" page.
2.  Upload the large CSV file.
3.  Start a timer.
4.  Click the "Import" button.
5.  Stop the timer when the import is complete.
**Expected Results:**
1.  The import process completes within an acceptable timeframe (e.g., < 5 minutes for 10,000 leads).
2.  The application does not experience any errors or crashes.

**Test ID:** PT-CC-001
**Title:** Concurrent Communication Suggestion Requests
**Description:** Measure the application's response time when multiple users simultaneously request communication suggestions.
**Preconditions:** The application is running and accessible. A performance testing tool is available (e.g., JMeter, Locust).
**Test Steps:**
1.  Configure the performance testing tool to simulate multiple concurrent users requesting communication suggestions (e.g., 50 users).
2.  Run the test for a specified duration (e.g., 10 minutes).
**Expected Results:**
1.  The average response time for communication suggestion requests remains within acceptable limits (e.g., < 1 second).
2.  The application does not experience any errors or crashes.
3.  Resource utilization (CPU, memory) remains within acceptable limits.

## 5. Security Tests

These tests assess the application's security vulnerabilities.

**Test ID:** ST-AU-001
**Title:** Unauthorized Access to Lead Data
**Description:** Verify that a user without proper authorization cannot access lead data.
**Preconditions:** User role management is implemented. Two users exist: one with access to lead data and one without.
**Test Steps:**
1.  Log in as the user without access to lead data.
2.  Attempt to access the "Read Lead" endpoint using a valid lead ID.
**Expected Results:**
1.  The system returns an "Unauthorized" or "Forbidden" error.
2.  The user is not able to view the lead data.

**Test ID:** ST-SQL-001
**Title:** SQL Injection Vulnerability Test
**Description:** Verify that the application is protected against SQL injection attacks.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Attempt to inject SQL code into the "Read Lead" endpoint by modifying the lead ID parameter.  For example: `1' OR '1'='1`
**Expected Results:**
1.  The system does not execute the injected SQL code.
2.  The system returns an error message or behaves normally without revealing sensitive information.

**Test ID:** ST-XXS-001
**Title:** Cross-Site Scripting (XSS) Vulnerability Test
**Description:** Verify that the application is protected against XSS attacks.
**Preconditions:** The application is running and accessible.
**Test Steps:**
1.  Attempt to inject JavaScript code into a lead field (e.g., firstName) during lead creation.  For example: `<script>alert('XSS')</script>`
2.  Attempt to view the created lead.
**Expected Results:**
1.  The injected JavaScript code is not executed.
2.  The application either sanitizes the input or encodes the output to prevent XSS attacks.

**Test ID:** ST-IDOR-001
**Title:** Insecure Direct Object References (IDOR)
**Description:** Verify that users cannot access resources belonging to other users by manipulating IDs.
**Preconditions:** Two leads are created by different users.
**Test Steps:**
1. Log in as user A.
2. Obtain the lead ID of a lead created by user B.
3. As user A, attempt to access the lead created by user B using the "Read Lead" endpoint with the lead ID obtained in the previous step.
**Expected Results:**
1. The system returns an "Unauthorized" or "Forbidden" error.
2. User A is not able to view the lead data belonging to user B.

These test cases provide a comprehensive framework for testing the Agentic CRM application. They cover functional, integration, edge case, performance, and security aspects of the system. Remember to adapt these test cases based on the specific implementation details and evolving requirements of the application.