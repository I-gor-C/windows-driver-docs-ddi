---
UID : NS:ndis._NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO
title : _NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO
author : windows-driver-content
description : The NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO structure specifies information that is used in offloading Internet protocol security offload version 2 (IPsecOV2) tasks from the TCP/IP transport to a NIC.
old-location : netvista\ndis_ipsec_offload_v2_net_buffer_list_info.htm
old-project : netvista
ms.assetid : f528ae2f-54fc-4edc-99bf-b1958837584b
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO, NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO, *PNDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.1 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO
req.alt-loc : ndis.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : See Remarks section
req.typenames : NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO, *PNDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO
---

# _NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO structure
<p class="CCE_Message">[The IPsec Task Offload feature is deprecated and should not be used.]

The <b>NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO</b> structure specifies information that is used in
  offloading Internet protocol security offload version 2 (IPsecOV2) tasks from the TCP/IP transport to a
  NIC.

## Syntax
````
typedef struct _NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO {
  union {
    struct {
      PVOID OffloadHandle;
    } Transmit;
    struct {
      ULONG SaDeleteReq  :1;
      ULONG CryptoDone  :1;
      ULONG NextCryptoDone  :1;
      ULONG Reserved  :13;
      ULONG CryptoStatus  :16;
    } Receive;
  };
} NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO, *PNDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO;
````

## Members


    ## Remarks
        Before the TCP/IP transport passes an outbound packet to a NIC for offload processing, the transport
    specifies the IPsec information in the NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO structure that is
    associated with the 
    <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structure.

Specifically, the TCP/IP transport supplies a value for the 
    <b>OffloadHandle</b> member in the NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO structure. The 
    <b>OffloadHandle</b> value specifies the handle to the outbound SA for a packet that has just one IPsec
    payload, regardless of whether that payload is for a transport or a tunnel SA. The 
    <b>OffloadHandle</b> value that is supplied in the NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO structure
    has the same value as the 
    <b>OffloadHandle</b> value that was reported to the TCP/IP transport when the miniport driver successfully
    added a set of SAs to a NIC. All the SAs were added to the NIC when the miniport driver responded to an 
    <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-tcp-task-ipsec-offload-v2-add-sa">
    OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA</a> request.

Before a miniport driver indicates up a receive packet that has one or more IPsec payloads, the driver
    specifies IPsec information in the NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO structure that is
    associated with the 
    <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structure.

To set and get the IPsec information, use the 
    <b>IPsecOffloadV2NetBufferListInfo</b> index with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro.
    NET_BUFFER_LIST_INFO returns the NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndis.h (include Ndis.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ndis\ns-ndis-_ndis_ipsec_offload_v1_net_buffer_list_info.md">NDIS_IPSEC_OFFLOAD_V1_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-tcp-task-ipsec-offload-v2-add-sa">
   OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-tcp-task-ipsec-offload-v2-delete-sa">
   OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>