---
UID: NS:d3dkmddi._DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA
title: "_DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA"
author: windows-driver-content
description: The DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA structure describes a standard allocation type.
old-location: display\dxgkarg_getstandardallocationdriverdata.htm
old-project: display
ms.assetid: 4327ba59-bd74-4018-85d2-54a1693c62c1
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*INOUT_PDXGKARG_GETSTANDARDALLOCATIONDRIVERDATA, DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA, DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA structure [Display Devices], DmStructs_2ef51052-bc21-4374-9471-c03b2a81b8b3.xml, _DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA, d3dkmddi/DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA, display.dxgkarg_getstandardallocationdriverdata"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA
product: Windows
targetos: Windows
req.typenames: DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA
---

# _DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA structure
The DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA structure describes a standard allocation type.

## Syntax
```
typedef struct _DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA {
  D3DKMDT_STANDARDALLOCATION_TYPE StandardAllocationType;
  union {
    D3DKMDT_GDISURFACEDATA           *pCreateGdiSurfaceData;
    D3DKMDT_SHADOWSURFACEDATA        *pCreateShadowSurfaceData;
    D3DKMDT_SHAREDPRIMARYSURFACEDATA *pCreateSharedPrimarySurfaceData;
    D3DKMDT_STAGINGSURFACEDATA       *pCreateStagingSurfaceData;
    D3DKMDT_VIRTUALGPUSURFACEDATA    *pCreateVirtualGpuSurfaceData;
  };
  VOID                            *pAllocationPrivateDriverData;
  UINT                            AllocationPrivateDriverDataSize;
  VOID                            *pResourcePrivateDriverData;
  UINT                            ResourcePrivateDriverDataSize;
  UINT                            PhysicalAdapterIndex;
} DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA;
```

## Members


`StandardAllocationType`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546589">D3DKMDT_STANDARDALLOCATION_TYPE</a>-typed value that identifies the type of standard allocation to describe.

`pAllocationPrivateDriverData`

[in/out] A pointer to a block of allocation private data that describes the standard allocation type; otherwise, this member is <b>NULL</b>. The allocation private data that the display miniport driver's <a href="https://msdn.microsoft.com/38a9859f-ed9f-41a5-9bf1-c734480499ea">DxgkDdiGetStandardAllocationDriverData</a> function returns depends on the type that the driver requests in <b>StandardAllocationType</b>.

`AllocationPrivateDriverDataSize`

[out] The size, in bytes, of the allocation private data that <b>pAllocationPrivateDriverData</b> points to. If the driver sets <b>pAllocationPrivateDriverData</b> to <b>NULL</b>, the driver should set <b>AllocationPrivateDriverDataSize</b> to the size of the buffer that the driver requires to describe the given standard allocation type.

If the driver does not use private data for each allocation for standard allocations types, the driver can set <b>AllocationPrivateDriverDataSize</b> to zero.

`pResourcePrivateDriverData`

[in/out] A pointer to a block of resource private data that describes the standard allocation type; otherwise, this member is <b>NULL</b>. The resource private data that the display miniport driver's <a href="https://msdn.microsoft.com/38a9859f-ed9f-41a5-9bf1-c734480499ea">DxgkDdiGetStandardAllocationDriverData</a> function returns depends on the type that the driver requests in <b>StandardAllocationType</b>.

`ResourcePrivateDriverDataSize`

[out] The size, in bytes, of the resource private data that <b>pResourcePrivateDriverData</b> points to. If the driver sets <b>pResourcePrivateDriverData</b> to <b>NULL</b>, the driver should set <b>ResourcePrivateDriverDataSize</b> to the size of the buffer that the driver requires to describe the given standard allocation type.

If the driver does not use private data for each resource for standard allocations types, the driver can set <b>ResourcePrivateDriverDataSize</b> to zero.

`PhysicalAdapterIndex`



## Remarks
If the display miniport driver returns <b>NULL</b> in the <b>pAllocationPrivateDriverData</b> and <b>pResourcePrivateDriverData</b> members, the driver should return the sizes of the buffers that the driver requires in the <b>AllocationPrivateDriverDataSize</b> and <b>ResourcePrivateDriverDataSize</b> members. However, the driver should not change the contents of the standard allocation structure in the union that DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA contains to obtain the required sizes of the buffers. 

Although the driver can set <b>ResourcePrivateDriverDataSize</b> or <b>AllocationPrivateDriverDataSize</b> to zero, the driver cannot set both to zero.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546021">D3DKMDT_GDISURFACEDATA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546168">D3DKMDT_SHADOWSURFACEDATA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546177">D3DKMDT_SHAREDPRIMARYSURFACEDATA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546583">D3DKMDT_STAGINGSURFACEDATA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546589">D3DKMDT_STANDARDALLOCATION_TYPE</a>



<a href="https://msdn.microsoft.com/38a9859f-ed9f-41a5-9bf1-c734480499ea">DxgkDdiGetStandardAllocationDriverData</a>