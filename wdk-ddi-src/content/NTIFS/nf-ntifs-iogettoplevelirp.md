---
UID: NF.ntifs.IoGetTopLevelIrp
title: IoGetTopLevelIrp
author: windows-driver-content
description: The IoGetTopLevelIrp routine returns the value of the TopLevelIrp field of the current thread.
old-location: ifsk\iogettoplevelirp.htm
ms.assetid: e92685f6-031a-464a-b26a-54bebf7d66b6
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoGetTopLevelIrp
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: IoGetTopLevelIrp
req.iface: 
---

# IoGetTopLevelIrp function



## -description
<p>The <b>IoGetTopLevelIrp</b> routine returns the value of the <b>TopLevelIrp</b> field of the current thread.</p>


## -syntax

````
PIRP IoGetTopLevelIrp(
   VOID 
);
````


## -parameters
<dl>

### -param <i></i> 

<dd>
<p>None</p>
</dd>
</dl>

## -returns
<p><b>IoGetTopLevelIrp</b> returns the value of the <b>TopLevelIrp</b> field of the current thread.</p>

## -remarks
<p><b>IoGetTopLevelIrp</b> can return <b>NULL</b>, an arbitrary file-system-specific value (such as a pointer to the current IRP), or one of the flags listed in the following table.</p>

<p>If the current thread holds no resources above the file system, <b>IoGetTopLevelIrp</b> returns <b>NULL</b>.</p>

<p>If the file system is the top-level component for the current thread, <b>IoGetTopLevelIrp</b> returns a pointer to the current IRP.</p>

<p>If a component other than the file system is the top-level component for the current thread, <b>IoGetTopLevelIrp</b> returns one of the following flags: </p>

<p>FSRTL_FSP_TOP_LEVEL_IRP</p>

<p>This is a recursive call.</p>

<p>FSRTL_CACHE_TOP_LEVEL_IRP</p>

<p>The cache manager is the top-level component for the current thread.</p>

<p>FSRTL_MOD_WRITE_TOP_LEVEL_IRP</p>

<p>The modified page writer is the top-level component for the current thread.</p>

<p>FSRTL_FAST_IO_TOP_LEVEL_IRP</p>

<p>The cache manager is the top-level component for the current thread, and the current thread is in a fast I/O path.</p>

<p> </p>

<p><b>IoGetTopLevelIrp</b> can return <b>NULL</b>, an arbitrary file-system-specific value (such as a pointer to the current IRP), or one of the flags listed in the following table.</p>

<p>If the current thread holds no resources above the file system, <b>IoGetTopLevelIrp</b> returns <b>NULL</b>.</p>

<p>If the file system is the top-level component for the current thread, <b>IoGetTopLevelIrp</b> returns a pointer to the current IRP.</p>

<p>If a component other than the file system is the top-level component for the current thread, <b>IoGetTopLevelIrp</b> returns one of the following flags: </p>

<p>FSRTL_FSP_TOP_LEVEL_IRP</p>

<p>This is a recursive call.</p>

<p>FSRTL_CACHE_TOP_LEVEL_IRP</p>

<p>The cache manager is the top-level component for the current thread.</p>

<p>FSRTL_MOD_WRITE_TOP_LEVEL_IRP</p>

<p>The modified page writer is the top-level component for the current thread.</p>

<p>FSRTL_FAST_IO_TOP_LEVEL_IRP</p>

<p>The cache manager is the top-level component for the current thread, and the current thread is in a fast I/O path.</p>

<p> </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548540">IoSetTopLevelIrp</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoGetTopLevelIrp routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
