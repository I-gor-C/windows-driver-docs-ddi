---
UID : NS:ntddndis._NDIS_IPSEC_OFFLOAD_V1
title : _NDIS_IPSEC_OFFLOAD_V1
author : windows-driver-content
description : The NDIS_IPSEC_OFFLOAD_V1 structure provides Internet protocol security (IPsec) task offload information in the NDIS_OFFLOAD structure.Note  NDIS_IPSEC_OFFLOAD_V1 is only for NDIS 6.0.
old-location : netvista\ndis_ipsec_offload_v1.htm
old-project : netvista
ms.assetid : 8ec0a052-2327-41e5-a9fa-83bcac9566f7
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : IPSEC_TPT_UDPESP_ENCAPTYPE_IKE, ntddndis/NDIS_IPSEC_OFFLOAD_V1, NDIS_IPSEC_OFFLOAD_V1, NDIS_IPSEC_OFFLOAD_V1 structure [Network Drivers Starting with Windows Vista], IPSEC_TPTOVERTUN_UDPESP_ENCAPTYPE_IKE, IPSEC_TPT_UDPESP_ENCAPTYPE_OTHER, *PNDIS_IPSEC_OFFLOAD_V1, ntddndis/PNDIS_IPSEC_OFFLOAD_V1, PNDIS_IPSEC_OFFLOAD_V1 structure pointer [Network Drivers Starting with Windows Vista], IPSEC_TPT_UDPESP_OVER_PURE_TUN_ENCAPTYPE_IKE, netvista.ndis_ipsec_offload_v1, IPSEC_TUN_UDPESP_ENCAPTYPE_OTHER, IPSEC_TPTOVERTUN_UDPESP_ENCAPTYPE_OTHER, PNDIS_IPSEC_OFFLOAD_V1, tcpip_offload_ref_8e1eae6b-44e5-425b-8312-ec890b8eb757.xml, IPSEC_TPT_UDPESP_OVER_PURE_TUN_ENCAPTYPE_OTHER, IPSEC_TUN_UDPESP_ENCAPTYPE_IKE, _NDIS_IPSEC_OFFLOAD_V1
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.0.
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
req.typenames : NDIS_IPSEC_OFFLOAD_V1, *PNDIS_IPSEC_OFFLOAD_V1
---

# _NDIS_IPSEC_OFFLOAD_V1 structure
The <b>NDIS_IPSEC_OFFLOAD_V1</b> structure provides Internet protocol security (IPsec) task offload
  information in the 
  <a href="..\ntddndis\ns-ntddndis-_ndis_offload.md">NDIS_OFFLOAD</a> structure.
<div class="alert"><b>Note</b>  <b>NDIS_IPSEC_OFFLOAD_V1</b> is only for NDIS 6.0. For NDIS 6.1 and later, use <a href="..\ntddndis\ns-ntddndis-_ndis_ipsec_offload_v2.md">NDIS_IPSEC_OFFLOAD_V2</a>.</div><div> </div>

## Syntax
````
typedef struct _NDIS_IPSEC_OFFLOAD_V1 {
  struct {
    ULONG Encapsulation;
    ULONG AhEspCombined;
    ULONG TransportTunnelCombined;
    ULONG IPv4Options;
    ULONG Flags;
  } Supported;
  struct {
    ULONG Md5  :2;
    ULONG Sha_1  :2;
    ULONG Transport  :2;
    ULONG Tunnel  :2;
    ULONG Send  :2;
    ULONG Receive  :2;
  } IPv4AH;
  struct {
    ULONG Des  :2;
    ULONG Reserved  :2;
    ULONG TripleDes  :2;
    ULONG NullEsp  :2;
    ULONG Transport  :2;
    ULONG Tunnel  :2;
    ULONG Send  :2;
    ULONG Receive  :2;
  } IPv4ESP;
} NDIS_IPSEC_OFFLOAD_V1, *PNDIS_IPSEC_OFFLOAD_V1;
````

## Members


`IPv4AH`

A structure within NDIS_IPSEC_OFFLOAD_V1 that specifies support for AH payloads and that contains
     the following information:

`IPv4ESP`

A structure within NDIS_IPSEC_OFFLOAD_V1 that specifies support for ESP payloads and that contains
     the following information:

`Supported`

A structure within NDIS_IPSEC_OFFLOAD_V1 that specifies support for IPsec task offload and that
     contains the following information:

## Remarks
The <b>NDIS_IPSEC_OFFLOAD_V1</b> structure is used in the 
    <b>IPsecV1</b> member of the 
    <a href="..\ntddndis\ns-ntddndis-_ndis_offload.md">NDIS_OFFLOAD</a> structure. The
    NDIS_IPSEC_OFFLOAD_V1 structure specifies the current or supported services that a miniport adapter
    provides for Internet protocol security (IPsec).


<a href="..\ntddndis\ns-ntddndis-_ndis_offload.md">NDIS_OFFLOAD</a> is used in the 
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
    the <a href="..\ntddndis\ns-ntddndis-_ndis_offload.md">NDIS_OFFLOAD</a> structure specifies the task offload capabilities that a miniport adapter supports. If
    the current offloads capabilities change, a miniport driver reports the new capabilities in an 
    <mshelp:link keywords="netvista.ndis_status_task_offload_current_config" tabindex="0"><b>
    NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</b></mshelp:link> status indication.

The 
    <b>Encapsulation</b> member of <b>NDIS_IPSEC_OFFLOAD_V1</b> defines the IPsec offload encapsulation settings for
    the miniport adapter.

In response to an 
    <mshelp:link keywords="netvista.oid_tcp_offload_current_config" tabindex="0">
    OID_TCP_OFFLOAD_CURRENT_CONFIG</mshelp:link> query request, NDIS provides a bitwise OR of the encapsulation
    flags, which indicate the supported encapsulation settings, in the 
    <b>Encapsulation</b> member. Miniport drivers must provide Ethernet encapsulation
    (NDIS_ENCAPSULATION_IEEE_802_3). The other types of encapsulation are optional.

For an 
    <mshelp:link keywords="netvista.ndis_status_task_offload_current_config" tabindex="0"><b>
    NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</b></mshelp:link> status indication, the miniport driver provides a bitwise
    OR of the encapsulation flags, which indicate the current capabilities, in the 
    <b>Encapsulation</b> member.

The following flags are defined for the 
    <b>Encapsulation</b> member:

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

<a href="..\ntddndis\ns-ntddndis-_ndis_ipsec_offload_v2.md">NDIS_IPSEC_OFFLOAD_V2</a>

<mshelp:link keywords="netvista.ndis_miniport_adapter_offload_attributes" tabindex="0"><b>
   NDIS_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES</b></mshelp:link>

<a href="..\ndis\ns-ndis-_ndis_bind_parameters.md">NDIS_BIND_PARAMETERS</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_offload.md">NDIS_OFFLOAD</a>

<mshelp:link keywords="netvista.ndis_status_task_offload_current_config" tabindex="0"><b>
   NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG</b></mshelp:link>

<a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a>

<a href="..\ndis\ns-ndis-_ndis_filter_attach_parameters.md">NDIS_FILTER_ATTACH_PARAMETERS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_IPSEC_OFFLOAD_V1 structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>