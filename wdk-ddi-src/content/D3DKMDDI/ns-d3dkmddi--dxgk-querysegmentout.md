---
UID: NS.d3dkmddi._DXGK_QUERYSEGMENTOUT
title: DXGK_QUERYSEGMENTOUT
author: windows-driver-content
description: The DXGK_QUERYSEGMENTOUT structure describes memory-segment information that the display miniport driver should return from a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_querysegmentout.htm
ms.assetid: df640b7a-865a-4a8b-94be-ebc60e44cf72
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
req.alt-api: DXGK_QUERYSEGMENTOUT
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
ms.keywords: DXGK_QUERYSEGMENTOUT, DXGK_QUERYSEGMENTOUT
req.iface: 
---

# DXGK_QUERYSEGMENTOUT structure



## -description
<p>The DXGK_QUERYSEGMENTOUT structure describes memory-segment information that the display miniport driver should return from a call to its <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function. </p>


## -syntax

````
typedef struct _DXGK_QUERYSEGMENTOUT {
  UINT                   NbSegment;
  DXGK_SEGMENTDESCRIPTOR *pSegmentDescriptor;
  UINT                   PagingBufferSegmentId;
  UINT                   PagingBufferSize;
  UINT                   PagingBufferPrivateDataSize;
} DXGK_QUERYSEGMENTOUT;
````


## -struct-fields
<dl>

### -field <b>NbSegment</b>

<dd>
<p>[out] The number of memory segments that the driver supports.</p>
</dd>

### -field <b>pSegmentDescriptor</b>

<dd>
<p>[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff562035">DXGK_SEGMENTDESCRIPTOR</a> structures that the driver populates with information about the segments it supports. The size of the array is the value that <b>NbSegment</b> specifies.</p>
</dd>

### -field <b>PagingBufferSegmentId</b>

<dd>
<p>[out] The identifier of the segment that the video memory manager should allocate the paging buffer from. This segment must be an aperture segment.</p>
</dd>

### -field <b>PagingBufferSize</b>

<dd>
<p>[out] The size, in bytes, that the video memory manager should allocate for the paging buffer.</p>
</dd>

### -field <b>PagingBufferPrivateDataSize</b>

<dd>
<p>[out] The size, in bytes, of the driver-resident private data structure that is associated with each paging buffer. Memory for this private data structure is allocated from nonpaged pool. If the driver specifies zero for <b>PagingBufferPrivateDataSize</b>, no memory is allocated for the private data structure.</p>
<p>The private data structure that is associated with a paging buffer is initialized to zero when the paging buffer is created. During the lifetime of the paging buffer, the video memory manager never accesses the private data structure that is associated with the paging buffer.</p>
</dd>
</dl>

## -remarks
<p>The video memory manager allocates a paging buffer either from an aperture segment (if the <b>PagingBufferSegmentId</b> member identifies the segment) or as a contiguous write-combined memory block (if <b>PagingBufferSegmentId</b> is set to 0). If <b>PagingBufferSegmentId</b> is set to 0, the graphics processing unit (GPU) must access direct memory access (DMA) buffers by using PCI cycles on systems where AGP transfers that occur outside the AGP aperture are not permitted.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562015">DXGK_QUERYSEGMENTIN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562035">DXGK_SEGMENTDESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557621">DXGKARG_QUERYADAPTERINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_QUERYSEGMENTOUT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
