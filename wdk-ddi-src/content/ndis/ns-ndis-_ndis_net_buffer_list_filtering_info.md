---
UID: NS:ndis._NDIS_NET_BUFFER_LIST_FILTERING_INFO
title: "_NDIS_NET_BUFFER_LIST_FILTERING_INFO"
author: windows-driver-content
description: The NDIS_NET_BUFFER_LIST_FILTERING_INFO structure defines filtering information that is associated with a NET_BUFFER_LIST structure.
old-location: netvista\ndis_net_buffer_list_filtering_info.htm
old-project: netvista
ms.assetid: 992a4c77-e22f-4123-81e8-86c8030accfa
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_NET_BUFFER_LIST_FILTERING_INFO, NDIS_NET_BUFFER_LIST_FILTERING_INFO, NDIS_NET_BUFFER_LIST_FILTERING_INFO structure [Network Drivers Starting with Windows Vista], PNDIS_NET_BUFFER_LIST_FILTERING_INFO, PNDIS_NET_BUFFER_LIST_FILTERING_INFO structure pointer [Network Drivers Starting with Windows Vista], _NDIS_NET_BUFFER_LIST_FILTERING_INFO, ndis/NDIS_NET_BUFFER_LIST_FILTERING_INFO, ndis/PNDIS_NET_BUFFER_LIST_FILTERING_INFO, ndis_netbuf_macros_media_specific_ad9f53c1-d93a-4b73-9903-76aa54acd563.xml, netvista.ndis_net_buffer_list_filtering_info"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
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
-	NDIS_NET_BUFFER_LIST_FILTERING_INFO
product: Windows
targetos: Windows
req.typenames: NDIS_NET_BUFFER_LIST_FILTERING_INFO, *PNDIS_NET_BUFFER_LIST_FILTERING_INFO
---

# _NDIS_NET_BUFFER_LIST_FILTERING_INFO structure
The <b>NDIS_NET_BUFFER_LIST_FILTERING_INFO</b> structure defines filtering information that is associated
  with a 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.

## Syntax
```
typedef struct _NDIS_NET_BUFFER_LIST_FILTERING_INFO {
  union {
    struct {
      USHORT FilterId;
      union {
        USHORT QueueId;
        USHORT VPortId;
      } QueueVPortInfo;
    } FilteringInfo;
    PVOID Value;
  };
} *PNDIS_NET_BUFFER_LIST_FILTERING_INFO, NDIS_NET_BUFFER_LIST_FILTERING_INFO;
```

## Members


## Remarks
Starting with NDIS 6.20, miniport drivers  use the <b>NDIS_NET_BUFFER_LIST_FILTERING_INFO</b> structure to specify receive
    filter information that accompanies the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures that are associated with a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.

To access the <b>NDIS_NET_BUFFER_LIST_FILTERING_INFO</b> structure from the NET_BUFFER_LIST OOB data, an NDIS
    driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro and specifies
    the 
    <b>NetBufferListFilteringInfo</b>  information type.

To access the identifier values directly, use the 
    <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff568406">
    NET_BUFFER_LIST_RECEIVE_FILTER_ID</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh439946">NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID</a>, or 
    <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff568407">
    NET_BUFFER_LIST_RECEIVE_QUEUE_ID</a> macros.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.20 and later. Supported in NDIS 6.20 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>



<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff568406">
   NET_BUFFER_LIST_RECEIVE_FILTER_ID</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439946">NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID</a>



<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff568407">
   NET_BUFFER_LIST_RECEIVE_QUEUE_ID</a>