---
UID: NE.ntddndis._NDIS_MAC_HEADER_FIELD
title: NDIS_MAC_HEADER_FIELD
author: windows-driver-content
description: The NDIS_MAC_HEADER_FIELD enumeration identifies the type of a field in a media access control (MAC) header to be filtered.
old-location: netvista\ndis_mac_header_field.htm
old-project: netvista
ms.assetid: 31db285c-a7e7-4ba5-ba07-a60cfcfa9af9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
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
req.alt-api: NDIS_MAC_HEADER_FIELD
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

# NDIS_MAC_HEADER_FIELD enumeration



## -description
<p>The <b>NDIS_MAC_HEADER_FIELD</b> enumeration identifies the type of a field in a media access control (MAC) header to be filtered.</p>


## -syntax

````
typedef enum _NDIS_MAC_HEADER_FIELD { 
  NdisMacHeaderFieldUndefined,
  NdisMacHeaderFieldDestinationAddress,
  NdisMacHeaderFieldSourceAddress,
  NdisMacHeaderFieldProtocol,
  NdisMacHeaderFieldVlanId,
  NdisMacHeaderFieldPriority,
  NdisMacHeaderFieldPacketType,
  NdisMacHeaderFieldMaximum
} NDIS_MAC_HEADER_FIELD, *PNDIS_MAC_HEADER_FIELD;
````


## -enum-fields
<dl>

### -field <a id="NdisMacHeaderFieldUndefined"></a><a id="ndismacheaderfieldundefined"></a><a id="NDISMACHEADERFIELDUNDEFINED"></a><b>NdisMacHeaderFieldUndefined</b>

<dd>
<p>An undefined MAC header field.</p>
</dd>

### -field <a id="NdisMacHeaderFieldDestinationAddress"></a><a id="ndismacheaderfielddestinationaddress"></a><a id="NDISMACHEADERFIELDDESTINATIONADDRESS"></a><b>NdisMacHeaderFieldDestinationAddress</b>

<dd>
<p>A destination address field.</p>
</dd>

### -field <a id="NdisMacHeaderFieldSourceAddress"></a><a id="ndismacheaderfieldsourceaddress"></a><a id="NDISMACHEADERFIELDSOURCEADDRESS"></a><b>NdisMacHeaderFieldSourceAddress</b>

<dd>
<p>A source address field.</p>
</dd>

### -field <a id="NdisMacHeaderFieldProtocol"></a><a id="ndismacheaderfieldprotocol"></a><a id="NDISMACHEADERFIELDPROTOCOL"></a><b>NdisMacHeaderFieldProtocol</b>

<dd>
<p>A protocol field in the DEC/Intel/Xerox (DIX) Ethernet

MAC header.</p>
</dd>

### -field <a id="NdisMacHeaderFieldVlanId"></a><a id="ndismacheaderfieldvlanid"></a><a id="NDISMACHEADERFIELDVLANID"></a><b>NdisMacHeaderFieldVlanId</b>

<dd>
<p>A virtual local area network (VLAN) identifier field.</p>
</dd>

### -field <a id="NdisMacHeaderFieldPriority"></a><a id="ndismacheaderfieldpriority"></a><a id="NDISMACHEADERFIELDPRIORITY"></a><b>NdisMacHeaderFieldPriority</b>

<dd>
<p>A VLAN priority field.</p>
</dd>

### -field <a id="NdisMacHeaderFieldPacketType"></a><a id="ndismacheaderfieldpackettype"></a><a id="NDISMACHEADERFIELDPACKETTYPE"></a><b>NdisMacHeaderFieldPacketType</b>

<dd>
<p>A packet type field in the IEEE 802.2 subnetwork access protocol (SNAP) header of an 802.3

MAC header.</p>
</dd>

### -field <a id="NdisMacHeaderFieldMaximum"></a><a id="ndismacheaderfieldmaximum"></a><a id="NDISMACHEADERFIELDMAXIMUM"></a><b>NdisMacHeaderFieldMaximum</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</p>
</dd>
</dl>

## -remarks
<p>The NDIS_MAC_HEADER_FIELD enumeration is used in the 
    <a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-field-parameters.md">
    NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</a> structure.</p>

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
<a href="..\ntddndis\ns-ntddndis--ndis-receive-filter-field-parameters.md">
   NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MAC_HEADER_FIELD enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
