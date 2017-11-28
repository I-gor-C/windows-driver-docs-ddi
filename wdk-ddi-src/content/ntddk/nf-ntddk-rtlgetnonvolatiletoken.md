---
UID: NF.ntddk.RtlGetNonVolatileToken
title: RtlGetNonVolatileToken
author: windows-driver-content
description: The routine, RtlGetNonVolatileToken, gets various properties about a non-volatile memory buffer and stores them in the variable NvToken.
old-location: ifsk\rtlgetnonvolatiletoken.htm
old-project: ifsk
ms.assetid: A9E866D4-C47F-4926-A838-EDB739CF1185
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlGetNonVolatileToken
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
req.alt-api: RtlGetNonVolatileToken
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

# RtlGetNonVolatileToken function



## -description
<p>The routine, <b>RtlGetNonVolatileToken</b>, gets various properties about a non-volatile memory
    buffer and stores them in the variable <b>NvToken</b>.</p>


## -syntax

````
NTSTATUS RtlGetNonVolatileToken(
   _In_reads_bytes_(Size) PVOID NvBuffer,
   _In_ SIZE_T                  Size,
   _Outptr_ PVOID               *NvToken
);
````


## -parameters
<dl>

### -param <i>NvBuffer</i> 

<dd>
<p>A pointer to the non-volatile memory that the returned <b>NvToken</b> is going to track state for. This should be an address obtained from a file mapping object.</p>
</dd>

### -param <i>Size</i> 

<dd>
<p>The length, in bytes, of the non-volatile memory buffer <b>NvBuffer</b> points to.</p>
</dd>

### -param <i>NvToken</i> 

<dd>
<p> A pointer to an opaque structure that tracks
        information about the given non-volatile memory region which <b>RtlGetNonVolatileToken</b> had returned.</p>
</dd>
</dl>

## -returns
<p>The routine <b>RtlGetNonVolatileToken</b> returns one of the status codes:</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller had insufficient access rights to perform the requested action.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH
</b></dt>
</dl><p>The specified base address is outside the range of accessible addresses.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <b>NvBuffer</b> is not the same length as specified in<b>Size</b>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The request was successful.</p>

<p> </p>

## -remarks
<p>This routine is currently not supported for Windows Server until the next major release of Windows Server.</p>

<p>This routine is currently not supported for Windows Server until the next major release of Windows Server.</p>

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
<a href="ifsk.RtlFlushNonVolatileMemory">
RtlFlushNonVolatileMemory</a>
</dt>
<dt>
<a href="ifsk.RtlFlushNonVolatileMemoryRanges">RtlFlushNonVolatileMemoryRanges</a>
</dt>
<dt>
<a href="ifsk.RtlFreeNonVolatileToken">RtlFreeNonVolatileToken</a>
</dt>
<dt>
<a href="ifsk.RtlWriteNonVolatileMemory">RtlWriteNonVolatileMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlGetNonVolatileToken routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
