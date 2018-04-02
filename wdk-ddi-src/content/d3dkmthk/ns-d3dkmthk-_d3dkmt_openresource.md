---
UID: NS:d3dkmthk._D3DKMT_OPENRESOURCE
title: "_D3DKMT_OPENRESOURCE"
author: windows-driver-content
description: The D3DKMT_OPENRESOURCE structure describes parameters for opening a resource.
old-location: display\d3dkmt_openresource.htm
old-project: display
ms.assetid: 5ff63606-ced1-4482-b967-41db4746ac1d
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_OPENRESOURCE, D3DKMT_OPENRESOURCE structure [Display Devices], OpenGL_Structs_b069a94a-b78c-4fbf-b78d-7c5b0d025655.xml, _D3DKMT_OPENRESOURCE, d3dkmthk/D3DKMT_OPENRESOURCE, display.d3dkmt_openresource
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmthk.h
api_name:
-	D3DKMT_OPENRESOURCE
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_OPENRESOURCE
---

# _D3DKMT_OPENRESOURCE structure
The D3DKMT_OPENRESOURCE structure describes parameters for opening a resource.

## Syntax
```
typedef struct _D3DKMT_OPENRESOURCE {
  D3DKMT_HANDLE hDevice;
  D3DKMT_HANDLE hGlobalShare;
  UINT          NumAllocations;
  union {
    D3DDDI_OPENALLOCATIONINFO  *pOpenAllocationInfo;
    D3DDDI_OPENALLOCATIONINFO2 *pOpenAllocationInfo2;
  };
  VOID          *pPrivateRuntimeData;
  UINT          PrivateRuntimeDataSize;
  VOID          *pResourcePrivateDriverData;
  UINT          ResourcePrivateDriverDataSize;
  VOID          *pTotalPrivateDriverDataBuffer;
  UINT          TotalPrivateDriverDataBufferSize;
  D3DKMT_HANDLE hResource;
} D3DKMT_OPENRESOURCE;
```

## Members


`hDevice`

[in] A handle to the device that the resource and allocations are associated with.

`hGlobalShare`

[in] A handle to the shared resource to open.

`NumAllocations`

[in] The number of elements in the array that <b>pOpenAllocationInfo</b> specifies, which represents the number of allocations that are associated with the resource.

`pPrivateRuntimeData`

[in] A pointer to a caller-supplied buffer where the OpenGL runtime copies private data that is associated with the resource.

`PrivateRuntimeDataSize`

[in] The size, in bytes, of the buffer that <b>pPrivateRuntimeData</b> points to.

`pResourcePrivateDriverData`

[in/out] A pointer to a buffer that receives the private data that is associated with the resource. This data is per resource and not per allocation.

`ResourcePrivateDriverDataSize`

[in] The size, in bytes, of the buffer that <b>pResourcePrivateDriverData</b> points to.

`pTotalPrivateDriverDataBuffer`

[in/out] A pointer to a buffer that receives the private data for all of the allocations that are associated with the resource. The caller should never access this private data directly.

`TotalPrivateDriverDataBufferSize`

[in/out] On input, the size, in bytes, of the buffer that <b>pTotalPrivateDriverDataBuffer</b> points to. On output, this member specifies the size, in bytes, of data that is written to the buffer that <b>pTotalPrivateDriverDataBuffer</b> points to.

`hResource`

[out] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the newly opened shared resource that is associated with the allocations.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544599">D3DDDI_OPENALLOCATIONINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547065">D3DKMTOpenResource</a>