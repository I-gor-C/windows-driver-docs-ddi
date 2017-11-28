---
UID: NE.ntddndis._NDIS_PM_PROTOCOL_OFFLOAD_TYPE
title: NDIS_PM_PROTOCOL_OFFLOAD_TYPE
author: windows-driver-content
description: The NDIS_PM_PROTOCOL_OFFLOAD_TYPE enumeration identifies the type of a protocol offload for NDIS network adapter power management.
old-location: netvista\ndis_pm_protocol_offload_type.htm
old-project: netvista
ms.assetid: ab9f98d3-1792-43be-b838-f9dd3953889c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ntddndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PM_PROTOCOL_OFFLOAD_TYPE
req.alt-loc: ntddndis.h
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

# NDIS_PM_PROTOCOL_OFFLOAD_TYPE enumeration



## -description
<p>The <b>NDIS_PM_PROTOCOL_OFFLOAD_TYPE</b> enumeration identifies the type of a protocol offload for NDIS
  network adapter power management.</p>


## -syntax

````
typedef enum _NDIS_PM_PROTOCOL_OFFLOAD_TYPE { 
  NdisPMProtocolOffloadIdUnspecified,
  NdisPMProtocolOffloadIdIPv4ARP,
  NdisPMProtocolOffloadIdIPv6NS,
  NdisPMProtocolOffload80211RSNRekey,
  NdisPMProtocolOffloadIdMaximum
} NDIS_PM_PROTOCOL_OFFLOAD_TYPE, *PNDIS_PM_PROTOCOL_OFFLOAD_TYPE;
````


## -enum-fields
<dl>

### -field <a id="NdisPMProtocolOffloadIdUnspecified"></a><a id="ndispmprotocoloffloadidunspecified"></a><a id="NDISPMPROTOCOLOFFLOADIDUNSPECIFIED"></a><b>NdisPMProtocolOffloadIdUnspecified</b>

<dd>
<p>The offloaded protocol is not specified.</p>
</dd>

### -field <a id="NdisPMProtocolOffloadIdIPv4ARP"></a><a id="ndispmprotocoloffloadidipv4arp"></a><a id="NDISPMPROTOCOLOFFLOADIDIPV4ARP"></a><b>NdisPMProtocolOffloadIdIPv4ARP</b>

<dd>
<p>An IPv4 ARP protocol offload. The parameters for this protocol offload type are specified in the 
     <b>IPv4ARPParameters</b> member of the 
     <a href="..\ntddndis\ns-ntddndis--ndis-pm-protocol-offload.md">
     NDIS_PM_PROTOCOL_OFFLOAD</a> structure.</p>
</dd>

### -field <a id="NdisPMProtocolOffloadIdIPv6NS"></a><a id="ndispmprotocoloffloadidipv6ns"></a><a id="NDISPMPROTOCOLOFFLOADIDIPV6NS"></a><b>NdisPMProtocolOffloadIdIPv6NS</b>

<dd>
<p>An IPv6 Neighbor Solicitation (NS) protocol offload. The parameters for this protocol offload type
     are specified in the 
     <b>IPv6NSParameters</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566760">NDIS_PM_PROTOCOL_OFFLOAD</a> structure.</p>
</dd>

### -field <a id="NdisPMProtocolOffload80211RSNRekey"></a><a id="ndispmprotocoloffload80211rsnrekey"></a><a id="NDISPMPROTOCOLOFFLOAD80211RSNREKEY"></a><b>NdisPMProtocolOffload80211RSNRekey</b>

<dd>
<p>An IEEE 802.11i Robust Security Network (RSN) 4-way and 2-way handshake protocol offload. This
     protocol offload type is specified in the 
     <b>Dot11RSNRekeyParameters</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566760">NDIS_PM_PROTOCOL_OFFLOAD</a> structure.</p>
</dd>

### -field <a id="NdisPMProtocolOffloadIdMaximum"></a><a id="ndispmprotocoloffloadidmaximum"></a><a id="NDISPMPROTOCOLOFFLOADIDMAXIMUM"></a><b>NdisPMProtocolOffloadIdMaximum</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_PM_PROTOCOL_OFFLOAD_TYPE</b> enumeration is used in the 
    <b>ProtocolOffloadType</b> member of the 
    <a href="..\ntddndis\ns-ntddndis--ndis-pm-protocol-offload.md">
    NDIS_PM_PROTOCOL_OFFLOAD</a> structure.</p>

<p>The <b>NDIS_PM_PROTOCOL_OFFLOAD_TYPE</b> enumeration is used in the 
    <b>ProtocolOffloadType</b> member of the 
    <a href="..\ntddndis\ns-ntddndis--ndis-pm-protocol-offload.md">
    NDIS_PM_PROTOCOL_OFFLOAD</a> structure.</p>

<p>The <b>NDIS_PM_PROTOCOL_OFFLOAD_TYPE</b> enumeration is used in the 
    <b>ProtocolOffloadType</b> member of the 
    <a href="..\ntddndis\ns-ntddndis--ndis-pm-protocol-offload.md">
    NDIS_PM_PROTOCOL_OFFLOAD</a> structure.</p>

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
<dt>Ntddndis.h (include Ntddndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566760">NDIS_PM_PROTOCOL_OFFLOAD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PM_PROTOCOL_OFFLOAD_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
