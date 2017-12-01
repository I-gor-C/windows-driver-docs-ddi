---
UID: NF.wdm.RtlFillMemory
title: RtlFillMemory
author: windows-driver-content
description: The RtlFillMemory routine fills a block of memory with the specified fill value.
old-location: kernel\rtlfillmemory.htm
old-project: kernel
ms.assetid: 9a73331a-cc73-4a47-948b-a821600ca6a6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlFillMemory
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
req.alt-api: RtlFillMemory
req.alt-loc: NtDll.dll,NtosKrnl.exe,API-MS-Win-Core-rtlsupport-l1-1-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtDll.lib (user mode); NtosKrnl.lib (kernel mode)
req.dll: NtDll.dll (user mode); NtosKrnl.exe (kernel mode)
req.irql: Any level (See Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# RtlFillMemory function



## -description
<p>The <b>RtlFillMemory</b> routine fills a block of memory with the specified fill value.</p>


## -syntax

````
VOID RtlFillMemory(
  _Out_ VOID UNALIGNED *Destination,
  _In_  SIZE_T         Length,
  _In_  UCHAR          Fill
);
````


## -parameters
<dl>

### -param <i>Destination</i> [out]

<dd>
<p>A pointer to the block of memory to be filled.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes in the block of memory to be filled.</p>
</dd>

### -param <i>Fill</i> [in]

<dd>
<p>The value to fill the destination memory block with. This value is copied to every byte in the memory block that is defined by <i>Destination</i> and <i>Length</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Callers of <b>RtlFillMemory</b> can be running at any IRQL if the destination memory block is in nonpaged system memory. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

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
<dt>NtDll.lib (user mode); </dt>
<dt>NtosKrnl.lib (kernel mode)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level (See Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-rtlzeromemory.md">RtlZeroMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlFillMemory routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
