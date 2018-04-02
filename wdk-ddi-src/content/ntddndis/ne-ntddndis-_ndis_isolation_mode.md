---
UID: NE:ntddndis._NDIS_ISOLATION_MODE
title: "_NDIS_ISOLATION_MODE"
author: windows-driver-content
description: The NDIS_ISOLATION_MODE enumeration defines the network isolation modes that can be specified for a VM network adapter.
old-location: netvista\ndis_isolation_mode.htm
old-project: netvista
ms.assetid: DA4765CD-808C-438A-9CA6-5ADC27A70EC8
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_ISOLATION_MODE, NDIS_ISOLATION_MODE, NDIS_ISOLATION_MODE enumeration [Network Drivers Starting with Windows Vista], NdisIsolationModeExternalVirtualSubnet, NdisIsolationModeNativeVirtualSubnet, NdisIsolationModeNone, NdisIsolationModeVlan, _NDIS_ISOLATION_MODE, netvista.ndis_isolation_mode, ntddndis/NDIS_ISOLATION_MODE, ntddndis/NdisIsolationModeExternalVirtualSubnet, ntddndis/NdisIsolationModeNativeVirtualSubnet, ntddndis/NdisIsolationModeNone, ntddndis/NdisIsolationModeVlan"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.40 and later.
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
-	NDIS_ISOLATION_MODE
product: Windows
targetos: Windows
req.typenames: NDIS_ISOLATION_MODE, *PNDIS_ISOLATION_MODE
---

# _NDIS_ISOLATION_MODE Enumeration
The <b>NDIS_ISOLATION_MODE</b> enumeration defines the network isolation modes that can be specified for a VM network adapter.

## Syntax
```
typedef enum _NDIS_ISOLATION_MODE {
  NdisIsolationModeNone                   ,
  NdisIsolationModeNativeVirtualSubnet    ,
  NdisIsolationModeExternalVirtualSubnet  ,
  NdisIsolationModeVlan
} *PNDIS_ISOLATION_MODE, NDIS_ISOLATION_MODE;
```

## Constants

<table>
            
                <tr>
                    <td>NdisIsolationModeNone</td>
                    <td>Network isolation is not supported.</td>
                </tr>
            
                <tr>
                    <td>NdisIsolationModeNativeVirtualSubnet</td>
                    <td>Native <b>VirtualSubnetId</b>-based isolation provided by Hyper-V Network Virtualization.</td>
                </tr>
            
                <tr>
                    <td>NdisIsolationModeExternalVirtualSubnet</td>
                    <td>External <b>VirtualSubnetId</b>-based isolation provided by a Hyper-V Extensible Switch extension.</td>
                </tr>
            
                <tr>
                    <td>NdisIsolationModeVlan</td>
                    <td>Virtual local area network (VLAN)-based isolation.</td>
                </tr>
</table>

## Remarks

<b>NDIS_ISOLATION_MODE</b> enumeration values are used in the <b>IsolationMode</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn383687">NDIS_SWITCH_PORT_PROPERTY_ISOLATION</a> structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.40 and later. Supported in NDIS 6.40 and later. |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn383679">NDIS_ISOLATION_PARAMETERS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn383687">NDIS_SWITCH_PORT_PROPERTY_ISOLATION</a>