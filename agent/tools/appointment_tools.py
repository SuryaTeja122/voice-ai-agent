from scheduler.appointment_engine.scheduler import check_availability, book_slot

def book_appointment(patient, doctor, date):

    slots = check_availability(doctor)

    if not slots:
        return "No available slots for this doctor."

    slot = slots[0]

    success = book_slot(doctor, slot)

    if success:
        return f"Appointment booked with {doctor} at {slot} on {date}"

    return "Slot already booked"