"""
CP1404 Week 07 Practical
Project
Estimate Time: 3 Hours
Actual Time: 4 hours 15 mins
"""
import datetime


class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """String representation of Project object."""
        return (
            f"{self.name}, start: {self.start_date.strftime('%d/%m/%y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f},"
            f" completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Return date compare for less than sign operator."""
        return self.start_date < other.start_date

    def is_complete(self):
        """Return true if project in 100% complete."""
        return self.completion_percentage == 100
