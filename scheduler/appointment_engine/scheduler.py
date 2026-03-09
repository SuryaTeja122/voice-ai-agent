doctor_schedule = {
    "cardiologist": ["10:00", "11:00", "14:00"],
    "dermatologist": ["09:30", "13:00", "16:00"]
}

booked_slots = []

def check_availability(doctor):

    if doctor not in doctor_schedule:
        return []

    available = []

    for slot in doctor_schedule[doctor]:

        if (doctor, slot) not in booked_slots:
            available.append(slot)

    return available


def book_slot(doctor, time):

    if (doctor, time) in booked_slots:
        return False

    booked_slots.append((doctor, time))

    return True