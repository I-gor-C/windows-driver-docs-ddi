---
UID: NS.nfcsedev._SECURE_ELEMENT_ROUTING_TABLE_ENTRY
title: SECURE_ELEMENT_ROUTING_TABLE_ENTRY
author: windows-driver-content
description: SECURE_ELEMENT_ROUTING_TABLE_ENTRY is a member of SECURE_ELEMENT_ROUTING_TABLE.
old-location: nfpdrivers\_secure_element_routing_table_entry.htm
ms.assetid: 199FEA6A-A57F-4B13-832A-65DB7729455F
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
req.alt-api: SECURE_ELEMENT_ROUTING_TABLE_ENTRY
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
ms.keywords: SECURE_ELEMENT_ROUTING_TABLE_ENTRY, SECURE_ELEMENT_ROUTING_TABLE_ENTRY, *PSECURE_ELEMENT_ROUTING_TABLE_ENTRY
req.iface: 
---

# SECURE_ELEMENT_ROUTING_TABLE_ENTRY structure



## -description
<p>SECURE_ELEMENT_ROUTING_TABLE_ENTRY is a member of <a href="https://msdn.microsoft.com/library/windows/hardware/dn905627">SECURE_ELEMENT_ROUTING_TABLE</a>.</p>


## -syntax

````
typedef struct _SECURE_ELEMENT_ROUTING_TABLE_ENTRY {
  SECURE_ELEMENT_ROUTING_TYPE eRoutingType;
  union {
    SECURE_ELEMENT_TECH_ROUTING_INFO  TechRoutingInfo;
    SECURE_ELEMENT_PROTO_ROUTING_INFO ProtoRoutingInfo;
    SECURE_ELEMENT_AID_ROUTING_INFO   AidRoutingInfo;
  };
} SECURE_ELEMENT_ROUTING_TABLE_ENTRY, *P_SECURE_ELEMENT_ROUTING_TABLE_ENTRY;
````


## -struct-fields
<dl>

### -field <b>eRoutingType</b>

<dd>
<p>NFC Forum listen mode routing table entry type.
</p>
</dd>

### -field <b>TechRoutingInfo</b>

<dd>
<p>RF technology routing table entry information.</p>
</dd>

### -field <b>ProtoRoutingInfo</b>

<dd>
<p>RF protocol routing table entry information.</p>
</dd>

### -field <b>AidRoutingInfo</b>

<dd>
<p>AID routing table control information.
</p>
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