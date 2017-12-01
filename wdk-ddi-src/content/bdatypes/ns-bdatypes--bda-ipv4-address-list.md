---
UID: NS.bdatypes._BDA_IPv4_ADDRESS_LIST
title: BDA_IPv4_ADDRESS_LIST
author: windows-driver-content
description: .
old-location: stream\bda_ipv4_address_list.htm
old-project: stream
ms.assetid: 92E90C2A-D59C-4A38-A444-978B16170B89
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDA_IPv4_ADDRESS_LIST, BDA_IPv4_ADDRESS_LIST, *PBDA_IPv4_ADDRESS_LIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_IPv4_ADDRESS_LIST
req.alt-loc: Bdatypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# BDA_IPv4_ADDRESS_LIST structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_IPv4_ADDRESS_LIST {
  ULONG            ulcAddresses;
  BDA_IPv4_ADDRESS rgAddressl[MIN_DIMENSION];
} BDA_IPv4_ADDRESS_LIST, *PBDA_IPv4_ADDRESS_LIST;
````


## -struct-fields
<dl>

### -field <b>ulcAddresses</b>

<dd></dd>

### -field <b>rgAddressl</b>

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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>