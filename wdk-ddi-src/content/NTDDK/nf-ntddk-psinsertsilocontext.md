---
UID: NF.ntddk.PsInsertSiloContext
title: PsInsertSiloContext
author: windows-driver-content
description: This routine inserts an object in an empty slot in a Silo.
old-location: kernel\psinsertsilocontext.htm
ms.assetid: 31C7A629-3B5E-44BA-AE03-3331E3200FC6
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsInsertSiloContext
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: PsInsertSiloContext
req.iface: 
---

# PsInsertSiloContext function



## -description
<p>This routine inserts an object in an empty slot in a <i>Silo</i>.</p>


## -syntax

````
NTSTATUS PsInsertSiloContext(
  _In_ PESILO Silo,
  _In_ ULONG  ContextSlot,
  _In_ PVOID  SiloContext
);
````


## -parameters
<dl>

### -param <i>Silo</i> [in]

<dd>
<p>A pointer to a silo.  This parameter is required and it cannot be <b>NULL</b>.</p>
</dd>

### -param <i>ContextSlot</i> [in]

<dd>
<p>A slot allocated by the <a href="https://msdn.microsoft.com/library/windows/hardware/mt735056">PsAllocSiloContextSlot</a> routine. </p>
</dd>

### -param <i>SiloContext</i> [in]

<dd>
<p>A pointer to the object created by the <a href="https://msdn.microsoft.com/library/windows/hardware/mt735058">PsCreateSiloContext</a> routine. The object must be created using the same silo pointer as the one specified in this routine. This parameter is required and it cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p>The following NT status codes are returned.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES </b></dt>
</dl><p>There are no resources in the system to perform the insert. This is an error code. </p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The slot is not empty. This is an error code. </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1607</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
</table>