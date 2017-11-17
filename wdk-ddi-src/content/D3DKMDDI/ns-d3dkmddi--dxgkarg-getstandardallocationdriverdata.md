---
UID: NS.d3dkmddi._DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA
title: DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA
author: windows-driver-content
description: The DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA structure describes a standard allocation type.
old-location: display\dxgkarg_getstandardallocationdriverdata.htm
ms.assetid: 4327ba59-bd74-4018-85d2-54a1693c62c1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA
req.alt-loc: d3dkmddi.h
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
ms.keywords: DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA, DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA
req.iface: 
---

# DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA structure



## -description
<p>The DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA structure describes a standard allocation type.</p>


## -syntax

````
typedef struct _DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA {
  D3DKMDT_STANDARDALLOCATION_TYPE StandardAllocationType;
  union {
    D3DKMDT_SHAREDPRIMARYSURFACEDATA *pCreateSharedPrimarySurfaceData;
    D3DKMDT_SHADOWSURFACEDATA        *pCreateShadowSurfaceData;
    D3DKMDT_STAGINGSURFACEDATA       *pCreateStagingSurfaceData;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN7)
    D3DKMDT_GDISURFACEDATA           *pCreateGdiSurfaceData;
#endif 
  };
  VOID                            *pAllocationPrivateDriverData;
  UINT                            AllocationPrivateDriverDataSize;
  VOID                            *pResourcePrivateDriverData;
  UINT                            ResourcePrivateDriverDataSize;
} DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA;
````


## -struct-fields
<dl>

### -field <b>StandardAllocationType</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546589">D3DKMDT_STANDARDALLOCATION_TYPE</a>-typed value that identifies the type of standard allocation to describe.</p>
</dd>

### -field <b>pCreateSharedPrimarySurfaceData</b>

<dd>
<p>[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546177">D3DKMDT_SHAREDPRIMARYSURFACEDATA</a> structure, if <b>StandardAllocationType</b> specifies D3DKMDT_STANDARDALLOCATION_SHAREDPRIMARYSURFACE.</p>
</dd>

### -field <b>pCreateShadowSurfaceData</b>

<dd>
<p>[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546168">D3DKMDT_SHADOWSURFACEDATA</a> structure, if <b>StandardAllocationType</b> specifies D3DKMDT_STANDARDALLOCATION_SHADOWSURFACE.</p>
</dd>

### -field <b>pCreateStagingSurfaceData</b>

<dd>
<p>[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546583">D3DKMDT_STAGINGSURFACEDATA</a> structure, if <b>StandardAllocationType</b> specifies D3DKMDT_STANDARDALLOCATION_STAGINGSURFACE.</p>
</dd>

### -field <b>pCreateGdiSurfaceData</b>

<dd>
<p>[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546021">D3DKMDT_GDISURFACEDATA</a> structure, only available if <b>StandardAllocationType</b> specifies D3DKMDT_STANDARDALLOCATION_GDISURFACE.</p>
<p>This member is available beginning with Windows 7.</p>
</dd>

### -field <b>pAllocationPrivateDriverData</b>

<dd>
<p>[in/out] A pointer to a block of allocation private data that describes the standard allocation type; otherwise, this member is <b>NULL</b>. The allocation private data that the display miniport driver's <a href="https://msdn.microsoft.com/38a9859f-ed9f-41a5-9bf1-c734480499ea">DxgkDdiGetStandardAllocationDriverData</a> function returns depends on the type that the driver requests in <b>StandardAllocationType</b>.</p>
</dd>

### -field <b>AllocationPrivateDriverDataSize</b>

<dd>
<p>[out] The size, in bytes, of the allocation private data that <b>pAllocationPrivateDriverData</b> points to. If the driver sets <b>pAllocationPrivateDriverData</b> to <b>NULL</b>, the driver should set <b>AllocationPrivateDriverDataSize</b> to the size of the buffer that the driver requires to describe the given standard allocation type.</p>
<p>If the driver does not use private data for each allocation for standard allocations types, the driver can set <b>AllocationPrivateDriverDataSize</b> to zero. </p>
</dd>

### -field <b>pResourcePrivateDriverData</b>

<dd>
<p>[in/out] A pointer to a block of resource private data that describes the standard allocation type; otherwise, this member is <b>NULL</b>. The resource private data that the display miniport driver's <a href="https://msdn.microsoft.com/38a9859f-ed9f-41a5-9bf1-c734480499ea">DxgkDdiGetStandardAllocationDriverData</a> function returns depends on the type that the driver requests in <b>StandardAllocationType</b>.</p>
</dd>

### -field <b>ResourcePrivateDriverDataSize</b>

<dd>
<p>[out] The size, in bytes, of the resource private data that <b>pResourcePrivateDriverData</b> points to. If the driver sets <b>pResourcePrivateDriverData</b> to <b>NULL</b>, the driver should set <b>ResourcePrivateDriverDataSize</b> to the size of the buffer that the driver requires to describe the given standard allocation type.</p>
<p>If the driver does not use private data for each resource for standard allocations types, the driver can set <b>ResourcePrivateDriverDataSize</b> to zero. </p>
</dd>
</dl>

## -remarks
<p>If the display miniport driver returns <b>NULL</b> in the <b>pAllocationPrivateDriverData</b> and <b>pResourcePrivateDriverData</b> members, the driver should return the sizes of the buffers that the driver requires in the <b>AllocationPrivateDriverDataSize</b> and <b>ResourcePrivateDriverDataSize</b> members. However, the driver should not change the contents of the standard allocation structure in the union that DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA contains to obtain the required sizes of the buffers. </p>

<p>Although the driver can set <b>ResourcePrivateDriverDataSize</b> or <b>AllocationPrivateDriverDataSize</b> to zero, the driver cannot set both to zero.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546021">D3DKMDT_GDISURFACEDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546168">D3DKMDT_SHADOWSURFACEDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546177">D3DKMDT_SHAREDPRIMARYSURFACEDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546583">D3DKMDT_STAGINGSURFACEDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546589">D3DKMDT_STANDARDALLOCATION_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/38a9859f-ed9f-41a5-9bf1-c734480499ea">DxgkDdiGetStandardAllocationDriverData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_GETSTANDARDALLOCATIONDRIVERDATA structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
