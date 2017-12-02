---
UID: NF.ntddk.RtlFlushNonVolatileMemory
title: RtlFlushNonVolatileMemory
author: windows-driver-content
description: The routine RtlFlushNonVolatileMemory optimally flushes the given non-volatile memory region.
old-location: ifsk\rtlflushnonvolatilememory.htm
old-project: ifsk
ms.assetid: 759CDFAA-D939-44E7-AE03-E3ED90F8E09D
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlFlushNonVolatileMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Winnt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlFlushNonVolatileMemory
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# RtlFlushNonVolatileMemory function



## -description
<p>The  routine <b>RtlFlushNonVolatileMemory</b> optimally flushes the given non-volatile memory region.</p>


## -syntax

````
NTSTATUS RtlFlushNonVolatileMemory(
   _In_ PVOID                   NvToken,
   _In_reads_bytes_(Size) PVOID NvBuffer,
   _In_ SIZE_T                  Size,
   _In_ ULONG                   Flags
);
````


## -parameters
<dl>

### -param NvToken 

<dd>
<p> A pointer to an opaque structure that has
        information about various properties of the non-volatile memory region which <a href="..\ntddk\nf-ntddk-rtlgetnonvolatiletoken.md">RtlGetNonVolatileToken</a> had returned.</p>
</dd>

### -param NvBuffer 

<dd>
<p>A pointer to the non-volatile memory to flush. This should be user addresses obtained from
        a file mapping object.</p>
</dd>

### -param Size 

<dd>
<p>The length, in bytes, of the non-volatile memory buffer <b>NvBuffer</b> points to.</p>
</dd>

### -param Flags 

<dd>
<p>One of the following flags can be specified:</p>
<table>
<tr>
<th>Flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FLUSH_NV_MEMORY_IN_FLAG_NO_DRAIN</p>
</td>
<td>
<p>Specifies that this routine does not need to wait for the flush to drain.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The routine <b>RtlFreeNonVolatileToken</b> returns one of the status codes:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p><b>NvToken</b> is an invalid pointer or token.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The request was successful.</p>

<p> </p>

## -remarks
<p> This routine <b>RtlFlushNonVolatileMemory</b> can also add more context to <b>NvToken</b> to help verifiers. This routine is currently not supported for Windows Server until the next major release of Windows Server. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Winnt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.RtlDrainNonVolatileFlush">RtlDrainNonVolatileFlush</a>
</dt>
<dt>
<a href="ifsk.RtlFlushNonVolatileMemoryRanges">RtlFlushNonVolatileMemoryRanges</a>
</dt>
<dt>
<a href="ifsk.RtlFreeNonVolatileToken">RtlFreeNonVolatileToken</a>
</dt>
<dt>
<a href="ifsk.RtlGetNonVolatileToken">RtlGetNonVolatileToken</a>
</dt>
<dt>
<a href="ifsk.RtlWriteNonVolatileMemory">RtlWriteNonVolatileMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlFlushNonVolatileMemory routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
