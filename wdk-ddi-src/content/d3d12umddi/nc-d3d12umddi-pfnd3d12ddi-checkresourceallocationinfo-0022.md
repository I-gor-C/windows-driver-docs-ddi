---
UID: NC.d3d12umddi.PFND3D12DDI_CHECKRESOURCEALLOCATIONINFO_0022
title: PFND3D12DDI_CHECKRESOURCEALLOCATIONINFO_0022
author: windows-driver-content
description: The pfnCheckResourceAllocationInfo callback function supports checking resource allocation information.
old-location: display\pfnd3d12ddi_checkresourceallocationinfo_0022.htm
old-project: display
ms.assetid: 9B223440-7462-4DF1-990B-82115DE50D67
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnCheckResourceAllocationInfo
req.alt-loc: D3d12umddi.h
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
req.iface: 
---

# PFND3D12DDI_CHECKRESOURCEALLOCATIONINFO_0022 callback



## -description
<p>The <i>pfnCheckResourceAllocationInfo</i> callback function supports checking resource allocation information.</p>


## -prototype

````
PFND3D12DDI_CHECKRESOURCEALLOCATIONINFO_0022 pfnCheckResourceAllocationInfo;

VOID APIENTRY* pfnCheckResourceAllocationInfo(
              D3D12DDI_HDEVICE                       hDevice,
  _In_  const D3D12DDIARG_CREATERESOURCE_0003        *CreateResource,
              D3D12DDI_RESOURCE_OPTIMIZATION_FLAGS   ResourceOptimizationFlags,
              UINT32                                 AlignmentRestriction,
              UINT                                   VisibleNodeMask,
  _Out_       D3D12DDI_RESOURCE_ALLOCATION_INFO_0022 *pInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> 

<dd>
<p>A device handle. </p>
</dd>

### -param <i>CreateResource</i> [in]

<dd>
<p>A pointer to a create resource.</p>
</dd>

### -param <i>ResourceOptimizationFlags</i> 

<dd>
<p>Resource optimization flags.</p>
</dd>

### -param <i>AlignmentRestriction</i> 

<dd>
<p>An alignment restriction value.</p>
</dd>

### -param <i>VisibleNodeMask</i> 

<dd>
<p>A visible node mask.</p>
</dd>

### -param <i>pInfo</i> [out]

<dd>
<p>Information for resource allocation.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>This callback function is part of a two step process of resource creation. This function determines the sizes and alignments of the resource data, additional data header, and additional data is determined, along with the texture layout. When the resource description is passed into this function, the layout of the resource description may be set to _UNDEFINED. This allows the driver to choose any texture layout. When the ayout of the resource description is <b>STANDARD_SWIZZLE</b> or <b>ROW_MAJOR</b>, the driver must return out the corresponding value as its choice.</p>

<p>This callback function is accessed by using the <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi-device-funcs-core-0010.md">D3D12DDI_DEVICE_FUNCS_CORE_0010</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>