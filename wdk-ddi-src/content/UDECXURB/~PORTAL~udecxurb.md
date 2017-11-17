# Declarations in the udecxurb header
This header Udecxurb contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [UdecxUrbSetBytesCompleted function](nf-udecxurb-udecxurbsetbytescompleted.md) | Sets the number of bytes transferred for the URB contained within a framework request object. |
| [UdecxUrbCompleteWithNtStatus function](nf-udecxurb-udecxurbcompletewithntstatus.md) | Completes the URB request with an NTSTATUS code. |
| [UdecxUrbRetrieveControlSetupPacket function](nf-udecxurb-udecxurbretrievecontrolsetuppacket.md) | Retrieves a USB control setup packet from a specified framework request object. |
| [UdecxUrbComplete function](nf-udecxurb-udecxurbcomplete.md) | Completes the URB request with a USB-specific completion status code. |
| [UdecxUrbRetrieveBuffer function](nf-udecxurb-udecxurbretrievebuffer.md) | Retrieves the transfer buffer of an URB from the specified framework request object sent to the endpoint queue. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [*PFN_UDECXURBRETRIEVEBUFFER callback function](nc-udecxurb-pfn-udecxurbretrievebuffer.md) | TBD |
| [*PFN_UDECXURBRETRIEVECONTROLSETUPPACKET callback function](nc-udecxurb-pfn-udecxurbretrievecontrolsetuppacket.md) | TBD |
| [*PFN_UDECXURBCOMPLETEWITHNTSTATUS callback function](nc-udecxurb-pfn-udecxurbcompletewithntstatus.md) | TBD |
| [*PFN_UDECXURBSETBYTESCOMPLETED callback function](nc-udecxurb-pfn-udecxurbsetbytescompleted.md) | TBD |
| [*PFN_UDECXURBCOMPLETE callback function](nc-udecxurb-pfn-udecxurbcomplete.md) | TBD |

This header is used in these topics:

- [usbref](..content/_usbref)
