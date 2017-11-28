---
UID: NF.wdm.KeIpiGenericCall
title: KeIpiGenericCall
author: windows-driver-content
description: The KeIpiGenericCall routine causes the specified routine to run on all processors simultaneously.
old-location: kernel\keipigenericcall.htm
old-project: kernel
ms.assetid: 11424e94-d279-4003-a97c-a46d1a75e8e5
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeIpiGenericCall
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Server 2003 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeIpiGenericCall
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
req.irql: < IPI_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# KeIpiGenericCall function



## -description
<p>The <b>KeIpiGenericCall</b> routine causes the specified routine to run on all processors simultaneously.</p>


## -syntax

````
ULONG_PTR KeIpiGenericCall(
  _In_ PKIPI_BROADCAST_WORKER BroadcastFunction,
  _In_ ULONG_PTR              Context
);
````


## -parameters
<dl>

### -param <i>BroadcastFunction</i> [in]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550688">IpiGenericCall</a> routine. This routine is run on every processor simultaneously.</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>Specifies the value to pass to <i>IpiGenericCall</i> when it is called. </p>
</dd>
</dl>

## -returns
<p><b>KeIpiGenericCall</b> returns the value that <a href="https://msdn.microsoft.com/library/windows/hardware/ff550688">IpiGenericCall</a> returns on the source processor (the processor that called <b>KeIpiGenericCall</b>). </p>

## -remarks
<p>When a driver calls <b>KeIpiGenericCall</b>, the system interrupts every processor and raises the IRQL to IPI_LEVEL (interprocessor interrupt level). Each processor spins on a barrier until all processors have reached the barrier; then, all processors begin calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550688">IpiGenericCall</a>. <b>KeIpiGenericCall</b> waits for all calls to <i>IpiGenericCall</i> to complete before returning. </p>

<p>When a driver calls <b>KeIpiGenericCall</b>, the system interrupts every processor and raises the IRQL to IPI_LEVEL (interprocessor interrupt level). Each processor spins on a barrier until all processors have reached the barrier; then, all processors begin calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550688">IpiGenericCall</a>. <b>KeIpiGenericCall</b> waits for all calls to <i>IpiGenericCall</i> to complete before returning. </p>

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
<p>Available in Windows Server 2003 and later versions of Windows.</p>
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
<p>&lt; IPI_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550688">IpiGenericCall</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeIpiGenericCall routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
