---
UID: NE:wdm._IO_SESSION_EVENT
title: "_IO_SESSION_EVENT"
author: windows-driver-content
description: The IO_SESSION_EVENT enumeration indicates the type of session event for which a driver is receiving notification.
old-location: kernel\io_session_event.htm
old-project: kernel
ms.assetid: 6bdc1c25-bac3-416e-af3d-66a125f0f036
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: "*PIO_SESSION_EVENT, IoSessionEventTerminated, wdm/IoSessionEventConnected, IoSessionEventCreated, IoSessionEventMax, kernel.io_session_event, sysenum_8fc6c99f-15c8-4dbb-90fd-b207d66c2f90.xml, IoSessionEventDisconnected, IO_SESSION_EVENT enumeration [Kernel-Mode Driver Architecture], IoSessionEventConnected, IoSessionEventLogon, wdm/IoSessionEventLogoff, wdm/IoSessionEventTerminated, wdm/IoSessionEventLogon, PIO_SESSION_EVENT enumeration pointer [Kernel-Mode Driver Architecture], wdm/PIO_SESSION_EVENT, _IO_SESSION_EVENT, PIO_SESSION_EVENT, wdm/IoSessionEventMax, IO_SESSION_EVENT, wdm/IoSessionEventDisconnected, wdm/IoSessionEventCreated, wdm/IO_SESSION_EVENT, IoSessionEventLogoff"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows 7 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	wdm.h
apiname:
-	IO_SESSION_EVENT
product: Windows
targetos: Windows
req.typenames: "*PIO_SESSION_EVENT, IO_SESSION_EVENT"
req.product: Windows 10 or later.
---

# _IO_SESSION_EVENT Enumeration
The <b>IO_SESSION_EVENT</b> enumeration indicates the type of session event for which a driver is receiving notification.

## Syntax
````
typedef enum _IO_SESSION_EVENT { 
  IoSessionEventCreated       = 1,
  IoSessionEventTerminated    = 2,
  IoSessionEventConnected     = 3,
  IoSessionEventDisconnected  = 4,
  IoSessionEventLogon         = 5,
  IoSessionEventLogoff        = 6,
  IoSessionEventMax           = 7
} IO_SESSION_EVENT, *PIO_SESSION_EVENT;
````

## Constants

<table>
            
                <tr>
                    <td>IoSessionEventConnected</td>
                    <td>The user session was connected.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventCreated</td>
                    <td>The user session was created.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventDisconnected</td>
                    <td>The user session was disconnected.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventIgnore</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>IoSessionEventLogoff</td>
                    <td>The user logged off of the session.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventLogon</td>
                    <td>The user logged on to the session.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventMax</td>
                    <td>Specifies the maximum value in this enumeration type.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventTerminated</td>
                    <td>The user session terminated.</td>
                </tr>
</table>

## Remarks

When the I/O manager calls the driver's <a href="..\wdm\nc-wdm-io_session_notification_function.md">IO_SESSION_NOTIFICATION_FUNCTION</a> function, it sets the <i>Event</i> parameter of this function to an <b>IO_SESSION_EVENT</b> enumeration constant (other than <b>IoSessionEventMax</b>).

A session event causes a transition from one session state to another. For more information about session state transitions, see <a href="..\wdm\ne-wdm-_io_session_state.md">IO_SESSION_STATE</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows 7 and later versions of the Windows operating system. Supported in Windows 7 and later versions of the Windows operating system. |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h) |

## See Also

<a href="..\wdm\ne-wdm-_io_session_state.md">IO_SESSION_STATE</a>



<a href="..\wdm\nc-wdm-io_session_notification_function.md">IO_SESSION_NOTIFICATION_FUNCTION</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IO_SESSION_EVENT enumeration%20 RELEASE:%20(2/16/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>