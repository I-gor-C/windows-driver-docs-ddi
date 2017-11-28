---
UID: NE.wdm._IO_SESSION_EVENT
title: IO_SESSION_EVENT
author: windows-driver-content
description: The IO_SESSION_EVENT enumeration indicates the type of session event for which a driver is receiving notification.
old-location: kernel\io_session_event.htm
old-project: kernel
ms.assetid: 6bdc1c25-bac3-416e-af3d-66a125f0f036
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
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
req.alt-api: IO_SESSION_EVENT
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IO_SESSION_EVENT enumeration



## -description
<p>The <b>IO_SESSION_EVENT</b> enumeration indicates the type of session event for which a driver is receiving notification.</p>


## -syntax

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


## -enum-fields
<dl>

### -field <a id="IoSessionEventCreated"></a><a id="iosessioneventcreated"></a><a id="IOSESSIONEVENTCREATED"></a><b>IoSessionEventCreated</b>

<dd>
<p>The user session was created.</p>
</dd>

### -field <a id="IoSessionEventTerminated"></a><a id="iosessioneventterminated"></a><a id="IOSESSIONEVENTTERMINATED"></a><b>IoSessionEventTerminated</b>

<dd>
<p>The user session terminated.</p>
</dd>

### -field <a id="IoSessionEventConnected"></a><a id="iosessioneventconnected"></a><a id="IOSESSIONEVENTCONNECTED"></a><b>IoSessionEventConnected</b>

<dd>
<p>The user session was connected.</p>
</dd>

### -field <a id="IoSessionEventDisconnected"></a><a id="iosessioneventdisconnected"></a><a id="IOSESSIONEVENTDISCONNECTED"></a><b>IoSessionEventDisconnected</b>

<dd>
<p>The user session was disconnected.</p>
</dd>

### -field <a id="IoSessionEventLogon"></a><a id="iosessioneventlogon"></a><a id="IOSESSIONEVENTLOGON"></a><b>IoSessionEventLogon</b>

<dd>
<p>The user logged on to the session.</p>
</dd>

### -field <a id="IoSessionEventLogoff"></a><a id="iosessioneventlogoff"></a><a id="IOSESSIONEVENTLOGOFF"></a><b>IoSessionEventLogoff</b>

<dd>
<p>The user logged off of the session.</p>
</dd>

### -field <a id="IoSessionEventMax"></a><a id="iosessioneventmax"></a><a id="IOSESSIONEVENTMAX"></a><b>IoSessionEventMax</b>

<dd>
<p>Specifies the maximum value in this enumeration type.</p>
</dd>
</dl>

## -remarks
<p>When the I/O manager calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff550626">IO_SESSION_NOTIFICATION_FUNCTION</a> function, it sets the <i>Event</i> parameter of this function to an <b>IO_SESSION_EVENT</b> enumeration constant (other than <b>IoSessionEventMax</b>).</p>

<p>A session event causes a transition from one session state to another. For more information about session state transitions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550631">IO_SESSION_STATE</a>. </p>

<p>When the I/O manager calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff550626">IO_SESSION_NOTIFICATION_FUNCTION</a> function, it sets the <i>Event</i> parameter of this function to an <b>IO_SESSION_EVENT</b> enumeration constant (other than <b>IoSessionEventMax</b>).</p>

<p>A session event causes a transition from one session state to another. For more information about session state transitions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550631">IO_SESSION_STATE</a>. </p>

<p>When the I/O manager calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff550626">IO_SESSION_NOTIFICATION_FUNCTION</a> function, it sets the <i>Event</i> parameter of this function to an <b>IO_SESSION_EVENT</b> enumeration constant (other than <b>IoSessionEventMax</b>).</p>

<p>A session event causes a transition from one session state to another. For more information about session state transitions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550631">IO_SESSION_STATE</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 7 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550626">IO_SESSION_NOTIFICATION_FUNCTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550631">IO_SESSION_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IO_SESSION_EVENT enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
