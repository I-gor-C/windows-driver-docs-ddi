---
UID: NF.wdm.MmFreePagesFromMdl
title: MmFreePagesFromMdl
author: windows-driver-content
description: The MmFreePagesFromMdl routine frees all the physical pages that are described by an MDL that was created by the MmAllocatePagesForMdl routine.
old-location: kernel\mmfreepagesfrommdl.htm
old-project: kernel
ms.assetid: bde26b75-9eae-494b-b943-f1e9534c5f7a
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MmFreePagesFromMdl
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
req.alt-api: MmFreePagesFromMdl
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
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# MmFreePagesFromMdl function



## -description
<p>The <b>MmFreePagesFromMdl</b> routine frees all the physical pages that are described by an MDL that was created by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554482">MmAllocatePagesForMdl</a> routine. </p>


## -syntax

````
VOID MmFreePagesFromMdl(
  _In_ PMDLX MemoryDescriptorList
);
````


## -parameters
<dl>

### -param <i>MemoryDescriptorList</i> [in]

<dd>
<p>Pointer to an MDL that was created by <b>MmAllocatePagesForMdl</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>MmFreePagesFromMdl</b> can only be used to free the memory pages that are described by an MDL that was created by <b>MmAllocatePagesForMdl</b>.</p>

<p>After calling <b>MmFreePagesFromMdl</b>, the caller must also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> to release the memory that was allocated for the MDL structure.</p>

<p><b>MmFreePagesFromMdl</b> runs at IRQL &lt;= APC_LEVEL. For Windows Server 2008 and later versions of the Windows operating system, you can also call this routine at DISPATCH_LEVEL. However, you can improve driver performance by calling at IRQL &lt;= APC_LEVEL.</p>

<p><b>MmFreePagesFromMdl</b> can only be used to free the memory pages that are described by an MDL that was created by <b>MmAllocatePagesForMdl</b>.</p>

<p>After calling <b>MmFreePagesFromMdl</b>, the caller must also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> to release the memory that was allocated for the MDL structure.</p>

<p><b>MmFreePagesFromMdl</b> runs at IRQL &lt;= APC_LEVEL. For Windows Server 2008 and later versions of the Windows operating system, you can also call this routine at DISPATCH_LEVEL. However, you can improve driver performance by calling at IRQL &lt;= APC_LEVEL.</p>

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
<p>See Remarks section.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554482">MmAllocatePagesForMdl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmFreePagesFromMdl routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
