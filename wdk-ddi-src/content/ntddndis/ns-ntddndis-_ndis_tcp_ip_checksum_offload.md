---
UID : NS:ntddndis._NDIS_TCP_IP_CHECKSUM_OFFLOAD
title : _NDIS_TCP_IP_CHECKSUM_OFFLOAD
author : windows-driver-content
description : The NDIS_TCP_IP_CHECKSUM_OFFLOAD structure provides checksum task offload information in the NDIS_OFFLOAD structure.
old-location : netvista\ndis_tcp_ip_checksum_offload.htm
old-project : netvista
ms.assetid : bf5369c5-8656-41a4-a23f-79e40a60d111
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : tcpip_offload_ref_0214ebce-2667-42c6-8be6-6086d358d2ab.xml, PNDIS_TCP_IP_CHECKSUM_OFFLOAD, _NDIS_TCP_IP_CHECKSUM_OFFLOAD, netvista.ndis_tcp_ip_checksum_offload, ntddndis/NDIS_TCP_IP_CHECKSUM_OFFLOAD, *PNDIS_TCP_IP_CHECKSUM_OFFLOAD, ntddndis/PNDIS_TCP_IP_CHECKSUM_OFFLOAD, NDIS_TCP_IP_CHECKSUM_OFFLOAD structure [Network Drivers Starting with Windows Vista], PNDIS_TCP_IP_CHECKSUM_OFFLOAD structure pointer [Network Drivers Starting with Windows Vista], NDIS_TCP_IP_CHECKSUM_OFFLOAD
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.0 and later.
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
req.typenames : NDIS_TCP_IP_CHECKSUM_OFFLOAD, *PNDIS_TCP_IP_CHECKSUM_OFFLOAD
---

# _NDIS_TCP_IP_CHECKSUM_OFFLOAD structure
The NDIS_TCP_IP_CHECKSUM_OFFLOAD structure provides checksum task offload information in the 
  <a href="..\ntddndis\ns-ntddndis-_ndis_offload.md">NDIS_OFFLOAD</a> structure.

## Syntax
````
typedef struct _NDIS_TCP_IP_CHECKSUM_OFFLOAD {
  struct {
    ULONG Encapsulation;
    ULONG IpOptionsSupported  :2;
    ULONG TcpOptionsSupported  :2;
    ULONG TcpChecksum  :2;
    ULONG UdpChecksum  :2;
    ULONG IpChecksum  :2;
  } IPv4Transmit;
  struct {
    ULONG Encapsulation;
    ULONG IpOptionsSupported  :2;
    ULONG TcpOptionsSupported  :2;
    ULONG TcpChecksum  :2;
    ULONG UdpChecksum  :2;
    ULONG IpChecksum  :2;
  } IPv4Receive;
  struct {
    ULONG Encapsulation;
    ULONG IpExtensionHeadersSupported  :2;
    ULONG TcpOptionsSupported  :2;
    ULONG TcpChecksum  :2;
    ULONG UdpChecksum  :2;
  } IPv6Transmit;
  struct {
    ULONG Encapsulation;
    ULONG IpExtensionHeadersSupported  :2;
    ULONG TcpOptionsSupported  :2;
    ULONG TcpChecksum  :2;
    ULONG UdpChecksum  :2;
  } IPv6Receive;
} NDIS_TCP_IP_CHECKSUM_OFFLOAD, *PNDIS_TCP_IP_CHECKSUM_OFFLOAD;
````

## Members


`IPv4Receive`

A structure within NDIS_TCP_IP_CHECKSUM_OFFLOAD that specifies IPv4 receive information and that
     contains the following members:

`IPv4Transmit`

A structure within NDIS_TCP_IP_CHECKSUM_OFFLOAD that specifies IPv4 transmit information and that
     contains the following members:

`IPv6Receive`

A structure within NDIS_TCP_IP_CHECKSUM_OFFLOAD that specifies IPv6 receive information and that
     contains the following members:

`IPv6Transmit`

A structure within NDIS_TCP_IP_CHECKSUM_OFFLOAD that specifies IPv6 transmit information and that
     contains the following members:

## Remarks
The NDIS_TCP_IP_CHECKSUM_OFFLOAD structure is used in the 
    <b>Checksum</b> member of the 
    <a href="..\ntddndis\ns-ntddndis-_ndis_offload.md">NDIS_OFFLOAD</a> structure. The
    NDIS_TCP_IP_CHECKSUM_OFFLOAD structure specifies the current or supported services that a miniport
    adapter provides for calculating IP, TCP, or UDP checksums (or all of them) for send packets and
    validating such checksums for receive packets.

NDIS_OFFLOAD is used in the 
    <mshelp:link keywords="netvista.ndis_miniport_adapter_offload_attributes" tabindex="0"><b>
    NDIS_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES</b></mshelp:link> structure, 
    <a href="..\ndis\ns-ndis-_ndis_bind_parameters.md">NDIS_BIND_PARAMETERS</a> structure, 
    <mshelp:link keywords="netvista.ndis_filter_attach_parameters" tabindex="0"><b>
    NDIS_FILTER_ATTACH_PARAMETERS</b></mshelp:link> structure, 
    <mshelp:link keywords="netvista.oid_tcp_offload_current_config" tabindex="0">
    OID_TCP_OFFLOAD_CURRENT_CONFIG</mshelp:link> OID, and the 
    <mshelp:link keywords="netvista.ndis_status_task_offload_current_config" tabindex="0"><b>
    NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</b></mshelp:link> status indication.

For 
    <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-tcp-offload-current-config">OID_TCP_OFFLOAD_CURRENT_CONFIG</a>,
    the NDIS_OFFLOAD structure specifies the task offload capabilities that a miniport adapter supports. If
    the current offloads capabilities change, a miniport driver reports the new capabilities in an 
    <mshelp:link keywords="netvista.ndis_status_task_offload_current_config" tabindex="0"><b>
    NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</b></mshelp:link> status indication.

The 
    <b>Encapsulation</b> members of NDIS_TCP_IP_CHECKSUM_OFFLOAD define the checksum offload encapsulation
    settings for the miniport adapter.

In response to an 
    <mshelp:link keywords="netvista.oid_tcp_offload_current_config" tabindex="0">
    OID_TCP_OFFLOAD_CURRENT_CONFIG</mshelp:link> query request, NDIS provides a bitwise OR of the encapsulation
    flags, which indicate the supported encapsulation settings, in each of the 
    <b>Encapsulation</b> members. Miniport drivers must provide Ethernet encapsulation
    (NDIS_ENCAPSULATION_IEEE_802_3). The other types of encapsulation are optional.

For an 
    <mshelp:link keywords="netvista.ndis_status_task_offload_current_config" tabindex="0"><b>
    NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</b></mshelp:link> status indication, the miniport driver provides a bitwise
    OR of the encapsulation flags, which indicate the current capabilities, in each of the 
    <b>Encapsulation</b> members.

The following flags are defined for the 
    <b>Encapsulation</b> members:



The meaning of the values in the 
    <b>IpOptionsSupported</b>, 
    <b>TcpOptionsSupported</b>, 
    <b>IpExtensionHeadersSupported</b>, 
    <b>TcpChecksum</b>, 
    <b>UdpChecksum</b>, and 
    <b>IpChecksum</b> members of <b>NDIS_TCP_IP_CHECKSUM_OFFLOAD</b> depends on which OID or status indication
    includes the task offload structure: These members can have one of the following values:

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-tcp-offload-current-config">OID_TCP_OFFLOAD_CURRENT_CONFIG</a>

<a href="..\ndis\ns-ndis-_ndis_oid_request.md">NDIS_OID_REQUEST</a>

<mshelp:link keywords="netvista.ndis_miniport_adapter_offload_attributes" tabindex="0"><b>
   NDIS_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES</b></mshelp:link>

<a href="..\ndis\ns-ndis-_ndis_bind_parameters.md">NDIS_BIND_PARAMETERS</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_offload.md">NDIS_OFFLOAD</a>

<mshelp:link keywords="netvista.ndis_status_task_offload_current_config" tabindex="0"><b>
   NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</b></mshelp:link>

<a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a>

<a href="..\ndis\ns-ndis-_ndis_filter_attach_parameters.md">NDIS_FILTER_ATTACH_PARAMETERS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_TCP_IP_CHECKSUM_OFFLOAD structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>