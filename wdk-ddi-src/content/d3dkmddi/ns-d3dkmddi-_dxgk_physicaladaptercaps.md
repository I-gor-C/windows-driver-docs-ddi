---
UID : NS:d3dkmddi._DXGK_PHYSICALADAPTERCAPS
title : _DXGK_PHYSICALADAPTERCAPS
author : windows-driver-content
description : The DXGK_PHYSICALADAPTERCAPS structure is used to report details of a physical adapter.
old-location : display\dxgk_physicaladaptercaps.htm
old-project : display
ms.assetid : 8D075473-605F-4B75-BB02-5B182EEB3B5F
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_PHYSICALADAPTERCAPS, DXGK_PHYSICALADAPTERCAPS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmddi.h
req.include-header : D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_PHYSICALADAPTERCAPS
req.alt-loc : d3dkmddi.h
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
req.typenames : DXGK_PHYSICALADAPTERCAPS
---

# _DXGK_PHYSICALADAPTERCAPS structure
The <b>DXGK_PHYSICALADAPTERCAPS</b> structure is used to report details of a physical adapter.

## Syntax
````
typedef struct _DXGK_PHYSICALADAPTERCAPS {
  WORD                      NumExecutionNodes;
  WORD                      PagingNodeIndex;
  HANDLE                    DxgkPhysicalAdapterHandle;
  DXGK_PHYSICALADAPTERFLAGS Flags;
  UINT                      VPRPagingNode;
} DXGK_PHYSICALADAPTERCAPS;
````

## Members

        
            `DxgkPhysicalAdapterHandle`

            Handle, which is passed to the kernel mode driver as <b>DXGKRNL_INTERFACE::DeviceHandle</b> in <a href="..\dispmprt\nc-dispmprt-dxgkddi_start_device.md">DxgkDdiStartDevice</a>.
        
            `Flags`

            <table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `NumExecutionNodes`

            The number of execution nodes in the physical adapter.
        
            `PagingNodeIndex`

            Index of the paging node for the physical adapter.
        
            `VPRPagingNode`

            Index of the node to be used for move paging in  the VPR.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |