---
UID: NS.d3dkmddi._DXGK_ALLOCATIONLIST
title: DXGK_ALLOCATIONLIST
author: windows-driver-content
description: The DXGK_ALLOCATIONLIST structure describes an allocation specification that is used in direct memory access (DMA) buffering.
old-location: display\dxgk_allocationlist.htm
ms.assetid: 1be057dc-6a97-4798-a152-7cc6d6febda5
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
req.alt-api: DXGK_ALLOCATIONLIST
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
ms.keywords: DXGK_ALLOCATIONLIST, DXGK_ALLOCATIONLIST
req.iface: 
---

# DXGK_ALLOCATIONLIST structure



## -description
<p>The <b>DXGK_ALLOCATIONLIST</b> structure describes an allocation specification that is used in direct memory access (DMA) buffering.</p>


## -syntax

````
typedef struct _DXGK_ALLOCATIONLIST {
  HANDLE           hDeviceSpecificAllocation;
  struct {
    UINT WriteOperation  :1;
    UINT SegmentId  :5;
    UINT Reserved  :26;
  };
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
  union {
    PHYSICAL_ADDRESS       PhysicalAddress;
    D3DGPU_VIRTUAL_ADDRESS VirtualAddress;
  };
#else 
  PHYSICAL_ADDRESS PhysicalAddress;
#endif 
} DXGK_ALLOCATIONLIST;
````


## -struct-fields
<dl>

### -field <b>hDeviceSpecificAllocation</b>

<dd>
<p>[in/out] An open handle to the allocation that is being referenced (that is, the handle that the driver returned in the <b>hDeviceSpecificAllocation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561983">DXGK_OPENALLOCATIONINFO</a> structure for the allocation in a call to the driver's <a href="https://msdn.microsoft.com/551154d7-950d-40e5-810b-8d803c1731ca">DxgkDdiOpenAllocation</a> function).</p>
</dd>

### -field ( <i>unnamed struct</i> )

<dd>
<p>Â </p>
<dl>

### -field <b>WriteOperation</b>

<dd>
<p>[in/out] A member in the structure that <b>DXGK_ALLOCATIONLIST</b> contains that can hold information about whether the allocation can be written to. Setting this member to 1 indicates that the allocation can be written to anywhere in the DMA buffer.</p>
<p>Setting this member is equivalent to setting the first bit of a 32-bit value (0x00000001). </p>
</dd>

### -field <b>SegmentId</b>

<dd>
<p>[in/out] A member in the structure that <b>DXGK_ALLOCATIONLIST</b> contains that can hold information about the identifier of a segment that the allocation was last paged in at. Setting this member to 0 indicates that no pre-patching information is available.</p>
<p>Setting this member is equivalent to setting the second through sixth bit of a 32-bit value (0x0000002E). </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>[in] A member in the structure that <b>DXGK_ALLOCATIONLIST</b> contains that is reserved. This member should be set to 0.</p>
<p>Setting this member is equivalent to setting the remaining 26 bits (0xFFFFFFC0) of a 32-bit value to zeros. </p>
</dd>
</dl>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>[in/out] A <b>PHYSICAL_ADDRESS</b> data type (which is defined as <b>LARGE_INTEGER</b>) that indicates the physical address, within the segment that <b>SegmentId</b> specifies, where the allocation was last paged-in at. This member is set to zero if no pre-patching information is available.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>VirtualAddress</b>

<dd>
<p>[in/out] A <b>D3DGPU_VIRTUAL_ADDRESS</b> data type that indicates the virtual address.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>[in/out] A <b>PHYSICAL_ADDRESS</b> data type (which is defined as <b>LARGE_INTEGER</b>) that indicates the physical address, within the segment that <b>SegmentId</b> specifies, where the allocation was last paged-in at. This member is set to zero if no pre-patching information is available.</p>
</dd>
</dl>

## -remarks
<p>In the display miniport driver's <a href="https://msdn.microsoft.com/fd634768-5e1e-4f40-82fd-5ef69148c3d7">DxgkDdiRender</a> function, the driver generates a list of <b>DXGK_ALLOCATIONLIST</b> structures for allocation specifications that will be used in a direct memory access (DMA) buffer. The video memory manager uses the list to split and patch DMA buffers appropriately. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a>
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
<dt>
<a href="https://msdn.microsoft.com/fd634768-5e1e-4f40-82fd-5ef69148c3d7">DxgkDdiRender</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_ALLOCATIONLIST structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
