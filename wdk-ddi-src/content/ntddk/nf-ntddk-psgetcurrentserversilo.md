---
UID: NF.ntddk.PsGetCurrentServerSilo
title: PsGetCurrentServerSilo
author: windows-driver-content
description: This routine returns the effective server silo for the thread.
old-location: kernel\psgetcurrentserversilo.htm
old-project: kernel
ms.assetid: 4E30CD53-C078-40D7-BEF8-A39F57D71D42
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsGetCurrentServerSilo
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
req.alt-api: PsGetCurrentServerSilo
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

# PsGetCurrentServerSilo function



## -description
<p>This routine returns the effective server silo for the thread.</p>


## -syntax

````
PESILO PsGetCurrentServerSilo(void);
````


## -parameters


## -returns
<p>A pointer to the current server silo.  This pointer is valid for the current thread, but must be referenced before transferring to another thread (for example, via a workitem).</p>

<p>A pointer to the current server silo.  This pointer is valid for the current thread, but must be referenced before transferring to another thread (for example, via a workitem).</p>

<p>A pointer to the current server silo.  This pointer is valid for the current thread, but must be referenced before transferring to another thread (for example, via a workitem).</p>

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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>_IRQL_requires_max_(DISPATCH_LEVEL)</p>
</td>
</tr>
</table>