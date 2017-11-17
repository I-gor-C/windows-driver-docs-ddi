---
UID: NS.ntddndis._NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN
title: NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN
author: windows-driver-content
description: The NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN structure is used to specify the routing domain properties of a VM network adapter.
old-location: netvista\ndis_switch_port_property_routing_domain.htm
ms.assetid: 6E1DF4F3-9ED4-4E34-A768-1B5008D61B0C
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
req.alt-api: NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN
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
ms.keywords: NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN, NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN, *PNDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN
req.iface: 
---

# NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN structure



## -description
<p>The <b>NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN</b> structure is used to specify the routing domain properties of a VM network adapter.</p>


## -syntax

````
typedef struct _NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN {
  NDIS_OBJECT_HEADER       Header;
  ULONG                    Flags;
  NDIS_ROUTING_DOMAIN_ID   RoutingDomainId;
  NDIS_ROUTING_DOMAIN_NAME RoutingDomainName;
  ULONG {
    USHORT FirstIsolationEntryOffset;
  }                   NumIsolationEntries;
} NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN, *PNDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN</b>  structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to <b>NDIS_OBJECT_TYPE_DEFAULT</b>. To specify the version of the <b>NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN_REVISION_1"></a><a id="ndis_switch_port_property_routing_domain_revision_1"></a>NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN_REVISION_1

<dd>
<p>Original version for NDIS 6.40 and later.</p>
<p>Set the <b>Size</b> member to <b>NDIS_SIZEOF_NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN_REVISION_1</b>.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.

</p>
</dd>

### -field <b>RoutingDomainId</b>

<dd>
<p>The routing domain identifier for the VM network adapter. This identifier is a GUID.</p>
</dd>

### -field <b>RoutingDomainName</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/dn383678">NDIS_ISOLATION_NAME</a> structure that contains the routing domain name for the VM network adapter.</p>
</dd>

### -field <b>NumIsolationEntries</b>

<dd>
<p>A <b>ULONG</b> value that specifies the number of <a href="https://msdn.microsoft.com/library/windows/hardware/dn383684">NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY</a> in the array that follows the <b>NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN</b> structure.</p>
<dl>

### -field <b>FirstIsolationEntryOffset</b>

<dd>
<p>The offset, in bytes, from the beginning of the buffer pointed to by the <b>InformationBuffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure to the first isolation entry.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383678">NDIS_ISOLATION_NAME</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383681">NDIS_ROUTING_DOMAIN_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383684">NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598256">NDIS_SWITCH_PROPERTY_PARAMETERS_GET_PROPERTY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
