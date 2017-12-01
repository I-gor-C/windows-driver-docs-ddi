---
UID: NF.ntddk.PsDereferenceSiloContext
title: PsDereferenceSiloContext
author: windows-driver-content
description: This routine decrements the reference count on the object.
old-location: kernel\psdereferencesilocontext.htm
old-project: kernel
ms.assetid: B71C7E8F-E136-4C13-B771-03B3C3C1BE64
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsDereferenceSiloContext
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
req.alt-api: PsDereferenceSiloContext
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
req.irql: _IRQL_requires_max_(DISPATCH_LEVEL)
req.iface: 
---

# PsDereferenceSiloContext function



## -description
<p>This routine decrements the reference count on the object.</p>


## -syntax

````
void PsDereferenceSiloContext(
  _In_ PVOID SiloContext
);
````


## -parameters
<dl>

### -param <i>SiloContext</i> [in]

<dd>
<p>A pointer to the object created by the <a href="..\ntddk\nf-ntddk-pscreatesilocontext.md">PsCreateSiloContext</a> routine. This parameter is required and it cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

## -remarks
<p>If the reference count reaches zero it will call the cleanup callback provided when the <a href="..\ntddk\nf-ntddk-pscreatesilocontext.md">PsCreateSiloContext</a> routine created the object. </p>

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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>_IRQL_requires_max_(DISPATCH_LEVEL)</p>
</td>
</tr>
</table>