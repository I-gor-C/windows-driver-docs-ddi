---
UID: NE:fwpsk.FWPS_FIELDS_IPFORWARD_V4_
title: FWPS_FIELDS_IPFORWARD_V4_
author: windows-driver-content
description: The FWPS_FIELDS_IPFORWARD_V4 enumeration type specifies the data field identifiers for the FWPS_LAYER_IPFORWARD_V4 and FWPS_LAYER_IPFORWARD_V4_DISCARD run-time filtering layers.
old-location: netvista\fwps_fields_ipforward_v4.htm
old-project: netvista
ms.assetid: af915976-2a2c-4cf4-a3e0-60ddea8e172c
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: FWPS_FIELDS_IPFORWARD_V4, FWPS_FIELDS_IPFORWARD_V4 enumeration [Network Drivers Starting with Windows Vista], FWPS_FIELDS_IPFORWARD_V4_, FWPS_FIELD_IPFORWARD_V4_ARRIVAL_INTERFACE_PROFILE_ID, FWPS_FIELD_IPFORWARD_V4_DESTINATION_INTERFACE_INDEX, FWPS_FIELD_IPFORWARD_V4_DESTINATION_SUB_INTERFACE_INDEX, FWPS_FIELD_IPFORWARD_V4_FLAGS, FWPS_FIELD_IPFORWARD_V4_IP_DESTINATION_ADDRESS, FWPS_FIELD_IPFORWARD_V4_IP_DESTINATION_ADDRESS_TYPE, FWPS_FIELD_IPFORWARD_V4_IP_FORWARD_INTERFACE, FWPS_FIELD_IPFORWARD_V4_IP_LOCAL_INTERFACE, FWPS_FIELD_IPFORWARD_V4_IP_PHYSICAL_ARRIVAL_INTERFACE, FWPS_FIELD_IPFORWARD_V4_IP_PHYSICAL_NEXTHOP_INTERFACE, FWPS_FIELD_IPFORWARD_V4_IP_SOURCE_ADDRESS, FWPS_FIELD_IPFORWARD_V4_MAX, FWPS_FIELD_IPFORWARD_V4_NEXTHOP_INTERFACE_PROFILE_ID, FWPS_FIELD_IPFORWARD_V4_SOURCE_INTERFACE_INDEX, FWPS_FIELD_IPFORWARD_V4_SOURCE_SUB_INTERFACE_INDEX, fwpsk/FWPS_FIELDS_IPFORWARD_V4, fwpsk/FWPS_FIELD_IPFORWARD_V4_ARRIVAL_INTERFACE_PROFILE_ID, fwpsk/FWPS_FIELD_IPFORWARD_V4_DESTINATION_INTERFACE_INDEX, fwpsk/FWPS_FIELD_IPFORWARD_V4_DESTINATION_SUB_INTERFACE_INDEX, fwpsk/FWPS_FIELD_IPFORWARD_V4_FLAGS, fwpsk/FWPS_FIELD_IPFORWARD_V4_IP_DESTINATION_ADDRESS, fwpsk/FWPS_FIELD_IPFORWARD_V4_IP_DESTINATION_ADDRESS_TYPE, fwpsk/FWPS_FIELD_IPFORWARD_V4_IP_FORWARD_INTERFACE, fwpsk/FWPS_FIELD_IPFORWARD_V4_IP_LOCAL_INTERFACE, fwpsk/FWPS_FIELD_IPFORWARD_V4_IP_PHYSICAL_ARRIVAL_INTERFACE, fwpsk/FWPS_FIELD_IPFORWARD_V4_IP_PHYSICAL_NEXTHOP_INTERFACE, fwpsk/FWPS_FIELD_IPFORWARD_V4_IP_SOURCE_ADDRESS, fwpsk/FWPS_FIELD_IPFORWARD_V4_MAX, fwpsk/FWPS_FIELD_IPFORWARD_V4_NEXTHOP_INTERFACE_PROFILE_ID, fwpsk/FWPS_FIELD_IPFORWARD_V4_SOURCE_INTERFACE_INDEX, fwpsk/FWPS_FIELD_IPFORWARD_V4_SOURCE_SUB_INTERFACE_INDEX, netvista.fwps_fields_ipforward_v4, wfp_ref_5_const_3_data_fields_cff20018-8ff1-43dc-937d-92a1a91137e3.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Unless otherwise noted, supported starting with Windows Vista.
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
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	fwpsk.h
api_name:
-	FWPS_FIELDS_IPFORWARD_V4
product: Windows
targetos: Windows
req.typenames: FWPS_FIELDS_IPFORWARD_V4
---

# FWPS_FIELDS_IPFORWARD_V4_ Enumeration
The FWPS_FIELDS_IPFORWARD_V4 enumeration type specifies the data field identifiers for the
  FWPS_LAYER_IPFORWARD_V4 and FWPS_LAYER_IPFORWARD_V4_DISCARD 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layers</a>.

## Syntax
```
typedef enum FWPS_FIELDS_IPFORWARD_V4_ {
  FWPS_FIELD_IPFORWARD_V4_IP_SOURCE_ADDRESS                ,
  FWPS_FIELD_IPFORWARD_V4_IP_DESTINATION_ADDRESS           ,
  FWPS_FIELD_IPFORWARD_V4_IP_DESTINATION_ADDRESS_TYPE      ,
  FWPS_FIELD_IPFORWARD_V4_IP_LOCAL_INTERFACE               ,
  FWPS_FIELD_IPFORWARD_V4_IP_FORWARD_INTERFACE             ,
  FWPS_FIELD_IPFORWARD_V4_SOURCE_INTERFACE_INDEX           ,
  FWPS_FIELD_IPFORWARD_V4_SOURCE_SUB_INTERFACE_INDEX       ,
  FWPS_FIELD_IPFORWARD_V4_DESTINATION_INTERFACE_INDEX      ,
  FWPS_FIELD_IPFORWARD_V4_DESTINATION_SUB_INTERFACE_INDEX  ,
  FWPS_FIELD_IPFORWARD_V4_FLAGS                            ,
  FWPS_FIELD_IPFORWARD_V4_IP_PHYSICAL_ARRIVAL_INTERFACE    ,
  FWPS_FIELD_IPFORWARD_V4_ARRIVAL_INTERFACE_PROFILE_ID     ,
  FWPS_FIELD_IPFORWARD_V4_IP_PHYSICAL_NEXTHOP_INTERFACE    ,
  FWPS_FIELD_IPFORWARD_V4_NEXTHOP_INTERFACE_PROFILE_ID     ,
  FWPS_FIELD_IPFORWARD_V4_COMPARTMENT_ID                   ,
  FWPS_FIELD_IPFORWARD_V4_MAX
} FWPS_FIELDS_IPFORWARD_V4;
```

## Constants

<table>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_IP_SOURCE_ADDRESS</td>
                    <td>The source IP address.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_IP_DESTINATION_ADDRESS</td>
                    <td>The destination IP address.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_IP_DESTINATION_ADDRESS_TYPE</td>
                    <td>The destination IP address type. The possible values are defined by the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a> enumeration.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_IP_LOCAL_INTERFACE</td>
                    <td>The locally unique identifier (<a href="https://msdn.microsoft.com/library/windows/hardware/ff557080">LUID</a>) for the network interface associated with the
     local IP address.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_IP_FORWARD_INTERFACE</td>
                    <td>The LUID for the network interface on which the packet being forwarded is to be sent out.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_SOURCE_INTERFACE_INDEX</td>
                    <td>The index of the source network interface, as enumerated by the network stack.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_SOURCE_SUB_INTERFACE_INDEX</td>
                    <td>The index of the source logical network interface, as enumerated by the network stack.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_DESTINATION_INTERFACE_INDEX</td>
                    <td>The index of the destination network interface, as enumerated by the network stack.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_DESTINATION_SUB_INTERFACE_INDEX</td>
                    <td>The index of the destination logical network interface, as enumerated by the network stack.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_FLAGS</td>
                    <td>A bitwise OR of a combination of filtering condition flags. For information about the possible
     flags, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549942">Filtering Condition Flags</a>.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_IP_PHYSICAL_ARRIVAL_INTERFACE</td>
                    <td>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff557080">LUID</a> for the physical network interface that the
     packet first arrived on.
     

<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_ARRIVAL_INTERFACE_PROFILE_ID</td>
                    <td>The profile identifier (network category) of the arrival interface. The possible network category
     values are: public (1), private (2), or domain (3).
     

<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_IP_PHYSICAL_NEXTHOP_INTERFACE</td>
                    <td>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff557080">LUID</a> for the physical network interface that will be
     used to continue forwarding of the outbound packet.
     

<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_NEXTHOP_INTERFACE_PROFILE_ID</td>
                    <td>The profile identifier (network category) of the next-hop interface. The possible network category
     values are: public (1), private (2), or domain (3).
     

<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_COMPARTMENT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_IPFORWARD_V4_MAX</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Unless otherwise noted, supported starting with Windows Vista. Unless otherwise noted, supported starting with Windows Vista. |
| **Header** | fwpsk.h (include Fwpsk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557080">LUID</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a>