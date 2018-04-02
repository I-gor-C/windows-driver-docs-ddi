---
UID: NS:ndis._NDIS_PD_FILTER_PARAMETERS
title: "_NDIS_PD_FILTER_PARAMETERS"
author: windows-driver-content
description: This structure holds metadata for a packet filter.
old-location: netvista\ndis_pd_filter_parameters.htm
old-project: netvista
ms.assetid: AE220435-C8EC-408E-8177-A88FC858FA5A
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NDIS_PD_FILTER_PARAMETERS, NDIS_PD_FILTER_PARAMETERS structure [Network Drivers Starting with Windows Vista], _NDIS_PD_FILTER_PARAMETERS, ndis/NDIS_PD_FILTER_PARAMETERS, netvista.ndis_pd_filter_parameters
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
-	NDIS_PD_FILTER_PARAMETERS
product:
- Windows
targetos: Windows
req.typenames: NDIS_PD_FILTER_PARAMETERS
---

# _NDIS_PD_FILTER_PARAMETERS structure
This structure holds metadata for a packet filter.

## Syntax
```
typedef struct _NDIS_PD_FILTER_PARAMETERS {
  NDIS_OBJECT_HEADER     Header;
  ULONG                  Flags;
  NDIS_GFP_PROFILE_ID    MatchProfileId;
  ULONG                  Priority;
  NDIS_PD_COUNTER_HANDLE CounterHandle;
  NDIS_PD_QUEUE          *TargetReceiveQueue;
  ULONG64                RxFilterContext;
  PUCHAR                 HeaderGroupMatchArray;
  ULONG                  HeaderGroupMatchArrayNumElements;
  ULONG                  HeaderGroupMatchArrayElementSize;
  ULONG                  HeaderGroupMatchArrayTotalSize;
} NDIS_PD_FILTER_PARAMETERS;
```

## Members


`Header`

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the <b>NDIS_PD_FILTER_PARAMETERS</b> structure. Set the members of this structure as follows:

<ul>
<li><b>Type</b> = <b>NDIS_OBJECT_TYPE_DEFAULT</b></li>
<li><b>Revision</b> = <b>NDIS_PD_FILTER_PARAMETERS_REVISION_1</b></li>
<li><b>Size</b> = <b>NDIS_SIZEOF_PD_FILTER_PARAMETERS_REVISION_1</b></li>
</ul>

`Flags`

This member is reserved and must be set to 0 by the client. It is ignored by the provider.

`MatchProfileId`

This value is used to determine if the HeaderGroupMatchArray members describe an NDIS_GFP_HEADER_GROUP_EXACT_MATCH array or a NDIS_GFP_HEADER_GROUP_WILDCARD_MATCH array.

`Priority`

The priority of this filter.

`CounterHandle`

A handle to a counter.

`TargetReceiveQueue`

The target receive queue to filter.

`RxFilterContext`

The context for the receive filter.

`HeaderGroupMatchArray`

An array of either NDIS_GFP_HEADER_GROUP_EXACT_MATCH or NDIS_GFP_HEADER_GROUP_WILDCARD_MATCH elements as determined by the MatchProfileId member.

`HeaderGroupMatchArrayNumElements`

The number of elements for the HeaderGroupMatchArray.

`HeaderGroupMatchArrayElementSize`

The size of each element for the HeaderGroupMatchArray.

`HeaderGroupMatchArrayTotalSize`

The total size of the HeaderGroupMatchArray.

## Remarks
This structure must be aligned on an 8-byte boundary.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | ndis.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>