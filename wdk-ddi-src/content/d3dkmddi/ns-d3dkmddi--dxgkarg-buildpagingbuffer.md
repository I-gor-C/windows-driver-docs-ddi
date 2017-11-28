---
UID: NS.d3dkmddi._DXGKARG_BUILDPAGINGBUFFER
title: DXGKARG_BUILDPAGINGBUFFER
author: windows-driver-content
description: The DXGKARG_BUILDPAGINGBUFFER structure describes parameters for building a paging buffer that is used in a memory-transfer operation.
old-location: display\dxgkarg_buildpagingbuffer.htm
old-project: display
ms.assetid: dc0de06b-d495-4ce2-b0e2-a6fefd6c8e0c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_BUILDPAGINGBUFFER, DXGKARG_BUILDPAGINGBUFFER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_BUILDPAGINGBUFFER
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

# DXGKARG_BUILDPAGINGBUFFER structure



## -description
<p>The <b>DXGKARG_BUILDPAGINGBUFFER</b> structure describes parameters for building a paging buffer that is used in a memory-transfer operation.</p>


## -syntax

````
typedef struct _DXGKARG_BUILDPAGINGBUFFER {
  VOID                             *pDmaBuffer;
  UINT                             DmaSize;
  VOID                             *pDmaBufferPrivateData;
  UINT                             DmaBufferPrivateDataSize;
  DXGK_BUILDPAGINGBUFFER_OPERATION Operation;
  UINT                             MultipassOffset;
  union {
    struct {
      HANDLE             hAllocation;
      UINT               TransferOffset;
      SIZE_T             TransferSize;
      struct {
        UINT SegmentId;
        union {
          LARGE_INTEGER SegmentAddress;
          MDL           *pMdl;
        };
      } Source;
      struct {
        UINT SegmentId;
        union {
          LARGE_INTEGER SegmentAddress;
          MDL           *pMdl;
        };
      } Destination;
      DXGK_TRANSFERFLAGS Flags;
      UINT               MdlOffset;
    } Transfer;
    struct {
      HANDLE hAllocation;
      SIZE_T FillSize;
      UINT   FillPattern;
      struct {
        UINT          SegmentId;
        LARGE_INTEGER SegmentAddress;
      } Destination;
    } Fill;
    struct {
      HANDLE                   hAllocation;
      DXGK_DISCARDCONTENTFLAGS Flags;
      UINT                     SegmentId;
      PHYSICAL_ADDRESS         SegmentAddress;
    } DiscardContent;
    struct {
      UINT             SegmentId;
      PHYSICAL_ADDRESS PhysicalAddress;
    } ReadPhysical;
    struct {
      UINT             SegmentId;
      PHYSICAL_ADDRESS PhysicalAddress;
    } WritePhysical;
    struct {
      HANDLE                hDevice;
      HANDLE                hAllocation;
      UINT                  SegmentId;
      SIZE_T                OffsetInPages;
      SIZE_T                NumberOfPages;
      PMDL                  pMdl;
      DXGK_MAPAPERTUREFLAGS Flags;
      ULONG                 MdlOffset;
    } MapApertureSegment;
    struct {
      HANDLE           hDevice;
      HANDLE           hAllocation;
      UINT             SegmentId;
      SIZE_T           OffsetInPages;
      SIZE_T           NumberOfPages;
      PHYSICAL_ADDRESS DummyPage;
    } UnmapApertureSegment;
    struct {
      HANDLE             hAllocation;
      UINT               TransferOffset;
      SIZE_T             TransferSize;
      struct {
        UINT SegmentId;
        union {
          LARGE_INTEGER SegmentAddress;
          MDL           *pMdl;
        };
      } Source;
      struct {
        UINT SegmentId;
        union {
          LARGE_INTEGER SegmentAddress;
          MDL           *pMdl;
        };
      } Destination;
      DXGK_TRANSFERFLAGS Flags;
      UINT               SwizzlingRangeId;
      UINT               SwizzlingRangeData;
    } SpecialLockTransfer;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
    struct {
      HANDLE hAllocation;
      struct {
        UINT                    SegmentId;
        union {
          LARGE_INTEGER SegmentAddress;
          MDL           *pMdl;
        };
        PVOID                   VirtualAddress;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
        D3DGPU_VIRTUAL_ADDRESS  GpuVirtualAddress;
#endif 
      } Destination;
    } InitContextResource;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
    DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL         TransferVirtual;
    DXGK_BUILDPAGINGBUFFER_FILLVIRTUAL             FillVirtual;
    DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE         UpdatePageTable;
    DXGK_BUILDPAGINGBUFFER_FLUSHTLB                FlushTlb;
    DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES    CopyPageTableEntries;
    DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION UpdateContextAllocation;
    DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY         NotifyResidency;
#endif 
    struct {
      UINT Reserved[64];
    } Reserved;
  };
  HANDLE                           hSystemContext;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
  D3DGPU_VIRTUAL_ADDRESS           DmaBufferGpuVirtualAddress;
#endif 
} DXGKARG_BUILDPAGINGBUFFER;
````


## -struct-fields
<dl>

### -field <b>pDmaBuffer</b>

<dd>
<p>[in/out] A virtual address to the first available byte in the paging buffer. When the driver is first called with a new paging buffer, this virtual address is aligned on 4 KB. The driver tightly packs operations in the paging buffer until the paging buffer is full and then uses a new paging buffer. Therefore, if the graphics processing unit (GPU) requires a specific alignment for a paging-buffer submission, the driver should enforce this alignment by padding the operations that it writes to the paging buffer. Before the <a href="display.dxgkddibuildpagingbuffer">DxgkDdiBuildPagingBuffer</a> function returns, the driver should update <b>pDmaBuffer</b> to point past the last byte that is written to the paging buffer. </p>
</dd>

### -field <b>DmaSize</b>

<dd>
<p>[in/out] The size, in bytes, of the paging buffer that <b>pDmaBuffer</b> specifies.</p>
</dd>

### -field <b>pDmaBufferPrivateData</b>

<dd>
<p>[in/out] A pointer to a driver-resident private data structure that is associated with the direct memory access (DMA) buffer (that is, paging buffer) that <b>pDmaBuffer</b> specifies.</p>
</dd>

### -field <b>DmaBufferPrivateDataSize</b>

<dd>
<p>[in/out] The number of bytes that remain in the private data structure that <b>pDmaBufferPrivateData</b> points to for the current operation.</p>
</dd>

### -field <b>Operation</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/dn906827">DXGK_BUILDPAGINGBUFFER_OPERATION</a>-typed value that indicates the type of memory operation to perform. </p>
</dd>

### -field <b>MultipassOffset</b>

<dd>
<p>[in/out] A UINT value that specifies the progress of the paging operation if multiple paging buffers are required. The driver sets this value to indicate a split into multiple paging buffers for more than one transfer operation. For example, the driver can store the page number that was last transferred for a paged-based transfer. </p>
</dd>

### -field <b>Transfer</b>

<dd>
<p>[in] A structure that describes the transfer operation.</p>
<dl>

### -field <b>hAllocation</b>

<dd>
<p>[in] A handle to the allocation that the driver's <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a> function previously returned in the <b>hAllocation</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a> structure, which is part of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a> structure's <b>pAllocationInfo</b> member. The allocation handle points to a buffer that contains private driver data for the transfer.</p>
</dd>

### -field <b>TransferOffset</b>

<dd>
<p>[in] The offset, in bytes, of the first page within the allocation that is transferred. This offset is applied only to a location that a segment location describes. This offset does not apply to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> description of a memory range. If the driver requires more than one paging buffer to complete the transfer (that is, the driver returns STATUS_GRAPHICS_INSUFFICIENT_DMA_BUFFER from its <a href="display.dxgkddibuildpagingbuffer">DxgkDdiBuildPagingBuffer</a> function), <b>TransferOffset</b> is the same for each call to <i>DxgkDdiBuildPagingBuffer</i> for this transfer.</p>
</dd>

### -field <b>TransferSize</b>

<dd>
<p>[in] The size, in bytes, of the memory information to transfer.</p>
</dd>

### -field <b>Source</b>

<dd>
<p>[in] A structure that describes the source allocation. This structure contains a <b>SegmentId</b> member and a union that contains either an offset into a segment of the source allocation (<b>SegmentAddress</b>) or a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> for the source (<b>pMdl</b>).</p>
<dl>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment within the source allocation, or zero if the source allocation is described by the <b>pMdl</b> member of the union that <b>Source</b> contains.</p>
</dd>

### -field <b>SegmentAddress</b>

<dd>
<p>[in] The source segment address, if the <b>SegmentId</b> member of <b>Source</b> is nonzero. The DirectX graphics kernel subsystem computes the segment address as the sum of the segment offset and the base address of the segment: <code>SegmentAddress = SegmentOffset + Segment.BaseAddr</code>.</p>
</dd>

### -field <b>pMdl</b>

<dd>
<p>[in] A pointer to a buffer that contains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> structure that describes the system memory pages for the source, if the <b>SegmentId</b> member of <b>Source</b> is zero.</p>
</dd>
</dl>
</dd>

### -field <b>Destination</b>

<dd>
<p>[in] A structure that describes the destination allocation. This structure contains a <b>SegmentId</b> member and a union that contains either an offset into a segment of the destination allocation (<b>SegmentAddress</b>) or a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> for the destination (<b>pMdl</b>).</p>
<dl>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment within the destination allocation, or zero if the destination allocation is described by the <b>pMdl</b> member of the union that <b>Destination</b> contains.</p>
</dd>

### -field <b>SegmentAddress</b>

<dd>
<p>[in] The destination segment address, if the <b>SegmentId</b> member of <b>Destination</b> is nonzero. The DirectX graphics kernel subsystem computes the segment address as the sum of the segment offset and the base address of the segment: <code>SegmentAddress = SegmentOffset + Segment.BaseAddr</code>.</p>
</dd>

### -field <b>pMdl</b>

<dd>
<p>[in] A pointer to a buffer that contains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> structure that describes the system memory pages for the destination, if the <b>SegmentId</b> member of <b>Destination</b> is zero.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562066">DXGK_TRANSFERFLAGS</a> structure that identifies, in bit-field flags, the type of special-lock-transfer operation to perform.</p>
</dd>

### -field <b>MdlOffset</b>

<dd>
<p>[in] The offset, in system memory pages, within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> structure that the <b>pMdl</b> member points to, to the first system memory page for the current operation. The driver can obtain the physical address of the first system memory page by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554537">MmGetMdlPfnArray</a> function as follows. </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>MmGetMdlPfnArray(pMdl)[MdlOffset];</pre>
</td>
</tr>
</table></span></div>
</dd>
</dl>
</dd>

### -field <b>Fill</b>

<dd>
<p>[in] A structure that describes the fill operation.</p>
<dl>

### -field <b>hAllocation</b>

<dd>
<p>[in] A handle to the allocation that contains content to fill.</p>
</dd>

### -field <b>FillSize</b>

<dd>
<p>[in] The size, in bytes, of the memory information to fill.</p>
</dd>

### -field <b>FillPattern</b>

<dd>
<p>[in] The pattern to fill the destination with. The video memory manager uses this information to initialize video memory to a specific pattern when an allocation without content is first paged in. In this case, no source exists for the fill request—only a destination exists.</p>
</dd>

### -field <b>Destination</b>

<dd>
<p>[in] A structure that describes the destination allocation for the fill operation.</p>
<dl>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment within the destination allocation.</p>
</dd>

### -field <b>SegmentAddress</b>

<dd>
<p>[in] The destination segment address. The DirectX graphics kernel subsystem computes the segment address as the sum of the segment offset and the base address of the segment: <code>SegmentAddress = SegmentOffset + Segment.BaseAddr</code>.</p>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field <b>DiscardContent</b>

<dd>
<p>[in] A structure that describes the discard-content operation.</p>
<dl>

### -field <b>hAllocation</b>

<dd>
<p>[in] A handle to the allocation that contains content to discard.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561055">DXGK_DISCARDCONTENTFLAGS</a> structure that identifies, in bit-field flags, the type of discard-content operation to perform.</p>
</dd>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment within the allocation to discard content from.</p>
</dd>

### -field <b>SegmentAddress</b>

<dd>
<p>[in] A PHYSICAL_ADDRESS data type (which is defined as LARGE_INTEGER) that indicates the segment address. The DirectX graphics kernel subsystem computes the segment address as the sum of the segment offset and the base address of the segment: <code>SegmentAddress = SegmentOffset + Segment.BaseAddr</code>. This location is where content is discarded from.</p>
</dd>
</dl>
</dd>

### -field <b>ReadPhysical</b>

<dd>
<p>[in] A structure that describes the read-physical operation.</p>
<dl>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment that data is read from.</p>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>[in] A PHYSICAL_ADDRESS data type (which is defined as LARGE_INTEGER) that indicates the physical address, within the segment that <b>SegmentId</b> specifies, where the data is read.</p>
</dd>
</dl>
</dd>

### -field <b>WritePhysical</b>

<dd>
<p>[in] A structure that describes the write-physical operation.</p>
<dl>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment to which data is written.</p>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>[in] A PHYSICAL_ADDRESS data type (which is defined as LARGE_INTEGER) that indicates the physical address, within the segment that <b>SegmentId</b> specifies, where the data is written.</p>
</dd>
</dl>
</dd>

### -field <b>MapApertureSegment</b>

<dd>
<p>[in] A structure that describes the map-aperture-segment operation.</p>
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the device that owns the allocation that <b>hAllocation</b> specifies that is mapped into the aperture segment that <b>SegmentId</b> specifies. </p>
<p>For a shared allocation, <b>hDevice</b> is set to the device that the video memory manager determined to be the owner of the allocation.</p>
<p><b>hDevice</b> is <b>NULL</b> for the primary allocation. </p>
</dd>

### -field <b>hAllocation</b>

<dd>
<p>[in] A handle to the allocation that is mapped into the aperture segment that <b>SegmentId</b> specifies. </p>
<p><b>hAllocation</b> is <b>NULL</b> when a DMA buffer is mapped into the aperture segment because DMA buffers are not explicitly created by the driver.</p>
</dd>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of an aperture segment to configure.</p>
</dd>

### -field <b>OffsetInPages</b>

<dd>
<p>[in] The offset, in pages, from the beginning of the segment to the first pages to map.</p>
</dd>

### -field <b>NumberOfPages</b>

<dd>
<p>[in] The number of pages to map.</p>
</dd>

### -field <b>pMdl</b>

<dd>
<p>[in] A pointer to a buffer that contains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> structure that describes the physical system memory pages to map into the aperture segment.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561139">DXGK_MAPAPERTUREFLAGS</a> structure that identifies, in bit-field flags, the type of map-aperture-segment operation to perform.</p>
</dd>

### -field <b>MdlOffset</b>

<dd>
<p>[in] The offset, in system memory pages, within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> structure that the <b>pMdl</b> member points to, to the first system memory page for the current operation. The driver can obtain the physical address of the first system memory page by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554537">MmGetMdlPfnArray</a> function as follows. </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>MmGetMdlPfnArray(pMdl)[MdlOffset];</pre>
</td>
</tr>
</table></span></div>
</dd>
</dl>
</dd>

### -field <b>UnmapApertureSegment</b>

<dd>
<p>[in] A structure that describes the unmap-aperture-segment operation.</p>
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the device that owns the allocation that <b>hAllocation</b> specifies that is unmapped from the aperture segment that <b>SegmentId</b> specifies. </p>
<p>For a shared allocation, <b>hDevice</b> is set to the device that the video memory manager determined to be the owner of the allocation. </p>
<p><b>hDevice</b> is <b>NULL</b> for the primary allocation. </p>
</dd>

### -field <b>hAllocation</b>

<dd>
<p>[in] A handle to the allocation that is unmapped from the aperture segment that <b>SegmentId</b> specifies. </p>
<p><b>hAllocation</b> is <b>NULL</b> when a DMA buffer is unmapped from the aperture segment because DMA buffers are not explicitly created by the driver.</p>
</dd>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of an aperture segment to configure.</p>
</dd>

### -field <b>OffsetInPages</b>

<dd>
<p>[in] The offset, in pages, from the beginning of the segment to the first pages to unmap.</p>
</dd>

### -field <b>NumberOfPages</b>

<dd>
<p>[in] The number of pages to unmap.</p>
</dd>

### -field <b>DummyPage</b>

<dd>
<p>[in] A PHYSICAL_ADDRESS data type (which is defined as LARGE_INTEGER) that indicates the physical address of the placeholder page where the driver should map the range that is unmapped.</p>
</dd>
</dl>
</dd>

### -field <b>SpecialLockTransfer</b>

<dd>
<p>[in] A structure that describes the special-lock-transfer operation.</p>
<dl>

### -field <b>hAllocation</b>

<dd>
<p>[in] A handle to the allocation that the driver's <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a> function previously returned in the <b>hAllocation</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a> structure, which is part of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a> structure's <b>pAllocationInfo</b> member. The allocation handle points to a buffer that contains private driver data for the special-lock transfer.</p>
</dd>

### -field <b>TransferOffset</b>

<dd>
<p>[in] The offset, in bytes, of the first page within the allocation that is transferred. This offset is applied only to a location that a segment location describes. This offset does not apply to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> description of a memory range. If the driver requires more than one paging buffer to complete the transfer (that is, the driver returns STATUS_GRAPHICS_INSUFFICIENT_DMA_BUFFER from its <a href="display.dxgkddibuildpagingbuffer">DxgkDdiBuildPagingBuffer</a> function), <b>TransferOffset</b> is the same for each call to <i>DxgkDdiBuildPagingBuffer</i> for this transfer.</p>
</dd>

### -field <b>TransferSize</b>

<dd>
<p>[in] The size, in bytes, of the memory information to transfer.</p>
</dd>

### -field <b>Source</b>

<dd>
<p>[in] A structure that describes the source allocation. This structure contains a <b>SegmentId</b> member and a union that contains either an offset into a segment of the source allocation (<b>SegmentAddress</b>) or a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> for the source (<b>pMdl</b>).</p>
<dl>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment within the source allocation, or zero if the source allocation is described by the <b>pMdl</b> member of the union that <b>Source</b> contains.</p>
</dd>

### -field (<i>unnamed union</i>)

<dd>
<p>[in] A union that contains either an offset into a segment of the source allocation (<b>SegmentAddress</b>) or a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> for the source (<b>pMdl</b>).</p>
<dl>

### -field <b>SegmentAddress</b>

<dd>
<p>[in] The source segment address, if the <b>SegmentId</b> member of <b>Source</b> is nonzero. The DirectX graphics kernel subsystem computes the segment address as the sum of the segment offset and the base address of the segment: <code>SegmentAddress = SegmentOffset + Segment.BaseAddr</code>.</p>
</dd>

### -field <b>pMdl</b>

<dd>
<p>[in] A pointer to a buffer that contains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> structure that describes the system memory pages for the source, if the <b>SegmentId</b> member of <b>Source</b> is zero.</p>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field <b>Destination</b>

<dd>
<p>[in] A structure that describes the destination allocation. This structure contains a <b>SegmentId</b> member and a union that contains either an offset into a segment of the destination allocation (<b>SegmentAddress</b>) or a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> for the destination (<b>pMdl</b>).</p>
<dl>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment within the destination allocation, or zero if the destination allocation is described by the <b>pMdl</b> member of the union that <b>Destination</b> contains.</p>
</dd>

### -field (<i>unnamed union</i>)

<dd>
<p>[in] A union that contains either an offset into a segment of the destination allocation (<b>SegmentAddress</b>) or a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> for the destination (<b>pMdl</b>).</p>
<dl>

### -field <b>SegmentAddress</b>

<dd>
<p>[in] The destination segment address, if the <b>SegmentId</b> member of <b>Destination</b> is nonzero. The DirectX graphics kernel subsystem computes the segment address as the sum of the segment offset and the base address of the segment: <code>SegmentAddress = SegmentOffset + Segment.BaseAddr</code>.</p>
</dd>

### -field <b>pMdl</b>

<dd>
<p>[in] A pointer to a buffer that contains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> structure that describes the system memory pages for the destination, if the <b>SegmentId</b> member of <b>Destination</b> is zero.</p>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562066">DXGK_TRANSFERFLAGS</a> structure that identifies, in bit-field flags, the type of special-lock-transfer operation to perform.</p>
</dd>

### -field <b>SwizzlingRangeId</b>

<dd>
<p>[in] A UINT value that identifies the swizzling range.</p>
</dd>

### -field <b>SwizzlingRangeData</b>

<dd>
<p>[in] A UINT value that specifies swizzling range data.</p>
</dd>
</dl>
</dd>

### -field <b>InitContextResource</b>

<dd>
<p>[in] A structure that describes the context initialization operation.
</p>
<p>Supported beginning with Windows 8.</p>
<dl>

### -field <b>hAllocation</b>

<dd>
<p>[in] A handle to the context allocation that was created when the driver called <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-createcontextallocation.md">DxgkCbCreateContextAllocation</a>. The handle to this allocation is returned in the <b>hAllocation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451242">DXGKARGCB_CREATECONTEXTALLOCATION</a> structure. The driver passes a pointer to this structure in the 

<i>ContextAllocation</i> parameter when it calls <b>DxgkCbCreateContextAllocation</b>.</p>
</dd>

### -field <b>Destination</b>

<dd>
<p>[in] A structure that describes the destination context allocation. This structure contains a <b>SegmentId</b> member and a union that contains either an offset into a segment of the destination context allocation (<b>SegmentAddress</b>) or a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> for the destination (<b>pMdl</b>).</p>
<dl>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment within the destination context allocation, or zero if the destination context allocation is described by the <b>pMdl</b> member of the union that <b>Destination</b> contains.</p>
</dd>

### -field (<i>unnamed union</i>)

<dd>
<p>[in] A union that contains either an offset into a segment of the destination context allocation (<b>SegmentAddress</b>) or a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> for the destination (<b>pMdl</b>).</p>
<dl>

### -field <b>SegmentAddress</b>

<dd>
<p>[in] The destination segment address, if the <b>SegmentId</b> member of <b>Destination</b> is nonzero. The DirectX graphics kernel subsystem computes the segment address as the sum of the segment offset and the base address of the segment: <code>SegmentAddress = SegmentOffset + Segment.BaseAddr</code>.</p>
</dd>

### -field <b>pMdl</b>

<dd>
<p>[in] A pointer to a buffer that contains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a> structure that describes the system memory pages for the destination, if the <b>SegmentId</b> member of <b>Destination</b> is zero.</p>
</dd>
</dl>
</dd>

### -field <b>VirtualAddress</b>

<dd>
<p>[in] The virtual address of the destination context allocation. This address is valid during the lifetime of the context allocation.</p>
<p>Follow procedures in  <a href="dxgkcbcreatecontextallocation.htm#virtual_addresses"><i>Virtual addresses for destination context allocations</i></a> in the <i>DxgkCbCreateContextAllocation</i> topic to ensure that the virtual address is valid.</p>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field <b>TransferVirtual</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn894169">DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL</a> structure that describes the operation used to transfer allocation content between locations in memory. </p>
</dd>

### -field <b>FillVirtual</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn894166">DXGK_BUILDPAGINGBUFFER_FILLVIRTUAL</a> structure that describes the operation used to fill an allocation with a pattern. </p>
</dd>

### -field <b>UpdatePageTable</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn894171">DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE</a> structure that describes the operation used to update a page table. </p>
</dd>

### -field <b>FlushTlb</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn894167">DXGK_BUILDPAGINGBUFFER_FLUSHTLB</a> structure that describes the operation used to flush the translation look-aside buffers. </p>
</dd>

### -field <b>CopyPageTableEntries</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn894164">DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES</a> structure that describes the operation used copy page table entries from one location to another. </p>
</dd>

### -field <b>UpdateContextAllocation</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn894170">DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION</a> structure that describes the operation used to update the content of a context or device allocation.</p>
</dd>

### -field <b>NotifyResidency</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn894168">DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY</a> structure that describes a residency allocation change operation. </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should not be used.</p>
<dl>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should not be used.</p>
</dd>
</dl>
</dd>

### -field <b>hSystemContext</b>

<dd>
<p>[in] A handle to the system context for the paging operation.</p>
</dd>

### -field <b>DmaBufferGpuVirtualAddress</b>

<dd></dd>
</dl>

## -remarks
<p>MDL is defined in the <a href="wdkgloss.m#wdkgloss.mdl#wdkgloss.mdl"><i>Windows Driver Model (WDM)</i></a> documentation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows Vista.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561055">DXGK_DISCARDCONTENTFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561139">DXGK_MAPAPERTUREFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562066">DXGK_TRANSFERFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451242">DXGKARGCB_CREATECONTEXTALLOCATION</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-createcontextallocation.md">DxgkCbCreateContextAllocation</a>
</dt>
<dt>
<a href="display.dxgkddibuildpagingbuffer">DxgkDdiBuildPagingBuffer</a>
</dt>
<dt>
<a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554537">MmGetMdlPfnArray</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lockcb.md">pfnLockCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894169">DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894166">DXGK_BUILDPAGINGBUFFER_FILLVIRTUAL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894171">DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894167">DXGK_BUILDPAGINGBUFFER_FLUSHTLB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894164">DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894168">DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894170">DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_BUILDPAGINGBUFFER structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
