---
UID : NE:ntddndis._NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION
title : "_NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION"
author : windows-driver-content
description : The NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION enumeration specifies the interrupt moderation setting of a single root I/O virtualization (SR-IOV) virtual port (VPort) on the NIC switch.
old-location : netvista\ndis_nic_switch_vport_interrupt_moderation.htm
old-project : netvista
ms.assetid : 86ec2e8f-1a89-4c0a-b761-d9bf0d3dc35a
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddndis/NdisNicSwitchVPortIntModMedium, ntddndis/NdisNicSwitchVPortIntModAdaptive, ntddndis/NdisNicSwitchVPortIntModOff, PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION enumeration pointer [Network Drivers Starting with Windows Vista], NdisNicSwitchVPortIntModLow, ntddndis/NdisNicSwitchVPortIntModUndefined, ntddndis/NdisNicSwitchVPortIntModLow, *PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, ntddndis/NdisNicSwitchVPortIntModHigh, _NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, ntddndis/PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, NdisNicSwitchVPortIntModOff, NdisNicSwitchVPortIntModUndefined, NdisNicSwitchVPortIntModMedium, NdisNicSwitchVPortIntModAdaptive, ntddndis/NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, netvista.ndis_nic_switch_vport_interrupt_moderation, NdisNicSwitchVPortIntModHigh, NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION enumeration [Network Drivers Starting with Windows Vista]
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
req.typenames : NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, *PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION
---

# _NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION Enumeration
The <b>NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION</b> enumeration specifies the interrupt moderation setting of a single root I/O virtualization (SR-IOV) virtual port (VPort) on the NIC switch.

## Syntax
````
typedef enum _NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION { 
  NdisNicSwitchVPortIntModUndefined  = 0,
  NdisNicSwitchVPortIntModAdaptive   = 1,
  NdisNicSwitchVPortIntModOff        = 2,
  NdisNicSwitchVPortIntModLow        = 100,
  NdisNicSwitchVPortIntModMedium     = 200,
  NdisNicSwitchVPortIntModHigh       = 300
} NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION, *PNDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION;
````

## Constants

<table>

<tr>
<td>NdisNicSwitchVPortInterruptModerationAdaptive</td>
<td></td>
</tr>

<tr>
<td>NdisNicSwitchVPortInterruptModerationHigh</td>
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
<td>NdisNicSwitchVPortInterruptModerationOff</td>
<td></td>
</tr>

<tr>
<td>NdisNicSwitchVPortInterruptModerationUndefined</td>
<td></td>
</tr>
</table>

## Remarks

The determination of low, medium, and high interrupt moderation levels is determined by the miniport driver based on a hardware algorithm that is based on the network adapter.

The <b>InterruptModeration</b> member of the <a href="..\ntddndis\ns-ntddndis-_ndis_nic_switch_vport_parameters.md">NDIS_NIC_SWITCH_VPORT_PARAMETERS</a> and <a href="..\ntddndis\ns-ntddndis-_ndis_nic_switch_vport_info.md">NDIS_NIC_SWITCH_VPORT_INFO</a> structures is an NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION enumeration data type.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.30 and later. Supported in NDIS 6.30 and later. |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="..\ntddndis\ns-ntddndis-_ndis_nic_switch_vport_parameters.md">NDIS_NIC_SWITCH_VPORT_PARAMETERS</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_nic_switch_vport_info.md">NDIS_NIC_SWITCH_VPORT_INFO</a>

<b></b>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NIC_SWITCH_VPORT_INTERRUPT_MODERATION enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>