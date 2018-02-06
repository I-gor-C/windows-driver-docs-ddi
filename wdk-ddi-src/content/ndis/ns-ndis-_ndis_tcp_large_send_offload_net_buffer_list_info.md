---
UID: NS:ndis._NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO
title: "_NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO"
author: windows-driver-content
description: The NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure specifies information that is used in offloading large send offload (LSO) tasks from the TCP/IP transport to a miniport adapter.
old-location: netvista\ndis_tcp_large_send_offload_net_buffer_list_info.htm
old-project: netvista
ms.assetid: 48827a51-d364-43f6-864b-b63395168429
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: ndis/NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, *PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, tcpip_offload_ref_ea60f429-377b-47e6-bb4b-aff34288fa17.xml, PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure pointer [Network Drivers Starting with Windows Vista], netvista.ndis_tcp_large_send_offload_net_buffer_list_info, NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure [Network Drivers Starting with Windows Vista], PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, _NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, ndis/PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ndis.h
apiname:
-	NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO
product: Windows
targetos: Windows
req.typenames: NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, *PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO
---

# _NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure
The <b>NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</b> structure specifies information that is used in
  offloading large send offload (LSO) tasks from the TCP/IP transport to a miniport adapter. The
  <b>NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</b> structure is part of the 
  <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> information.

## Syntax
````
typedef struct _NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO {
  union {
    struct {
      ULONG Unused  :30;
      ULONG Type  :1;
      ULONG Reserved2  :1;
    } Transmit;
    struct {
      ULONG MSS  :20;
      ULONG TcpHeaderOffset  :10;
      ULONG Type  :1;
      ULONG Reserved2  :1;
    } LsoV1Transmit;
    struct {
      ULONG TcpPayload  :30;
      ULONG Type  :1;
      ULONG Reserved2  :1;
    } LsoV1TransmitComplete;
    struct {
      ULONG MSS  :20;
      ULONG TcpHeaderOffset  :10;
      ULONG Type  :1;
      ULONG IPVersion  :1;
    } LsoV2Transmit;
    struct {
      ULONG Reserved  :30;
      ULONG Type  :1;
      ULONG Reserved2  :1;
    } LsoV2TransmitComplete;
    PVOID  Value;
  };
} NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO, *PNDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO;
````

## Members


## Remarks
The <b>NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</b> structure specifies information for LSOV1 and
    LSOV2 operations. The <b>NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO</b> structure is part of the
    information that is included in a 
    <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structure.

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
<div class="alert"><b>Note</b>  Any <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structure that contains the LSOv1 or LSOv2 information also
    contains a single 
    <a href="..\ndis\ns-ndis-_net_buffer.md">NET_BUFFER</a> structure.</div><div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.0 and later. Supported in NDIS 6.0 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>

<a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a>

<a href="..\ndis\ns-ndis-_net_buffer.md">NET_BUFFER</a>

<a href="https://msdn.microsoft.com/windows/hardware/drivers/network/offloading-the-segmentation-of-large-tcp-packets">Offloading the Segmentation of Large TCP Packets</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>