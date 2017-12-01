---
UID: NS.ks.PBUS_INTERFACE_MEDIUMS
title: PBUS_INTERFACE_MEDIUMS
author: windows-driver-content
description: .
old-location: stream\bus_interface_mediums.htm
old-project: stream
ms.assetid: 0A2D1D8F-8C82-4335-9FBF-4515A8DC20C1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PBUS_INTERFACE_MEDIUMS, BUS_INTERFACE_MEDIUMS, *PBUS_INTERFACE_MEDIUMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BUS_INTERFACE_MEDIUMS
req.alt-loc: Ks.h
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

# PBUS_INTERFACE_MEDIUMS structure



## -description
<p></p>


## -syntax

````
typedef struct {
  INTERFACE           Interface;
  PFNQUERYMEDIUMSLIST QueryMediumsList;
} BUS_INTERFACE_MEDIUMS, *PBUS_INTERFACE_MEDIUMS;
````


## -struct-fields
<dl>

### -field <b>Interface</b>

<dd>
<p>Specifies the standard interface header.</p>
</dd>

### -field <b>QueryMediumsList</b>

<dd>
<p>Specifies the interface definition.</p>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>