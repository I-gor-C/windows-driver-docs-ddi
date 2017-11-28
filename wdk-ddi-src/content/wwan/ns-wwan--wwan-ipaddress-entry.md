---
UID: NS.wwan._WWAN_IPADDRESS_ENTRY
title: WWAN_IPADDRESS_ENTRY
author: windows-driver-content
description: The WWAN_IPADDRESS_ENTRY structure represents either the IPV4 or IPV6 address of a PDP context.
old-location: netvista\wwan_ipaddress_entry.htm
old-project: netvista
ms.assetid: 85615799-5AA0-4D83-9246-73F3C7ABFFF6
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WWAN_IPADDRESS_ENTRY, WWAN_IPADDRESS_ENTRY, *PWWAN_IPADDRESS_ENTRY
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
req.alt-api: WWAN_IPADDRESS_ENTRY
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

# WWAN_IPADDRESS_ENTRY structure



## -description
<p>The WWAN_IPADDRESS_ENTRY structure represents either the IPV4 or IPV6 address of a PDP context.</p>


## -syntax

````
typedef struct _WWAN_IPADDRESS_ENTRY {
  ULONG IsIpv6:1;
  ULONG IsReported:1;
  union {
    WWAN_IPV4_ADDRESS Ipv4;
    WWAN_IPV6_ADDRESS Ipv6;
  };
} WWAN_IPADDRESS_ENTRY, *PWWAN_IPADDRESS_ENTRY;
````


## -struct-fields
<dl>

### -field <b>IsIpv6:1</b>

<dd>
<p>Set if the IP address of the PDP context is an IPV6 address.</p>
</dd>

### -field <b>IsReported:1</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field ( <i>unnamed union</i> )

<dd>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>
union
{
    WWAN_IPV4_ADDRESS    Ipv4;
    WWAN_IPV6_ADDRESS    Ipv6;
};</pre>
</td>
</tr>
</table></span></div>
<dl>

### -field <b>Ipv4</b>

<dd>
<p>The IPV4 address of the PDP context, if <b>IsIpv6</b> is not set.</p>
</dd>

### -field <b>Ipv6</b>

<dd>
<p>The IPV6 address of the PDP context, if <b>IsIpv6</b> is set.</p>
</dd>
</dl>
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