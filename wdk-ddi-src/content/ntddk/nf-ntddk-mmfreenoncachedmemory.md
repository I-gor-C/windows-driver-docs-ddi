---
UID: NF.ntddk.MmFreeNonCachedMemory
title: MmFreeNonCachedMemory
author: windows-driver-content
description: The MmFreeNonCachedMemory routine releases a range of noncached memory that was allocated by the MmAllocateNonCachedMemory routine.
old-location: kernel\mmfreenoncachedmemory.htm
old-project: kernel
ms.assetid: 284c7e69-50c6-4eef-bcf1-547bc7032a4a
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MmFreeNonCachedMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmFreeNonCachedMemory
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlMmApcLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <=APC_LEVEL
req.iface: 
---

# MmFreeNonCachedMemory function



## -description
<p>The <b>MmFreeNonCachedMemory</b> routine releases a range of noncached memory that was allocated by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554479">MmAllocateNonCachedMemory</a> routine. </p>


## -syntax

````
VOID MmFreeNonCachedMemory(
  _In_ PVOID  BaseAddress,
  _In_ SIZE_T NumberOfBytes
);
````


## -parameters
<dl>

### -param <i>BaseAddress</i> [in]

<dd>
<p>Pointer to the virtual address of the memory to be freed. </p>
</dd>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>Specifies the size of the range to be freed. This value must match the size passed in a preceding call to <b>MmAllocateNonCachedMemory</b>. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>MmFreeNonCachedMemory</b> routine performs the opposite action of <a href="https://msdn.microsoft.com/library/windows/hardware/ff554479">MmAllocateNonCachedMemory</a>. </p>

<p>The <b>MmFreeNonCachedMemory</b> routine performs the opposite action of <a href="https://msdn.microsoft.com/library/windows/hardware/ff554479">MmAllocateNonCachedMemory</a>. </p>

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
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqlmmapclte">IrqlMmApcLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554479">MmAllocateNonCachedMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmFreeNonCachedMemory routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
