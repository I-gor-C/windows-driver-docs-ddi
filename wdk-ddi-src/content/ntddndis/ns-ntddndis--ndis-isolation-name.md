---
UID: NS.ntddndis._NDIS_ISOLATION_NAME
title: NDIS_ISOLATION_NAME
author: windows-driver-content
description: The NDIS_ISOLATION_NAME structure contains an NDIS isolation name for a VM network adapter.
old-location: netvista\ndis_isolation_name.htm
ms.assetid: 4712F853-8819-476C-8AD9-426EA5A0802E
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.40 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_ISOLATION_NAME
req.alt-loc: Ntddndis.h
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
ms.keywords: NDIS_ISOLATION_NAME, NDIS_ISOLATION_NAME
req.iface: 
---

# NDIS_ISOLATION_NAME structure



## -description
<p>The <b>NDIS_ISOLATION_NAME</b> structure contains an NDIS isolation name for a VM network adapter. The isolation name can be an isolation ID name or a routing domain name. This structure supports the following derived types:<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef NDIS_ISOLATION_NAME NDIS_ISOLATION_ID_NAME, *PNDIS_ISOLATION_ID_NAME;
typedef NDIS_ISOLATION_NAME NDIS_ROUTING_DOMAIN_NAME, *PNDIS_ROUTING_DOMAIN_NAME;
</pre>
</td>
</tr>
</table></span></div>
</p>


## -syntax

````
typedef NDIS_ISOLATION_NAME NDIS_ISOLATION_ID_NAME, *PNDIS_ISOLATION_ID_NAME;
typedef NDIS_ISOLATION_NAME NDIS_ROUTING_DOMAIN_NAME, *PNDIS_ROUTING_DOMAIN_NAME;

````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>Length, in bytes, of the NDIS isolation name. This member must be less than or equal to <b>NDIS_ISOLATION_NAME_MAX_STRING_SIZE</b>.</p>
</dd>

### -field <b>       String</b>

<dd>
<p>A <b>NULL</b>-terminated string that contains the NDIS isolation name. The isolation name can be an isolation ID name or a routing domain name.</p>
</dd>
</dl>

## -remarks
<p>This structure is used in:<ul>
<li>
<p>The <b>IsolationIdName</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383684">NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY</a> structure.</p>
</li>
<li>
<p>The <b>RoutingDomainName</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383681">NDIS_ROUTING_DOMAIN_ENTRY</a> structure.</p>
</li>
<li>
<p>The <b>RoutingDomainName</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383688">NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN</a> structure.</p>
</li>
</ul>
</p>

<p>The <b>IsolationIdName</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383684">NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY</a> structure.</p>

<p>The <b>RoutingDomainName</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383681">NDIS_ROUTING_DOMAIN_ENTRY</a> structure.</p>

<p>The <b>RoutingDomainName</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383688">NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.40 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383677">NDIS_ISOLATION_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383681">NDIS_ROUTING_DOMAIN_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383684">NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383688">NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_ISOLATION_NAME structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
