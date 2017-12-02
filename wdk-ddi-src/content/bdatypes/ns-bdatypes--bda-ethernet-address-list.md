---
UID: NS.bdatypes._BDA_ETHERNET_ADDRESS_LIST
title: BDA_ETHERNET_ADDRESS_LIST
author: windows-driver-content
description: .
old-location: stream\bda_ethernet_address_list.htm
old-project: stream
ms.assetid: 2985A0EC-4B5F-43FA-A2E9-487877A3C9A0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDA_ETHERNET_ADDRESS_LIST, BDA_ETHERNET_ADDRESS_LIST, *PBDA_ETHERNET_ADDRESS_LIST
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
req.alt-api: BDA_ETHERNET_ADDRESS_LIST
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

# BDA_ETHERNET_ADDRESS_LIST structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_ETHERNET_ADDRESS_LIST {
  ULONG                ulcAddresses;
  BDA_ETHERNET_ADDRESS rgAddressl[MIN_DIMENSION];
} BDA_ETHERNET_ADDRESS_LIST, *PBDA_ETHERNET_ADDRESS_LIST;
````


## -struct-fields
<dl>

### -field ulcAddresses

<dd></dd>

### -field rgAddressl

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