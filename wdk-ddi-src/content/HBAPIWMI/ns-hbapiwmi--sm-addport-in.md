---
UID: NS.hbapiwmi._SM_AddPort_IN
title: SM_AddPort_IN
author: windows-driver-content
description: The SM_AddPort_IN structure is used to provide input parameters to the SM_AddPort WMI method.
old-location: storage\sm_addport_in.htm
ms.assetid: 29b05fa7-0393-47df-a77e-63745c0cd1e1
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SM_AddPort_IN
req.alt-loc: hbapiwmi.h
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
ms.keywords: SM_AddPort_IN, SM_AddPort_IN, *PSM_AddPort_IN
req.iface: 
---

# SM_AddPort_IN structure



## -description
<p>The SM_AddPort_IN structure is used to provide input parameters to the SM_AddPort WMI method.</p>


## -syntax

````
typedef struct _SM_AddPort_IN {
  UCHAR PortWWN[8];
  ULONG EventType;
} SM_AddPort_IN, *PSM_AddPort_IN;
````


## -struct-fields
<dl>

### -field <b>PortWWN</b>

<dd>
<p>A worldwide name (WWN) that indicates the port whose events are to be reported.</p>
</dd>

### -field <b>EventType</b>

<dd>
<p>An event type value.</p>
</dd>
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
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>