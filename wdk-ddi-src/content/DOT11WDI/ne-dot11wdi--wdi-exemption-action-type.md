---
UID: NE.dot11wdi._WDI_EXEMPTION_ACTION_TYPE
title: WDI_EXEMPTION_ACTION_TYPE
author: windows-driver-content
description: The WDI_EXEMPTION_ACTION_TYPE enumeration defines the exemption types.
old-location: netvista\wdi_exemption_action_type.htm
ms.assetid: 46640961-828c-411b-b1b9-bcceb04bdf17
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_EXEMPTION_ACTION_TYPE
req.alt-loc: dot11wdi.h
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
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
req.iface: ISynthSinkDMus
---

# WDI_EXEMPTION_ACTION_TYPE enumeration



## -description
<p>The WDI_EXEMPTION_ACTION_TYPE enumeration defines the exemption types.</p>


## -syntax

````
typedef enum _WDI_EXEMPTION_ACTION_TYPE { 
  WDI_EXEMPT_NO_EXEMPTION                    = 0,
  WDI_EXEMPT_ALWAYS                          = 1,
  WDI_EXEMPT_ON_KEY_MAPPING_KEY_UNAVAILABLE  = 2
} WDI_EXEMPTION_ACTION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WDI_EXEMPT_NO_EXEMPTION"></a><a id="wdi_exempt_no_exemption"></a><b>WDI_EXEMPT_NO_EXEMPTION</b>

<dd>
<p>Packets are not exempt from any cipher operations performed by the port.</p>
</dd>

### -field <a id="WDI_EXEMPT_ALWAYS"></a><a id="wdi_exempt_always"></a><b>WDI_EXEMPT_ALWAYS</b>

<dd>
<p>On send, packets are exempt from cipher operations and are transmitted unencrypted. On receive, the received packet is discarded if the Protected Frame subfield of the Frame Control field in the 802.11 MAC header is set to 1.</p>
</dd>

### -field <a id="WDI_EXEMPT_ON_KEY_MAPPING_KEY_UNAVAILABLE"></a><a id="wdi_exempt_on_key_mapping_key_unavailable"></a><b>WDI_EXEMPT_ON_KEY_MAPPING_KEY_UNAVAILABLE</b>

<dd>
<p>On send, packets are exempt from cipher operations if there is no key-mapping key for the packet's destination MAC address. On receive, the received packet is discarded if a key-mapping key for the source MAC address is available and the Protected Frame subfield of the Frame Control field in the 802.11 MAC header is set to 0.</p>
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
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>