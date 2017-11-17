---
UID: NS.ntddndis._NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS
title: NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS
author: windows-driver-content
description: The NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS structure specifies the information about a virtual port (VPort) that will be deleted from a network adapter switch on the network adapter.
old-location: netvista\ndis_nic_switch_delete_vport_parameters.htm
ms.assetid: 7cbdaa08-51c9-495d-a5c7-bb2c4009d7a4
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS
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
ms.keywords: NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS, NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS, *PNDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS
req.iface: 
---

# NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS structure



## -description
<p>The <b>NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS</b> structure specifies the information about a virtual port (VPort) that will be deleted from a network adapter switch on the network adapter. </p>


## -syntax

````
typedef struct _NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS {
  NDIS_OBJECT_HEADER       Header;
  ULONG                    Flags;
  NDIS_NIC_SWITCH_VPORT_ID VPortId;
} NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS, *PNDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS_REVISION_1"></a><a id="ndis_nic_switch_delete_vport_parameters_revision_1"></a>NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS_REVISION_1

<dd>
<p>Original version for NDIS 6.30.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NIC_SWITCH_DELETE_VPORT_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>VPortId</b>

<dd>
<p>An NDIS_NIC_SWITCH_VPORT_ID value  that uniquely identifies the virtual port (VPort) to be deleted. The VPort with the specified NDIS_NIC_SWITCH_VPORT_ID value must have previously been created through an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>.</p>
<div class="alert"><b>Note</b>  The default VPort that is attached to the PCI Express (PCIe) Physical Function (PF) cannot be deleted. The <b>VPortId</b> member must not be set to  DEFAULT_PORT_NUMBER.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>The NDIS_NIC_SWITCH_DELETE_PORT_PARAMETERS structure is used in OID set requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451818">OID_NIC_SWITCH_DELETE_VPORT</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
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
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451816">OID_NIC_SWITCH_CREATE_VPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451818">OID_NIC_SWITCH_DELETE_VPORT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NIC_SWITCH_DELETE_VPORT_PARAMETERS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
