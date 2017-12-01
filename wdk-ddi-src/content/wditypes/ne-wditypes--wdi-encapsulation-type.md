---
UID: NE.wditypes._WDI_ENCAPSULATION_TYPE
title: WDI_ENCAPSULATION_TYPE
author: windows-driver-content
description: The WDI_ENCAPSULATION_TYPE enumeration defines the Wi-Fi encapsulation types.
old-location: netvista\wdi_encapsulation_type.htm
old-project: netvista
ms.assetid: 6EDCC69B-F156-416B-9824-5E26F9834D14
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_ENCAPSULATION_TYPE
req.alt-loc: wditypes.hpp
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDI_ENCAPSULATION_TYPE enumeration



## -description
<p>The WDI_ENCAPSULATION_TYPE enumeration defines the Wi-Fi encapsulation types.</p>


## -syntax

````
typedef enum _WDI_ENCAPSULATION_TYPE { 
  WDI_ENCAPSULATION_RFC_1042  = 1,
  WDI_ENCAPSULATION_802_1H    = 2
} WDI_ENCAPSULATION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WDI_ENCAPSULATION_RFC_1042"></a><a id="wdi_encapsulation_rfc_1042"></a><b>WDI_ENCAPSULATION_RFC_1042</b>

<dd>
<p>The encapsulation that is defined in IETF RFC 1042.</p>
</dd>

### -field <a id="WDI_ENCAPSULATION_802_1H"></a><a id="wdi_encapsulation_802_1h"></a><b>WDI_ENCAPSULATION_802_1H</b>

<dd>
<p>The encapsulation that is defined in the IEEE 802.1h-1997 standard.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>