---
UID: NF.ntddk.PsInsertPermanentSiloContext
title: PsInsertPermanentSiloContext
author: windows-driver-content
description: This routine inserts an object in an empty slot in a Silo.
old-location: kernel\psinsertpermanentsilocontext.htm
old-project: kernel
ms.assetid: ADBAB25B-7646-4E0E-AFD8-18B87A293674
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsInsertPermanentSiloContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsInsertPermanentSiloContext
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
req.iface: 
---

# PsInsertPermanentSiloContext function



## -description
<p>This routine inserts an object in an empty slot in a <i>Silo</i>.</p>


## -syntax

````
NTSTATUS PsInsertPermanentSiloContext(
  _In_ PESILO Silo,
  _In_ ULONG  ContextSlot,
  _In_ PVOID  SiloContext
);
````


## -parameters
<dl>

### -param <i>Silo</i> [in]

<dd>
<p>The silo in which the object is to be inserted. This parameter is required and it cannot be <b>NULL</b>. </p>
</dd>

### -param <i>ContextSlot</i> [in]

<dd>
<p>The slot in which the object is to be inserted. A slot allocated by the <a href="..\ntddk\nf-ntddk-psallocsilocontextslot.md">PsAllocSiloContextSlot</a> routine.</p>
</dd>

### -param <i>SiloContext</i> [in]

<dd>
<p>The object to be inserted, created by the <a href="..\ntddk\nf-ntddk-pscreatesilocontext.md">PsCreateSiloContext</a> routine. The object must be created using the same silo as specified in the <i>Silo</i> parameter. This parameter is required and it cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p>The following NT status codes are returned.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There are no resources in the system to perform the insert. This is an error code. </p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The slot is not empty. This is an error code.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p>

<p> </p>

## -remarks
<p>A successful call to <b>PsInsertPermanentSiloContext</b> increments the reference count on <i>SiloContext</i>. If <b>PsInsertPermanentSiloContext</b> fails, the reference count remains unchanged. In either case, after the routine completes, the caller must call <a href="..\ntddk\nf-ntddk-psdereferencesilocontext.md">PsDereferenceSiloContext</a> to decrement the <i>SiloContext</i> object.</p>

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