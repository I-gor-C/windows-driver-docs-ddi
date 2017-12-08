---
UID: NF.ntddk.RtlWriteNonVolatileMemory
title: RtlWriteNonVolatileMemory function
author: windows-driver-content
description: The routine RtlWriteNonVolatileMemory copies the contents of a source buffer to a non-volatile destination memory buffer.
old-location: ifsk\rtlwritenonvolatilememory.htm
old-project: ifsk
ms.assetid: 49DDDEF8-F949-4674-A18B-9BB091D163C2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlWriteNonVolatileMemory
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
req.alt-api: RtlWriteNonVolatileMemory
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
---

# RtlWriteNonVolatileMemory function



## -description
The routine <b>RtlWriteNonVolatileMemory</b> copies the contents of a source buffer to a non-volatile destination memory buffer.


## -syntax

````
NTSTATUS RtlWriteNonVolatileMemory(
   _In_ PVOID                              NvToken,
   _Out_writes_bytes_(Size) VOID UNALIGNED *NvDestination,
   _In_reads_bytes_(Size) VOID UNALIGNED   *Source,
   _In_ SIZE_T                             Size,
   _In_ ULONG                              Flags
);
````


## -parameters

### -param NvToken 

 A pointer to an opaque structure that has
        information about various properties of the non-volatile memory region which <a href="ifsk.rtlgetnonvolatiletoken">RtlGetNonVolatileToken</a> had returned.

### -param NvDestination 

A pointer to the non-volatile destination buffer to copy to.

### -param Source 

A pointer to the source buffer to copy from.

### -param Size 

The length, in bytes, of the copy operation.

### -param Flags 

Reserved for future use.

## -returns
The routine <b>RtlWriteNonVolatileMemory</b> returns one of the following:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><b>NvToken</b> is an invalid pointer or token.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The request was successful.

 

## -remarks
 This is a <a href="kernel.rtlcopymemory">RtlCopyMemory</a> equivalent for non-volatile memory
    the value add is only with verifier enabled. When the verifier is enabled,
    ranges that are modified can be tracked in <b>NvToken</b> and can be reported
    in <a href="ifsk.rtlfreenonvolatiletoken">RtlFreeNonVolatileToken</a> if a flush is not called for a write. This routine is currently not supported for Windows Server until the next major release of Windows Server.

## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 10, version 1703
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
None supported
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="kernel.rtlcopymemory">RtlCopyMemory</a>
</dt>
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
<a href="ifsk.RtlGetNonVolatileToken">RtlGetNonVolatileToken</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlWriteNonVolatileMemory routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
