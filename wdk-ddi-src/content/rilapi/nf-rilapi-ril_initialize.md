---
UID: NF.rilapi.RIL_Initialize
title: RIL_Initialize function
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\ril_initialize.htm
old-project: netvista
ms.assetid: 7287281b-8c7b-4842-b312-1fff130a5de6
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: RIL_Initialize
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
req.alt-api: RIL_Initialize
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

# RIL_Initialize function



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 

            



## -syntax

````
HRESULT  RIL_Initialize(
   DWORD             dwIndex,
   RILRESULTCALLBACK pfnResult,
   RILNOTIFYCALLBACK pfnNotify,
   DWORD             lpdwNotifications,
   DWORD             dwNotificationCount,
   LPVOID            lpParam,
   WCHAR             pwszClientName,
   HRIL              lphRil
);
````


## -parameters

### -param dwIndex 


### -param pfnResult 


### -param pfnNotify 


### -param lpdwNotifications 


### -param dwNotificationCount 


### -param lpParam 


### -param pwszClientName 


### -param lphRil 


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