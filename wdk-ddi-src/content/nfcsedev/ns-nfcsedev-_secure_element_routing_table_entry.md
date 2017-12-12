---
UID: NS.NFCSEDEV._SECURE_ELEMENT_ROUTING_TABLE_ENTRY
title: _SECURE_ELEMENT_ROUTING_TABLE_ENTRY
author: windows-driver-content
description: SECURE_ELEMENT_ROUTING_TABLE_ENTRY is a member of SECURE_ELEMENT_ROUTING_TABLE.
old-location: nfpdrivers\_secure_element_routing_table_entry.htm
old-project: nfpdrivers
ms.assetid: 199FEA6A-A57F-4B13-832A-65DB7729455F
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: _SECURE_ELEMENT_ROUTING_TABLE_ENTRY, SECURE_ELEMENT_ROUTING_TABLE_ENTRY, *PSECURE_ELEMENT_ROUTING_TABLE_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
---

# _SECURE_ELEMENT_ROUTING_TABLE_ENTRY structure



## -description
SECURE_ELEMENT_ROUTING_TABLE_ENTRY is a member of <a href="nfpdrivers._secure_element_routing_table">SECURE_ELEMENT_ROUTING_TABLE</a>.



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

### -field eRoutingType

NFC Forum listen mode routing table entry type.



### -field TechRoutingInfo

RF technology routing table entry information.


### -field ProtoRoutingInfo

RF protocol routing table entry information.


### -field AidRoutingInfo

AID routing table control information.



## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>