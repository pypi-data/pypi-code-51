ICOM = {
    "Patient ID": (b" \x00LO\x00P", str, "first"),
    "Patient Name": (b"\x10\x00PN\x00P", str, "first"),
    "Rx Site": (b"\x01\x10LO\x00P", str, "first"),
    "Field ID": (b"\x03\x10LO\x00P", str, "first"),
    "Machine ID": (b"\xb2\x00SH\x00P", int, "first"),
    "Radiation Type": (b"\xc6\x00CS\x00R", str, "first"),
    "Energy": (b"\x14\x01SH\x00R", str, "first"),
    "Wedge": (b"\x18\x01CS\x00R", str, "first"),
    "Segment": (b"\x07\x10DS\x00R", int, "first"),
    "Total MU": (b"\t\x10DS\x00R", float, "first"),
    "Delivery MU": (b"2\x00DS\x00R", float, "first"),
    "Backup Delivery MU": (b"3\x00DS\x00R", float, "first"),
    "Beam Timer": (b"8\x00SH\x00R", float, "first"),
    "Segment MU": (b"\x0b\x00DS\x00R", float, "first"),
    "Gantry": (b"\x1e\x01DS\x00R", float, "first"),
    "Collimator": (b" \x01DS\x00R", float, "first"),
    "Table Column": (b'"\x01DS\x00R', int, "first"),
    "Table Isocentric": (rb"\%\x01DS\x00R", int, "first"),
    "Table Vertical": (rb"\(\x01DS\x00R", float, "first"),
    "Table Longitudinal": (rb"\)\x01DS\x00R", float, "first"),
    "Table Lateral": (rb"\*\x01DS\x00R", float, "first"),
    "Beam Description": (b"\x0c\x00SH\x00R", str, "first"),
    "Interlocks": (b"\x16\x10LO\x00R", str, "all"),
    "Previous Interlocks": (b"\x18\x10LO\x00R", str, "all"),
}
