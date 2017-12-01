---
UID: NF.ntddk.IoSetActivityIdIrp
title: IoSetActivityIdIrp
author: windows-driver-content
description: The IoSetActivityIdIrp routine associates an activity ID with an IRP.
old-location: kernel\iosetactivityidirp.htm
old-project: kernel
ms.assetid: 81D3BE8C-D6E0-47E2-959C-3834988E4C61
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoSetActivityIdIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoSetActivityIdIrp
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
req.irql: Any level if a GUID is passed in, otherwise PASSIVE_LEVEL.
req.iface: 
---

# IoSetActivityIdIrp function



## -description
<p>The IoSetActivityIdIrp routine associates an activity ID with an IRP.</p>


## -syntax

````
NTSTATUS IoSetActivityIdIrp(
  _In_     PIRP   Irp,
  _In_opt_ LPGUID Guid
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>The IRP to associate the activity ID with.</p>
</dd>

### -param <i>Guid</i> [in, optional]

<dd>
<p>A pointer to the GUID that represents the ID to store in the IRP.  If NULL, IoSetActivityIdIrp attempts to retrieve the activity ID from the current thread if it was the thread that originally issued the request.</p>
</dd>
</dl>

## -returns
<p>IoSetActivityIdIrp returns STATUS_SUCCESS if the call is successful. Possible error return values include the following.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>No GUID was provided and the ETW activity ID was unavailable.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The I/O tracing provider has not been enabled on the IRP.</p>

<p> </p>

## -remarks
<p>Drivers should use IoSetActivityIdIrp only on IRPs that have been allocated using <a href="..\wdm\nf-wdm-ioallocateirp.md">IoAllocateIrp</a> (and freed using <a href="..\wdm\nf-wdm-iofreeirp.md">IoFreeIrp</a>). Otherwise, memory leakage may result.</p>

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
<p>Available starting with  Windows 8.</p>
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
<p>Any level if a GUID is passed in, otherwise PASSIVE_LEVEL.</p>
</td>
</tr>
</table>