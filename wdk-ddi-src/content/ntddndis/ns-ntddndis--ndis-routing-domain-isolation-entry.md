---
UID: NS.ntddndis._NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY
title: NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY
author: windows-driver-content
description: The NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY structure is used by the OID_GEN_ISOLATION_PARAMETERS OID to return information relating to a single isolation ID within a routing domain entry for a Hyper-V extensible switch network adapter's port.
old-location: netvista\ndis_routing_domain_isolation_entry.htm
old-project: netvista
ms.assetid: 4297097D-4796-4714-B51C-3F477ABAF1E6
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY, NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY, *PNDIS_ROUTING_DOMAIN_ISOLATION_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.40 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY
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
req.iface: 
---

# NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY structure



## -description
<p>The <b>NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY</b> structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383690">OID_GEN_ISOLATION_PARAMETERS</a> OID to return information relating to a single isolation ID within a routing domain entry for a Hyper-V extensible switch network adapter's port.</p>


## -syntax

````
typedef struct _NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY {
  NDIS_OBJECT_HEADER     Header;
  ULONG                  Flags;
  NDIS_ISOLATION_ID_NAME IsolationIdName;
  union {
    struct {
      UINT32 VirtualSubnetId  :24;
    };
    struct {
      UINT32 VlanId  :24;
    };
    UINT32 IsolationId;
  };
} NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY, *PNDIS_ROUTING_DOMAIN_ISOLATION_ENTRY;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY</b>  structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to <b>NDIS_OBJECT_TYPE_DEFAULT</b>. To specify the version of the <b>NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY_REVISION_1"></a><a id="ndis_routing_domain_isolation_entry_revision_1"></a>NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY_REVISION_1

<dd>
<p>Original version for NDIS 6.40 and later.</p>
<p>Set the <b>Size</b> member to <b>NDIS_SIZEOF_NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY_REVISION_1</b>.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.

</p>
</dd>

### -field <b>IsolationIdName</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/dn383678">NDIS_ISOLATION_NAME</a> structure that contains the isolation ID name for the Hyper-V extensible switch network adapter.</p>
</dd>

### -field ( <i>unnamed union</i> )

<dd>
<p>The default virtual switch port ID or virtual local area network (VLAN) ID that will be set on all sent or received packets if untagged packets are allowed. (See the <b>AllowUntaggedTraffic</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a> structure.)</p>
<dl>

### -field <b>VirtualSubnetId</b>

<dd>
<p>The virtual switch port ID.</p>
</dd>

### -field <b>VlanId</b>

<dd>
<p>The virtual local area network (VLAN) ID.</p>
</dd>

### -field <b>IsolationId</b>

<dd>
<p>The default isolation ID that will be set on all sent or received packets if untagged packets are allowed. (See the <b>AllowUntaggedTraffic</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a> structure.)</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383685">NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY_GET_NEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383690">OID_GEN_ISOLATION_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
