---
UID: NF.ntddk.PsMakeSiloContextPermanent
title: PsMakeSiloContextPermanent
author: windows-driver-content
description: This routine makes the slot in a silo instance read-only, allowing the object in the slot to be retrieved without affecting the reference count on that object.
old-location: kernel\psmakesilocontextpermanent.htm
ms.assetid: 74BE4FF9-0342-4942-A58F-9C6D5F76E5F0
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
req.alt-api: PsMakeSiloContextPermanent
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
ms.keywords: PsMakeSiloContextPermanent
req.iface: 
---

# PsMakeSiloContextPermanent function



## -description
<p>This routine makes the slot in a silo instance read-only, allowing the object in the slot to be retrieved without affecting the reference count on that object.</p>


## -syntax

````
NTSTATUS PsMakeSiloContextPermanent(
  _In_ PESILO Silo,
  _In_ ULONG  ContextSlot
);
````


## -parameters
<dl>

### -param <i>Silo</i> [in]

<dd>
<p>The silo in which the slot resides. This parameter is required and it cannot be <b>NULL</b>. </p>
</dd>

### -param <i>ContextSlot</i> [in]

<dd>
<p>The slot to make read-only. The slot must be previously allocated by the <a href="https://msdn.microsoft.com/library/windows/hardware/mt735056">PsAllocSiloContextSlot</a> routine.</p>
</dd>
</dl>

## -returns
<p>The following NT status codes are returned.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The slot does not contain a valid object. This is an error code.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The slot has not been allocated. This is an error code.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p>

<p> </p>

## -remarks
<p>Before calling this routine, the slot must contain a valid object. After it completes, the <a href="https://msdn.microsoft.com/library/windows/hardware/mt735081">PsReplaceSiloContext</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/mt735080">PsRemoveSiloContext</a> routines will fail with <b>STATUS_NOT_SUPPORTED</b>. </p>

<p>Before calling this routine, the slot must contain a valid object. After it completes, the <a href="https://msdn.microsoft.com/library/windows/hardware/mt735081">PsReplaceSiloContext</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/mt735080">PsRemoveSiloContext</a> routines will fail with <b>STATUS_NOT_SUPPORTED</b>. </p>

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