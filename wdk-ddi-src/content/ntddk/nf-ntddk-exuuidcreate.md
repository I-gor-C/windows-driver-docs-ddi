---
UID: NF.ntddk.ExUuidCreate
title: ExUuidCreate
author: windows-driver-content
description: The ExUuidCreate routine initializes a UUID (GUID) structure to a newly generated value.
old-location: kernel\exuuidcreate.htm
old-project: kernel
ms.assetid: e85fe5fa-b11e-41ff-a355-4da0394377d1
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ExUuidCreate
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
req.alt-api: ExUuidCreate
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlExPassive, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
---

# ExUuidCreate function



## -description
<p>The <b>ExUuidCreate</b> routine initializes a UUID (GUID) structure to a newly generated value.</p>


## -syntax

````
NTSTATUS ExUuidCreate(
  _Out_ UUID *Uuid
);
````


## -parameters
<dl>

### -param <i>Uuid</i> [out]

<dd>
<p>A pointer to a caller-allocated UUID (GUID) structure that is set to a new UUID value. </p>
</dd>
</dl>

## -returns
<p>
            Possible return values include the following status codes.</p><dl>
<dt><b><b>STATUS_SUCCESS</b></b></dt>
</dl><p>The routine successfully generated a UUID that is universally unique.</p><dl>
<dt><b><b>RPC_NT_UUID_LOCAL_ONLY</b></b></dt>
</dl><p>The routine generated a UUID that is unique only to this computer. This can occur when the MAC address is not an IEEE universally-administered address or when no NICs are present.</p><dl>
<dt><b><b>STATUS_RETRY</b></b></dt>
</dl><p>The system is not ready to generate a new UUID.</p>

<p> </p>

## -remarks
<p>A UUID and a GUID are the same data type.</p>

<p>The caller can iteratively attempt to obtain a new UUID value. </p>

<p>A UUID and a GUID are the same data type.</p>

<p>The caller can iteratively attempt to obtain a new UUID value. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547756">IrqlExPassive</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>