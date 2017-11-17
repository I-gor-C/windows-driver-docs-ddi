---
UID: NS.wwan.WWAN_IP_CONFIGURATION_FLAGS
title: WWAN_IP_CONFIGURATION_FLAGS
author: windows-driver-content
description: The WWAN_IP_CONFIGURATION_FLAGS structure represents flags that describe the availability of the IP address, gateway, DNS server, and/or MTU information of a PDP context.
old-location: netvista\wwan_ip_configuration_flags.htm
ms.assetid: 5157F48F-E1D3-4B22-BBB0-0FC7965C794B
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8.1 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_IP_CONFIGURATION_FLAGS
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
ms.keywords: WWAN_IP_CONFIGURATION_FLAGS, WWAN_IP_CONFIGURATION_FLAGS
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_IP_CONFIGURATION_FLAGS structure



## -description
<p>The WWAN_IP_CONFIGURATION_FLAGS structure represents flags that describe the availability of the IP address, gateway, DNS server, and/or MTU information of a PDP context.</p>


## -syntax

````
typedef union {
  ULONG  Value;
  struct {
    ULONG AddressAvailable:1;
    ULONG GatewayAvailable:1;
    ULONG DnsServerAvailable:1;
    ULONG MTUAvailable:1;
  };
} WWAN_IP_CONFIGURATION_FLAGS;
````


## -struct-fields
<dl>

### -field <b>Value</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field ( <i>unnamed struct</i> )

<dd>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>
struct
{
    ULONG    AddressAvailable:1;
    ULONG    GatewayAvailable:1;
    ULONG    DnsServerAvailable:1;
    ULONG    MTUAvailable:1;
};</pre>
</td>
</tr>
</table></span></div>
<dl>

### -field <b>AddressAvailable:1</b>

<dd>
<p>An address is available.</p>
</dd>

### -field <b>GatewayAvailable:1</b>

<dd>
<p>A gateway is available.</p>
</dd>

### -field <b>DnsServerAvailable:1</b>

<dd>
<p>A DNS server is available.</p>
</dd>

### -field <b>MTUAvailable:1</b>

<dd>
<p>An MTU is available.</p>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn449758">WWAN_IP_CONFIGURATION_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_IP_CONFIGURATION_FLAGS union%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
