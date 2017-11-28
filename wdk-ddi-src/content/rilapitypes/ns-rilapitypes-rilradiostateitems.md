---
UID: NS.rilapitypes.RILRADIOSTATEITEMS
title: RILRADIOSTATEITEMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradiostateitems_2.htm
old-project: netvista
ms.assetid: 41f8c9fc-7793-47c8-b381-4ef59dfde6b8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILRADIOSTATEITEMS, RILRADIOSTATEITEMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILRADIOSTATEITEMS
req.alt-loc: rilapitypes.h
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

# RILRADIOSTATEITEMS structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILRADIOSTATEITEMS {
  DWORD                 dwGroupId;
  DWORD                 dwCntItems;
  RILRADIOSTATEITEM [1] rilItems;
} RILRADIOSTATEITEMS, RILRADIOSTATEITEMS;
````


## -struct-fields
<dl>

### -field <b>dwGroupId</b>

<dd></dd>

### -field <b>dwCntItems</b>

<dd></dd>

### -field <b>rilItems</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>