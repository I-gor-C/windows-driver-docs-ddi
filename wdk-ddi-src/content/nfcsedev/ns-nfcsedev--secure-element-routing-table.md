---
UID: NS.nfcsedev._SECURE_ELEMENT_ROUTING_TABLE
title: SECURE_ELEMENT_ROUTING_TABLE
author: windows-driver-content
description: SECURE_ELEMENT_ROUTING_TABLE is an input parameter for IOCTL_NFCSE_SET_ROUTING_TABLE.
old-location: nfpdrivers\_secure_element_routing_table.htm
ms.assetid: AD5E6434-BBBF-44CB-8153-B8F4D4F75E94
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: nfpdrivers
req.header: nfcsedev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SECURE_ELEMENT_ROUTING_TABLE
req.alt-loc: nfcsedev.h
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
ms.keywords: SECURE_ELEMENT_ROUTING_TABLE, SECURE_ELEMENT_ROUTING_TABLE, *PSECURE_ELEMENT_ROUTING_TABLE
req.iface: 
---

# SECURE_ELEMENT_ROUTING_TABLE structure



## -description
<p>SECURE_ELEMENT_ROUTING_TABLE is an input parameter for <a href="https://msdn.microsoft.com/library/windows/hardware/dn905513">IOCTL_NFCSE_SET_ROUTING_TABLE</a>.</p>


## -syntax

````
typedef struct _SECURE_ELEMENT_ROUTING_TABLE {
  DWORD                                                                NumberOfEntries;
  _Field_size_(NumberOfEntries)
    SECURE_ELEMENT_ROUTING_TABLE_ENTRY TableEntries[ANYSIZE_ARRAY];
} SECURE_ELEMENT_ROUTING_TABLE, *P_SECURE_ELEMENT_ROUTING_TABLE;
````


## -struct-fields
<dl>

### -field <b>NumberOfEntries</b>

<dd>
<p>Number of routing table entries.</p>
</dd>

### -field <b>TableEntries[ANYSIZE_ARRAY]</b>

<dd>
<p>Listen mode routing table.</p>
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
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>