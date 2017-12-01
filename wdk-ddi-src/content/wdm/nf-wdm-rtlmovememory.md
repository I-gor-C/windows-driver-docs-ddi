---
UID: NF.wdm.RtlMoveMemory
title: RtlMoveMemory
author: windows-driver-content
description: The RtlMoveMemory routine copies the contents of a source memory block to a destination memory block, and supports overlapping source and destination memory blocks.
old-location: kernel\rtlmovememory.htm
old-project: kernel
ms.assetid: f6727247-e704-42d7-b4f1-ce7d20e317bb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlMoveMemory
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
req.alt-api: RtlMoveMemory
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctlA, BufAfterReqCompletedReadA, BufAfterReqCompletedWriteA
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level (See Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# RtlMoveMemory function



## -description
<p>The <b>RtlMoveMemory</b> routine copies the contents of a source memory block to a destination memory block, and supports overlapping source and destination memory blocks.</p>


## -syntax

````
VOID RtlMoveMemory(
  _Out_       VOID UNALIGNED *Destination,
  _In_  const VOID UNALIGNED *Source,
  _In_        SIZE_T         Length
);
````


## -parameters
<dl>

### -param <i>Destination</i> [out]

<dd>
<p>A pointer to the destination memory block to copy the bytes to.</p>
</dd>

### -param <i>Source</i> [in]

<dd>
<p>A pointer to the source memory block to copy the bytes from.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes to copy from the source to the destination.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The source memory block, which is defined by <i>Source</i> and <i>Length</i>, can overlap the destination memory block, which is defined by <i>Destination</i> and <i>Length</i>.</p>

<p>The <a href="..\wdm\nf-wdm-rtlcopymemory.md">RtlCopyMemory</a> routine runs faster than <b>RtlMoveMemory</b>, but <b>RtlCopyMemory</b> requires that the source and destination memory blocks do not overlap.</p>

<p>Callers of <b>RtlMoveMemory</b> can be running at any IRQL if the source and destination memory blocks are in nonpaged system memory. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

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
<p>Any level (See Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_bufafterreqcompletedintioctla">BufAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedioctla">BufAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedreada">BufAfterReqCompletedReadA</a>, <a href="devtest.kmdf_bufafterreqcompletedwritea">BufAfterReqCompletedWriteA</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-rtlcopymemory.md">RtlCopyMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlMoveMemory routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
