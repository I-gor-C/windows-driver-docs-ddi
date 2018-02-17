---
UID: NS:d3dukmdt._D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION
title: "_D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION"
author: windows-driver-content
description: D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION describes a virtual address update operation.
old-location: display\d3dddi_updategpuvirtualaddress_operation.htm
old-project: display
ms.assetid: BCA741A8-2294-43C1-8B9C-3724274D637B
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: d3dukmdt/D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION, D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION structure [Display Devices], display.d3dddi_updategpuvirtualaddress_operation, D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION, _D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dukmdt.h
apiname:
-	D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION
product: Windows
targetos: Windows
req.typenames: D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION
---

# _D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION structure
<b>D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION</b> describes a virtual address update operation.

## Syntax
````
typedef struct _D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION {
  D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION_TYPE OperationType;
  union {
    struct {
      D3DGPU_VIRTUAL_ADDRESS BaseAddress;
      D3DGPU_SIZE_T          SizeInBytes;
      D3DKMT_HANDLE          hAllocation;
      D3DGPU_SIZE_T          AllocationOffsetInBytes;
      D3DGPU_SIZE_T          AllocationSizeInBytes;
    } Map;
    struct {
      D3DGPU_VIRTUAL_ADDRESS                  BaseAddress;
      D3DGPU_SIZE_T                           SizeInBytes;
      D3DKMT_HANDLE                           hAllocation;
      D3DGPU_SIZE_T                           AllocationOffsetInBytes;
      D3DGPU_SIZE_T                           AllocationSizeInBytes;
      D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE Protection;
      UINT64                                  DriverProtection;
    } MapProtect;
    struct {
      D3DGPU_VIRTUAL_ADDRESS                  BaseAddress;
      D3DGPU_SIZE_T                           SizeInBytes;
      D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE Protection;
    } Unmap;
    struct {
      D3DGPU_VIRTUAL_ADDRESS BaseAddress;
      D3DGPU_SIZE_T          SizeInBytes;
      D3DGPU_VIRTUAL_ADDRESS DestAddress;
    } Copy;
  };
} D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION;
````

## Members


`OperationType`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_reservegpuvirtualaddresscb.md">pfnReserveGpuVirtualAddressCb</a>



<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_updategpuvirtualaddresscb.md">pfnUpdateGpuVirtualAddressCb</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_UPDATEGPUVIRTUALADDRESS_OPERATION structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>