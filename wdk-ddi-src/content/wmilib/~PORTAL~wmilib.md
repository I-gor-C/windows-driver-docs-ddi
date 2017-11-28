# Wmilib.h header


This header is used by unknown technology.

Wmilib.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [WmiCompleteRequest function](nf-wmilib-wmicompleterequest.md) | The WmiCompleteRequest routine indicates that a driver has finished processing a WMI request in a DpWmiXxx routine. |
| [WmiFireEvent function](nf-wmilib-wmifireevent.md) | The WmiFireEvent routine sends an event to WMI for delivery to data consumers that have requested notification of the event. |
| [WmiSystemControl function](nf-wmilib-wmisystemcontrol.md) | The WmiSystemControl routine is a dispatch routine for drivers that use WMI library support routines to handle WMI IRPs. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [WMIGUIDREGINFO structure](ns-wmilib--wmiguidreginfo.md) | The WMIGUIDREGINFO structure contains registration information for a given data block or event block exposed by a driver that uses the WMI library support routines. |
| [WMILIB_CONTEXT structure](ns-wmilib--wmilib-context.md) | The WMILIB_CONTEXT structure provides registration information for a driver's data blocks and event blocks and defines entry points for the driver's WMI library callback routines. |
