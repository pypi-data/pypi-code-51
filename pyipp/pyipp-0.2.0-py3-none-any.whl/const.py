"""Constants for IPP."""

DEFAULT_CHARSET = "utf-8"
DEFAULT_CHARSET_LANGUAGE = "en-US"

DEFAULT_CLASS_ATTRIBUTES = ["printer-name", "member-names"]

DEFAULT_JOB_ATTRIBUTES = [
    "job-id",
    "job-name",
    "printer-uri",
    "job-state",
    "job-state-reasons",
    "job-hold-until",
    "job-media-progress",
    "job-k-octets",
    "number-of-documents",
    "copies",
    "job-originating-user-name",
]

DEFAULT_PRINTER_ATTRIBUTES = [
    "printer-name",
    "printer-type",
    "printer-location",
    "printer-info",
    "printer-make-and-model",
    "printer-state",
    "printer-state-message",
    "printer-state-reason",
    "printer-uri-supported",
    "device-uri",
    "printer-is-shared",
]

DEFAULT_PORT = 631
DEFAULT_PROTO_VERSION = (2, 0)
