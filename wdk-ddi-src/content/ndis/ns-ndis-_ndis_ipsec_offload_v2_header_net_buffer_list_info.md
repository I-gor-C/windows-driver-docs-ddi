---
UID: NS:ndis._NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO
title: "_NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO"
author: windows-driver-content
description: The NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO structure specifies IPsec header information in the OOB data of a NET_BUFFER_LIST structure.
old-location: netvista\ndis_ipsec_offload_v2_header_net_buffer_list_info.htm
old-project: netvista
ms.assetid: 657c7941-5475-4351-a429-94003a5c21d9
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: PNDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO, ndis/NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO, NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO, ndis/PNDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO, task_offload_IPsecv2_ref_696f856b-fb77-437d-ba9d-0b00b71d1cab.xml, NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO structure [Network Drivers Starting with Windows Vista], _NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO, *PNDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO, netvista.ndis_ipsec_offload_v2_header_net_buffer_list_info, PNDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO structure pointer [Network Drivers Starting with Windows Vista]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.1 and later.
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
-	NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO
product: Windows
targetos: Windows
req.typenames: NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO, *PNDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO
---

# _NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO structure
<p class="CCE_Message">[The IPsec Task Offload feature is deprecated and should not be used.]

The NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO structure specifies IPsec header information in
  the OOB data of a 
  <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structure.

## Syntax
````
typedef struct _NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO {
  union {
    struct {
      ULONG NextHeader  :8;
      ULONG PadLength  :8;
      ULONG AhHeaderOffset  :8;
      ULONG EspHeaderOffset  :8;
    } Transmit;
    struct {
      ULONG NextHeader  :8;
      ULONG PadLength  :8;
      ULONG HeaderInfoSet  :1;
    } Receive;
  };
} NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO, *PNDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO;
````

## Members


## Remarks
The information in the NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO structure makes it easy for
    the miniport driver to parse an outbound packet. NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO
    specifies the header offsets for IPsec headers in the 
    <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structure as well as the
    location of the next header and the padding length.

To set and get the IPsec tunnel information, use the 
    <b>IPsecOffloadV2HeaderNetBufferListInfo</b> index with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro.
    NET_BUFFER_LIST_INFO returns an NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.1 and later. Supported in NDIS 6.1 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>

<a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>