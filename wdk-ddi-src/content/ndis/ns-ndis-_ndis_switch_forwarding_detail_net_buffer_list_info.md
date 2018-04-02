---
UID: NS:ndis._NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO
title: "_NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO"
author: windows-driver-content
description: The NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO union specifies the information for forwarding a packet to one or more Hyper-V extensible switch ports.
old-location: netvista\ndis_switch_forwarding_detail_net_buffer_list_info.htm
old-project: netvista
ms.assetid: 6377CC08-A261-465A-AA04-0BE31EEACF01
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO, NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO, NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO union [Network Drivers Starting with Windows Vista], PNDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO, PNDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO union pointer [Network Drivers Starting with Windows Vista], _NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO, ndis/NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO, ndis/PNDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO, netvista.ndis_switch_forwarding_detail_net_buffer_list_info"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
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
req.irql: See Remarks section
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ndis.h
api_name:
-	NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO
product:
- Windows
targetos: Windows
req.typenames: NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO, *PNDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO
---

# _NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO structure
The <b>NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</b> union specifies the information for forwarding a packet to one or more Hyper-V extensible switch ports. 

This information is contained in the out-of-band (OOB) data of the packet's  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.

## Syntax
```
typedef struct _NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO {
  UINT64 AsUINT64;
  struct {
    UINT32  : 1  IsPacketDataSafe;
    UINT32  : 1  NativeForwardingRequired;
    UINT32  : 16 NumAvailableDestinations;
    UINT32  : 1  Reserved1;
    UINT32  : 9  Reserved2;
    UINT32  : 12 SafePacketDataSize;
    UINT32  : 8  SourceNicIndex;
    UINT32  : 16 SourcePortId;
  };
} NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO, *PNDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO;
```

## Members


`AsUINT64`

The complete 64-bit <b>NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</b> value.

## Remarks
Extensible switch extensions can use the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598259">NET_BUFFER_LIST_SWITCH_FORWARDING_DETAIL</a> macro to access the <b>NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</b> union in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.

The <b>NumAvailableDestinations</b> member of the <b>NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</b> union specifies the number of unused extensible switch destination port elements within a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. Each extensible switch destination port is specified by an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a> element within the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a> structure of a <b>NET_BUFFER_LIST</b> structure. The extensible switch extension calls <a href="https://msdn.microsoft.com/55B5C0B4-5359-410B-9110-79EDDBA3010C">GetNetBufferListDestinations</a> to obtain the current <b>NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</b> in a <b>NET_BUFFER_LIST</b> structure.

The <b>NativeForwardingRequired</b> member specifies whether the packet is an NVGRE packet or not. If it is <b>TRUE</b>, the packet is an NVGRE packet, and the forwarding extension doesn't determine the packet's forwarding destination port array, although it can add or exclude destination ports in the array. For more information, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/hybrid-forwarding">Hybrid Forwarding</a>.

The <b>SafePacketDataSize</b> member specifies the size of the packet data that is located in local, or <i>trusted</i>, memory in the parent operating system of the Hyper-V parent partition. This memory is not accessible by the child partition. Therefore, it  is considered "safe" from unsynchronized updates by the guest operating system that runs in that partition. 

If an extensible switch extension requires more trusted space in order to inspect the packet data, it must follow these steps:

<ol>
<li>
The extension must duplicate the packet's <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure by allocating  a <b>NET_BUFFER_LIST</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure. The extension then calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff561718">NdisCopyFromNetBufferToNetBuffer</a> to duplicate the packet's <b>NET_BUFFER</b> structure. If this function completes successfully, the packet's data is copied to trusted memory.

</li>
<li>
The extension must call <a href="https://msdn.microsoft.com/5CC345FA-C3EF-4122-8E9C-6EA27B20DD5A">CopyNetBufferListInfo</a> to copy the packet's OOB data to the duplicated packet.

</li>
<li>
After the original packet has been duplicated, the extension must obtain the <b>NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO</b> union in the duplicated packet by using the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598259">NET_BUFFER_LIST_SWITCH_FORWARDING_DETAIL</a> macro. The extension must set the <b>IsPacketDataSafe</b> member to <b>TRUE</b>.

</li>
</ol>
For more information on how to duplicate packets in the extensible switch interface, see <a href="https://msdn.microsoft.com/613C7E82-387D-47AE-A699-A799087D3C1D">Originating Packet Traffic</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.30 and later. Supported in NDIS 6.30 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<b></b>



<a href="https://msdn.microsoft.com/7ABBB3F3-66F5-4651-8A5A-94940F3FD82D">Forwarding Extensions</a>



<a href="https://msdn.microsoft.com/C8DA9064-21EE-45F4-BE6D-D24851C5480B">Forwarding Packets to Hyper-V Extensible Switch Ports</a>



<a href="https://msdn.microsoft.com/14A78DB2-6643-471D-97B9-4D8524EC3E73">Forwarding Packets to Physical Network Adapters</a>



<a href="https://msdn.microsoft.com/55B5C0B4-5359-410B-9110-79EDDBA3010C">GetNetBufferListDestinations</a>



<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/hybrid-forwarding">Hybrid Forwarding</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh598210">NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh598224">NDIS_SWITCH_PORT_DESTINATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh598259">NET_BUFFER_LIST_SWITCH_FORWARDING_DETAIL</a>



<a href="https://msdn.microsoft.com/78181C72-FBFD-4860-A664-C297997D780F">Overview of the Hyper-V Extensible Switch</a>