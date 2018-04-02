---
UID: NE:wdm._IO_SESSION_EVENT
title: "_IO_SESSION_EVENT"
author: windows-driver-content
description: The IO_SESSION_EVENT enumeration indicates the type of session event for which a driver is receiving notification.
old-location: kernel\io_session_event.htm
old-project: kernel
ms.assetid: 6bdc1c25-bac3-416e-af3d-66a125f0f036
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PIO_SESSION_EVENT, IO_SESSION_EVENT, IO_SESSION_EVENT enumeration [Kernel-Mode Driver Architecture], IoSessionEventConnected, IoSessionEventCreated, IoSessionEventDisconnected, IoSessionEventLogoff, IoSessionEventLogon, IoSessionEventMax, IoSessionEventTerminated, PIO_SESSION_EVENT, PIO_SESSION_EVENT enumeration pointer [Kernel-Mode Driver Architecture], _IO_SESSION_EVENT, kernel.io_session_event, sysenum_8fc6c99f-15c8-4dbb-90fd-b207d66c2f90.xml, wdm/IO_SESSION_EVENT, wdm/IoSessionEventConnected, wdm/IoSessionEventCreated, wdm/IoSessionEventDisconnected, wdm/IoSessionEventLogoff, wdm/IoSessionEventLogon, wdm/IoSessionEventMax, wdm/IoSessionEventTerminated, wdm/PIO_SESSION_EVENT"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdm.h
api_name:
-	IO_SESSION_EVENT
product:
- Windows
targetos: Windows
req.typenames: IO_SESSION_EVENT, *PIO_SESSION_EVENT
req.product: Windows 10 or later.
---

# _IO_SESSION_EVENT Enumeration
The <b>IO_SESSION_EVENT</b> enumeration indicates the type of session event for which a driver is receiving notification.

## Syntax
```
typedef enum _IO_SESSION_EVENT {
  IoSessionEventIgnore        ,
  IoSessionEventCreated       ,
  IoSessionEventTerminated    ,
  IoSessionEventConnected     ,
  IoSessionEventDisconnected  ,
  IoSessionEventLogon         ,
  IoSessionEventLogoff        ,
  IoSessionEventMax
} IO_SESSION_EVENT, *PIO_SESSION_EVENT;
```

## Constants

<table>
            
                <tr>
                    <td>IoSessionEventIgnore</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>IoSessionEventCreated</td>
                    <td>The user session was created.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventTerminated</td>
                    <td>The user session terminated.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventConnected</td>
                    <td>The user session was connected.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventDisconnected</td>
                    <td>The user session was disconnected.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventLogon</td>
                    <td>The user logged on to the session.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventLogoff</td>
                    <td>The user logged off of the session.</td>
                </tr>
            
                <tr>
                    <td>IoSessionEventMax</td>
                    <td>Specifies the maximum value in this enumeration type.</td>
                </tr>
</table>

## Remarks

When the I/O manager calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff550626">IO_SESSION_NOTIFICATION_FUNCTION</a> function, it sets the <i>Event</i> parameter of this function to an <b>IO_SESSION_EVENT</b> enumeration constant (other than <b>IoSessionEventMax</b>).

A session event causes a transition from one session state to another. For more information about session state transitions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550631">IO_SESSION_STATE</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows 7 and later versions of the Windows operating system. Supported in Windows 7 and later versions of the Windows operating system. |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550626">IO_SESSION_NOTIFICATION_FUNCTION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550631">IO_SESSION_STATE</a>