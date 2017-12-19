---
UID: NE.ntddndis._NDIS_RECEIVE_FILTER_TYPE
title: _NDIS_RECEIVE_FILTER_TYPE
author: windows-driver-content
description: The NDIS_RECEIVE_FILTER_TYPE enumeration identifies the receive filter types that the miniport driver supports.
old-location: netvista\ndis_receive_filter_type.htm
old-project: NetVista
ms.assetid: 2810be51-4b38-4462-9c16-67a9f28da5c9
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _NDIS_RECEIVE_FILTER_TYPE, PNDIS_RECEIVE_FILTER_TYPE, NDIS_RECEIVE_FILTER_TYPE, *PNDIS_RECEIVE_FILTER_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_RECEIVE_FILTER_TYPE
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

# _NDIS_RECEIVE_FILTER_TYPE enumeration



## -description
The <b>NDIS_RECEIVE_FILTER_TYPE</b> enumeration identifies the receive filter types that the miniport driver
  supports.



## -syntax

````
typedef enum _NDIS_RECEIVE_FILTER_TYPE { 
  NdisReceiveFilterTypeUndefined,
  NdisReceiveFilterTypeVMQueue,
  NdisReceiveFilterTypePacketCoalescing,
  NdisReceiveFilterTypeMaximum
} NDIS_RECEIVE_FILTER_TYPE, *PNDIS_RECEIVE_FILTER_TYPE;
````


## -enum-fields

### -field NdisReceiveFilterTypeUndefined

An undefined filter.


### -field NdisReceiveFilterTypeVMQueue

A filter for a virtual machine (VM) receive queue. This receive queue has been allocated by the miniport driver that supports the virtual machine queue (VMQ) or single root I/O virtualization (SR-IOV) interface.


### -field NdisReceiveFilterTypePacketCoalescing

A packet coalescing filter.


### -field NdisReceiveFilterTypeMaximum

The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.


## -remarks
The NDIS_RECEIVE_FILTER_TYPE enumeration is used in the 
    <a href="netvista.ndis_receive_filter_parameters">
    NDIS_RECEIVE_FILTER_PARAMETERS</a> structure.

For more information about VMQ, see <a href="netvista.virtual_machine_queue__vmq_">Virtual Machine Queue (VMQ)</a>.

For more information about SR-IOV, see <a href="netvista.single_root_i_o_virtualization__sr-iov_">Single Root I/O Virtualization (SR-IOV)</a>.

For more information about packet coalescing, see <a href="netvista.ndis_packet_coalescing">NDIS Packet Coalescing</a>.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.20 and later.

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
<dt>
<a href="netvista.ndis_receive_filter_parameters">
   NDIS_RECEIVE_FILTER_PARAMETERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NDIS_RECEIVE_FILTER_TYPE enumeration%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

