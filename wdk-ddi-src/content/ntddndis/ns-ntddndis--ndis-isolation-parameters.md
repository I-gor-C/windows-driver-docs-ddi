---
UID: NS.ntddndis._NDIS_ISOLATION_PARAMETERS
title: NDIS_ISOLATION_PARAMETERS
author: windows-driver-content
description: The NDIS_ISOLATION_PARAMETERS structure is used by the OID_GEN_ISOLATION_PARAMETERS OID to return the isolation parameters that are set on a VM network adapter's port.
old-location: netvista\ndis_isolation_parameters.htm
old-project: netvista
ms.assetid: 71A01647-3415-4F76-A67C-D1022C8A11D9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_ISOLATION_PARAMETERS, NDIS_ISOLATION_PARAMETERS, *PNDIS_ISOLATION_PARAMETERS
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
req.alt-api: NDIS_ISOLATION_PARAMETERS
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

# NDIS_ISOLATION_PARAMETERS structure



## -description
<p>The <b>NDIS_ISOLATION_PARAMETERS</b> structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383690">OID_GEN_ISOLATION_PARAMETERS</a> OID to return the isolation parameters that are set on a VM network adapter's port.</p>


## -syntax

````
typedef struct _NDIS_ISOLATION_PARAMETERS {
  NDIS_OBJECT_HEADER  Header;
  ULONG               Flags;
  NDIS_ISOLATION_MODE IsolationMode;
  BOOLEAN             AllowUntaggedTraffic;
  ULONG               NumRoutingDomainEntries;
  ULONG               FirstRoutingDomainEntryOffset;
} NDIS_ISOLATION_PARAMETERS, *PNDIS_ISOLATION_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The type, revision, and size of the <b>NDIS_ISOLATION_PARAMETERS</b>  structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to <b>NDIS_OBJECT_TYPE_DEFAULT</b>. To specify the version of the <b>NDIS_ISOLATION_PARAMETERS</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value: </p>
<p></p>
<dl>

### -field NDIS_ISOLATION_PARAMETERS_REVISION_1

<dd>
<p>Original version for NDIS 6.40 and later.</p>
<p>Set the <b>Size</b> member to <b>NDIS_SIZEOF_NDIS_ISOLATION_PARAMETERS_REVISION_1</b>.</p>
</dd>
</dl>
</dd>

### -field Flags

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.

</p>
</dd>

### -field IsolationMode

<dd>
<p>An <a href="..\ntddndis\ne-ntddndis--ndis-isolation-mode.md">NDIS_ISOLATION_MODE</a> enumeration value that specifies the isolation mode.</p>
</dd>

### -field AllowUntaggedTraffic

<dd>
<p>Specifies whether the VM network adapter's port is allowed to send or receive untagged packets. If untagged packets are allowed, the VM network adapter miniport driver tags untagged packets with the default isolation ID. Otherwise, the miniport driver drops them.</p>
</dd>

### -field NumRoutingDomainEntries

<dd>
<p>A <b>ULONG</b> value that specifies the number of <a href="..\ntddndis\ns-ntddndis--ndis-routing-domain-entry.md">NDIS_ROUTING_DOMAIN_ENTRY</a> in the array that follows the <b>NDIS_ISOLATION_PARAMETERS</b> structure.</p>
</dd>

### -field FirstRoutingDomainEntryOffset

<dd>
<p>A <b>ULONG</b> value that specifies the offset, in bytes, to the first <a href="..\ntddndis\ns-ntddndis--ndis-routing-domain-entry.md">NDIS_ROUTING_DOMAIN_ENTRY</a> element in the array that follows the <b>NDIS_ISOLATION_PARAMETERS</b> structure. The offset is measured from the start of the <b>NDIS_ISOLATION_PARAMETERS</b> structure to the beginning of the first element of the array.</p>
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
<a href="..\ntddndis\ne-ntddndis--ndis-isolation-mode.md">NDIS_ISOLATION_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383680">NDIS_ISOLATION_PARAMETERS_GET_FIRST_ROUTING_DOMAIN_ENTRY</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-routing-domain-entry.md">NDIS_ROUTING_DOMAIN_ENTRY</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-switch-port-property-isolation.md">NDIS_SWITCH_PORT_PROPERTY_ISOLATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn383690">OID_GEN_ISOLATION_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_ISOLATION_PARAMETERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
