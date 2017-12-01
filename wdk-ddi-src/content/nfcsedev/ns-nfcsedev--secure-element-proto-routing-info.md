---
UID: NS.nfcsedev._SECURE_ELEMENT_PROTO_ROUTING_INFO
title: SECURE_ELEMENT_PROTO_ROUTING_INFO
author: windows-driver-content
description: SECURE_ELEMENT_PROTO_ROUTING_INFO is a member of SECURE_ELEMENT_ROUTING_TABLE_ENTRY.
old-location: nfpdrivers\_secure_element_proto_routing_info.htm
old-project: nfpdrivers
ms.assetid: E22C5985-13A8-4A55-A97B-DABD7E475BD3
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: SECURE_ELEMENT_PROTO_ROUTING_INFO, SECURE_ELEMENT_PROTO_ROUTING_INFO, *PSECURE_ELEMENT_PROTO_ROUTING_INFO
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
req.alt-api: SECURE_ELEMENT_PROTO_ROUTING_INFO
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

# SECURE_ELEMENT_PROTO_ROUTING_INFO structure



## -description
<p>SECURE_ELEMENT_PROTO_ROUTING_INFO
 is a member of <a href="..\nfcsedev\ns-nfcsedev--secure-element-routing-table-entry.md">SECURE_ELEMENT_ROUTING_TABLE_ENTRY</a>. </p>


## -syntax

````
typedef struct _SECURE_ELEMENT_PROTO_ROUTING_INFO {
  GUID guidSecureElementId;
  BYTE eRfProtocolType;
} SECURE_ELEMENT_PROTO_ROUTING_INFO, *P_SECURE_ELEMENT_PROTO_ROUTING_INFO;
````


## -struct-fields
<dl>

### -field <b>guidSecureElementId</b>

<dd>
<p>Secure element unique identifier returned by enumeration DDI.</p>
</dd>

### -field <b>eRfProtocolType</b>

<dd>
<p>NFC Forum RF protocol.</p>
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