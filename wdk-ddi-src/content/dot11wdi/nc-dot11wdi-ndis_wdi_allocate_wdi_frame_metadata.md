---
UID: NC:dot11wdi.NDIS_WDI_ALLOCATE_WDI_FRAME_METADATA
title: NDIS_WDI_ALLOCATE_WDI_FRAME_METADATA
author: windows-driver-content
description: The NdisWdiAllocateWiFiFrameMetaData callback function allocates a frame metadata buffer.
old-location: netvista\ndiswdiallocatewdiframemetadata.htm
old-project: netvista
ms.assetid: 6C565DAF-3363-466F-AC4A-9DB534E581FC
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NDIS_WDI_ALLOCATE_WDI_FRAME_METADATA, NdisWdiAllocateWiFiFrameMetaData, NdisWdiAllocateWiFiFrameMetaData callback function [Network Drivers Starting with Windows Vista], dot11wdi/NdisWdiAllocateWiFiFrameMetaData, netvista.ndiswdiallocatewdiframemetadata
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dot11wdi.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	dot11wdi.h
api_name:
-	NdisWdiAllocateWiFiFrameMetaData
product:
- Windows
targetos: Windows
req.typenames: SYNTH_STATS, *PSYNTH_STATS
---


# NDIS_WDI_ALLOCATE_WDI_FRAME_METADATA callback function
The NdisWdiAllocateWiFiFrameMetaData callback function  allocates a frame metadata buffer.

This is a callback inside <a href="https://msdn.microsoft.com/library/windows/hardware/mt297620">NDIS_WDI_DATA_API</a>.

## Syntax

```
NDIS_WDI_ALLOCATE_WDI_FRAME_METADATA NdisWdiAllocateWdiFrameMetadata;

PWDI_FRAME_METADATA NdisWdiAllocateWdiFrameMetadata(
  NDIS_HANDLE NdisMiniportDataPathHandle
)
{...}
```

## Parameters

`NdisMiniportDataPathHandle`

The NdisMiniportDataPathHandle passed to the IHV miniport in <a href="https://msdn.microsoft.com/C297D681-D43F-4105-9E08-7FF42807E9A0">MiniportWdiTalTxRxInitialize</a>.


## Return Value

The allocated frame metadata buffer.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | dot11wdi.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt297620">NDIS_WDI_DATA_API</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn897827">WDI_FRAME_METADATA</a>