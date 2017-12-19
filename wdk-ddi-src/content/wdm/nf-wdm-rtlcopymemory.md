---
UID: NF.wdm.RtlCopyMemory
title: RtlCopyMemory macro
author: windows-driver-content
description: The RtlCopyMemory routine copies the contents of a source memory block to a destination memory block.
old-location: kernel\rtlcopymemory.htm
old-project: kernel
ms.assetid: d204eeb4-e109-4a86-986f-0fccdda3f8f8
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: RtlCopyMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlCopyMemory
req.alt-loc: NtDll.dll,NtosKrnl.exe,API-MS-Win-Core-Rtlsupport-l1-1-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtDll.dll (user mode); NtosKrnl.exe (kernel mode)
req.irql: Any level (See Remarks section)
req.product: Windows 10 or later.
---

# RtlCopyMemory macro



## -description
The <b>RtlCopyMemory</b> routine copies the contents of a source memory block to a destination memory block.



## -syntax

````
VOID RtlCopyMemory(
  _Out_       VOID UNALIGNED *Destination,
  _In_  const VOID UNALIGNED *Source,
  _In_        SIZE_T         Length
);
````


## -parameters

### -param Destination [out]

A pointer to the destination memory block to copy the bytes to.


### -param Source [in]

A pointer to the source memory block to copy the bytes from.


### -param Length [in]

The number of bytes to copy from the source to the destination.


## -remarks
<b>RtlCopyMemory</b> runs faster than <b>RtlMoveMemory</b>. However, <b>RtlCopyMemory</b> requires that the source memory block, which is defined by <i>Source</i> and <i>Length</i>, cannot overlap the destination memory block, which is defined by <i>Destination</i> and <i>Length</i>. In contrast, <b>RtlMoveMemory</b> correctly handles the case in which the source and destination memory blocks overlap.

Callers of <b>RtlCopyMemory</b> can be running at any IRQL if the source and destination memory blocks are in nonpaged system memory. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.


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
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<dt>NtDll.dll (user mode); </dt>
<dt>NtosKrnl.exe (kernel mode)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level (See Remarks section)

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlmovememory">RtlMoveMemory</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlCopyMemory routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

