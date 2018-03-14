---
UID: NE:ntddndis._NDIS_MAC_HEADER_FIELD
title: "_NDIS_MAC_HEADER_FIELD"
author: windows-driver-content
description: The NDIS_MAC_HEADER_FIELD enumeration identifies the type of a field in a media access control (MAC) header to be filtered.
old-location: netvista\ndis_mac_header_field.htm
old-project: netvista
ms.assetid: 31db285c-a7e7-4ba5-ba07-a60cfcfa9af9
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PNDIS_MAC_HEADER_FIELD, NDIS_MAC_HEADER_FIELD, NDIS_MAC_HEADER_FIELD enumeration [Network Drivers Starting with Windows Vista], NdisMacHeaderFieldDestinationAddress, NdisMacHeaderFieldMaximum, NdisMacHeaderFieldPacketType, NdisMacHeaderFieldPriority, NdisMacHeaderFieldProtocol, NdisMacHeaderFieldSourceAddress, NdisMacHeaderFieldUndefined, NdisMacHeaderFieldVlanId, PNDIS_MAC_HEADER_FIELD, PNDIS_MAC_HEADER_FIELD enumeration pointer [Network Drivers Starting with Windows Vista], _NDIS_MAC_HEADER_FIELD, netvista.ndis_mac_header_field, ntddndis/NDIS_MAC_HEADER_FIELD, ntddndis/NdisMacHeaderFieldDestinationAddress, ntddndis/NdisMacHeaderFieldMaximum, ntddndis/NdisMacHeaderFieldPacketType, ntddndis/NdisMacHeaderFieldPriority, ntddndis/NdisMacHeaderFieldProtocol, ntddndis/NdisMacHeaderFieldSourceAddress, ntddndis/NdisMacHeaderFieldUndefined, ntddndis/NdisMacHeaderFieldVlanId, ntddndis/PNDIS_MAC_HEADER_FIELD, virtual_machine_queue_ref_e521f802-ada1-444a-bf43-63405f40e45a.xml"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddndis.h
api_name:
-	NDIS_MAC_HEADER_FIELD
product: Windows
targetos: Windows
req.typenames: NDIS_MAC_HEADER_FIELD, *PNDIS_MAC_HEADER_FIELD
---

# _NDIS_MAC_HEADER_FIELD Enumeration
The <b>NDIS_MAC_HEADER_FIELD</b> enumeration identifies the type of a field in a media access control (MAC) header to be filtered.

## Syntax
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

## Constants

<table>
            
                <tr>
                    <td>NdisMacHeaderFieldDestinationAddress</td>
                    <td>A destination address field.</td>
                </tr>
            
                <tr>
                    <td>NdisMacHeaderFieldMaximum</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
                </tr>
            
                <tr>
                    <td>NdisMacHeaderFieldPacketType</td>
                    <td>A packet type field in the IEEE 802.2 subnetwork access protocol (SNAP) header of an 802.3

MAC header.</td>
                </tr>
            
                <tr>
                    <td>NdisMacHeaderFieldPriority</td>
                    <td>A VLAN priority field.</td>
                </tr>
            
                <tr>
                    <td>NdisMacHeaderFieldProtocol</td>
                    <td>A protocol field in the DEC/Intel/Xerox (DIX) Ethernet

MAC header.</td>
                </tr>
            
                <tr>
                    <td>NdisMacHeaderFieldSourceAddress</td>
                    <td>A source address field.</td>
                </tr>
            
                <tr>
                    <td>NdisMacHeaderFieldUndefined</td>
                    <td>An undefined MAC header field.</td>
                </tr>
            
                <tr>
                    <td>NdisMacHeaderFieldVlanId</td>
                    <td>A virtual local area network (VLAN) identifier field.</td>
                </tr>
</table>

## Remarks

The NDIS_MAC_HEADER_FIELD enumeration is used in the 
    <a href="..\ntddndis\ns-ntddndis-_ndis_receive_filter_field_parameters.md">
    NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.20 and later. Supported in NDIS 6.20 and later. |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="..\ntddndis\ns-ntddndis-_ndis_receive_filter_field_parameters.md">
   NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MAC_HEADER_FIELD enumeration%20 RELEASE:%20(2/27/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>