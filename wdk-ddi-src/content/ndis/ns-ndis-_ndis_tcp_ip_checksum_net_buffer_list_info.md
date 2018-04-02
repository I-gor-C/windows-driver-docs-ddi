---
UID: NS:ndis._NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO
title: "_NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO"
author: windows-driver-content
description: The NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO structure specifies information used in offloading checksum tasks from the TCP/IP transport to a NIC.
old-location: netvista\ndis_tcp_ip_checksum_net_buffer_list_info.htm
old-project: netvista
ms.assetid: 989ecf50-18c4-4977-b845-b3fea0cade47
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO, NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO, NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO structure [Network Drivers Starting with Windows Vista], PNDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO, PNDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO structure pointer [Network Drivers Starting with Windows Vista], _NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO, ndis/NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO, ndis/PNDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO, netvista.ndis_tcp_ip_checksum_net_buffer_list_info, tcpip_offload_ref_2ce657f6-a894-420b-bcb0-310819237c5b.xml"
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
-	NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO
product:
- Windows
targetos: Windows
req.typenames: NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO, *PNDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO
---

# _NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO structure
The <b>NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</b> structure specifies information used in offloading
  checksum tasks from the TCP/IP transport to a NIC. The <b>NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</b> structure
  is part of the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> information (out-of-band data)
  that is associated with a <b>NET_BUFFER_LIST</b> structure.

## Syntax
```
typedef struct _NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO {
  union {
    struct {
      ULONG  : 1  IsIPv4;
      ULONG  : 1  IsIPv6;
      ULONG  : 1  TcpChecksum;
      ULONG  : 1  UdpChecksum;
      ULONG  : 1  IpHeaderChecksum;
      ULONG  : 11 Reserved;
      ULONG  : 10 TcpHeaderOffset;
    } Transmit;
    PVOID Value;
    struct {
      ULONG  : 1 TcpChecksumFailed;
      ULONG  : 1 UdpChecksumFailed;
      ULONG  : 1 IpChecksumFailed;
      ULONG  : 1 TcpChecksumSucceeded;
      ULONG  : 1 UdpChecksumSucceeded;
      ULONG  : 1 IpChecksumSucceeded;
      ULONG  : 1 Loopback;
      ULONG  : 1 TcpChecksumValueInvalid;
      ULONG  : 1 IpChecksumValueInvalid;
    } Receive;
  };
} NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO, *PNDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO;
```

## Members


## Remarks
The <b>NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</b> structure specifies information that is used in
    offloading checksum tasks from the TCP/IP transport to a NIC. The
    <b>NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</b> structure is part of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> information (out-of-band
    data) that is associated with a <b>NET_BUFFER_LIST</b> structure.

Before the TCP/IP transport passes to the miniport driver a TCP/IP packet on which the miniport driver
    will perform checksum tasks, the TCP/IP transport updates the <b>NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</b>
    structure that is associated with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. Specifically, the TCP/IP transport sets
    the 
    <b>IsIPv4</b> or 
    <b>IsIPv6</b> flag to indicate that the send packet is an IPv4 or IPv6 packet. If the TCP/IP transport
    does not set either the 
    <b>IsIPv4</b> or 
    <b>IsIPv6</b> flag, the miniport driver should not perform checksum tasks on the packet. If the TCP/IP
    transport sets the 
    <b>IsIPv4</b> or 
    <b>IsIPv6</b> flag, it also sets the 
    <b>IpHeaderChecksum</b>, <b>TcpChecksum</b>, or 
    <b>UdpChecksum</b> flags that are required to indicate which checksums the miniport driver should
    calculate for the packet.

Before indicating up a receive TCP/IP packet on which it performs checksum tasks, a miniport driver
    sets the appropriate 
    Xxx<b>ChecksumFailed</b> or 
    Xxx<b>ChecksumSucceeded</b> flags in the <b>NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</b> structure.

<div class="alert"><b>Note</b>  Checksum offload is disabled until the miniport receives <a href="https://msdn.microsoft.com/library/windows/hardware/ff569762">OID_OFFLOAD_ENCAPSULATION</a>. After it receives this OID, the miniport is then permitted to start validating the checksums on some received packets. The miniport is not required to validate the checksum on every packet; if both the Xxx<b>ChecksumFailed</b> and Xxx<b>ChecksumSucceeded</b> flags are clear, the OS will fall back to validating the checksum in software.</div>
<div> </div>
To obtain the <b>NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO</b> structure, a driver should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro with an 
    <i>_Id</i> of 
    <b>TcpIpChecksumNetBufferListInfo</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.0 and later. Supported in NDIS 6.0 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/79A37DAB-D9B3-4FA2-8258-05E10BD6E3CB">Indicating Coalesced Segments</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>