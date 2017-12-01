---
UID: NE.nfcsedev._SECURE_ELEMENT_ROUTING_TYPE
title: SECURE_ELEMENT_ROUTING_TYPE
author: windows-driver-content
description: SECURE_ELEMENT_ROUTING_TYPE is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY.
old-location: nfpdrivers\_secure_element_routing_type.htm
old-project: nfpdrivers
ms.assetid: 1420D957-546E-4795-A545-B098C411CCA5
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: NFCRM_SET_RADIO_STATE, NFCRM_SET_RADIO_STATE, *PNFCRM_SET_RADIO_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: nfcsedev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SECURE_ELEMENT_ROUTING_TYPE
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
req.iface: 
---

# SECURE_ELEMENT_ROUTING_TYPE enumeration



## -description
<p>SECURE_ELEMENT_ROUTING_TYPE
is a member of <a href="..\nfcsedev\ns-nfcsedev--secure-element-routing-table-entry.md">SECURE_ELEMENT_ROUTING_TABLE_ENTRY</a>.</p>


## -syntax

````
typedef enum _SECURE_ELEMENT_ROUTING_TYPE { 
  RoutingTypeTech      = 0,
  RoutingTypeProtocol  = 1,
  RoutingTypeAid       = 2
} SECURE_ELEMENT_ROUTING_TYPE;
````


## -enum-fields
<dl>

### -field <a id="RoutingTypeTech"></a><a id="routingtypetech"></a><a id="ROUTINGTYPETECH"></a><b>RoutingTypeTech</b>

<dd>
<p>NFC Forum technology-based routing type.
</p>
</dd>

### -field <a id="RoutingTypeProtocol"></a><a id="routingtypeprotocol"></a><a id="ROUTINGTYPEPROTOCOL"></a><b>RoutingTypeProtocol</b>

<dd>
<p>NFC Forum protocol-based routing type.
</p>
</dd>

### -field <a id="RoutingTypeAid"></a><a id="routingtypeaid"></a><a id="ROUTINGTYPEAID"></a><b>RoutingTypeAid</b>

<dd>
<p>NFC Forum AID-based routing type.
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