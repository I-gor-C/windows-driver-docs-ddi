---
UID: NE:ntddndis._NDIS_SWITCH_NIC_STATE
title: "_NDIS_SWITCH_NIC_STATE"
author: windows-driver-content
description: The NDIS_SWITCH_NIC_STATE enumeration specifies the current state of the Hyper-V extensible switch network adapter.
old-location: netvista\ndis_switch_nic_state.htm
old-project: netvista
ms.assetid: 06FFECB3-0883-41CA-9BD3-A6A1D95D5F8C
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NDIS_SWITCH_NIC_STATE, NDIS_SWITCH_NIC_STATE enumeration [Network Drivers Starting with Windows Vista], NdisSwitchNicStateConnected, NdisSwitchNicStateCreated, NdisSwitchNicStateDeleted, NdisSwitchNicStateDisconnected, NdisSwitchNicStateUnknown, _NDIS_SWITCH_NIC_STATE, netvista.ndis_switch_nic_state, ntddndis/NDIS_SWITCH_NIC_STATE, ntddndis/NdisSwitchNicStateConnected, ntddndis/NdisSwitchNicStateCreated, ntddndis/NdisSwitchNicStateDeleted, ntddndis/NdisSwitchNicStateDisconnected, ntddndis/NdisSwitchNicStateUnknown
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
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
-	NDIS_SWITCH_NIC_STATE
product:
- Windows
targetos: Windows
req.typenames: NDIS_SWITCH_NIC_STATE
---

# _NDIS_SWITCH_NIC_STATE Enumeration
The <b>NDIS_SWITCH_NIC_STATE</b> enumeration specifies the current state of the Hyper-V extensible switch network adapter.

## Syntax
```
typedef enum _NDIS_SWITCH_NIC_STATE {
  NdisSwitchNicStateUnknown       ,
  NdisSwitchNicStateCreated       ,
  NdisSwitchNicStateConnected     ,
  NdisSwitchNicStateDisconnected  ,
  NdisSwitchNicStateDeleted
} NDIS_SWITCH_NIC_STATE;
```

## Constants

<table>
            
                <tr>
                    <td>NdisSwitchNicStateUnknown</td>
                    <td>This value specifies an undefined NIC state. This value is unused.</td>
                </tr>
            
                <tr>
                    <td>NdisSwitchNicStateCreated</td>
                    <td>This value specifies that the NIC is in the created state.</td>
                </tr>
            
                <tr>
                    <td>NdisSwitchNicStateConnected</td>
                    <td>This value specifies that the NIC is connected.</td>
                </tr>
            
                <tr>
                    <td>NdisSwitchNicStateDisconnected</td>
                    <td>This value specifies that the NIC is disconnected.</td>
                </tr>
            
                <tr>
                    <td>NdisSwitchNicStateDeleted</td>
                    <td>This value specifies that the NIC is deleted.</td>
                </tr>
</table>

## Remarks

The <b>NicState</b>  member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598215">NDIS_SWITCH_NIC_PARAMETERS</a> structure is an <b>NDIS_SWITCH_NIC_STATE</b> enumeration data type. 


For more information about extensible switch port states, see <a href="https://msdn.microsoft.com/61403FDE-90BF-4D0A-83E1-5AF8ADBD37A5">Overview of Hyper-V Extensible Switch Network Adapters</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.30 and later. Supported in NDIS 6.30 and later. |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh598215">NDIS_SWITCH_NIC_PARAMETERS</a>