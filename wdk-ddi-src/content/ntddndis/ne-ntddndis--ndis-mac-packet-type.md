---
UID: NE.ntddndis._NDIS_MAC_PACKET_TYPE
title: NDIS_MAC_PACKET_TYPE
author: windows-driver-content
description: The NDIS_MAC_PACKET_TYPE enumeration identifies the type of a destination address field in a media access control (MAC) header to be filtered.
old-location: netvista\ndis_mac_packet_type.htm
old-project: netvista
ms.assetid: 3cfa8fa4-fab0-4f94-abc1-5c7900af208b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_MAC_PACKET_TYPE
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

# NDIS_MAC_PACKET_TYPE enumeration



## -description
<p>The <b>NDIS_MAC_PACKET_TYPE</b> enumeration identifies the type of a destination address field in a media access control (MAC) header to be filtered.</p>


## -syntax

````
typedef enum _NDIS_MAC_PACKET_TYPE { 
  NdisMacPacketTypeUndefined  = 0,
  NdisMacPacketTypeUnicast    = 1,
  NdisMacPacketTypeMulticast  = 2,
  NdisMacPacketTypeBroadcast  = 3,
  NdisMacPacketTypeMaximum    = 4
} NDIS_MAC_PACKET_TYPE, *PNDIS_MAC_PACKET_TYPE;
````


## -enum-fields
<dl>

### -field <a id="NdisMacPacketTypeUndefined"></a><a id="ndismacpackettypeundefined"></a><a id="NDISMACPACKETTYPEUNDEFINED"></a><b>NdisMacPacketTypeUndefined</b>

<dd>
<p>An undefined MAC packet type.</p>
</dd>

### -field <a id="NdisMacPacketTypeUnicast"></a><a id="ndismacpackettypeunicast"></a><a id="NDISMACPACKETTYPEUNICAST"></a><b>NdisMacPacketTypeUnicast</b>

<dd>
<p>A unicast MAC packet type.</p>
</dd>

### -field <a id="NdisMacPacketTypeMulticast"></a><a id="ndismacpackettypemulticast"></a><a id="NDISMACPACKETTYPEMULTICAST"></a><b>NdisMacPacketTypeMulticast</b>

<dd>
<p>A multicast MAC packet type.</p>
</dd>

### -field <a id="NdisMacPacketTypeBroadcast"></a><a id="ndismacpackettypebroadcast"></a><a id="NDISMACPACKETTYPEBROADCAST"></a><b>NdisMacPacketTypeBroadcast</b>

<dd>
<p>A broadcast MAC packet type.</p>
</dd>

### -field <a id="NdisMacPacketTypeMaximum"></a><a id="ndismacpackettypemaximum"></a><a id="NDISMACPACKETTYPEMAXIMUM"></a><b>NdisMacPacketTypeMaximum</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_MAC_PACKET_TYPE</b> enumeration is used in the 
    <a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-field-parameters.md">
    NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</a> structure.</p>

<p>The <b>NDIS_MAC_PACKET_TYPE</b> enumeration is used in the 
    <a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-field-parameters.md">
    NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</a> structure.</p>

<p>The <b>NDIS_MAC_PACKET_TYPE</b> enumeration is used in the 
    <a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-field-parameters.md">
    NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</a> structure.</p>

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
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-field-parameters.md">
   NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MAC_PACKET_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
