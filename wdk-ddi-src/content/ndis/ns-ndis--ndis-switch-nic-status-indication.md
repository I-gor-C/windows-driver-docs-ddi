---
UID: NS.ndis._NDIS_SWITCH_NIC_STATUS_INDICATION
title: NDIS_SWITCH_NIC_STATUS_INDICATION
author: windows-driver-content
description: The NDIS_SWITCH_NIC_STATUS_INDICATION structure specifies the information that is required to forward or originate an NDIS status indication from an underlying physical network adapter.
old-location: netvista\ndis_switch_nic_status_indication.htm
old-project: netvista
ms.assetid: a3841a14-0876-47f4-a4dc-6231b76086ca
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_SWITCH_NIC_STATUS_INDICATION, NDIS_SWITCH_NIC_STATUS_INDICATION, *PNDIS_SWITCH_NIC_STATUS_INDICATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_NIC_STATUS_INDICATION
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NDIS_SWITCH_NIC_STATUS_INDICATION structure



## -description
<p>The <b>NDIS_SWITCH_NIC_STATUS_INDICATION</b> structure specifies the information that is required to forward or originate an NDIS status indication from an underlying physical network adapter.</p>


## -syntax

````
typedef struct _NDIS_SWITCH_NIC_STATUS_INDICATION {
  NDIS_OBJECT_HEADER      Header;
  ULONG                   Flags;
  NDIS_SWITCH_PORT_ID     SourcePortId;
  NDIS_SWITCH_NIC_INDEX   SourceNicIndex;
  NDIS_SWITCH_PORT_ID     DestinationPortId;
  NDIS_SWITCH_NIC_INDEX   DestinationNicIndex;
  PNDIS_STATUS_INDICATION *StatusIndication;
} NDIS_SWITCH_NIC_STATUS_INDICATION, *PNDIS_SWITCH_NIC_STATUS_INDICATION;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_SWITCH_NIC_STATUS_INDICATION</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_NIC_STATUS_INDICATION</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_SWITCH_NIC_STATUS_INDICATION_REVISION_1"></a><a id="ndis_switch_nic_status_indication_revision_1"></a>NDIS_SWITCH_NIC_STATUS_INDICATION_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_SWITCH_NIC_STATUS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.

</p>
</dd>

### -field <b>SourcePortId</b>

<dd>
<p>An NDIS_SWITCH_PORT_ID value that contains the unique identifier of the Hyper-V extensible switch port from which the NDIS status indication was originally generated.

</p>
</dd>

### -field <b>SourceNicIndex</b>

<dd>
<p>An NDIS_SWITCH_NIC_INDEX value that specifies the index of the source network adapter that is connected to the source extensible switch port. This port is specified by the <b>SourcePortId</b> member. 

</p>
</dd>

### -field <b>DestinationPortId</b>

<dd>
<p>An NDIS_SWITCH_PORT_ID value that contains the unique identifier of the extensible switch port to which the NDIS status indication is to be forwarded.

</p>
</dd>

### -field <b>DestinationNicIndex</b>

<dd>
<p>An NDIS_SWITCH_NIC_INDEX value that specifies the index of the destination network adapter that is connected to the  extensible switch port specified by the <b>DestinationPortId</b> member. 

</p>
</dd>

### -field <b>StatusIndication</b>

<dd>
<p>A pointer to an <a href="..\ndis\ns-ndis--ndis-status-indication.md">NDIS_STATUS_INDICATION</a> structure. This structure contains the data for the NDIS status indication originally issued by the source network adapter as specified by the <b>SourcePortId</b> and <b>SourceNicIndex</b> members.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_SWITCH_NIC_STATUS_INDICATION</b> structure is used in NDIS status indications of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598205">NDIS_STATUS_SWITCH_NIC_STATUS</a>.</p>

<p>An extension can forward or originate status indications from any underlying physical adapter that is connected to the extensible switch <a href="netvista.external_network_adapters">external network adapter</a>. Typically, the extension issues these status indications in order to change the advertised hardware offload capabilities of the underlying physical adapter. </p>

<p>The extension can forward or originate status notifications for the following types of hardware offloads:</p>

<p>Internet Protocol security (IPsec).</p>

<p>Virtualized machine queue (VMQ).</p>

<p>Single root I/O virtualization (SR-IOV).</p>

<p>For guidelines on how to issue NDIS status indications from underlying physical adapters, see <a href="NULL">Managing NDIS Status Indications from Physical Network Adapters</a>.</p>

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
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-status-indication.md">NDIS_STATUS_INDICATION</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-switch-nic-status-indication.md">NDIS_SWITCH_NIC_STATUS_INDICATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_NIC_STATUS_INDICATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
