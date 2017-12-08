---
UID: NS.d3dkmddi._DXGKARG_CREATEALLOCATION
title: DXGKARG_CREATEALLOCATION
author: windows-driver-content
description: The DXGKARG_CREATEALLOCATION structure describes how the display miniport driver should create allocations.
old-location: display\dxgkarg_createallocation.htm
old-project: display
ms.assetid: e1464561-b9f2-41aa-921e-84f3a855130f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_CREATEALLOCATION, DXGKARG_CREATEALLOCATION
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
req.alt-api: DXGKARG_CREATEALLOCATION
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
req.iface: 
---

# DXGKARG_CREATEALLOCATION structure



## -description
<p>The DXGKARG_CREATEALLOCATION structure describes how the display miniport driver should create allocations.</p>


## -syntax

````
typedef struct _DXGKARG_CREATEALLOCATION {
  const VOID                 *pPrivateDriverData;
  UINT                       PrivateDriverDataSize;
  UINT                       NumAllocations;
  DXGK_ALLOCATIONINFO        *pAllocationInfo;
  HANDLE                     hResource;
  DXGK_CREATEALLOCATIONFLAGS Flags;
} DXGKARG_CREATEALLOCATION;
````


## -struct-fields
<dl>

### -field pPrivateDriverData

<dd>
<p>[in] A pointer to a block of private data that is passed from the user-mode display driver to the display miniport driver. This member is typically used to provide data for a group of allocations. Note that this member is distinct from the <b>pPrivateDriverData</b> members of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationinfo.md">DXGK_ALLOCATIONINFO</a> structures in the array that <b>pAllocationInfo</b> specifies. You can set private data for this member in addition to private data for each allocation. </p>
</dd>

### -field PrivateDriverDataSize

<dd>
<p>[in] The size, in bytes, of the private data that <b>pPrivateDriverData</b> points to.</p>
</dd>

### -field NumAllocations

<dd>
<p>[in] The number of elements in the array that <b>pAllocationInfo</b> specifies, which represents the number of allocations to create.</p>
</dd>

### -field pAllocationInfo

<dd>
<p>[in/out] An array of <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationinfo.md">DXGK_ALLOCATIONINFO</a> structures that describe the allocations to create.</p>
</dd>

### -field hResource

<dd>
<p>[in/out] A handle to a resource. The display miniport driver can set this handle to a value that the Microsoft DirectX graphics kernel subsystem can subsequently pass in driver calls and that refers to information for the allocations. If the resource was already created by a previous <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a> call, this member contains the handle that the driver previously returned.</p>
</dd>

### -field Flags

<dd>
<p>[in] A <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-createallocationflags.md">DXGK_CREATEALLOCATIONFLAGS</a> structure that identifies how to create allocations. Setting all of the bit-field flags to 0 indicates that allocations belong to the device and not to a particular resource.</p>
</dd>
</dl>

## -remarks


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
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationinfo.md">DXGK_ALLOCATIONINFO</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-createallocationflags.md">DXGK_CREATEALLOCATIONFLAGS</a>
</dt>
<dt>
<a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_CREATEALLOCATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
