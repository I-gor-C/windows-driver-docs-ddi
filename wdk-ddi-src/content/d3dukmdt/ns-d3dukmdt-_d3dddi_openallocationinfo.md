---
UID: NS:d3dukmdt._D3DDDI_OPENALLOCATIONINFO
title: "_D3DDDI_OPENALLOCATIONINFO"
author: windows-driver-content
description: The D3DDDI_OPENALLOCATIONINFO structure describes an allocation to be opened.
old-location: display\d3dddi_openallocationinfo.htm
old-project: display
ms.assetid: cd50602a-c4aa-410b-9ed6-56d7237571cd
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DDDI_OPENALLOCATIONINFO, D3DDDI_OPENALLOCATIONINFO structure [Display Devices], D3D_other_Structs_cfb185b4-cc7d-4c1a-9e76-6032816feab0.xml, _D3DDDI_OPENALLOCATIONINFO, d3dukmdt/D3DDDI_OPENALLOCATIONINFO, display.d3dddi_openallocationinfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
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
-	d3dukmdt.h
api_name:
-	D3DDDI_OPENALLOCATIONINFO
product: Windows
targetos: Windows
req.typenames: D3DDDI_OPENALLOCATIONINFO
---

# _D3DDDI_OPENALLOCATIONINFO structure
The D3DDDI_OPENALLOCATIONINFO structure describes an allocation to be opened.

## Syntax
````
typedef struct _D3DDDI_OPENALLOCATIONINFO {
  D3DKMT_HANDLE hAllocation;
  const VOID    *pPrivateDriverData;
  UINT          PrivateDriverDataSize;
} D3DDDI_OPENALLOCATIONINFO;
````

## Members


`hAllocation`

[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the allocation. The user-mode display driver should use this handle to reference the allocation in the command buffer.

`pPrivateDriverData`

[in] A pointer to a block of private data, which was passed to the display miniport driver when the resource was created.

`PrivateDriverDataSize`

[in] The size, in bytes, of the block of private data that is pointed to by <b>pPrivateDriverData</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |