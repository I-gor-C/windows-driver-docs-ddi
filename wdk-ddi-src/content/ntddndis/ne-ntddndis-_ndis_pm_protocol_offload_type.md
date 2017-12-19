---
UID: NE.ntddndis._NDIS_PM_PROTOCOL_OFFLOAD_TYPE
title: _NDIS_PM_PROTOCOL_OFFLOAD_TYPE
author: windows-driver-content
description: The NDIS_PM_PROTOCOL_OFFLOAD_TYPE enumeration identifies the type of a protocol offload for NDIS network adapter power management.
old-location: netvista\ndis_pm_protocol_offload_type.htm
old-project: NetVista
ms.assetid: ab9f98d3-1792-43be-b838-f9dd3953889c
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _NDIS_PM_PROTOCOL_OFFLOAD_TYPE, PNDIS_PM_PROTOCOL_OFFLOAD_TYPE, *PNDIS_PM_PROTOCOL_OFFLOAD_TYPE, NDIS_PM_PROTOCOL_OFFLOAD_TYPE
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
---

# _NDIS_PM_PROTOCOL_OFFLOAD_TYPE enumeration



## -description
The <b>NDIS_PM_PROTOCOL_OFFLOAD_TYPE</b> enumeration identifies the type of a protocol offload for NDIS
  network adapter power management.



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

### -field NdisPMProtocolOffloadIdUnspecified

The offloaded protocol is not specified.


### -field NdisPMProtocolOffloadIdIPv4ARP

An IPv4 ARP protocol offload. The parameters for this protocol offload type are specified in the 
     <b>IPv4ARPParameters</b> member of the 
     <a href="netvista.ndis_pm_protocol_offload">
     NDIS_PM_PROTOCOL_OFFLOAD</a> structure.


### -field NdisPMProtocolOffloadIdIPv6NS

An IPv6 Neighbor Solicitation (NS) protocol offload. The parameters for this protocol offload type
     are specified in the 
     <b>IPv6NSParameters</b> member of the <a href="netvista.ndis_pm_protocol_offload">NDIS_PM_PROTOCOL_OFFLOAD</a> structure.


### -field NdisPMProtocolOffload80211RSNRekey

An IEEE 802.11i Robust Security Network (RSN) 4-way and 2-way handshake protocol offload. This
     protocol offload type is specified in the 
     <b>Dot11RSNRekeyParameters</b> member of the <a href="netvista.ndis_pm_protocol_offload">NDIS_PM_PROTOCOL_OFFLOAD</a> structure.


### -field NdisPMProtocolOffloadIdMaximum

The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.


## -remarks
The <b>NDIS_PM_PROTOCOL_OFFLOAD_TYPE</b> enumeration is used in the 
    <b>ProtocolOffloadType</b> member of the 
    <a href="netvista.ndis_pm_protocol_offload">
    NDIS_PM_PROTOCOL_OFFLOAD</a> structure.


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
<dt>Ntddndis.h (include Ntddndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndis_pm_protocol_offload">NDIS_PM_PROTOCOL_OFFLOAD</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NDIS_PM_PROTOCOL_OFFLOAD_TYPE enumeration%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

