---
UID: NF.ntifs.RtlCompareMemoryUlong
title: RtlCompareMemoryUlong
author: windows-driver-content
description: The RtlCompareMemoryUlong routine returns how many bytes in a block of memory match a specified pattern.
old-location: ifsk\rtlcomparememoryulong.htm
old-project: ifsk
ms.assetid: 78ff21da-be0f-4b57-9162-1052a6c12b5c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlCompareMemoryUlong
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlCompareMemoryUlong
req.alt-loc: NtosKrnl.exe,Ntdll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); Ntdll.dll (user mode)
req.irql: Any level (see Remarks section)
req.iface: 
---

# RtlCompareMemoryUlong function



## -description
<p>The <b>RtlCompareMemoryUlong</b> routine returns how many bytes in a block of memory match a specified pattern. </p>


## -syntax

````
SIZE_T RtlCompareMemoryUlong(
  _In_ PVOID  Source,
  _In_ SIZE_T Length,
  _In_ ULONG  Pattern
);
````


## -parameters
<dl>

### -param <i>Source</i> [in]

<dd>
<p>Pointer to a block of memory. Must be aligned on a ULONG boundary. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Number of bytes over which the comparison should be done. Must be a multiple of <b>sizeof(</b>ULONG<b>)</b>. </p>
</dd>

### -param <i>Pattern</i> [in]

<dd>
<p>Pattern to be compared byte by byte, repeatedly, through the specified memory range. </p>
</dd>
</dl>

## -returns
<p><b>RtlCompareMemoryUlong</b> returns the number of bytes that were compared and found to be equal. If all bytes compare as equal, the input <i>Length</i> is returned. <b>RtlCompareMemoryUlong</b> returns zero if <i>Source</i> is not ULONG-aligned or if <i>Length</i> is not a multiple of <b>sizeof(</b>ULONG<b>)</b>. </p>

## -remarks
<p>If the block of memory at <i>Source</i> is nonpaged, the caller can be running at any IRQL. Otherwise, callers of <b>RtlCompareMemoryUlong</b> must be running at IRQL &lt; DISPATCH_LEVEL. </p>

<p>For more information about managing buffered data and initializing driver-allocated buffers, see <a href="kernel.buffered_data_and_buffer_initialization">Buffered Data and Buffer Initialization</a>. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<dt>NtosKrnl.exe (kernel mode); </dt>
<dt>Ntdll.dll (user mode)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-rtlcomparememory.md">RtlCompareMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlCompareMemoryUlong routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
