---
UID: NS.wwan._WWAN_IPV6_ADDRESS
title: WWAN_IPV6_ADDRESS
author: windows-driver-content
description: The WWAN_IPV6_ADDRESS structure represents an IPV6 address of a PDP context.
old-location: netvista\wwan_ipv6_address.htm
old-project: netvista
ms.assetid: 3DAC7E30-B938-429C-B389-59F924216B04
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WWAN_IPV6_ADDRESS, WWAN_IPV6_ADDRESS, *PWWAN_IPV6_ADDRESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8.1 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_IPV6_ADDRESS
req.alt-loc: wwan.h
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
req.product: Windows 10 or later.
---

# WWAN_IPV6_ADDRESS structure



## -description
<p>The WWAN_IPV6_ADDRESS structure represents an IPV6 address of a PDP context.</p>


## -syntax

````
typedef struct _WWAN_IPV6_ADDRESS {
  ULONG OnLinkPrefixLength;
  UCHAR IPV6Address[16];
} WWAN_IPV6_ADDRESS, *PWWAN_IPV6_ADDRESS;
````


## -struct-fields
<dl>

### -field <b>OnLinkPrefixLength</b>

<dd>
<p>The length of the prefix or network part of the IP address.</p>
</dd>

### -field <b>IPV6Address[16]</b>

<dd>
<p>The IPV6 address of the PDP context.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 8.1 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>