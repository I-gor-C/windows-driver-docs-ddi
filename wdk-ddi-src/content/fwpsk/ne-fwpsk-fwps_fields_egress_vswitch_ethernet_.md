---
UID: NE:fwpsk.FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET_
title: FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET_
author: windows-driver-content
description: The FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET (formerly FWPS_FIELDS_EGRESS_VSWITCH_802_3) enumeration type specifies the data field identifiers for the FWPS_LAYER_EGRESS_VSWITCH_ETHERNET run-time filtering layer.
old-location: netvista\fwps_fields_egress_vswitch_802_3.htm
old-project: netvista
ms.assetid: de899526-ea77-4f0c-a05a-b28bb422a9b4
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAX, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS_TYPE, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS_TYPE, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS_TYPE, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_INTERFACE_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_TYPE, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS, netvista.fwps_fields_egress_vswitch_802_3, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VLAN_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_TENANT_NETWORK_ID, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_NETWORK_TYPE, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS_TYPE, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_ID, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_TYPE, FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET enumeration [Network Drivers Starting with Windows Vista], FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS, fwpsk/FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_NETWORK_TYPE, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_ETHER_TYPE, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_INTERFACE_TYPE, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VLAN_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_FLAGS, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_INTERFACE_ID, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAX, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_FLAGS, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_TENANT_NETWORK_ID, FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_VM_ID, FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET_, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_ETHER_TYPE, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_ID, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_INTERFACE_TYPE, FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET, fwpsk/FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_VM_ID
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	fwpsk.h
apiname:
-	FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET
product: Windows
targetos: Windows
req.typenames: FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET
---

# FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET_ Enumeration
The FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET (formerly FWPS_FIELDS_EGRESS_VSWITCH_802_3) enumeration type specifies the data field identifiers for the
  FWPS_LAYER_EGRESS_VSWITCH_ETHERNET 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layer</a>.

## Syntax
````
typedef enum FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET_ { 
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS_TYPE,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS_TYPE,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_ETHER_TYPE,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VLAN_ID,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_TENANT_NETWORK_ID,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_ID,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_NETWORK_TYPE,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_ID,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_TYPE,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_INTERFACE_ID,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_INTERFACE_TYPE,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_VM_ID,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_FLAGS,
  FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAX
} FWPS_FIELDS_EGRESS_VSWITCH_ETHERNET;
````

## Constants

<table>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_COMPARTMENT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_ETHER_TYPE</td>
                    <td>The virtual switch egress Ethernet EtherType field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_L2_FLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS</td>
                    <td>The virtual switch egress MAC destination address field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_DESTINATION_ADDRESS_TYPE</td>
                    <td>The virtual switch egress MAC destination address type field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS</td>
                    <td>The virtual switch egress MAC source address field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAC_SOURCE_ADDRESS_TYPE</td>
                    <td>The virtual switch egress MAC source address type field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_MAX</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the NDIS header files and binaries.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VLAN_ID</td>
                    <td>The virtual switch egress virtual LAN (VLAN) identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_INTERFACE_ID</td>
                    <td>The virtual switch egress Ethernet virtual switch destination  interface identifier  field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_INTERFACE_TYPE</td>
                    <td>The virtual switch egress Ethernet virtual switch destination interface type  field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_DESTINATION_VM_ID</td>
                    <td>The virtual switch egress Ethernet virtual switch destination virtual machine (VM) identifier  field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_ID</td>
                    <td>The virtual switch egress Ethernet virtual switch identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_NETWORK_TYPE</td>
                    <td>The virtual switch egress Ethernet virtual switch network type field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_ID</td>
                    <td>The virtual switch egress Ethernet virtual switch source identifier field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_INTERFACE_TYPE</td>
                    <td>The virtual switch egress Ethernet virtual switch source interface type  field.</td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_SOURCE_VM_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>FWPS_FIELD_EGRESS_VSWITCH_ETHERNET_VSWITCH_TENANT_NETWORK_ID</td>
                    <td>The virtual switch egress  tenant network identifier field.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 8. Supported starting with Windows 8. |
| **Header** | fwpsk.h (include Fwpsk.h) |