---
UID: NS.d3dkmddi._DXGK_ALLOCATIONINFO
title: DXGK_ALLOCATIONINFO
author: windows-driver-content
description: The DXGK_ALLOCATIONINFO structure describes parameters for creating an allocation.
old-location: display\dxgk_allocationinfo.htm
old-project: display
ms.assetid: d5767bd3-11f8-45a7-b760-3ed51c54c044
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_ALLOCATIONINFO, DXGK_ALLOCATIONINFO
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
req.alt-api: DXGK_ALLOCATIONINFO
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

# DXGK_ALLOCATIONINFO structure



## -description
<p>The DXGK_ALLOCATIONINFO structure describes parameters for creating an allocation.</p>


## -syntax

````
typedef struct _DXGK_ALLOCATIONINFO {
  VOID                       *pPrivateDriverData;
  UINT                       PrivateDriverDataSize;
  UINT                       Alignment;
  SIZE_T                     Size;
  SIZE_T                     PitchAlignedSize;
  DXGK_SEGMENTBANKPREFERENCE HintedBank;
  DXGK_SEGMENTPREFERENCE     PreferredSegment;
  UINT                       SupportedReadSegmentSet;
  UINT                       SupportedWriteSegmentSet;
  UINT                       EvictionSegmentSet;
  union {
    UINT MaximumRenamingListLength;
    UINT PhysicalAdapterIndex;
  };
  HANDLE                     hAllocation;
  union {
    DXGK_ALLOCATIONINFOFLAGS         Flags;
    DXGK_ALLOCATIONINFOFLAGS_WDDM2_0 FlagsWddm2;
  };
  DXGK_ALLOCATIONUSAGEHINT   *pAllocationUsageHint;
  UINT                       AllocationPriority;
} DXGK_ALLOCATIONINFO;
````


## -struct-fields
<dl>

### -field pPrivateDriverData

<dd>
<p>[in] A pointer to a block of private data. This data is for each allocation and is distinct from the <b>pPrivateDriverData</b> member in the <a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-createallocation.md">DXGKARG_CREATEALLOCATION</a> structure. The user-mode display driver might pass this data to the display miniport driver. However, if  the Microsoft DirectX graphics kernel subsystem passes this data to describe the shared primary or other lockable surface, the data is passed as the first element of the array in the <b>pAllocationInfo</b> member of DXGKARG_CREATEALLOCATION.</p>
</dd>

### -field PrivateDriverDataSize

<dd>
<p>[in] The size, in bytes, of the block of private data in <b>pPrivateDriverData</b>.</p>
</dd>

### -field Alignment

<dd>
<p>[out] The required alignment, in bytes, for the allocation.</p>
</dd>

### -field Size

<dd>
<p>[out] The size, in bytes, that is required for the allocation. The size value is expanded to a multiple of the native host page size (for example, 4 KB on the x86 architecture). The display miniport driver specifies the allocation size to the video memory manager.</p>
</dd>

### -field PitchAlignedSize

<dd>
<p>[out] The size, in bytes, of the allocation when it is located in a pitch-aligned segment, which is specified by the <b>PitchAlignment</b> bit-field flag in the <b>Flags</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-segmentdescriptor.md">DXGK_SEGMENTDESCRIPTOR</a> structure for the segment. If the allocation is not supported in a pitch-aligned segment (graphics processing units [GPUs] commonly do not support this type of segment), the driver should set the value in <b>PitchAlignedSize</b> to zero. If the driver specifies a nonzero value in <b>PitchAlignedSize</b>, the value must be greater than or equal to the value in the <b>Size</b> member.</p>
</dd>

### -field HintedBank

<dd>
<p>[out] A <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-segmentbankpreference.md">DXGK_SEGMENTBANKPREFERENCE</a> structure that indicates the bank ordering preferences that the display miniport driver requests that the video memory manager use to page-in the allocation. If this member is specified, the video memory manager uses banking information about the most preferred segment, which is specified by the <b>SegmentId0</b> member of the <a href="display.dxgk_segmentpreference">DXGK_SEGMENTPREFERENCE</a> structure that the <b>PreferredSegment</b> member specifies.</p>
</dd>

### -field PreferredSegment

<dd>
<p>[out] A <a href="display.dxgk_segmentpreference">DXGK_SEGMENTPREFERENCE</a> structure that indicates preferred segments identifiers that the display miniport driver requests that the video memory manager use to page-in the allocation.</p>
</dd>

### -field SupportedReadSegmentSet

<dd>
<p>[out] Segment identifiers that the display miniport driver can set in the <b>PreferredSegment</b> member for read operations. The segments that these identifiers indicate are segments that the display miniport driver requests that the video memory manager use to page-in the allocation for read operations, regardless of performance. Setting bit 0 indicates that the first segment is supported, setting bit 1 indicates that the second segment is supported, and so on. </p>
<p>The display miniport driver can set preferences only for segments that are supported for read operations. The video memory manager asserts if the driver attempts to set preferences for unsupported segments in the <b>PreferredSegment</b> member.</p>
</dd>

### -field SupportedWriteSegmentSet

<dd>
<p>[out] Segment identifiers that the display miniport driver can set in the <b>PreferredSegment</b> member for write operations. The segments that these identifiers indicate are segments that the display miniport driver requests that the video memory manager use to page-in the allocation for write operations, regardless of performance. Setting bit 0 indicates that the first segment is supported, setting bit 1 indicates that the second segment is supported, and so on. </p>
<p>The display miniport driver can set preferences only for segments that are supported for write operations. The video memory manager asserts if the driver attempts to set preferences for unsupported segments in the <b>PreferredSegment</b> member.</p>
</dd>

### -field EvictionSegmentSet

<dd>
<p>[out] Identifiers of segments that can be used for eviction. Setting bit 0 indicates that the first segment can be used for eviction, setting bit 1 indicates that the second segment can be used for eviction, and so on. </p>
<p>Only aperture segments can be specified by this member. If the driver specifies valid segments to be used for eviction, the video memory manager attempts to allocate resources in those aperture segments to accelerate the eviction process. If the driver specifies 0, the video memory manager calls the driver to transfer the content of an allocation directly to paged-locked system memory without mapping the underlying pages through an aperture segment.</p>
</dd>

### -field MaximumRenamingListLength

<dd>
<p>[out] The maximum length of the renaming list for the allocation. For more information about the renaming list, see <a href="https://msdn.microsoft.com/f22e19ba-9ff3-4aa1-a3f0-103f67ea7c60">Requesting to Rename an Allocation</a>.</p>
<p>Support for this member started with Windows 10 and the WDDM v2.</p>
</dd>

### -field PhysicalAdapterIndex

<dd>
<p>[out] The index of the physical adapter. </p>
<p>Support for this member started with Windows 10 and the WDDM v2.</p>
</dd>

### -field hAllocation

<dd>
<p>[out] A handle to the allocation. The display miniport driver must set this member to a value that it can use to refer to its private tracking structure for the allocation.</p>
</dd>

### -field Flags

<dd>
<p>[out] A <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationinfoflags.md">DXGK_ALLOCATIONINFOFLAGS</a> structure that identifies properties for an allocation in bit-field flags. These properties indicate the type of allocation to create. The display miniport driver specifies these flags for the video memory manager.</p>
</dd>

### -field FlagsWddm2

<dd>
<p>[out] The index of the physical adapter. </p>
<p>Support for this member started with Windows 10 and WDDM 2.0.</p>
</dd>

### -field pAllocationUsageHint

<dd>
<p>[out] A pointer to a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationusagehint.md">DXGK_ALLOCATIONUSAGEHINT</a> structure that the memory manager uses to determine how to use the allocation.</p>
</dd>

### -field AllocationPriority

<dd>
<p>[out] A UINT value that specifies the starting priority level of the allocation. </p>
<p>The driver determines the appropriate priority level for each allocation. For more information about priority levels, see the Remarks section of the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setprioritycb.md">pfnSetPriorityCb</a> function. If priority level for allocations is not an issue to the driver, the driver should set all priority levels to <b>D3DDDI_ALLOCATIONPRIORITY_NORMAL</b>. Note that 0 is an invalid initial allocation priority. </p>
</dd>
</dl>

## -remarks
<p>With the WDDM v2, the <b>DXGK_ALLOCATIONINFO</b> structure has been changed so that the read and write segment set are no longer differentiated. During surface creation the video memory manager will ignore the <b>SupportedReadSegmentSet</b> value and use only the segment set provide by <b>SupportedWriteSegmentSet</b>. Drivers should ensure that this value accurately represents the segment set that can be used by the allocation for its intended purpose.
</p>

<p>Ignoring the supported read segment set does not mean that it is no longer supported, but simply that there should no longer be a difference between these sets, and the video memory manager will be allowed to choose an appropriate segment for any allocation from a single segment set.
</p>

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
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-sharedprimarysurfacedata.md">D3DKMDDI_SHAREDPRIMARYSURFACEDATA</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationinfoflags.md">DXGK_ALLOCATIONINFOFLAGS</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationlist.md">DXGK_ALLOCATIONLIST</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-allocationusagehint.md">DXGK_ALLOCATIONUSAGEHINT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-segmentbankpreference.md">DXGK_SEGMENTBANKPREFERENCE</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-segmentdescriptor.md">DXGK_SEGMENTDESCRIPTOR</a>
</dt>
<dt>
<a href="display.dxgk_segmentpreference">DXGK_SEGMENTPREFERENCE</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-createallocation.md">DXGKARG_CREATEALLOCATION</a>
</dt>
<dt>
<a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>
</dt>
<dt>
<a href="display.dxgkddirender">DxgkDdiRender</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-allocatecb.md">pfnAllocateCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_ALLOCATIONINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
