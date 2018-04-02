---
UID: NS:ndis._NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO
title: "_NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO"
author: windows-driver-content
description: The NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure specifies information that is used in offloading large send offload (LSO) tasks from the TCP/IP transport to a miniport adapter.
old-location: netvista\ndis_tcp_large_send_offload_net_buffer_list_info.htm
old-project: netvista
ms.assetid: 48827a51-d364-43f6-864b-b63395168429
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure [Network Drivers Starting with Windows Vista], PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure pointer [Network Drivers Starting with Windows Vista], _NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, ndis/NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, ndis/PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, netvista.ndis_tcp_large_send_offload_net_buffer_list_info, tcpip_offload_ref_ea60f429-377b-47e6-bb4b-aff34288fa17.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
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
-	ndis.h
api_name:
-	NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO
product: Windows
targetos: Windows
req.typenames: NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, *PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO
---

# _NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure
The <b>NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</b> structure specifies information that is used in
  offloading large send offload (LSO) tasks from the TCP/IP transport to a miniport adapter. The
  <b>NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</b> structure is part of the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> information.

## Syntax
```
typedef struct _NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO {
  union {
    struct {
      ULONG  : 30 Unused;
      ULONG  : 1  Type;
      ULONG  : 1  Reserved2;
    } Transmit;
    PVOID Value;
    struct {
      ULONG  : 20 MSS;
      ULONG  : 10 TcpHeaderOffset;
      ULONG  : 1  Type;
      ULONG  : 1  Reserved2;
    } LsoV1Transmit;
    struct {
      ULONG  : 30 TcpPayload;
      ULONG  : 1  Type;
      ULONG  : 1  Reserved2;
    } LsoV1TransmitComplete;
    struct {
      ULONG  : 20 MSS;
      ULONG  : 10 TcpHeaderOffset;
      ULONG  : 1  Type;
      ULONG  : 1  IPVersion;
    } LsoV2Transmit;
    struct {
      ULONG  : 30 Reserved;
      ULONG  : 1  Type;
      ULONG  : 1  Reserved2;
    } LsoV2TransmitComplete;
  };
} NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, *PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO;
```

## Members


## Remarks
The <b>NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</b> structure specifies information for LSOV1 and
    LSOV2 operations. The <b>NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</b> structure is part of the
    information that is included in a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.

To set and get the LSOV1 or LSOV2 information, use the 
    <b>TcpLargeSendNetBufferListInfo</b> index with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro.
    <b>NET_BUFFER_LIST_INFO</b> returns a ULONG value (not a pointer to a ULONG value).

The TCP/IP transport updates the 
    <b>MSS</b> and 
    <b>TcpHeaderOffset</b> members of the <b>NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</b> structure before
    sending a large packet to a miniport driver.

For LSOV1, miniport drivers write the TCP payload size in the 
    <b>TcpPayload</b> member before completing a send operation for a segmented packet.

<div class="alert"><b>Note</b>  Any <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that contains the LSOv1 or LSOv2 information also
    contains a single 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure.</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.0 and later. Supported in NDIS 6.0 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>



<a href="https://msdn.microsoft.com/windows/hardware/drivers/network/offloading-the-segmentation-of-large-tcp-packets">Offloading the Segmentation of Large TCP Packets</a>