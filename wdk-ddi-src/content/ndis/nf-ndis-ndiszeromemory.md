---
UID: NF.ndis.NdisZeroMemory
title: NdisZeroMemory
author: windows-driver-content
description: The NdisZeroMemory function fills a block of memory with zeros.
old-location: netvista\ndiszeromemory.htm
old-project: netvista
ms.assetid: 1cb829e1-bd4f-4d6b-a936-0e7cf8024381
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisZeroMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for existing drivers in  NDIS 6.0 and later, but new drivers should use RtlZeroMemory instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisZeroMemory
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NdisZeroMemory function



## -description
<p>The 
  <b>NdisZeroMemory</b> function fills a block of memory with zeros.</p>


## -syntax

````
VOID NdisZeroMemory(
  _In_ PVOID Destination,
  _In_ ULONG Length
);
````


## -parameters
<dl>

### -param <i>Destination</i> [in]

<dd>
<p>The base virtual address of a block of memory.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes to fill with zeros.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisZeroMemory</b> fills the specified range of memory with zeros. The given 
    <i>Destination</i> and 
    <i>Length</i> must be a proper subrange of a caller-accessible memory range.</p>

<p>As long as the given range was allocated from nonpaged pool, the caller can be running at any IRQL.
    Otherwise, a caller must be running at IRQL &lt; DISPATCH_LEVEL as, for example, when a caller clears a
    structure it allocated on the stack.</p>

<p><b>NdisZeroMemory</b> fills the specified range of memory with zeros. The given 
    <i>Destination</i> and 
    <i>Length</i> must be a proper subrange of a caller-accessible memory range.</p>

<p>As long as the given range was allocated from nonpaged pool, the caller can be running at any IRQL.
    Otherwise, a caller must be running at IRQL &lt; DISPATCH_LEVEL as, for example, when a caller clears a
    structure it allocated on the stack.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for existing drivers in  NDIS 6.0 and later, but new drivers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff563610">RtlZeroMemory</a> instead.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatememorywithtagpriority.md">
   NdisAllocateMemoryWithTagPriority</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564692">NdisZeroMappedMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisZeroMemory function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
