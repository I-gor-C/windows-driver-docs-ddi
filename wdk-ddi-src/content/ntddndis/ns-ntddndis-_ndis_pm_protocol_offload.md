---
UID: NS:ntddndis._NDIS_PM_PROTOCOL_OFFLOAD
title: "_NDIS_PM_PROTOCOL_OFFLOAD"
author: windows-driver-content
description: The NDIS_PM_PROTOCOL_OFFLOAD structure specifies parameters for a low power protocol offload to a network adapter.
old-location: netvista\ndis_pm_protocol_offload.htm
old-project: netvista
ms.assetid: 1ae68e5c-f9ea-4454-b015-82e3af0f7ccd
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_PM_PROTOCOL_OFFLOAD, NDIS_PM_PROTOCOL_OFFLOAD, NDIS_PM_PROTOCOL_OFFLOAD structure [Network Drivers Starting with Windows Vista], PNDIS_PM_PROTOCOL_OFFLOAD, PNDIS_PM_PROTOCOL_OFFLOAD structure pointer [Network Drivers Starting with Windows Vista], _NDIS_PM_PROTOCOL_OFFLOAD, miniport_power_management_ref_f8a5be81-c46e-41cd-ac96-9877e1f9ebec.xml, netvista.ndis_pm_protocol_offload, ntddndis/NDIS_PM_PROTOCOL_OFFLOAD, ntddndis/PNDIS_PM_PROTOCOL_OFFLOAD"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ntddndis.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddndis.h
api_name:
-	NDIS_PM_PROTOCOL_OFFLOAD
product:
- Windows
targetos: Windows
req.typenames: NDIS_PM_PROTOCOL_OFFLOAD, *PNDIS_PM_PROTOCOL_OFFLOAD
---

# _NDIS_PM_PROTOCOL_OFFLOAD structure
The <b>NDIS_PM_PROTOCOL_OFFLOAD</b> structure specifies parameters for a low power protocol offload to a
  network adapter.

## Syntax
```
typedef struct _NDIS_PM_PROTOCOL_OFFLOAD {
  NDIS_OBJECT_HEADER            Header;
  ULONG                         Flags;
  ULONG                         Priority;
  NDIS_PM_PROTOCOL_OFFLOAD_TYPE ProtocolOffloadType;
  NDIS_PM_COUNTED_STRING        FriendlyName;
  ULONG                         ProtocolOffloadId;
  ULONG                         NextProtocolOffloadOffset;
  union {
    struct {
      ULONG Flags;
      UCHAR RemoteIPv4Address[4];
      UCHAR HostIPv4Address[4];
      UCHAR MacAddress[6];
    } IPv4ARPParameters;
    struct {
      ULONG Flags;
      UCHAR RemoteIPv6Address[16];
      UCHAR SolicitedNodeIPv6Address[16];
      UCHAR MacAddress[6];
      UCHAR TargetIPv6Addresses[2];
    } IPv6NSParameters;
    struct {
      ULONG     Flags;
      UCHAR     KCK[DOT11_RSN_KCK_LENGTH];
      UCHAR     KEK[DOT11_RSN_KEK_LENGTH];
      ULONGLONG KeyReplayCounter;
    } Dot11RSNRekeyParameters;
  } ProtocolOffloadParameters;
  _PROTOCOL_OFFLOAD_PARAMETERS  _PROTOCOL_OFFLOAD_PARAMETERS;
} *PNDIS_PM_PROTOCOL_OFFLOAD, NDIS_PM_PROTOCOL_OFFLOAD;
```

## Members


`Header`

The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     structure (NDIS_PM_PROTOCOL_OFFLOAD). The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_PM_PROTOCOL_OFFLOAD_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_NDIS_PM_PROTOCOL_OFFLOAD_REVISION_1.

`Flags`

A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.

`Priority`

A ULONG value that contains the priority of the protocol offload. If an overlying driver adds a
     higher priority protocol offload when there are no resources that are available for more protocol offloads, NDIS
     might remove a lower priority protocol offload to free resources. Miniport drivers should ignore this
     member. Protocol drivers can provide any value within the predefined range. The following values are
     predefined:
     





#### NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_LOWEST

Specifies the lowest priority protocol offload.



#### NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_NORMAL

Specifies a normal priority protocol offload.



#### NDIS_PM_PROTOCOL_OFFLOAD_PRIORITY_HIGHEST

Specifies the highest priority protocol offload.

`ProtocolOffloadType`

An 
     <a href="https://msdn.microsoft.com/ab9f98d3-1792-43be-b838-f9dd3953889c">
     NDIS_PM_PROTOCOL_OFFLOAD_TYPE</a> value that contains the type of protocol offload.

`FriendlyName`

An 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566753">NDIS_PM_COUNTED_STRING</a> structure
     that contains the user-readable description of the low power protocol offload.

`ProtocolOffloadId`

A ULONG value that contains an NDIS-provided value that identifies the offloaded protocol. Before
     NDIS sends the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569763">OID_PM_ADD_PROTOCOL_OFFLOAD</a> OID
     request down to the underlying NDIS drivers or completes the request to the overlying driver, NDIS sets 
     <b>ProtocolOffloadId</b> to a value that is unique among the protocol offloads on a network adapter.

`NextProtocolOffloadOffset`

A ULONG value that contains an offset, in bytes. The 
     <b>NextProtocolOffloadOffset</b> member of each <b>NDIS_PM_PROTOCOL_OFFLOAD</b> structure in a list is set to
     the offset (from the beginning of the OID request 
     InformationBuffer) of the next <b>NDIS_PM_PROTOCOL_OFFLOAD</b> structure in the list. If 
     <b>NextProtocolOffloadOffset</b> is zero, the current structure is the last structure in the list.

`ProtocolOffloadParameters`

A union that contains the following member structures:

`_PROTOCOL_OFFLOAD_PARAMETERS`



## Remarks
The <b>NDIS_PM_PROTOCOL_OFFLOAD</b> structure is used in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569763">OID_PM_ADD_PROTOCOL_OFFLOAD</a> and 
    <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-pm-protocol-offload-list">
    OID_PM_PROTOCOL_OFFLOAD_LIST</a> OIDs.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.20 and later. Supported in NDIS 6.20 and later. |
| **Header** | ntddndis.h (include Ntddndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566753">NDIS_PM_COUNTED_STRING</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566765">NDIS_PM_PROTOCOL_OFFLOAD_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff569763">OID_PM_ADD_PROTOCOL_OFFLOAD</a>



<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-pm-protocol-offload-list">OID_PM_PROTOCOL_OFFLOAD_LIST</a>