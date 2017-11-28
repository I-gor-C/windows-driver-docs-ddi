---
UID: NS.winsplp._NOTIFICATION_CONFIG_1
title: NOTIFICATION_CONFIG_1
author: windows-driver-content
description: .
old-location: print\notification_config_1.htm
old-project: print
ms.assetid: 4A33F3EB-9A2E-40F4-B5BC-EDEA5085301E
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: NOTIFICATION_CONFIG_1, NOTIFICATION_CONFIG_1, *PNOTIFICATION_CONFIG_1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winsplp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NOTIFICATION_CONFIG_1
req.alt-loc: Winsplp.h
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

# NOTIFICATION_CONFIG_1 structure



## -description
<p></p>


## -syntax

````
typedef struct _NOTIFICATION_CONFIG_1 {
  UINT                   cbSize;
  DWORD                  fdwFlags;
  ROUTER_NOTIFY_CALLBACK pfnNotifyCallback;
  PVOID                  pContext;
} NOTIFICATION_CONFIG_1, *PNOTIFICATION_CONFIG_1;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>fdwFlags</b>

<dd></dd>

### -field <b>pfnNotifyCallback</b>

<dd></dd>

### -field <b>pContext</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winsplp.h</dt>
</dl>
</td>
</tr>
</table>