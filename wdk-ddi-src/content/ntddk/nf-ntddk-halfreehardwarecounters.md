---
UID: NF.ntddk.HalFreeHardwareCounters
title: HalFreeHardwareCounters
author: windows-driver-content
description: The HalFreeHardwareCounters routine frees a set of hardware performance counters that was acquired in a previous call to HalAllocateHardwareCounters routine.
old-location: kernel\halfreehardwarecounters.htm
old-project: kernel
ms.assetid: 646a073b-e0c5-4d41-b60c-3935c129fb39
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HalFreeHardwareCounters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HalFreeHardwareCounters
req.alt-loc: Hal.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hal.lib
req.dll: Hal.dll
req.irql: PASSIVE_LEVEL
req.iface: 
---

# HalFreeHardwareCounters function



## -description
<p>The <b>HalFreeHardwareCounters</b> routine frees a set of hardware performance counters that was acquired in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546577">HalAllocateHardwareCounters</a> routine.</p>


## -syntax

````
NTSTATUS HalFreeHardwareCounters(
  _In_ HANDLE CounterSetHandle
);
````


## -parameters
<dl>

### -param <i>CounterSetHandle</i> [in]

<dd>
<p>A handle to the allocated counter resources. The caller acquired this handle in a previous call to <b>HalAllocateHardwareCounters</b>.</p>
</dd>
</dl>

## -returns
<p><b>HalFreeHardwareCounters</b> returns STATUS_SUCCESS if the call was successful. Possible error return values include the following:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Parameter <i>CounterSetHandle</i> is not a valid counter resources handle.</p>

<p> </p>

## -remarks


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
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hal.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hal.dll</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546577">HalAllocateHardwareCounters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20HalFreeHardwareCounters routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
