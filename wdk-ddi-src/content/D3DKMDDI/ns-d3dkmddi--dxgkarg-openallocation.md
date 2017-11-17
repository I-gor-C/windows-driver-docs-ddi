---
UID: NS.d3dkmddi._DXGKARG_OPENALLOCATION
title: DXGKARG_OPENALLOCATION
author: windows-driver-content
description: The DXGKARG_OPENALLOCATION structure describes allocations that the display miniport driver should open.
old-location: display\dxgkarg_openallocation.htm
ms.assetid: cddb85c7-137c-4ceb-b53c-170ce020cea1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available beginning with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_OPENALLOCATION
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
ms.keywords: DXGKARG_OPENALLOCATION, DXGKARG_OPENALLOCATION
req.iface: 
---

# DXGKARG_OPENALLOCATION structure



## -description
<p>The DXGKARG_OPENALLOCATION structure describes allocations that the display miniport driver should open.</p>


## -syntax

````
typedef struct _DXGKARG_OPENALLOCATION {
  UINT                     NumAllocations;
  DXGK_OPENALLOCATIONINFO  *pOpenAllocation;
  VOID                     *pPrivateDriverData;
  UINT                     PrivateDriverSize;
  DXGK_OPENALLOCATIONFLAGS Flags;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  UINT                     SubresourceIndex;
  SIZE_T                   SubresourceOffset;
  UINT                     Pitch;
#endif 
} DXGKARG_OPENALLOCATION;
````


## -struct-fields
<dl>

### -field <b>NumAllocations</b>

<dd>
<p>[in] The number of elements in the array that the <b>pOpenAllocation</b> member specifies, which represents the number of device-specific allocations to open.</p>
</dd>

### -field <b>pOpenAllocation</b>

<dd>
<p>[in/out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561983">DXGK_OPENALLOCATIONINFO</a> structures for the allocations to open.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>[in] A pointer to a block of private data that is passed from the user-mode display driver to the display miniport driver. This block of private data is the same resource-specific data that is passed in the <b>pPrivateDriverData</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a> structure in the call to the <a href="https://msdn.microsoft.com/a28287d6-4dfa-4db4-92df-bbcd9379a5b2">DxgkDdiCreateAllocation</a> function. The display miniport driver cannot modify this block of private data.</p>
</dd>

### -field <b>PrivateDriverSize</b>

<dd>
<p>[in] The size, in bytes, of the block of private data that <b>pPrivateDriverData</b> points to.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561981">DXGK_OPENALLOCATIONFLAGS</a> structure that identifies the operation to perform for allocations.</p>
</dd>

### -field <b>SubresourceIndex</b>

<dd>
<p>[in] Supported beginning with Windows 8.</p>
<p>An index into the resource for the render target surface.</p>
<p>The operating system specifies this member only if the display miniport driver supports <a href="https://msdn.microsoft.com/03db58e6-a6d5-4b6f-ba71-d22a985f9c57">GDI Hardware Acceleration</a>. Specifically, the display miniport driver must implement  the <a href="https://msdn.microsoft.com/5841934d-7e0a-4bb8-a7f8-17d8c0af351f">DxgkDdiRenderKm</a> function and must create the device with the <b>GdiDevice</b> member set in <a href="https://msdn.microsoft.com/library/windows/hardware/ff557570">DXGKARG_CREATEDEVICE</a>.<b>Flags</b>.</p>
<p>If the value of <b>SubresourceIndex</b> is greater than the number of subresources in the allocation, the display miniport driver should return an error.</p>
</dd>

### -field <b>SubresourceOffset</b>

<dd>
<p>[out] Supported beginning with Windows 8.</p>
<p>The offset, in bytes, from the start of the allocation to the start of the subresource.</p>
</dd>

### -field <b>Pitch</b>

<dd>
<p>[out] Supported beginning with Windows 8.</p>
<p>The pitch, in bytes, of the allocation—that is, the distance, in bytes, to the start of the next row.</p>
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
<p>Available beginning with Windows Vista.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561981">DXGK_OPENALLOCATIONFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561983">DXGK_OPENALLOCATIONINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a28287d6-4dfa-4db4-92df-bbcd9379a5b2">DxgkDdiCreateAllocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/551154d7-950d-40e5-810b-8d803c1731ca">DxgkDdiOpenAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_OPENALLOCATION structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
