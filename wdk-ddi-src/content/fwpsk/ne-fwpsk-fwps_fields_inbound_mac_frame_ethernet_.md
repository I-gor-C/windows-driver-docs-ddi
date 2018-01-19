---
UID : NE:fwpsk.FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET_
title : FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET_
author : windows-driver-content
description : The FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET enumeration type specifies the data field identifiers for the FWPS_LAYER_INBOUND_MAC_FRAME_ETHERNET run-time filtering layer.
old-location : netvista\fwps_fields_inbound_mac_frame_802_3.htm
old-project : netvista
ms.assetid : 41313b4e-2f26-42a2-b3ec-d9b8c3041fac
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET_, FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : fwpsk.h
req.include-header : Fwpsk.h
req.target-type : Windows
req.target-min-winverclnt : Windows 7
req.target-min-winversvr : Windows Server 2008 R2
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET
req.alt-loc : fwpsk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= DISPATCH_LEVEL
req.typenames : FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET
---

# FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET_ Enumeration
The <b>FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET</b> enumeration type specifies the data field identifiers for the
  FWPS_LAYER_INBOUND_MAC_FRAME_ETHERNET 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layer</a>.
  <div class="alert"><b>Note</b>  In Windows 7 and Windows Server 2008 R2, the name of this enumeration was <b>FWPS_FIELDS_INBOUND_MAC_FRAME_802_3</b>.</div>
<div> </div>

## Syntax
````
typedef enum FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET_ { 
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_INTERFACE_MAC_ADDRESS,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_MAC_LOCAL_ADDRESS,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_MAC_REMOTE_ADDRESS,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_MAC_LOCAL_ADDRESS_TYPE,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_MAC_REMOTE_ADDRESS_TYPE,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_ETHER_TYPE,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_VLAN_ID,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_INTERFACE,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_INTERFACE_INDEX,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_NDIS_PORT,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_L2_FLAGS,
  FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_MAX
} FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET;
````

## Constants

<table>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_ETHER_TYPE</td>
<td>The inbound MAC frame  IEEE 802.3 EtherType field.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_INTERFACE</td>
<td>The inbound MAC frame  IEEE 802.3 interface field.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_INTERFACE_INDEX</td>
<td>The inbound MAC frame interface IEEE 802.3 interface index field.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_INTERFACE_MAC_ADDRESS</td>
<td>The inbound MAC frame IEEE 802.3 interface  MAC address field.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_L2_FLAGS</td>
<td>The inbound MAC frame IEEE 802.3 flags field.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_MAC_LOCAL_ADDRESS</td>
<td>The inbound MAC frame IEEE 802.3 local MAC address field.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_MAC_LOCAL_ADDRESS_TYPE</td>
<td>The inbound MAC frame IEEE 802.3 local MAC address type field.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_MAC_REMOTE_ADDRESS</td>
<td>The inbound MAC frame IEEE 802.3 remote MAC address field.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_MAC_REMOTE_ADDRESS_TYPE</td>
<td>The inbound MAC frame IEEE 802.3 remote MAC address type field.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_MAX</td>
<td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_NDIS_PORT</td>
<td>The inbound MAC frame IEEE 802.3 NDIS port field.</td>
</tr>

<tr>
<td>FWPS_FIELD_INBOUND_MAC_FRAME_ETHERNET_VLAN_ID</td>
<td>The inbound MAC frame IEEE 802.3 VLAN identifier field.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | fwpsk.h (include Fwpsk.h) |

## See Also

<dl>
<dt>
<a href="..\fwpsk\ne-fwpsk-fwps_fields_outbound_mac_frame_ethernet_.md">FWPS_FIELDS_OUTBOUND_MAC_FRAME_ETHERNET</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_FIELDS_INBOUND_MAC_FRAME_ETHERNET enumeration%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>