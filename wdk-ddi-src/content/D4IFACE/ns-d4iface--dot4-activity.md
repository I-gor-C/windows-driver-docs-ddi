---
UID: NS.d4iface._DOT4_ACTIVITY
title: DOT4_ACTIVITY
author: windows-driver-content
description: .
old-location: print\dot4_activity.htm
ms.assetid: CD3DBBA5-AE5C-4DC1-BE52-696138494701
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: d4iface.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT4_ACTIVITY
req.alt-loc: D4iface.h
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
ms.keywords: DOT4_ACTIVITY, DOT4_ACTIVITY, *PDOT4_ACTIVITY
req.iface: 
---

# DOT4_ACTIVITY structure



## -description
<p></p>


## -syntax

````
typedef struct _DOT4_ACTIVITY {
  ULONG          ulMessage;
  ULONG          ulByteCount;
  CHANNEL_HANDLE hChannel;
} DOT4_ACTIVITY, *PDOT4_ACTIVITY;
````


## -struct-fields
<dl>

### -field <b>ulMessage</b>

<dd></dd>

### -field <b>ulByteCount</b>

<dd></dd>

### -field <b>hChannel</b>

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
<dt>D4iface.h</dt>
</dl>
</td>
</tr>
</table>