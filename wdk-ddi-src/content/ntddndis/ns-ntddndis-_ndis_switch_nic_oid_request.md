---
UID: NS.NTDDNDIS._NDIS_SWITCH_NIC_OID_REQUEST
title: _NDIS_SWITCH_NIC_OID_REQUEST
author: windows-driver-content
description: The NDIS_SWITCH_NIC_OID_REQUEST structure specifies the information that is required to forward or originate OID requests.
old-location: netvista\ndis_switch_nic_oid_request.htm
old-project: netvista
ms.assetid: 0a097769-0c74-4465-b339-13696b4dbb6b
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _NDIS_SWITCH_NIC_OID_REQUEST, *PNDIS_SWITCH_NIC_OID_REQUEST, NDIS_SWITCH_NIC_OID_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_NIC_OID_REQUEST
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
---

# _NDIS_SWITCH_NIC_OID_REQUEST structure



## -description
The <b>NDIS_SWITCH_NIC_OID_REQUEST</b> structure specifies the information that is required to forward or originate OID requests.


## -syntax

````
typedef struct _NDIS_SWITCH_NIC_OID_REQUEST {
  NDIS_OBJECT_HEADER    Header;
  ULONG                 Flags;
  NDIS_SWITCH_PORT_ID   SourcePortId;
  NDIS_SWITCH_NIC_INDEX SourceNicIndex;
  NDIS_SWITCH_PORT_ID   DestinationPortId;
  NDIS_SWITCH_NIC_INDEX DestinationNicIndex;
  PNDIS_OID_REQUEST     OidRequest;
} NDIS_SWITCH_NIC_OID_REQUEST, *PNDIS_SWITCH_NIC_OID_REQUEST;
````


## -struct-fields

### -field Header

The type, revision, and size of the <b>NDIS_SWITCH_NIC_OID_REQUEST</b> structure. This member is formatted as an <a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a> structure.
The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_NIC_OID_REQUEST</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value: 


### -field NDIS_SWITCH_NIC_OID_REQUEST_REVISION_1

Original version for NDIS 6.30 and later.
Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_SWITCH_NIC_OID_REQUEST_REVISION_1.
</dd>
</dl>

### -field Flags

A ULONG value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.



### -field SourcePortId

An NDIS_SWITCH_PORT_ID value that contains the unique identifier of the Hyper-V extensible switch port to which the OID request was originally issued.



### -field SourceNicIndex

An NDIS_SWITCH_NIC_INDEX value that specifies the index of the source network adapter that is connected to the source extensible switch port specified by the <b>SourcePortId</b> member.

### -field DestinationPortId

An NDIS_SWITCH_PORT_ID value that contains the unique identifier of the extensible switch port to which the OID request is to be forwarded.



### -field DestinationNicIndex

An NDIS_SWITCH_NIC_INDEX value that specifies the index of the destination network adapter that is connected to the  extensible switch port specified by the <b>DestinationPortId</b> member.

### -field OidRequest

A pointer to an <a href="netvista.ndis_oid_request">NDIS_OID_REQUEST</a> structure. This structure contains the data for the OID request that will be forwarded to the miniport driver of the network adapter specified by the <b>DestinationPortId</b> and <b>DestinationNicIndex</b> members.

## -remarks
The <b>NDIS_SWITCH_NIC_OID_REQUEST</b> structure is used in OID method requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598266">OID_SWITCH_NIC_REQUEST</a>.

A extension can forward or originate OID requests to underlying physical network adapters in the extensible switch driver stack. This enables an extension to do the following:

Manage the configuration of hardware offloads on an underlying physical adapter for the following offload technologies:

Internet Protocol security (IPsec).

Virtualized machine queue (VMQ).

Single root I/O virtualization (SR-IOV).

Query the configuration of an underlying physical network adapter by issuing standard NDIS OIDs. For example, the extension can issue an OID query request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569069">OID_802_3_CURRENT_ADDRESS</a> to obtain the adapter's current media access control (MAC) address.

For guidelines on how to issue OID requests to underlying physical adapters, see <a href="netvista.managing_oid_requests_to_physical_network_adapters">Managing OID Requests to Physical Network Adapters</a>.

## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported in NDIS 6.30 and later.
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.ndis_oid_request">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598266">OID_SWITCH_NIC_REQUEST</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_NIC_OID_REQUEST structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>