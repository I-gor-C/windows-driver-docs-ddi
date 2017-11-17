---
UID: NS.ntddndis._NDIS_ROUTING_DOMAIN_ENTRY
title: NDIS_ROUTING_DOMAIN_ENTRY
author: windows-driver-content
description: The NDIS_ROUTING_DOMAIN_ENTRY structure is used by the OID_GEN_ISOLATION_PARAMETERS OID to return the routing domain entries for a VM network adapter's port.
old-location: netvista\ndis_routing_domain_entry.htm
ms.assetid: 65E39285-AFD2-4098-A983-C7FA06505407
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
req.alt-api: NDIS_ROUTING_DOMAIN_ENTRY
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
ms.keywords: NDIS_ROUTING_DOMAIN_ENTRY, NDIS_ROUTING_DOMAIN_ENTRY, *PNDIS_ROUTING_DOMAIN_ENTRY
req.iface: 
---

# NDIS_ROUTING_DOMAIN_ENTRY structure



## -description
<p>The <b>NDIS_ROUTING_DOMAIN_ENTRY</b> structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383690">OID_GEN_ISOLATION_PARAMETERS</a> OID to return the routing domain entries for a VM network adapter's port.</p>


## -syntax

````
typedef struct _NDIS_ROUTING_DOMAIN_ENTRY {
  NDIS_OBJECT_HEADER       Header;
  ULONG                    Flags;
  NDIS_ROUTING_DOMAIN_ID   RoutingDomainId;
  NDIS_ROUTING_DOMAIN_NAME RoutingDomainName;
  ULONG                    NumIsolationEntries;
  ULONG                    FirstIsolationEntryOffset;
} NDIS_ROUTING_DOMAIN_ENTRY, *PNDIS_ROUTING_DOMAIN_ENTRY;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_ROUTING_DOMAIN_ENTRY</b>  structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to <b>NDIS_OBJECT_TYPE_DEFAULT</b>. To specify the version of the <b>NDIS_ROUTING_DOMAIN_ENTRY</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_ROUTING_DOMAIN_ENTRY_REVISION_1"></a><a id="ndis_routing_domain_entry_revision_1"></a>NDIS_ROUTING_DOMAIN_ENTRY_REVISION_1

<dd>
<p>Original version for NDIS 6.40 and later.</p>
<p>Set the <b>Size</b> member to <b>NDIS_SIZEOF_NDIS_ROUTING_DOMAIN_ENTRY_REVISION_1</b>.</p>
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
<p>The routing domain identifier for the VM network adapter. This identifier is  a GUID.</p>
</dd>

### -field <b>RoutingDomainName</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/dn383678">NDIS_ISOLATION_NAME</a> structure that contains the routing domain name for the VM network adapter.</p>
</dd>

### -field <b>NumIsolationEntries</b>

<dd>
<p>A <b>ULONG</b> value that specifies the number of <a href="https://msdn.microsoft.com/library/windows/hardware/dn383684">NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY</a> structures in the array that follows the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a> structure.</p>
</dd>

### -field <b>FirstIsolationEntryOffset</b>

<dd>
<p>A <b>ULONG</b> value that specifies the offset, in bytes, to the first <b>NDIS_ROUTING_DOMAIN_ENTRY</b> element in the array that follows the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a> structure in the buffer that the <b>InformationBuffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure points to. The offset is measured from the start of the <b>NDIS_ROUTING_DOMAIN_ENTRY</b> structure to the beginning of the first element of the array.</p>
<div class="alert"><b>Note</b>  If the value of <b>NumRoutingDomainEntries</b> is zero, this member is ignored.</div>
<div> </div>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383683">NDIS_ROUTING_DOMAIN_ENTRY_GET_NEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383684">NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383690">OID_GEN_ISOLATION_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_ROUTING_DOMAIN_ENTRY structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
