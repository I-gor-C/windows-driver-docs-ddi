---
UID: NF.wdm.PoSetSystemWake
title: PoSetSystemWake
author: windows-driver-content
description: The PoSetSystemWake routine marks the specified IRP as one that contributed to waking the system from a sleep state.
old-location: kernel\posetsystemwake.htm
ms.assetid: e79ed9a1-b271-4c0a-a82f-9fecab930569
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoSetSystemWake
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
ms.keywords: PoSetSystemWake
req.iface: 
req.product: Windows 10 or later.
---

# PoSetSystemWake function



## -description
<p>The <b>PoSetSystemWake</b> routine marks the specified IRP as one that contributed to waking the system from a sleep state.</p>


## -syntax

````
VOID PoSetSystemWake(
  _Inout_ PIRP Irp
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in, out]

<dd>
<p>A pointer to the wait/wake IRP.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Drivers call <b>PoSetSystemWake</b> to mark an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551766">IRP_MN_WAIT_WAKE</a> IRP as contributing to waking the system from a sleep state. By default, wait/wake IRPs are considered to be device wake-up IRPs. It is the responsibility of the terminal device in a wait/wake chain to determine if it woke the system and to call <b>PoSetSystemWake</b> for the terminal wait/wake IRP. When a driver calls <b>PoSetSystemWake</b> on an IRP, it is marked as having contributed to waking the system from a sleep state. Only one driver in a stack needs to call this routine, and it should normally be the bus driver in a driver stack.</p>

<p>All other drivers in a wait/wake chain can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559674">PoGetSystemWake</a> for their own wait/wake IRPs at completion to determine if they should call <b>PoSetSystemWake</b> on any child wait/wake IRPs that they are about to complete. This ensures that system wake information properly progresses throughout the wait/wake chain.</p>

<p>After a wait/wake IRP completes, the power manager checks if the IRP is marked as a system wake IRP. If the IRP is marked as a system wake IRP, the power manager adds the IRP to an internal list of the devices that woke the system. However, the power manager only keeps track of the most specific devices that work the system. For example, if device A is added as a device that woke the system, and then device B—a child of device A—is also added, the power manager only retains device B in the list because device B is the most specific. If the power manager cannot determine the most specific device that woke the system, the power manager might keep track of more than one device that reported it woke the system.</p>

<p>The power manager logs an Event Tracing for Windows (ETW) event (viewable in the global system channel) that includes information about which devices woke the system.</p>

<p>Drivers call <b>PoSetSystemWake</b> to mark an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551766">IRP_MN_WAIT_WAKE</a> IRP as contributing to waking the system from a sleep state. By default, wait/wake IRPs are considered to be device wake-up IRPs. It is the responsibility of the terminal device in a wait/wake chain to determine if it woke the system and to call <b>PoSetSystemWake</b> for the terminal wait/wake IRP. When a driver calls <b>PoSetSystemWake</b> on an IRP, it is marked as having contributed to waking the system from a sleep state. Only one driver in a stack needs to call this routine, and it should normally be the bus driver in a driver stack.</p>

<p>All other drivers in a wait/wake chain can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559674">PoGetSystemWake</a> for their own wait/wake IRPs at completion to determine if they should call <b>PoSetSystemWake</b> on any child wait/wake IRPs that they are about to complete. This ensures that system wake information properly progresses throughout the wait/wake chain.</p>

<p>After a wait/wake IRP completes, the power manager checks if the IRP is marked as a system wake IRP. If the IRP is marked as a system wake IRP, the power manager adds the IRP to an internal list of the devices that woke the system. However, the power manager only keeps track of the most specific devices that work the system. For example, if device A is added as a device that woke the system, and then device B—a child of device A—is also added, the power manager only retains device B in the list because device B is the most specific. If the power manager cannot determine the most specific device that woke the system, the power manager might keep track of more than one device that reported it woke the system.</p>

<p>The power manager logs an Event Tracing for Windows (ETW) event (viewable in the global system channel) that includes information about which devices woke the system.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559674">PoGetSystemWake</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoSetSystemWake routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
