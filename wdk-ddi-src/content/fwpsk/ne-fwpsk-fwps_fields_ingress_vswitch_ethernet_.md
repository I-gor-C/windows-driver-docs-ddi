---
UID: NE:fwpsk.FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET_
title: FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET_
author: windows-driver-content
description: The FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET (formerly WPS_FIELDS_INGRESS_VSWITCH_802_3) enumeration type specifies the data field identifiers for the FWPS_LAYER_INGRESS_VSWITCH_ETHERNET run-time filtering layer.
old-location: netvista\fwps_fields_ingress_vswitch_802_3.htm
old-project: netvista
ms.assetid: ec206a59-33a1-4812-8290-4a2d417e4747
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET, FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET enumeration [Network Drivers Starting with Windows Vista], FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET_, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_ETHER_TYPE, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_FLAGS, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS_TYPE, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS_TYPE, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAX, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_TENANT_NETWORK_ID, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VLAN_ID, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_ID, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_NETWORK_TYPE, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_ID, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_TYPE, FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_VM_ID, fwpsk/FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_ETHER_TYPE, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_FLAGS, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS_TYPE, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS_TYPE, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAX, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_TENANT_NETWORK_ID, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VLAN_ID, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_ID, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_NETWORK_TYPE, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_ID, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_TYPE, fwpsk/FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_VM_ID, netvista.fwps_fields_ingress_vswitch_802_3
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
-	FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET
product: Windows
targetos: Windows
req.typenames: FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET
---

# FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET_ Enumeration
The FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET (formerly WPS_FIELDS_INGRESS_VSWITCH_802_3) enumeration type specifies the data field identifiers for the
  FWPS_LAYER_INGRESS_VSWITCH_ETHERNET 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layer</a>.

## Syntax
````
typedef enum FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET_ { 
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS_TYPE,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS_TYPE,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_ETHER_TYPE,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VLAN_ID,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_TENANT_NETWORK_ID,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_ID,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_NETWORK_TYPE,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_ID,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_TYPE,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_VM_ID,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_FLAGS,
  FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAX
} FWPS_FIELDS_INGRESS_VSWITCH_ETHERNET;
````

## Constants

<table>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_COMPARTMENT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_ETHER_TYPE</td>
                    <td>The virtual switch ingress Ethernet EtherType field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_L2_FLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS</td>
                    <td>The virtual switch ingress MAC destination address field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS_TYPE</td>
                    <td>The virtual switch ingress MAC destination address type field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS</td>
                    <td>The virtual switch ingress MAC source address field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS_TYPE</td>
                    <td>The virtual switch ingress MAC source address type field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_MAX</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the NDIS header files and binaries.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VLAN_ID</td>
                    <td>The virtual switch ingress virtual  LAN (VLAN) identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_ID</td>
                    <td>The virtual switch ingress identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_NETWORK_TYPE</td>
                    <td>The virtual switch ingress network type field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_ID</td>
                    <td>The virtual switch ingress source interface identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_TYPE</td>
                    <td>The virtual switch ingress source interface type field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_VM_ID</td>
                    <td>The virtual switch ingress source virtual machine (VM)  identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_INGRESS_VSWITCH_ETHERNET_VSWITCH_TENANT_NETWORK_ID</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 8. Supported starting with Windows 8. |
| **Header** | fwpsk.h (include Fwpsk.h) |