import os

def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list) or \
       not all(isinstance(person, dict) for person in attendees):
        print("Invalid input: template must be a string and attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, person in enumerate(attendees, start=1):
        name = person.get("name", "N/A") or "N/A"
        event_title = person.get("event_title", "N/A") or "N/A"
        event_date = person.get("event_date", "N/A") or "N/A"
        event_location = person.get("event_location", "N/A") or "N/A"

        invitation = template.replace("{name}", name)
        invitation = invitation.replace("{event_title}", event_title)
        invitation = invitation.replace("{event_date}", event_date)
        invitation = invitation.replace("{event_location}", event_location)

        filename = f"output_{i}.txt"
        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")