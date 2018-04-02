---
UID: NS:ndis._NDIS_PD_PROVIDER_DISPATCH
title: "_NDIS_PD_PROVIDER_DISPATCH"
author: windows-driver-content
description: This structure is used as input for the OID_PD_OPEN_PROVIDER and serves as a container for all the provider's driver routines.
old-location: netvista\ndis_pd_provider_dispatch.htm
old-project: netvista
ms.assetid: E93B8A07-7C06-470B-9B26-8D59C2685D2C
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NDIS_PD_PROVIDER_DISPATCH, NDIS_PD_PROVIDER_DISPATCH structure [Network Drivers Starting with Windows Vista], PNDIS_PD_PROVIDER_DISPATCH, PNDIS_PD_PROVIDER_DISPATCH structure pointer [Network Drivers Starting with Windows Vista], _NDIS_PD_PROVIDER_DISPATCH, ndis/NDIS_PD_PROVIDER_DISPATCH, ndis/PNDIS_PD_PROVIDER_DISPATCH, netvista.ndis_pd_provider_dispatch
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	NDIS_PD_PROVIDER_DISPATCH
product: Windows
targetos: Windows
req.typenames: NDIS_PD_PROVIDER_DISPATCH
---

# _NDIS_PD_PROVIDER_DISPATCH structure
This structure is used as input for the <a href="https://msdn.microsoft.com/library/windows/hardware/dn931852">OID_PD_OPEN_PROVIDER</a> and serves as a container for all the provider's driver routines.

## Syntax
```
typedef struct _NDIS_PD_PROVIDER_DISPATCH {
  NDIS_OBJECT_HEADER                         Header;
  ULONG                                      Flags;
  NDIS_PD_ALLOCATE_QUEUE_HANDLER             NdisPDAllocateQueue;
  NDIS_PD_FREE_QUEUE_HANDLER                 NdisPDFreeQueue;
  NDIS_PD_ACQUIRE_RECEIVE_QUEUES_HANDLER     NdisPDAcquireReceiveQueues;
  NDIS_PD_RELEASE_RECEIVE_QUEUES_HANDLER     NdisPDReleaseReceiveQueues;
  NDIS_PD_ALLOCATE_COUNTER_HANDLER           NdisPDAllocateCounter;
  NDIS_PD_FREE_COUNTER_HANDLER               NdisPDFreeCounter;
  NDIS_PD_QUERY_COUNTER_HANDLER              NdisPDQueryCounter;
  NDIS_PD_SET_RECEIVE_FILTER_HANDLER         NdisPDSetReceiveFilter;
  NDIS_PD_CLEAR_RECEIVE_FILTER_HANDLER       NdisPDClearReceiveFilter;
  NDIS_PD_REQUEST_DRAIN_NOTIFICATION_HANDLER NdisPDRequestDrainNotification;
  NDIS_PD_QUEUE_CONTROL_HANDLER              NdisPDQueueControl;
  NDIS_PD_PROVIDER_CONTROL_HANDLER           NdisPDProviderControl;
} NDIS_PD_PROVIDER_DISPATCH;
```

## Members


`Header`

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the <b>NDIS_PD_PROVIDER_DISPATCH</b> structure. Set the members of this structure as follows:

<ul>
<li><b>Type</b> = <b>NDIS_OBJECT_TYPE_DEFAULT</b></li>
<li><b>Revision</b> = <b>NDIS_PD_PROVIDER_DISPATCH_REVISION_1</b></li>
<li><b>Size</b> = <b>NDIS_SIZEOF_PD_PROVIDER_DISPATCH_REVISION_1</b></li>
</ul>

`Flags`

This member is reserved and must be set to 0 by the provider.

`NdisPDAllocateQueue`

See <a href="https://msdn.microsoft.com/E9091C69-0E21-40CC-B3D3-1F770ABA0D47">NdisPDAllocateQueue</a>.

`NdisPDFreeQueue`

See <a href="https://msdn.microsoft.com/1DE8582C-AF11-4CBA-8F4C-159266A7F3BA">NdisPDFreeQueue</a>.

`NdisPDAcquireReceiveQueues`



`NdisPDReleaseReceiveQueues`



`NdisPDAllocateCounter`

See <a href="https://msdn.microsoft.com/86AA537D-952F-4A7A-ACA4-24B8C1AE932A">NdisPDAllocateCounter</a>.

`NdisPDFreeCounter`

See <a href="https://msdn.microsoft.com/60C47437-A999-4F82-B144-6F77410E5C07">NdisPDFreeCounter</a>.

`NdisPDQueryCounter`

See <a href="https://msdn.microsoft.com/C4860A43-2C53-4967-81A8-41FFF5CD2A5E">NdisPDQueryCounter</a>.

`NdisPDSetReceiveFilter`

See <a href="https://msdn.microsoft.com/49587142-9C84-4F73-BE0C-D256A8E6BF4B">NdisPDSetReceiveFilter</a>.

`NdisPDClearReceiveFilter`

See <a href="https://msdn.microsoft.com/C91F2E5D-C37F-48A9-9AE0-F5A8C5D8F54D">NdisPDClearReceiveFilter</a>.

`NdisPDRequestDrainNotification`



`NdisPDQueueControl`



`NdisPDProviderControl`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | ndis.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>