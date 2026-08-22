import streamlit as st

from report_generator import generate_report


st.set_page_config(
    page_title="AI Bug Report Generator",
    page_icon="🐞"
)

st.title("🐞 AI Bug Report Generator")

st.write(
    "Generate professional bug bounty reports using AI."
)

vuln_type = st.selectbox(
    "Vulnerability Type",
    [
        "IDOR",
        "XSS",
        "SSRF",
        "CSRF",
        "Authentication Bypass",
        "Authorization Bypass",
        "Information Disclosure",
        "Open Redirect",
        "Rate Limit Bypass",
        "Other"
    ]
)

scope = st.text_input(
    "Scope / Affected Asset"
)

steps = st.text_area(
    "Steps to Reproduce"
)

impact = st.text_area(
    "Impact"
)

fix = st.text_area(
    "Suggested Fix"
)


if st.button("Generate Report"):

    if not scope or not steps:

        st.warning(
            "Please provide the affected asset and reproduction steps."
        )

    else:

        with st.spinner("Generating report..."):

            report = generate_report(
                vuln_type,
                scope,
                steps,
                impact,
                fix
            )

        st.subheader("Generated Report")

        st.markdown(report)

        st.download_button(
            "Download Report",
            report,
            file_name="bug_report.md",
            mime="text/markdown"
        )
