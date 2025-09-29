# utils.py
# This file can contain utility functions, helper classes, or other reusable code.
# For example, you might include functions for:
# - Validating data
# - Formatting data
# - Interacting with external APIs
# - Implementing business logic

# Example: A simple function to calculate a lead score (this would ideally be in a separate microservice)
def calculate_lead_score(lead_data):
    """Calculates a lead score based on lead data."""
    score = 0
    if lead_data.get("travelPreferences"):  # type: ignore
        score += 5
    if lead_data.get("source") == "website": # type: ignore
        score += 3
    # Add more scoring logic based on your requirements
    return score
