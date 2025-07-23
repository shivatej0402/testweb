"""
LifePilot AI Agent - Demo Preview
=================================

This is a standalone demo version that shows the LifePilot interface
with sample data. No API keys or setup required for preview.
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# Configure the page
st.set_page_config(
    page_title="LifePilot AI Agent - Demo",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Demo data
SAMPLE_EMAILS = [
    {"time": "09:15", "subject": "Q4 Budget Review Meeting", "sender": "sarah@company.com", "priority": "High", "status": "✅"},
    {"time": "09:32", "subject": "Project Proposal Feedback", "sender": "mike@client.com", "priority": "Medium", "status": "⏳"},
    {"time": "10:05", "subject": "Job Alert: Senior Developer at TechCorp", "sender": "linkedin-jobs@linkedin.com", "priority": "Low", "status": "📋"},
    {"time": "10:18", "subject": "Team Lunch Coordination", "sender": "team@company.com", "priority": "Low", "status": "✅"},
    {"time": "11:24", "subject": "URGENT: Server Downtime Report", "sender": "ops@company.com", "priority": "High", "status": "🚨"},
]

SAMPLE_MEETINGS = [
    {"time": "10:00", "title": "Daily Standup", "attendees": 5, "agenda": "Generated"},
    {"time": "11:30", "title": "Client Review Meeting", "attendees": 8, "agenda": "Generated"},
    {"time": "14:00", "title": "Product Planning", "attendees": 6, "agenda": "Generated"},
    {"time": "15:30", "title": "1:1 with Manager", "attendees": 2, "agenda": "Generated"},
    {"time": "16:30", "title": "🔥 Focus Time", "attendees": 1, "agenda": "Auto-scheduled"},
]

SAMPLE_TASKS = [
    {"task": "Review Q4 budget proposal", "status": "In Progress", "priority": "High", "due": "Today"},
    {"task": "Email: Respond to client feedback", "status": "To Do", "priority": "High", "due": "Today"},
    {"task": "Prepare presentation slides", "status": "To Do", "priority": "Medium", "due": "Tomorrow"},
    {"task": "Update project documentation", "status": "Completed", "priority": "Low", "due": "Yesterday"},
    {"task": "Schedule team offsite", "status": "To Do", "priority": "Medium", "due": "This week"},
]

RECENT_ACTIVITY = [
    {"time": "09:15", "action": "Sent daily digest via WhatsApp", "status": "✅"},
    {"time": "09:30", "action": "Processed 5 new emails", "status": "✅"},
    {"time": "10:00", "action": "Created 2 tasks from emails", "status": "✅"},
    {"time": "10:15", "action": "Scheduled focus time (3+ meetings detected)", "status": "✅"},
    {"time": "10:30", "action": "Generated agenda for Client Review Meeting", "status": "✅"},
    {"time": "11:00", "action": "Detected calendar conflict - sent alert", "status": "⚠️"},
]


def create_demo_metrics():
    """Create demo metrics with realistic numbers."""
    return {
        "emails_processed": (142, 12),
        "tasks_completed": (28, 5),
        "meetings_scheduled": (15, 3),
        "time_saved": (8.5, 2.1),
        "productivity_score": 87,
        "uptime": "2d 14h 32m",
        "last_digest": "Today 08:30 AM",
        "integration_status": {
            "Gmail": "✅ Active",
            "Calendar": "✅ Active",
            "Notion": "✅ Active",
            "WhatsApp": "✅ Active",
            "AI Assistant": "✅ Active",
        },
    }


def simulate_agent_status():
    """Simulate live agent status."""
    return random.choice(["🟢 Active", "🟡 Processing", "🟢 Active"])


def main():
    """Main demo interface."""

    # Header
    st.title("🤖 LifePilot AI Agent")
    st.markdown("**Your Autonomous Personal Productivity Manager** - *Demo Preview*")

    # Demo notice
    st.info("🎭 **This is a demo preview** with sample data. The actual agent requires API setup for Gmail, Notion, etc.")

    metrics = create_demo_metrics()

    # Sidebar
    with st.sidebar:
        st.header("🎛️ Agent Controls")

        status = simulate_agent_status()
        st.markdown(f"**Status:** {status}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("▶️ Start"):
                st.success("Agent started! (Demo)")
        with col2:
            if st.button("⏸️ Pause"):
                st.warning("Agent paused! (Demo)")

        st.header("⚙️ Configuration")

        st.subheader("Quiet Hours")
        quiet_start = st.time_input(
            "Start Time", value=datetime.strptime("22:00", "%H:%M").time(), key="quiet_start"
        )
        quiet_end = st.time_input(
            "End Time", value=datetime.strptime("07:00", "%H:%M").time(), key="quiet_end"
        )

        st.subheader("Daily Digest")
        digest_time = st.time_input(
            "Send Time", value=datetime.strptime("08:30", "%H:%M").time(), key="digest_time"
        )

        if st.button("💾 Save Configuration"):
            st.success("Configuration saved! (Demo)")

        st.header("🔗 Integrations")
        for service, status in metrics["integration_status"].items():
            st.markdown(f"**{service}:** {status}")

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📧 Email Summary", "📅 Calendar", "📋 Tasks"])

    # Dashboard
    with tab1:
        st.header("📊 Agent Dashboard")

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Emails Processed", metrics["emails_processed"][0], f"+{metrics['emails_processed'][1]}")
        with c2:
            st.metric("Tasks Completed", metrics["tasks_completed"][0], f"+{metrics['tasks_completed'][1]}")
        with c3:
            st.metric("Meetings Scheduled", metrics["meetings_scheduled"][0], f"+{metrics['meetings_scheduled'][1]}")
        with c4:
            st.metric("Time Saved", f"{metrics['time_saved'][0]} hrs", f"+{metrics['time_saved'][1]} hrs")

        c5, c6 = st.columns(2)
        with c5:
            st.metric("Productivity Score", f"{metrics['productivity_score']}%", "+5%")
        with c6:
            st.metric("Uptime", metrics["uptime"])

        st.subheader("📈 Recent Activity")
        for a in RECENT_ACTIVITY:
            st.markdown(f"{a['status']} **{a['time']}** - {a['action']}")

        st.subheader("📊 Performance Trends")
        dates = [datetime.now() - timedelta(days=x) for x in range(7, 0, -1)]
        emails_data = [random.randint(15, 25) for _ in range(7)]
        tasks_data = [random.randint(3, 8) for _ in range(7)]
        chart_data = pd.DataFrame(
            {"Date": dates, "Emails Processed": emails_data, "Tasks Completed": tasks_data}
        )
        st.line_chart(chart_data.set_index("Date"))

    # Email Summary
    with tab2:
        st.header("📧 Email Summary")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Unread Emails", "7", "-3")
        with c2:
            st.metric("Priority Emails", "2", "+1")
        with c3:
            st.metric("Auto-Replies Sent", "4", "+2")

        st.subheader("Recent Email Activity")
        for email in SAMPLE_EMAILS:
            priority_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
            with st.expander(f"{email['status']} {email['time']} - {email['subject']} {priority_color[email['priority']]}"):
                st.markdown(f"**From:** {email['sender']}")
                st.markdown(f"**Priority:** {email['priority']}")
                if "Job Alert" in email["subject"]:
                    st.markdown("**AI Analysis:** Job posting detected - 78% match with your profile")
                    st.markdown("**Action:** Saved to Job Leads database in Notion")
                elif "URGENT" in email["subject"]:
                    st.markdown("**AI Analysis:** High priority - immediate attention required")
                    st.markdown("**Action:** Priority alert sent via WhatsApp")
                else:
                    st.markdown("**AI Analysis:** Actionable email - task created")
                    st.markdown("**Suggested Reply:** Generated and ready for review")

    # Calendar
    with tab3:
        st.header("📅 Calendar Intelligence")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Today's Meetings", "5", "+2")
        with c2:
            st.metric("Focus Time Scheduled", "1 hour", "Auto")
        with c3:
            st.metric("Conflicts Detected", "1", "Resolved")

        st.subheader("Today's Schedule")
        for mtg in SAMPLE_MEETINGS:
            agenda_icon = "📋" if mtg["agenda"] == "Generated" else "🔥"
            with st.expander(f"{agenda_icon} {mtg['time']} - {mtg['title']} ({mtg['attendees']} attendees)"):
                if mtg["title"] == "🔥 Focus Time":
                    st.markdown("**Type:** Auto-scheduled focus block")
                    st.markdown("**Reason:** 3+ meetings detected today")
                    st.markdown("**Recommendation:** Use for deep work on high-priority tasks")
                else:
                    st.markdown(f"**Attendees:** {mtg['attendees']} people")
                    st.markdown("**AI-Generated Agenda:**")
                    if "Standup" in mtg["title"]:
                        st.markdown("1. Yesterday's accomplishments\n2. Today's priorities\n3. Blockers\n4. Sprint update")
                    elif "Client" in mtg["title"]:
                        st.markdown("1. Status\n2. Deliverable review\n3. Feedback\n4. Next steps")
                    elif "Planning" in mtg["title"]:
                        st.markdown("1. Roadmap\n2. Features\n3. Resources\n4. Timeline")
                    else:
                        st.markdown("1. Check-in\n2. Goals\n3. Feedback\n4. Action items")

    # Tasks
    with tab4:
        st.header("📋 Task Management")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Active Tasks", "12", "+3")
        with c2:
            st.metric("Completed Today", "5", "+5")
        with c3:
            st.metric("Overdue", "1", "-2")

        st.subheader("Current Tasks")
        status_icons = {"Completed": "✅", "In Progress": "🔄", "To Do": "⏳"}
        priority_colors = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}

        for task in SAMPLE_TASKS:
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col1:
                st.markdown(f"{status_icons[task['status']]} {task['task']}")
            with col2:
                st.markdown(f"{priority_colors[task['priority']]} {task['priority']}")
            with col3:
                st.markdown(task["status"])
            with col4:
                st.markdown(task["due"])

        st.subheader("📬 Auto-Created from Emails")
        st.markdown("✅ **Review Q4 budget proposal** - Created from email at 09:15")
        st.markdown("⏳ **Respond to client feedback** - Created from email at 09:32")

        st.subheader("➕ Quick Task Entry")
        new_task = st.text_input("Add a quick task...", placeholder="e.g., Call dentist for appointment")
        if st.button("Add Task") and new_task:
            st.success(f"Task '{new_task}' added and will be auto-processed! (Demo)")

    # Footer
    st.markdown("---")
    st.markdown("**🤖 LifePilot AI Agent Demo** - Built for productivity enthusiasts")
    st.markdown(
        "*This preview shows the interface with sample data. The real agent automates your Gmail, Calendar, Notion, and messaging workflows.*"
    )


if __name__ == "__main__":
    main()
