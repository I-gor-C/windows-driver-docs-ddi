---
UID: NS:ndis._NDIS_NET_BUFFER_LIST_8021Q_INFO
title: "_NDIS_NET_BUFFER_LIST_8021Q_INFO"
author: windows-driver-content
description: The NDIS_NET_BUFFER_LIST_8021Q_INFO structure specifies 802.1Q information that is associated with a NET_BUFFER_LIST structure.
old-location: netvista\ndis_net_buffer_list_8021q_info.htm
old-project: netvista
ms.assetid: 4314d3f9-2457-41f6-844c-197e5d05b0fe
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_NET_BUFFER_LIST_8021Q_INFO, NDIS_NET_BUFFER_LIST_8021Q_INFO, NDIS_NET_BUFFER_LIST_8021Q_INFO structure [Network Drivers Starting with Windows Vista], PNDIS_NET_BUFFER_LIST_8021Q_INFO, PNDIS_NET_BUFFER_LIST_8021Q_INFO structure pointer [Network Drivers Starting with Windows Vista], _NDIS_NET_BUFFER_LIST_8021Q_INFO, ndis/NDIS_NET_BUFFER_LIST_8021Q_INFO, ndis/PNDIS_NET_BUFFER_LIST_8021Q_INFO, ndis_netbuf_structures_ref_6581b8a1-543e-46fe-a513-f8b2b6780cdd.xml, netvista.ndis_net_buffer_list_8021q_info"
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
-	NDIS_NET_BUFFER_LIST_8021Q_INFO
product: Windows
targetos: Windows
req.typenames: NDIS_NET_BUFFER_LIST_8021Q_INFO, *PNDIS_NET_BUFFER_LIST_8021Q_INFO
---

# _NDIS_NET_BUFFER_LIST_8021Q_INFO structure
The NDIS_NET_BUFFER_LIST_8021Q_INFO structure specifies 802.1Q information that is associated with a 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.

## Syntax
```
typedef struct _NDIS_NET_BUFFER_LIST_8021Q_INFO {
  union {
    struct {
      UINT32  : 3  UserPriority;
      UINT32  : 1  CanonicalFormatId;
      UINT32  : 12 VlanId;
      UINT32  : 16 Reserved;
    } TagHeader;
    PVOID Value;
    struct {
      UINT32  : 3  UserPriority;
      UINT32  : 1  CanonicalFormatId;
      UINT32  : 12 VlanId;
      UINT32  : 4  WMMInfo;
      UINT32  : 12 Reserved;
    } WLanTagHeader;
  };
} *PNDIS_NET_BUFFER_LIST_8021Q_INFO, NDIS_NET_BUFFER_LIST_8021Q_INFO;
```

## Members


## Remarks
To retrieve or insert 802.1Q information that is associated with a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure, an NDIS driver
    calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro and specifies
    the 
    <b>Ieee8021QNetBufferListInfo</b> information type.

The NET_BUFFER_LIST_INFO macro returns the pointer that is specified in the 
    <b>Value</b> member of the NDIS_NET_BUFFER_LIST_8021Q_INFO structure. The NDIS driver can use the 
    <b>TagHeader</b> or 
    <b>WLanTagHeader</b> member of the union to access specific types of information, such as 802.1p priority
    and VLAN identifier information. The 
    <b>WLanTagHeader</b> member provides access to the wireless multimedia (WMM) information in addition to
    the information that is available through the 
    <b>TagHeader</b> member.

Miniport drivers that support the 802.1Q tag in hardware must use the NDIS_NET_BUFFER_LIST_8021Q_INFO
    structure for transmit and receive operations:

<ul>
<li>
For transmit operations, the miniport driver must check for NDIS_NET_BUFFER_LIST_8021Q_INFO OOB data
      in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. The miniport
      driver must ensure that the hardware creates the 802.1Q tag from the NDIS_NET_BUFFER_LIST_8021Q_INFO
      specifications and insert it into the Ethernet frame.

</li>
<li>
For receive operations, the miniport driver must remove the 802.1Q tag from the Ethernet frame and
      map the 802.1Q tag information into the NDIS_NET_BUFFER_LIST_8021Q_INFO OOB data in the NET_BUFFER_LIST
      structure before indicating the data to NDIS with the 
      <a href="https://msdn.microsoft.com/b87dba3e-c18f-4ea2-8bd5-ec3cdafc534b">
      NdisMIndicateReceiveNetBufferLists</a> function.

</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.0 and later. Supported in NDIS 6.0 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>



<a href="https://msdn.microsoft.com/b87dba3e-c18f-4ea2-8bd5-ec3cdafc534b">
   NdisMIndicateReceiveNetBufferLists</a>