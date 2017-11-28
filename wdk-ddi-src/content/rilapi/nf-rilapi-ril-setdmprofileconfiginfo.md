---
UID: NF.rilapi.RIL_SetDMProfileConfigInfo
title: RIL_SetDMProfileConfigInfo
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\ril_setdmprofileconfiginfo.htm
old-project: netvista
ms.assetid: 4d2ab950-a045-4b5a-be9b-0b80c442e63d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RIL_SetDMProfileConfigInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rilapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RIL_SetDMProfileConfigInfo
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
req.iface: 
req.product: Windows 10 or later.
---

# RIL_SetDMProfileConfigInfo function



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 

            </p>


## -syntax

````
HRESULT  RIL_SetDMProfileConfigInfo(
   HRIL                        hRil,
   LPVOID                      lpContext,
   DWORD                       dwExecutor,
   DWORD                       dwConfigItem,
   const RILDMCONFIGINFOVALUE  rciValue
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

### -param <i>dwConfigItem</i> 

<dd></dd>

### -param <i>rciValue</i> 

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