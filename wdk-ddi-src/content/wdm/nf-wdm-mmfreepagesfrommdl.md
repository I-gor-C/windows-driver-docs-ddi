---
UID: NF:wdm.MmFreePagesFromMdl
title: MmFreePagesFromMdl function
author: windows-driver-content
description: The MmFreePagesFromMdl routine frees all the physical pages that are described by an MDL that was created by the MmAllocatePagesForMdl routine.
old-location: kernel\mmfreepagesfrommdl.htm
old-project: kernel
ms.assetid: bde26b75-9eae-494b-b943-f1e9534c5f7a
ms.author: windowsdriverdev
ms.date: 1/4/2018
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
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---

# MmFreePagesFromMdl function



## -description
The <b>MmFreePagesFromMdl</b> routine frees all the physical pages that are described by an MDL that was created by the <a href="..\wdm\nf-wdm-mmallocatepagesformdl.md">MmAllocatePagesForMdl</a> routine. 



## -syntax

````
VOID MmFreePagesFromMdl(
  _In_ PMDLX MemoryDescriptorList
);
````


## -parameters

### -param MemoryDescriptorList [in]

Pointer to an MDL that was created by <b>MmAllocatePagesForMdl</b>.


## -returns
None


## -remarks
<b>MmFreePagesFromMdl</b> can only be used to free the memory pages that are described by an MDL that was created by <b>MmAllocatePagesForMdl</b>.

After calling <b>MmFreePagesFromMdl</b>, the caller must also call <a href="..\wdm\nf-wdm-exfreepool.md">ExFreePool</a> to release the memory that was allocated for the MDL structure.

<b>MmFreePagesFromMdl</b> runs at IRQL &lt;= APC_LEVEL. For Windows Server 2008 and later versions of the Windows operating system, you can also call this routine at DISPATCH_LEVEL. However, you can improve driver performance by calling at IRQL &lt;= APC_LEVEL.


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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/075f5710-b2bf-4546-9648-661a3c8521f8">IrqlMmApcLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-exfreepool.md">ExFreePool</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmallocatepagesformdl.md">MmAllocatePagesForMdl</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmFreePagesFromMdl routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

