---
UID: NF.rilapi.RIL_DisableNotifications
title: RIL_DisableNotifications
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\ril_disablenotifications.htm
old-project: netvista
ms.assetid: 70635820-9912-4d27-87e2-e713ea33e819
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RIL_DisableNotifications
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
req.alt-api: RIL_DisableNotifications
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

# RIL_DisableNotifications function



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 

            </p>


## -syntax

````
HRESULT  RIL_DisableNotifications(
   HRIL   hRil,
   LPVOID usersContext,
   DWORD  lpdwNotifications,
   DWORD  dwNotificationCount
);
````


## -parameters
<dl>

### -param <i>hRil</i> 

<dd></dd>

### -param <i>usersContext</i> 

<dd></dd>

### -param <i>lpdwNotifications</i> 

<dd></dd>

### -param <i>dwNotificationCount</i> 

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