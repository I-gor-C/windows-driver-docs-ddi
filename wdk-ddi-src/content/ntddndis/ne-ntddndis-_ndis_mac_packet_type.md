---
UID : NE:ntddndis._NDIS_MAC_PACKET_TYPE
title : "_NDIS_MAC_PACKET_TYPE"
author : windows-driver-content
description : The NDIS_MAC_PACKET_TYPE enumeration identifies the type of a destination address field in a media access control (MAC) header to be filtered.
old-location : netvista\ndis_mac_packet_type.htm
old-project : netvista
ms.assetid : 3cfa8fa4-fab0-4f94-abc1-5c7900af208b
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : NDIS_MAC_PACKET_TYPE enumeration [Network Drivers Starting with Windows Vista], NdisMacPacketTypeUndefined, *PNDIS_MAC_PACKET_TYPE, ntddndis/NdisMacPacketTypeMaximum, NdisMacPacketTypeMulticast, PNDIS_MAC_PACKET_TYPE, NDIS_MAC_PACKET_TYPE, ntddndis/NdisMacPacketTypeBroadcast, ntddndis/NdisMacPacketTypeMulticast, NdisMacPacketTypeBroadcast, netvista.ndis_mac_packet_type, NdisMacPacketTypeUnicast, NdisMacPacketTypeMaximum, _NDIS_MAC_PACKET_TYPE, ntddndis/PNDIS_MAC_PACKET_TYPE, ntddndis/NdisMacPacketTypeUnicast, ntddndis/NDIS_MAC_PACKET_TYPE, PNDIS_MAC_PACKET_TYPE enumeration pointer [Network Drivers Starting with Windows Vista], ntddndis/NdisMacPacketTypeUndefined
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.30 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : NDIS_MAC_PACKET_TYPE, *PNDIS_MAC_PACKET_TYPE
---

# _NDIS_MAC_PACKET_TYPE Enumeration
The <b>NDIS_MAC_PACKET_TYPE</b> enumeration identifies the type of a destination address field in a media access control (MAC) header to be filtered.

## Syntax
````
typedef enum _NDIS_MAC_PACKET_TYPE { 
  NdisMacPacketTypeUndefined  = 0,
  NdisMacPacketTypeUnicast    = 1,
  NdisMacPacketTypeMulticast  = 2,
  NdisMacPacketTypeBroadcast  = 3,
  NdisMacPacketTypeMaximum    = 4
} NDIS_MAC_PACKET_TYPE, *PNDIS_MAC_PACKET_TYPE;
````

## Constants

<table>

<tr>
<td>NdisMacPacketTypeBroadcast</td>
<td>A broadcast MAC packet type.</td>
</tr>

<tr>
<td>NdisMacPacketTypeMaximum</td>
<td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
</tr>

<tr>
<td>NdisMacPacketTypeMulticast</td>
<td>A multicast MAC packet type.</td>
</tr>

<tr>
<td>NdisMacPacketTypeUndefined</td>
<td>An undefined MAC packet type.</td>
</tr>

<tr>
<td>NdisMacPacketTypeUnicast</td>
<td>A unicast MAC packet type.</td>
</tr>
</table>

## Remarks

The <b>NDIS_MAC_PACKET_TYPE</b> enumeration is used in the 
    <a href="..\ntddndis\ns-ntddndis-_ndis_receive_filter_field_parameters.md">
    NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.30 and later. Supported in NDIS 6.30 and later. |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="..\ntddndis\ns-ntddndis-_ndis_receive_filter_field_parameters.md">
   NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MAC_PACKET_TYPE enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>