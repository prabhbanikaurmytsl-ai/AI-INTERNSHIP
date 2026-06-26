import os
import streamlit as st
from pathlib import Path
from datetime import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FileOS",
    page_icon="🗂",
    layout="centered",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&family=Inter:wght@300;400;500&display=swap');

/* Reset & base */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0d0f12;
    color: #c9d1d9;
}

.stApp {
    background-color: #0d0f12;
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 680px; }

/* ── Header bar ── */
.os-header {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 400;
    color: #484f58;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    border-bottom: 1px solid #1c2128;
    padding-bottom: 14px;
    margin-bottom: 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.os-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 22px;
    font-weight: 700;
    color: #e6edf3;
    letter-spacing: -0.02em;
    margin-bottom: 2px;
}

.os-subtitle {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #3fb950;
    letter-spacing: 0.08em;
}

/* ── Operation selector pills ── */
.pill-row {
    display: flex;
    gap: 8px;
    margin-bottom: 24px;
    flex-wrap: wrap;
}

/* ── Panel ── */
.panel {
    background: #161b22;
    border: 1px solid #1c2128;
    border-radius: 6px;
    padding: 24px;
    margin-bottom: 16px;
}

.panel-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    color: #484f58;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.panel-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1c2128;
}

/* ── Inputs ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background-color: #0d1117 !important;
    border: 1px solid #30363d !important;
    border-radius: 4px !important;
    color: #e6edf3 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 13px !important;
    padding: 10px 12px !important;
    transition: border-color 0.15s ease !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #3fb950 !important;
    box-shadow: 0 0 0 2px rgba(63, 185, 80, 0.12) !important;
}

.stTextInput label, .stTextArea label, .stSelectbox label, .stRadio label {
    color: #8b949e !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 11px !important;
    font-weight: 500 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
}

/* ── Radio as segmented tabs ── */
.stRadio > div {
    flex-direction: row !important;
    gap: 0 !important;
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 4px;
    padding: 3px;
    display: inline-flex !important;
}

.stRadio > div > label {
    background: transparent !important;
    border-radius: 3px !important;
    padding: 6px 14px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    color: #484f58 !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
    margin: 0 !important;
}

.stRadio > div > label:has(input:checked) {
    background: #21262d !important;
    color: #e6edf3 !important;
}

/* ── Buttons ── */
.stButton > button {
    background: #238636 !important;
    color: #fff !important;
    border: 1px solid #2ea043 !important;
    border-radius: 4px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em !important;
    padding: 8px 20px !important;
    transition: all 0.15s ease !important;
}

.stButton > button:hover {
    background: #2ea043 !important;
    border-color: #3fb950 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(35, 134, 54, 0.3) !important;
}

/* Danger button for delete */
.danger-btn .stButton > button {
    background: #21262d !important;
    border-color: #da3633 !important;
    color: #f85149 !important;
}

.danger-btn .stButton > button:hover {
    background: #da3633 !important;
    color: #fff !important;
    box-shadow: 0 4px 12px rgba(218, 54, 51, 0.3) !important;
}

/* ── Output terminal ── */
.terminal-out {
    background: #0d1117;
    border: 1px solid #1c2128;
    border-left: 3px solid #3fb950;
    border-radius: 4px;
    padding: 16px 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.5px;
    line-height: 1.7;
    color: #aff0b5;
    margin-top: 16px;
    white-space: pre-wrap;
    word-break: break-word;
}

.terminal-err {
    background: #0d1117;
    border: 1px solid #1c2128;
    border-left: 3px solid #f85149;
    border-radius: 4px;
    padding: 16px 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.5px;
    color: #f85149;
    margin-top: 16px;
}

.terminal-warn {
    background: #0d1117;
    border: 1px solid #1c2128;
    border-left: 3px solid #d29922;
    border-radius: 4px;
    padding: 16px 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.5px;
    color: #e3b341;
    margin-top: 16px;
}

/* ── File list ── */
.file-entry {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 0;
    border-bottom: 1px solid #1c2128;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
}

.file-entry:last-child { border-bottom: none; }

.file-icon { color: #484f58; }
.file-name { color: #79c0ff; flex: 1; }
.file-size { color: #484f58; font-size: 10px; }

/* ── Selectbox ── */
.stSelectbox > div > div {
    background-color: #0d1117 !important;
    border: 1px solid #30363d !important;
    color: #e6edf3 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 13px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "output" not in st.session_state:
    st.session_state.output = None
if "output_type" not in st.session_state:
    st.session_state.output_type = "success"

# ── Helpers ───────────────────────────────────────────────────────────────────
def set_output(msg, kind="success"):
    st.session_state.output = msg
    st.session_state.output_type = kind

def file_size_str(path: Path) -> str:
    b = path.stat().st_size
    if b < 1024: return f"{b} B"
    elif b < 1024**2: return f"{b/1024:.1f} KB"
    return f"{b/1024**2:.1f} MB"

def list_local_files():
    cwd = Path(".")
    return [f for f in sorted(cwd.iterdir()) if f.is_file()]

# ── Header ────────────────────────────────────────────────────────────────────
now = datetime.now().strftime("%Y-%m-%d  %H:%M")
st.markdown(f"""
<div class="os-header">
  <div>
    <div class="os-title">FileOS</div>
    <div class="os-subtitle">● filesystem manager v1.0</div>
  </div>
  <div>{now}</div>
</div>
""", unsafe_allow_html=True)

# ── Operation tabs ─────────────────────────────────────────────────────────────
op = st.radio(
    "OPERATION",
    ["CREATE", "READ", "UPDATE", "DELETE", "BROWSE"],
    horizontal=True,
    label_visibility="collapsed",
)

st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# CREATE
# ═══════════════════════════════════════════════════════════════════════════════
if op == "CREATE":
    st.markdown('<div class="panel"><div class="panel-label">New File</div>', unsafe_allow_html=True)
    fname = st.text_input("FILENAME", placeholder="notes.txt", key="c_name")
    content = st.text_area("CONTENT", placeholder="Start writing…", height=140, key="c_content")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("CREATE FILE →"):
        if not fname.strip():
            set_output("No filename provided.", "error")
        else:
            p = Path(fname.strip())
            if p.exists():
                set_output(f"'{p}' already exists.", "warn")
            else:
                try:
                    p.write_text(content)
                    set_output(f"Created  →  {p}\nSize     →  {file_size_str(p)}\nTime     →  {datetime.now().strftime('%H:%M:%S')}")
                except Exception as e:
                    set_output(str(e), "error")

# ═══════════════════════════════════════════════════════════════════════════════
# READ
# ═══════════════════════════════════════════════════════════════════════════════
elif op == "READ":
    files = list_local_files()
    st.markdown('<div class="panel"><div class="panel-label">Open File</div>', unsafe_allow_html=True)
    if files:
        fname = st.selectbox("SELECT FILE", [f.name for f in files], key="r_sel")
    else:
        st.markdown('<div class="terminal-warn">No files found in current directory.</div>', unsafe_allow_html=True)
        fname = None
    manual = st.text_input("OR TYPE PATH", placeholder="path/to/file.txt", key="r_manual")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("READ FILE →"):
        target = manual.strip() if manual.strip() else fname
        if not target:
            set_output("No file selected.", "error")
        else:
            p = Path(target)
            if not p.exists():
                set_output(f"'{p}' does not exist.", "error")
            else:
                try:
                    txt = p.read_text()
                    lines = txt.count('\n') + 1
                    set_output(f"── {p}  ({file_size_str(p)}, {lines} lines) ──\n\n{txt}")
                except Exception as e:
                    set_output(str(e), "error")

# ═══════════════════════════════════════════════════════════════════════════════
# UPDATE
# ═══════════════════════════════════════════════════════════════════════════════
elif op == "UPDATE":
    files = list_local_files()
    st.markdown('<div class="panel"><div class="panel-label">Modify File</div>', unsafe_allow_html=True)
    if files:
        fname = st.selectbox("SELECT FILE", [f.name for f in files], key="u_sel")
    else:
        fname = None
    manual = st.text_input("OR TYPE PATH", placeholder="path/to/file.txt", key="u_manual")

    action = st.radio("ACTION", ["Append", "Overwrite", "Rename"], horizontal=True, key="u_action")
    st.markdown("</div>", unsafe_allow_html=True)

    target = manual.strip() if manual.strip() else fname

    if action in ("Append", "Overwrite"):
        st.markdown('<div class="panel"><div class="panel-label">Content</div>', unsafe_allow_html=True)
        new_data = st.text_area(
            "TEXT" if action == "Overwrite" else "TEXT TO APPEND",
            height=120, key="u_data"
        )
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button(f"{action.upper()} →"):
            if not target:
                set_output("No file selected.", "error")
            else:
                p = Path(target)
                if not p.exists():
                    set_output(f"'{p}' does not exist.", "error")
                else:
                    try:
                        mode = 'a' if action == "Append" else 'w'
                        with open(p, mode) as f:
                            f.write(new_data)
                        set_output(f"{'Appended to' if mode=='a' else 'Overwrote'}  →  {p}\nSize now  →  {file_size_str(p)}")
                    except Exception as e:
                        set_output(str(e), "error")

    else:  # Rename
        st.markdown('<div class="panel"><div class="panel-label">New Name</div>', unsafe_allow_html=True)
        new_name = st.text_input("NEW FILENAME", placeholder="renamed.txt", key="u_newname")
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("RENAME →"):
            if not target:
                set_output("No file selected.", "error")
            elif not new_name.strip():
                set_output("New filename is empty.", "error")
            else:
                p = Path(target)
                np = Path(new_name.strip())
                if not p.exists():
                    set_output(f"'{p}' does not exist.", "error")
                elif np.exists():
                    set_output(f"'{np}' already exists.", "warn")
                else:
                    try:
                        os.rename(p, np)
                        set_output(f"Renamed  →  {p}  →  {np}")
                    except Exception as e:
                        set_output(str(e), "error")

# ═══════════════════════════════════════════════════════════════════════════════
# DELETE
# ═══════════════════════════════════════════════════════════════════════════════
elif op == "DELETE":
    files = list_local_files()
    st.markdown('<div class="panel"><div class="panel-label">Remove File</div>', unsafe_allow_html=True)
    if files:
        fname = st.selectbox("SELECT FILE", [f.name for f in files], key="d_sel")
    else:
        st.markdown('<div class="terminal-warn">No files found in current directory.</div>', unsafe_allow_html=True)
        fname = None
    manual = st.text_input("OR TYPE PATH", placeholder="path/to/file.txt", key="d_manual")
    confirm = st.checkbox("I understand this action is permanent", key="d_confirm")
    st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="danger-btn">', unsafe_allow_html=True)
        clicked = st.button("DELETE FILE →")
        st.markdown("</div>", unsafe_allow_html=True)

    if clicked:
        target = manual.strip() if manual.strip() else fname
        if not target:
            set_output("No file selected.", "error")
        elif not confirm:
            set_output("Check the confirmation box first.", "warn")
        else:
            p = Path(target)
            if not p.exists():
                set_output(f"'{p}' does not exist.", "error")
            else:
                try:
                    os.remove(p)
                    set_output(f"Deleted  →  {p}\nTime     →  {datetime.now().strftime('%H:%M:%S')}")
                except Exception as e:
                    set_output(str(e), "error")

# ═══════════════════════════════════════════════════════════════════════════════
# BROWSE
# ═══════════════════════════════════════════════════════════════════════════════
elif op == "BROWSE":
    files = list_local_files()
    st.markdown('<div class="panel"><div class="panel-label">Current Directory</div>', unsafe_allow_html=True)

    if not files:
        st.markdown('<div class="terminal-warn">Directory is empty.</div>', unsafe_allow_html=True)
    else:
        rows = ""
        for f in files:
            ext = f.suffix.lower()
            icon = {"py": "🐍", ".txt": "📄", ".md": "📝", ".json": "📦",
                    ".csv": "📊", ".log": "📋"}.get(ext, "📄")
            rows += f"""
            <div class="file-entry">
                <span class="file-icon">{icon}</span>
                <span class="file-name">{f.name}</span>
                <span class="file-size">{file_size_str(f)}</span>
            </div>"""
        st.markdown(rows, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(f'<div style="font-family:\'JetBrains Mono\',monospace;font-size:10px;color:#484f58;margin-top:8px">{len(files)} file(s)  ·  {Path(".").resolve()}</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# Output
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.output:
    kind = st.session_state.output_type
    css_class = {"success": "terminal-out", "error": "terminal-err", "warn": "terminal-warn"}.get(kind, "terminal-out")
st.markdown(f'<div class="{css_class}">{st.session_state.output}</div>', unsafe_allow_html=True)