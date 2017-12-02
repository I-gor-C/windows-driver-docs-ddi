---
UID: NF.ntddk.PsIsHostSilo
title: PsIsHostSilo
author: windows-driver-content
description: This routine will check if the supplied Silo is the host silo.
old-location: kernel\psishostsilo.htm
old-project: kernel
ms.assetid: 4C6D85F2-C9B8-425D-A307-5609E1C1465B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsIsHostSilo
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
req.alt-api: PsIsHostSilo
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

# PsIsHostSilo function



## -description
<p>This routine  will check if the supplied <i>Silo</i> is the host silo.</p>


## -syntax

````
BOOLEAN PsIsHostSilo(
  _In_ PESILO Silo
);
````


## -parameters
<dl>

### -param Silo [in]

<dd>
<p>The  silo to evaluate.</p>
</dd>
</dl>

## -returns
<p>Returns <b>true</b> if the specified silo is the host silo; otherwise, <b>false</b>.</p>

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