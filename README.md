# 🌱 Hydroponic Management System

A Python-based desktop application designed to assist school hydroponic teams in automating plant system monitoring and control through Arduino integration, a structured SQL database, and a user-friendly graphical interface.

---

## 📘 Project Background

In collaboration with Cathy, a student leader maintaining our school’s hydroponic systems, this project addresses two major pain points:

1. Manual operation of lighting and fan systems.  
2. Tedious daily measurement of environmental data (e.g., water level, temperature).

To reduce this workload and prevent crop failure from human error, Cathy and I designed an application that:
- **Connects with Arduino sensors and controllers**
- **Stores and analyzes data using an SQLite database**
- **Provides a GUI with user-access control and visual feedback**

> “I want the application to provide different functions to the guests and our members of the project.” — *Cathy, client interview*

---

## 🧠 Solution Overview

### Core Features
- Real-time monitoring of multiple hydroponic systems
- Secure login with user authority levels (Guest, Admin, Super Admin)
- Auto-generated graphs and reports
- GUI-based system control (e.g., lighting schedules)
- Local SQLite database with potential for future cloud migration

### Technical Stack
- **Frontend:** Python `tkinter`, `tkcalendar`, `tktimepicker`
- **Backend:** Python + SQLite3
- **Data Visualization:** `pygmt`
- **Hardware Interface:** Arduino integration via PySerial (planned)

---

## ✅ Success Criteria

### Frontend
- ✔️ GUI includes login, tabs, sliders, time selectors, and graphs
- ✔️ Access varies by user role: Guests (read-only), Admins (limited input), Super Admins (full control)
- ✔️ Values displayed clearly with unit labels and decimal formatting
- ✔️ Interactive date/time pickers for modeling and input
- ✔️ Scalable graphs with dynamic axis adjustment

### Backend
- ✔️ SQLite database synchronized with GUI
- ✔️ Sensor simulation via multithreading mock data generator
- ✔️ Editable data fields and responsive data display
- ✔️ User management system with admin control panel
- ✔️ Secure login with password masking and storage outside GUI

### Hardware Integration
- ⚠️ Lighting successfully controlled via Arduino LED setup
- ⚠️ Other sensors not yet tested due to hardware constraints

---

## 🧪 Techniques Used

- Multithreading (mock sensor simulation)
- Inheritance and modular class structure
- Secure SQLite data transactions
- GUI layout using prebuilt libraries to save development time
- Custom status analysis logic using value thresholds

```python
IF current > high:
    result = "very high"
    alarmText += f"{type} is too high. Please check it immediately!"
````

---

## 🛠 Development Timeline

| Task                            | Description                  | Status |
| ------------------------------- | ---------------------------- | ------ |
| Initial client interview        | Define project needs         | ✅      |
| UML, wireframes, pseudocode     | Technical design             | ✅      |
| DB setup + mock data simulation | Back-end foundation          | ✅      |
| GUI + data visual tools         | Front-end layout             | ✅      |
| Arduino LED control             | Partial hardware integration | ✅      |
| Full sensor communication       | Not completed                | ❌      |
| Client testing & feedback       | Final evaluation             | ✅      |

> “The program works well, but I want to upload the database to the cloud and make the GUI prettier.” — *Cathy, feedback interview*

---

## 🔮 Future Improvements

1. **Cloud database migration** for multi-device access
2. **UI enhancements** for better readability and design
3. **On-screen usage instructions** for novice users
4. **Dynamic system scaling** to manage more than 10 hydroponic setups

---

## 📚 References

* [SQLite Home Page](https://www.sqlite.org) — SQLite team
* [PyGMT Documentation](https://www.pygmt.org/latest/) — PyGMT developers
* “Python GUI Programming with Tkinter – Real Python” — David Amos
* “Python Serial Port Communication” — Instructables
* [Tkcalendar Docs](https://tkcalendar.readthedocs.io/en/stable/)
* [Threading in Python](https://docs.python.org/3/library/threading.html)
