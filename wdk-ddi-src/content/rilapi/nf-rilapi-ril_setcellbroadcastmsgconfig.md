---
UID: NF.rilapi.RIL_SetCellBroadcastMsgConfig
title: RIL_SetCellBroadcastMsgConfig function
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\ril_setcellbroadcastmsgconfig.htm
old-project: NetVista
ms.assetid: c2b7b9b7-a76f-4bd9-bf25-edb5c103a578
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RIL_SetCellBroadcastMsgConfig
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
req.alt-api: RIL_SetCellBroadcastMsgConfig
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
req.product: Windows 10 or later.
---

# RIL_SetCellBroadcastMsgConfig function



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 

            



## -syntax

````
HRESULT  RIL_SetCellBroadcastMsgConfig(
   HRIL                  hRil,
   LPVOID                lpContext,
   HUICCAPP              hUiccApp,
   const RILCBMSGCONFIG  lpCbMsgConfigInfo
);
````


## -parameters

### -param hRil 


### -param lpContext 


### -param hUiccApp 


### -param lpCbMsgConfigInfo 


## -returns
If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Rilapi.h</dt>
</dl>
</td>
</tr>
</table>