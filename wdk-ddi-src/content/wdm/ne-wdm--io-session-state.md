---
UID: NE.wdm._IO_SESSION_STATE
title: IO_SESSION_STATE
author: windows-driver-content
description: The IO_SESSION_STATE enumeration contains constants that indicate the current state of a user session.
old-location: kernel\io_session_state.htm
old-project: kernel
ms.assetid: 3e181b22-ae82-4287-8175-bc6043332d5a
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: IO_SESSION_STATE
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IO_SESSION_STATE enumeration



## -description
<p>The <b>IO_SESSION_STATE</b> enumeration contains constants that indicate the current state of a user session.</p>


## -syntax

````
typedef enum _IO_SESSION_STATE { 
  IoSessionStateCreated               = 1,
  IoSessionStateInitialized           = 2,
  IoSessionStateConnected             = 3,
  IoSessionStateDisconnected          = 4,
  IoSessionStateDisconnectedLoggedOn  = 5,
  IoSessionStateLoggedOn              = 6,
  IoSessionStateLoggedOff             = 7,
  IoSessionStateTerminated            = 8,
  IoSessionStateMax                   = 9
} IO_SESSION_STATE, *PIO_SESSION_STATE;
````


## -enum-fields
<dl>

### -field <a id="IoSessionStateCreated"></a><a id="iosessionstatecreated"></a><a id="IOSESSIONSTATECREATED"></a><b>IoSessionStateCreated</b>

<dd>
<p>The session has been created.</p>
</dd>

### -field <a id="IoSessionStateInitialized"></a><a id="iosessionstateinitialized"></a><a id="IOSESSIONSTATEINITIALIZED"></a><b>IoSessionStateInitialized</b>

<dd>
<p>The session has been initialized but has not yet been created.</p>
</dd>

### -field <a id="IoSessionStateConnected"></a><a id="iosessionstateconnected"></a><a id="IOSESSIONSTATECONNECTED"></a><b>IoSessionStateConnected</b>

<dd>
<p>The session is connected but the user has not yet logged on.</p>
</dd>

### -field <a id="IoSessionStateDisconnected"></a><a id="iosessionstatedisconnected"></a><a id="IOSESSIONSTATEDISCONNECTED"></a><b>IoSessionStateDisconnected</b>

<dd>
<p>The session has been disconnected.</p>
</dd>

### -field <a id="IoSessionStateDisconnectedLoggedOn"></a><a id="iosessionstatedisconnectedloggedon"></a><a id="IOSESSIONSTATEDISCONNECTEDLOGGEDON"></a><b>IoSessionStateDisconnectedLoggedOn</b>

<dd>
<p>The session was disconnected while the user was logged on.</p>
</dd>

### -field <a id="IoSessionStateLoggedOn"></a><a id="iosessionstateloggedon"></a><a id="IOSESSIONSTATELOGGEDON"></a><b>IoSessionStateLoggedOn</b>

<dd>
<p>The user is logged on to the session.</p>
</dd>

### -field <a id="IoSessionStateLoggedOff"></a><a id="iosessionstateloggedoff"></a><a id="IOSESSIONSTATELOGGEDOFF"></a><b>IoSessionStateLoggedOff</b>

<dd>
<p>The user has logged off of the session. </p>
</dd>

### -field <a id="IoSessionStateTerminated"></a><a id="iosessionstateterminated"></a><a id="IOSESSIONSTATETERMINATED"></a><b>IoSessionStateTerminated</b>

<dd>
<p>The session has been terminated.</p>
</dd>

### -field <a id="IoSessionStateMax"></a><a id="iosessionstatemax"></a><a id="IOSESSIONSTATEMAX"></a><b>IoSessionStateMax</b>

<dd>
<p>Specifies the maximum value in this enumeration type. </p>
</dd>
</dl>

## -remarks
<p>When a driver calls the <a href="..\wdm\nf-wdm-iogetcontainerinformation.md">IoGetContainerInformation</a> routine to obtain information about a user session (<i>InformationClass</i> = <b>IoSessionStateInformation</b>), the I/O manager writes an <a href="..\wdm\ns-wdm--io-session-state-information.md">IO_SESSION_STATE_INFORMATION</a> structure to the buffer pointed to by the routine's <i>Buffer</i> parameter. The I/O manager sets the <b>SessionState</b> member of this structure to an <b>IO_SESSION_STATE</b> enumeration constant (other than <b>IoSessionStateMax</b>).</p>

<p>The following table shows the session state transitions. For each state transition, the table shows the following:</p>

<p>The <i>from</i> state (a column label in a gray box)</p>

<p>The <i>to</i> state (a row label in a gray box)</p>

<p>The event that causes the transition (a table entry in a white box)</p>

<p>A blank white box indicates that no transition can occur directly from the associated <i>from</i> state to the corresponding <i>to</i> state.</p>

<p>In the preceding table, the <i>from</i> and <i>to</i> states are represented by <b>IO_SESSION_STATE</b> enumeration constants, and the events are represented by <a href="..\wdm\ne-wdm--io-session-event.md">IO_SESSION_EVENT</a> enumeration constants. For example, if the session state is <b>IoSessionStateConnected</b> (abbreviated as "Connected" in the table), an <b>IoSessionEventLogon</b> event (abbreviated as "Logon") causes a transition to the <b>IoSessionStateLoggedOn</b> state (abbreviated as "LoggedOn"). The starting state for a new session is <b>IoSessionStateInitialized</b> (abbreviated as "Initialized"). </p>

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
<a href="..\wdm\nf-wdm-iogetcontainerinformation.md">IoGetContainerInformation</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--io-session-event.md">IO_SESSION_EVENT</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--io-session-state-information.md">IO_SESSION_STATE_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IO_SESSION_STATE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
