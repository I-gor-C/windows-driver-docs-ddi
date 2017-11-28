---
UID: NF.wdm.KeResetEvent
title: KeResetEvent
author: windows-driver-content
description: The KeResetEvent routine resets a specified event object to a not-signaled state and returns the previous state of that event object.
old-location: kernel\keresetevent.htm
old-project: kernel
ms.assetid: 90be986b-e63e-4ae3-a0f3-87f6f58583dc
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeResetEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeResetEvent
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlKeDispatchLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# KeResetEvent function



## -description
<p>The <b>KeResetEvent</b> routine resets a specified event object to a not-signaled state and returns the previous state of that event object.</p>


## -syntax

````
LONG KeResetEvent(
  _Inout_ PRKEVENT Event
);
````


## -parameters
<dl>

### -param <i>Event</i> [in, out]

<dd>
<p>A pointer to an initialized dispatcher object of type event for which the caller provides the storage. </p>
</dd>
</dl>

## -returns
<p><b>KeResetEvent</b> returns a value that indicates the previous state of the specified <i>Event</i>, which is nonzero for a signaled state. </p>

## -remarks
<p><i>Event</i> is reset to a not-signaled state, meaning that its value is set to zero.</p>

<p>Unless the caller requires the value that is returned by <b>KeResetEvent</b>, using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551980">KeClearEvent</a> routine is a faster way to set an event object to a not-signaled state.</p>

<p>For more information about event objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544323">Event Objects</a>. </p>

<p><i>Event</i> is reset to a not-signaled state, meaning that its value is set to zero.</p>

<p>Unless the caller requires the value that is returned by <b>KeResetEvent</b>, using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551980">KeClearEvent</a> routine is a faster way to set an event object to a not-signaled state.</p>

<p>For more information about event objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544323">Event Objects</a>. </p>

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
<p>Available starting with Windows 2000.</p>
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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547812">IrqlKeDispatchLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551980">KeClearEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552137">KeInitializeEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553089">KeReadStateEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553253">KeSetEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553324">KeWaitForMultipleObjects</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeResetEvent routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
