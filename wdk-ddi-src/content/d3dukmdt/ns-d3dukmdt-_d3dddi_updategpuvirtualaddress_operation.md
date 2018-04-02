---
UID: NS:d3dukmdt._D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION
title: "_D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION"
author: windows-driver-content
description: D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION describes a virtual address update operation.
old-location: display\d3dddi_updategpuvirtualaddress_operation.htm
old-project: display
ms.assetid: BCA741A8-2294-43C1-8B9C-3724274D637B
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION, D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION structure [Display Devices], _D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION, d3dukmdt/D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION, display.d3dddi_updategpuvirtualaddress_operation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
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
-	HeaderDef
api_location:
-	d3dukmdt.h
api_name:
-	D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION
product: Windows
targetos: Windows
req.typenames: D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION
---

# _D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION structure
<b>D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION</b> describes a virtual address update operation.

## Syntax
```
typedef struct _D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION {
  D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE OperationType;
  union {
    struct {
      D3DGPU_VIRTUAL_ADDRESS BaseAddress;
      D3DGPU_SIZE_T          SizeInBytes;
      D3DKMT_HANDLE          hAllocation;
      D3DGPU_SIZE_T          AllocationOffsetInBytes;
      D3DGPU_SIZE_T          AllocationSizeInBytes;
    } Map;
    struct {
      D3DGPU_VIRTUAL_ADDRESS                  BaseAddress;
      D3DGPU_SIZE_T                           SizeInBytes;
      D3DKMT_HANDLE                           hAllocation;
      D3DGPU_SIZE_T                           AllocationOffsetInBytes;
      D3DGPU_SIZE_T                           AllocationSizeInBytes;
      D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE Protection;
      UINT64                                  DriverProtection;
    } MapProtect;
    struct {
      D3DGPU_VIRTUAL_ADDRESS                  BaseAddress;
      D3DGPU_SIZE_T                           SizeInBytes;
      D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE Protection;
    } Unmap;
    struct {
      D3DGPU_VIRTUAL_ADDRESS SourceAddress;
      D3DGPU_SIZE_T          SizeInBytes;
      D3DGPU_VIRTUAL_ADDRESS DestAddress;
    } Copy;
  };
} D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION;
```

## Members


`OperationType`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/CEDE03E1-4B0D-4839-B7D6-0826CC103C5E">pfnReserveGpuVirtualAddressCb</a>



<a href="https://msdn.microsoft.com/99D075A0-4483-47D1-BA24-80C45BFF407A">pfnUpdateGpuVirtualAddressCb</a>