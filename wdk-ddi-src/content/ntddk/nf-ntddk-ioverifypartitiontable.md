---
UID: NF.ntddk.IoVerifyPartitionTable
title: IoVerifyPartitionTable
author: windows-driver-content
description: The IoVerifyPartitionTable routine checks the validity of the partition table for a disk.
old-location: kernel\ioverifypartitiontable.htm
old-project: kernel
ms.assetid: dc7b543b-1fb5-477c-a612-c8e7381e637e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoVerifyPartitionTable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoVerifyPartitionTable
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
req.irql: <= APC_LEVEL
req.iface: 
---

# IoVerifyPartitionTable function



## -description
<p>The <b>IoVerifyPartitionTable</b> routine checks the validity of the partition table 
   for a disk.</p>


## -syntax

````
NTSTATUS IoVerifyPartitionTable(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ BOOLEAN        FixErrors
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Specifies the device object of the disk to verify.</p>
</dd>

### -param <i>FixErrors</i> [in]

<dd>
<p>Specifies if the routine should correct any correctable errors in the partition table.</p>
</dd>
</dl>

## -returns
<p>The routine returns STATUS_SUCCESS if the partition table is error-free.</p>

<p>If the caller specifies <b>FALSE</b> for the <i>FixErrors</i> parameter 
       and the partition table has errors, the routine returns STATUS_DISK_CORRUPT_ERROR. If the caller specifies 
       <b>TRUE</b> for <i>FixErrors</i>, and the routine is able to correct all 
       errors in the partition table, it returns STATUS_SUCCESS. Otherwise it returns STATUS_DISK_CORRUPT_ERROR.</p>

<p>The routine might also return other NT status error codes.</p>

## -remarks
<p><b>IoVerifyPartitionTable</b> must be used only by disk drivers.</p>

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
<p>Available starting with Windows XP.</p>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>