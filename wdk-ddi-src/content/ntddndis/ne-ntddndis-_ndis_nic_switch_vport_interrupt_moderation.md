---
UID: NE:ntddndis._NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION
title: "_NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION"
author: windows-driver-content
description: The NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION enumeration specifies the interrupt moderation setting of a single root I/O virtualization (SR-IOV) virtual port (VPort) on the NIC switch.
old-location: netvista\ndis_nic_switch_vport_interrupt_moderation.htm
old-project: netvista
ms.assetid: 86ec2e8f-1a89-4c0a-b761-d9bf0d3dc35a
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION enumeration [Network Drivers Starting with Windows Vista], NdisNicSwitchVPortIntModAdaptive, NdisNicSwitchVPortIntModHigh, NdisNicSwitchVPortIntModLow, NdisNicSwitchVPortIntModMedium, NdisNicSwitchVPortIntModOff, NdisNicSwitchVPortIntModUndefined, PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION enumeration pointer [Network Drivers Starting with Windows Vista], _NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, netvista.ndis_nic_switch_vport_interrupt_moderation, ntddndis/NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, ntddndis/NdisNicSwitchVPortIntModAdaptive, ntddndis/NdisNicSwitchVPortIntModHigh, ntddndis/NdisNicSwitchVPortIntModLow, ntddndis/NdisNicSwitchVPortIntModMedium, ntddndis/NdisNicSwitchVPortIntModOff, ntddndis/NdisNicSwitchVPortIntModUndefined, ntddndis/PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION"
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
-	NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION
product:
- Windows
targetos: Windows
req.typenames: NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, *PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION
---

# _NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION Enumeration
The <b>NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION</b> enumeration specifies the interrupt moderation setting of a single root I/O virtualization (SR-IOV) virtual port (VPort) on the NIC switch.

## Syntax
```
typedef enum _NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION {
  NdisNicSwitchVPortInterruptModerationUndefined  ,
  NdisNicSwitchVPortInterruptModerationAdaptive   ,
  NdisNicSwitchVPortInterruptModerationOff        ,
  NdisNicSwitchVPortInterruptModerationLow        ,
  NdisNicSwitchVPortInterruptModerationMedium     ,
  NdisNicSwitchVPortInterruptModerationHigh
} *PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION;
```

## Constants

<table>
            
                <tr>
                    <td>NdisNicSwitchVPortInterruptModerationUndefined</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NdisNicSwitchVPortInterruptModerationAdaptive</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NdisNicSwitchVPortInterruptModerationOff</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NdisNicSwitchVPortInterruptModerationLow</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NdisNicSwitchVPortInterruptModerationMedium</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NdisNicSwitchVPortInterruptModerationHigh</td>
                    <td></td>
                </tr>
</table>

## Remarks

The determination of low, medium, and high interrupt moderation levels is determined by the miniport driver based on a hardware algorithm that is based on the network adapter.

The <b>InterruptModeration</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451597">NDIS_NIC_SWITCH_VPORT_PARAMETERS</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh451594">NDIS_NIC_SWITCH_VPORT_INFO</a> structures is an NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION enumeration data type.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.30 and later. Supported in NDIS 6.30 and later. |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<b></b>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451594">NDIS_NIC_SWITCH_VPORT_INFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451597">NDIS_NIC_SWITCH_VPORT_PARAMETERS</a>