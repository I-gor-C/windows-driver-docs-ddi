---
UID: NE:fwpsk.FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4_
title: FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4_
author: windows-driver-content
description: The FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4 enumeration type specifies the data field identifiers for the FWPS_LAYER_EGRESS_VSWITCH_TRANSPORT_V4 run-time filtering layer.
old-location: netvista\fwps_fields_egress_vswitch_transport_v4.htm
old-project: netvista
ms.assetid: 6b0a2993-edc6-48bc-828e-4f74d889e79f
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4, FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4 enumeration [Network Drivers Starting with Windows Vista], FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4_, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_FLAGS, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_DESTINATION_ADDRESS, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_DESTINATION_PORT, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_PROTOCOL, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_SOURCE_ADDRESS, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_SOURCE_PORT, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_MAX, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VLAN_ID, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_INTERFACE_ID, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_INTERFACE_TYPE, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_VM_ID, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_ID, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_NETWORK_TYPE, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_INTERFACE_ID, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_INTERFACE_TYPE, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_VM_ID, FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_TENANT_NETWORK_ID, fwpsk/FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_FLAGS, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_DESTINATION_ADDRESS, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_DESTINATION_PORT, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_PROTOCOL, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_SOURCE_ADDRESS, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_SOURCE_PORT, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_MAX, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VLAN_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_INTERFACE_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_INTERFACE_TYPE, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_VM_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_NETWORK_TYPE, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_INTERFACE_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_INTERFACE_TYPE, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_VM_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_TENANT_NETWORK_ID, netvista.fwps_fields_egress_vswitch_transport_v4
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
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
-	FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4
product: Windows
targetos: Windows
req.typenames: FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4
---

# FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4_ Enumeration
The FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4 enumeration type specifies the data field identifiers for the
  FWPS_LAYER_EGRESS_VSWITCH_TRANSPORT_V4 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layer</a>.

## Syntax
````
typedef enum FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4_ { 
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_SOURCE_ADDRESS,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_DESTINATION_ADDRESS,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_PROTOCOL,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_SOURCE_PORT,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_DESTINATION_PORT,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VLAN_ID,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_TENANT_NETWORK_ID,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_ID,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_NETWORK_TYPE,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_INTERFACE_ID,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_INTERFACE_TYPE,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_VM_ID,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_INTERFACE_ID,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_INTERFACE_TYPE,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_VM_ID,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_FLAGS,
  FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_MAX
} FWPS_FIELDS_EGRESS_VSWITCH_TRANSPORT_V4;
````

## Constants

<table>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_SOURCE_ADDRESS</td>
                    <td>The virtual switch egress IP source address field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_DESTINATION_ADDRESS</td>
                    <td>The virtual switch egress IP destination address field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_PROTOCOL</td>
                    <td>The virtual switch egress IP protocol  field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_SOURCE_PORT</td>
                    <td>The virtual switch egress IP source port field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_IP_DESTINATION_PORT</td>
                    <td>The virtual switch egress IP destination port  field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VLAN_ID</td>
                    <td>The virtual switch egress virtual LAN (VLAN) identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_TENANT_NETWORK_ID</td>
                    <td>The virtual switch egress virtual switch tenant network identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_ID</td>
                    <td>The virtual switch egress identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_NETWORK_TYPE</td>
                    <td>The virtual switch egress network type field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_INTERFACE_ID</td>
                    <td>The virtual switch egress source interface identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_INTERFACE_TYPE</td>
                    <td>The virtual switch egress source interface type  field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_SOURCE_VM_ID</td>
                    <td>The virtual switch egress source virtual machine (VM) identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_INTERFACE_ID</td>
                    <td>The virtual switch egress destination interface identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_INTERFACE_TYPE</td>
                    <td>The virtual switch egress destination interface type field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_VSWITCH_DESTINATION_VM_ID</td>
                    <td>The virtual switch egress destination virtual machine (VM) identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_L2_FLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_COMPARTMENT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_TRANSPORT_V4_MAX</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the NDIS header files and binaries.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 8. Supported starting with Windows 8. |
| **Header** | fwpsk.h (include Fwpsk.h) |