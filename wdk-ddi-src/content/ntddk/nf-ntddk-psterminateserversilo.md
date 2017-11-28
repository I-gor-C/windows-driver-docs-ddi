---
UID: NF.ntddk.PsTerminateServerSilo
title: PsTerminateServerSilo
author: windows-driver-content
description: This routine terminates the specified silo.
old-location: kernel\psterminateserversilo.htm
old-project: kernel
ms.assetid: C19190A3-57F9-4482-A550-045805734909
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PsTerminateServerSilo
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
req.alt-api: PsTerminateServerSilo
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

# PsTerminateServerSilo function



## -description
<p>This routine terminates the specified silo.</p>


## -syntax

````
void PsTerminateServerSilo(
  _In_ PESILO   ServerSilo,
  _In_ NTSTATUS ExistStatus
);
````


## -parameters
<dl>

### -param <i>ServerSilo</i> [in]

<dd>
<p>A pointer to the silo being terminated.</p>
</dd>

### -param <i>ExistStatus</i> [in]

<dd>
<p>The exit status for the silo.</p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

## -remarks
<p>This routine can be called within or from outside a silo context.
    Note that this is different from a BugCheck; this routine will return to
    the caller.</p>

<p>This routine can be called within or from outside a silo context.
    Note that this is different from a BugCheck; this routine will return to
    the caller.</p>

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