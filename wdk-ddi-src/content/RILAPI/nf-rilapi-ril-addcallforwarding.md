---
UID: NF.rilapi.RIL_AddCallForwarding
title: RIL_AddCallForwarding
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\ril_addcallforwarding.htm
ms.assetid: 86b08757-bbc0-4f19-8153-c6ecae158cf2
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RIL_AddCallForwarding
req.alt-loc: rilapi.h
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
ms.keywords: RIL_AddCallForwarding
req.iface: 
req.product: Windows 10 or later.
---

# RIL_AddCallForwarding function



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

            </p>


## -syntax

````
HRESULT  RIL_AddCallForwarding(
   HRIL                             hRil,
   LPVOID                           lpContext,
   DWORD                            dwExecutor,
   RILCALLFORWARDINGSETTINGSREASON  dwReason,
   const RILCALLFORWARDINGSETTINGS  lpSettings
);
````


## -parameters
<dl>

### -param <i>hRil</i> 

<dd></dd>

### -param <i>lpContext</i> 

<dd></dd>

### -param <i>dwExecutor</i> 

<dd></dd>

### -param <i>dwReason</i> 

<dd></dd>

### -param <i>lpSettings</i> 

<dd></dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
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
<dt>Rilapi.h</dt>
</dl>
</td>
</tr>
</table>