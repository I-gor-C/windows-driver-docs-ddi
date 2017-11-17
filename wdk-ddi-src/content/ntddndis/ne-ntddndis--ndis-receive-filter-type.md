---
UID: NE.ntddndis._NDIS_RECEIVE_FILTER_TYPE
title: NDIS_RECEIVE_FILTER_TYPE
author: windows-driver-content
description: The NDIS_RECEIVE_FILTER_TYPE enumeration identifies the receive filter types that the miniport driver supports.
old-location: netvista\ndis_receive_filter_type.htm
ms.assetid: 2810be51-4b38-4462-9c16-67a9f28da5c9
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
req.iface: 
---

# NDIS_RECEIVE_FILTER_TYPE enumeration



## -description
<p>The <b>NDIS_RECEIVE_FILTER_TYPE</b> enumeration identifies the receive filter types that the miniport driver
  supports.</p>


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
<dl>

### -field <a id="NdisReceiveFilterTypeUndefined"></a><a id="ndisreceivefiltertypeundefined"></a><a id="NDISRECEIVEFILTERTYPEUNDEFINED"></a><b>NdisReceiveFilterTypeUndefined</b>

<dd>
<p>An undefined filter.</p>
</dd>

### -field <a id="NdisReceiveFilterTypeVMQueue"></a><a id="ndisreceivefiltertypevmqueue"></a><a id="NDISRECEIVEFILTERTYPEVMQUEUE"></a><b>NdisReceiveFilterTypeVMQueue</b>

<dd>
<p>A filter for a virtual machine (VM) receive queue. This receive queue has been allocated by the miniport driver that supports the virtual machine queue (VMQ) or single root I/O virtualization (SR-IOV) interface.</p>
</dd>

### -field <a id="NdisReceiveFilterTypePacketCoalescing"></a><a id="ndisreceivefiltertypepacketcoalescing"></a><a id="NDISRECEIVEFILTERTYPEPACKETCOALESCING"></a><b>NdisReceiveFilterTypePacketCoalescing</b>

<dd>
<p>A packet coalescing filter.</p>
</dd>

### -field <a id="NdisReceiveFilterTypeMaximum"></a><a id="ndisreceivefiltertypemaximum"></a><a id="NDISRECEIVEFILTERTYPEMAXIMUM"></a><b>NdisReceiveFilterTypeMaximum</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</p>
</dd>
</dl>

## -remarks
<p>The NDIS_RECEIVE_FILTER_TYPE enumeration is used in the 
    <a href="https://msdn.microsoft.com/39dc6b3a-f24d-4f1a-96f8-416fbcb3f894">
    NDIS_RECEIVE_FILTER_PARAMETERS</a> structure.</p>

<p>For more information about VMQ, see <a href="NULL">Virtual Machine Queue (VMQ)</a>.</p>

<p>For more information about SR-IOV, see <a href="NULL">Single Root I/O Virtualization (SR-IOV)</a>.</p>

<p>For more information about packet coalescing, see <a href="NULL">NDIS Packet Coalescing</a>.</p>

<p>The NDIS_RECEIVE_FILTER_TYPE enumeration is used in the 
    <a href="https://msdn.microsoft.com/39dc6b3a-f24d-4f1a-96f8-416fbcb3f894">
    NDIS_RECEIVE_FILTER_PARAMETERS</a> structure.</p>

<p>For more information about VMQ, see <a href="NULL">Virtual Machine Queue (VMQ)</a>.</p>

<p>For more information about SR-IOV, see <a href="NULL">Single Root I/O Virtualization (SR-IOV)</a>.</p>

<p>For more information about packet coalescing, see <a href="NULL">NDIS Packet Coalescing</a>.</p>

<p>The NDIS_RECEIVE_FILTER_TYPE enumeration is used in the 
    <a href="https://msdn.microsoft.com/39dc6b3a-f24d-4f1a-96f8-416fbcb3f894">
    NDIS_RECEIVE_FILTER_PARAMETERS</a> structure.</p>

<p>For more information about VMQ, see <a href="NULL">Virtual Machine Queue (VMQ)</a>.</p>

<p>For more information about SR-IOV, see <a href="NULL">Single Root I/O Virtualization (SR-IOV)</a>.</p>

<p>For more information about packet coalescing, see <a href="NULL">NDIS Packet Coalescing</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.20 and later.</p>
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
<a href="https://msdn.microsoft.com/39dc6b3a-f24d-4f1a-96f8-416fbcb3f894">
   NDIS_RECEIVE_FILTER_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_FILTER_TYPE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
