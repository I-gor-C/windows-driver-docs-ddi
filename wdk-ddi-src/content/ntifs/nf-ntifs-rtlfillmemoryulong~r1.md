---
UID: NF.ntifs.RtlFillMemoryUlong~r1
title: RtlFillMemoryUlong function
author: windows-driver-content
description: The RtlFillMemoryUlong routine fills the specified range of memory with one or more repetitions of a ULONG value.
old-location: ifsk\rtlfillmemoryulong.htm
old-project: ifsk
ms.assetid: a3758f32-daa9-4795-9a79-694b02da43cd
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RtlFillMemoryUlong
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
req.alt-api: RtlFillMemoryUlong
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
req.irql: See Remarks section.
---

# RtlFillMemoryUlong function



## -description
The <b>RtlFillMemoryUlong</b> routine fills the specified range of memory with one or more repetitions of a ULONG value. 



## -syntax

````
VOID RtlFillMemoryUlong(
  _Out_ PVOID  Destination,
  _In_  SIZE_T Length,
  _In_  ULONG  Pattern
);
````


## -parameters

### -param Destination [out]

Pointer to a block of memory to be filled. Must be ULONG-aligned.


### -param Length [in]

Length in bytes of the memory to fill. Must be a multiple of <b>sizeof(</b>ULONG<b>)</b>. (Note: SIZE_T is defined in <i>basetsd.h</i>.)


### -param Pattern [in]

ULONG value with which to fill the memory block. 


## -returns
None


## -remarks
If the block of memory at <i>Destination</i> is nonpaged, the caller can be running at any IRQL. Otherwise, callers of <b>RtlFillMemoryUlong</b> must be running at IRQL &lt; DISPATCH_LEVEL. 

For more information about managing buffered data and initializing driver-allocated buffers, see <a href="kernel.buffered_data_and_buffer_initialization">Buffered Data and Buffer Initialization</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
See Remarks section.

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlfillmemory">RtlFillMemory</a>
</dt>
<dt>
<a href="ifsk.rtlfillmemoryulonglong">RtlFillMemoryUlonglong</a>
</dt>
<dt>
<a href="kernel.rtlzeromemory">RtlZeroMemory</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlFillMemoryUlong routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

