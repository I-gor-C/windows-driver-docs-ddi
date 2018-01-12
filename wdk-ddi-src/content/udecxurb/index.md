---
UID: NA:udecxurb
---

# Udecxurb.h header

## -description

This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Udecxurb.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UdecxUrbComplete function](nf-udecxurb-udecxurbcomplete.md) | Completes the URB request with a USB-specific completion status code. |
| [UdecxUrbCompleteWithNtStatus function](nf-udecxurb-udecxurbcompletewithntstatus.md) | Completes the URB request with an NTSTATUS code. |
| [UdecxUrbRetrieveBuffer function](nf-udecxurb-udecxurbretrievebuffer.md) | Retrieves the transfer buffer of an URB from the specified framework request object sent to the endpoint queue. |
| [UdecxUrbRetrieveControlSetupPacket function](nf-udecxurb-udecxurbretrievecontrolsetuppacket.md) | Retrieves a USB control setup packet from a specified framework request object. |
| [UdecxUrbSetBytesCompleted function](nf-udecxurb-udecxurbsetbytescompleted.md) | Sets the number of bytes transferred for the URB contained within a framework request object. |
