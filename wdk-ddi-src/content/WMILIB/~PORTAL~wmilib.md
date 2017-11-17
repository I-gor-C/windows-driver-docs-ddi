# Declarations in the wmilib header
This header Wmilib contains these programming interfaces:

Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SYSCTL_IRP_DISPOSITION enumeration](ne-wmilib--sysctl-irp-disposition.md) | TBD |
| [WMIENABLEDISABLECONTROL enumeration](ne-wmilib--wmienabledisablecontrol.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WMIGUIDREGINFO structure](ns-wmilib--wmiguidreginfo.md) | The WMIGUIDREGINFO structure contains registration information for a given data block or event block exposed by a driver that uses the WMI library support routines. |
| [WMILIB_CONTEXT structure](ns-wmilib--wmilib-context.md) | The WMILIB_CONTEXT structure provides registration information for a driver's data blocks and event blocks and defines entry points for the driver's WMI library callback routines. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WmiSystemControl function](nf-wmilib-wmisystemcontrol.md) | The WmiSystemControl routine is a dispatch routine for drivers that use WMI library support routines to handle WMI IRPs. |
| [WmiFireEvent function](nf-wmilib-wmifireevent.md) | The WmiFireEvent routine sends an event to WMI for delivery to data consumers that have requested notification of the event. |
| [WmiCompleteRequest function](nf-wmilib-wmicompleterequest.md) | The WmiCompleteRequest routine indicates that a driver has finished processing a WMI request in a DpWmiXxx routine. |

This header is used in these topics:

- [kernel](..content/_kernel)
