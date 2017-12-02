---
UID: NF.wdm.PsQueryTotalCycleTimeProcess
title: PsQueryTotalCycleTimeProcess
author: windows-driver-content
description: The PsQueryTotalCycleTimeProcess routine returns the accumulated cycle time for the specified process.
old-location: kernel\psquerytotalcycletimeprocess.htm
old-project: kernel
ms.assetid: 4DA34F96-A69A-46BE-B3D8-D542794052DE
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsQueryTotalCycleTimeProcess
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsQueryTotalCycleTimeProcess
req.alt-loc: ntoskrnl.lib,ntoskrnl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PsQueryTotalCycleTimeProcess function



## -description
<p>The <b>PsQueryTotalCycleTimeProcess</b> routine returns the accumulated cycle time for the specified process.</p>


## -syntax

````
ULONG64 PsQueryTotalCycleTimeProcess(
  _Inout_ PEPROCESS Process,
  _Out_   PULONG64  CycleTimeStamp
);
````


## -parameters
<dl>

### -param Process [in, out]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544273">EPROCESS</a> structure that serves as the kernel object for the process.</p>
</dd>

### -param CycleTimeStamp [out]

<dd>
<p>A pointer to a ULONG64 variable to which the routine writes the current cycle counter value for the process.</p>
</dd>
</dl>

## -returns
<p><b>PsQueryTotalCycleTimeProcess</b> returns the accumulated cycle time for the specified process.</p>

## -remarks
<p>This routine uses the time stamp counter to get the number of processor clock cycles used by the specified process.</p>

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
<p>Available in Windows 8 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544273">EPROCESS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PsQueryTotalCycleTimeProcess routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
