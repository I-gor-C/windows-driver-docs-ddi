---
UID: NF.ntddk.RtlFlushNonVolatileMemoryRanges
title: RtlFlushNonVolatileMemoryRanges
author: windows-driver-content
description: The routine RtlFlushNonVolatileMemoryRanges optimally flushes the given non-volatile memory regions.
old-location: ifsk\rtlflushnonvolatilememoryranges.htm
old-project: ifsk
ms.assetid: 169C5F41-B372-4056-AAC5-53DD0582A563
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlFlushNonVolatileMemoryRanges
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
req.alt-api: RtlFlushNonVolatileMemoryRanges
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

# RtlFlushNonVolatileMemoryRanges function



## -description
<p>The routine <b>RtlFlushNonVolatileMemoryRanges</b> optimally flushes the given non-volatile memory regions.</p>


## -syntax

````
NTSTATUS RtlFlushNonVolatileMemoryRanges(
   _In_ PVOID                               NvToken,
   _In_reads_(TotalRanges) PNV_MEMORY_RANGE NvRanges,
   _In_ SIZE_T                              TotalRanges,
   _In_ ULONG                               Flags
);
````


## -parameters
<dl>

### -param <i>NvToken</i> 

<dd>
<p> A pointer to an opaque structure that has
        information about various properties of the non-volatile memory region which <a href="..\ntddk\nf-ntddk-rtlgetnonvolatiletoken.md">RtlGetNonVolatileToken</a> had returned.</p>
</dd>

### -param <i>NvRanges</i> 

<dd>
<p>Specifies an array of <b>NV_MEMORY_RANGE</b> structures which describe the non-volatile memory regions to flush</p>
</dd>

### -param <i>TotalRanges</i> 

<dd>
<p>Specifies the number of elements in the <b>NVRanges</b> array.</p>
</dd>

### -param <i>Flags</i> 

<dd>
<p>For flags specified, refer <a href="..\ntddk\nf-ntddk-rtlflushnonvolatilememory.md">RtlFlushNonVolatileMemory</a> as this routine also honors the flags apart from passing it to <b>RtlFlushNonVolatileMemory</b>.</p>
</dd>
</dl>

## -returns
<p>The routine <b>RtlFlushNonVolatileMemoryRanges</b> returns one of the following:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p><b>NvToken</b> is an invalid pointer or token.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The request was successful.</p>

<p> </p>

## -remarks
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlFlushNonVolatileMemoryRanges routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
