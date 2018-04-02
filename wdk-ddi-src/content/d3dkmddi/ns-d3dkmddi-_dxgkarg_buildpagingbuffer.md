---
UID: NS:d3dkmddi._DXGKARG_BUILDPAGINGBUFFER
title: "_DXGKARG_BUILDPAGINGBUFFER"
author: windows-driver-content
description: The DXGKARG_BUILDPAGINGBUFFER structure describes parameters for building a paging buffer that is used in a memory-transfer operation.
old-location: display\dxgkarg_buildpagingbuffer.htm
old-project: display
ms.assetid: dc0de06b-d495-4ce2-b0e2-a6fefd6c8e0c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*IN_PDXGKARG_BUILDPAGINGBUFFER, DXGKARG_BUILDPAGINGBUFFER, DXGKARG_BUILDPAGINGBUFFER structure [Display Devices], DXGKARG_BUILDPAGINGBUFFER_OPERATION, DXGK_BUILDPAGINGBUFFER_OPERATION, DmStructs_06cb7ec2-482d-41ba-b550-3c4f27d36070.xml, _DXGKARG_BUILDPAGINGBUFFER, d3dkmddi/DXGKARG_BUILDPAGINGBUFFER, display.dxgkarg_buildpagingbuffer"
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
-	DXGKARG_BUILDPAGINGBUFFER
product: Windows
targetos: Windows
req.typenames: DXGKARG_BUILDPAGINGBUFFER
---

# _DXGKARG_BUILDPAGINGBUFFER structure
The <b>DXGKARG_BUILDPAGINGBUFFER</b> structure describes parameters for building a paging buffer that is used in a memory-transfer operation.

## Syntax
```
typedef struct _DXGKARG_BUILDPAGINGBUFFER {
  VOID                             *pDmaBuffer;
  UINT                             DmaSize;
  VOID                             *pDmaBufferPrivateData;
  UINT                             DmaBufferPrivateDataSize;
  DXGK_BUILDPAGINGBUFFER_OPERATION Operation;
  UINT                             MultipassOffset;
  union {
    DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES    CopyPageTableEntries;
    DXGK_BUILDPAGINGBUFFER_FILLVIRTUAL             FillVirtual;
    DXGK_BUILDPAGINGBUFFER_FLUSHTLB                FlushTlb;
    DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY         NotifyResidency;
    DXGK_BUILDPAGINGBUFFER_SIGNALMONITOREDFENCE    SignalMonitoredFence;
    struct {
      HANDLE             hAllocation;
      UINT               TransferOffset;
      SIZE_T             TransferSize;
      struct {
        UINT SegmentId;
        struct {
          LARGE_INTEGER SegmentAddress;
          MDL           *pMdl;
        };
      } Source;
      struct {
        UINT SegmentId;
        struct {
          LARGE_INTEGER SegmentAddress;
          MDL           *pMdl;
        };
      } Destination;
      DXGK_TRANSFERFLAGS Flags;
      UINT               MdlOffset;
    } Transfer;
    DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL         TransferVirtual;
    DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION UpdateContextAllocation;
    DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE         UpdatePageTable;
    struct {
      HANDLE hAllocation;
      SIZE_T FillSize;
      UINT   FillPattern;
      struct {
        LARGE_INTEGER SegmentAddress;
        UINT          SegmentId;
      } Destination;
    } Fill;
    struct {
      HANDLE                   hAllocation;
      DXGK_DISCARDCONTENTFLAGS Flags;
      UINT                     SegmentId;
      PHYSICAL_ADDRESS         SegmentAddress;
    } DiscardContent;
    struct {
      UINT             SegmentId;
      PHYSICAL_ADDRESS PhysicalAddress;
    } ReadPhysical;
    struct {
      UINT             SegmentId;
      PHYSICAL_ADDRESS PhysicalAddress;
    } WritePhysical;
    struct {
      HANDLE                hDevice;
      HANDLE                hAllocation;
      UINT                  SegmentId;
      SIZE_T                OffsetInPages;
      SIZE_T                NumberOfPages;
      PMDL                  pMdl;
      DXGK_MAPAPERTUREFLAGS Flags;
      ULONG                 MdlOffset;
    } MapApertureSegment;
    struct {
      HANDLE           hDevice;
      HANDLE           hAllocation;
      UINT             SegmentId;
      SIZE_T           OffsetInPages;
      SIZE_T           NumberOfPages;
      PHYSICAL_ADDRESS DummyPage;
    } UnmapApertureSegment;
    struct {
      HANDLE             hAllocation;
      UINT               TransferOffset;
      SIZE_T             TransferSize;
      struct {
        UINT SegmentId;
        struct {
          LARGE_INTEGER SegmentAddress;
          MDL           *pMdl;
        };
      } Source;
      struct {
        UINT SegmentId;
        struct {
          LARGE_INTEGER SegmentAddress;
          MDL           *pMdl;
        };
      } Destination;
      DXGK_TRANSFERFLAGS Flags;
      UINT               SwizzlingRangeId;
      UINT               SwizzlingRangeData;
    } SpecialLockTransfer;
    struct {
      HANDLE hAllocation;
      struct {
        D3DGPU_VIRTUAL_ADDRESS GpuVirtualAddress;
        UINT                   SegmentId;
        PVOID                  VirtualAddress;
        struct {
          LARGE_INTEGER SegmentAddress;
          MDL           *pMdl;
        };
      } Destination;
    } InitContextResource;
    struct {
      UINT Reserved[64];
    } Reserved;
  };
  HANDLE                           hSystemContext;
  D3DGPU_VIRTUAL_ADDRESS           DmaBufferGpuVirtualAddress;
  UINT                             DmaBufferWriteOffset;
} DXGKARG_BUILDPAGINGBUFFER;
```

## Members


`pDmaBuffer`

[in/out] A virtual address to the first available byte in the paging buffer. When the driver is first called with a new paging buffer, this virtual address is aligned on 4 KB. The driver tightly packs operations in the paging buffer until the paging buffer is full and then uses a new paging buffer. Therefore, if the graphics processing unit (GPU) requires a specific alignment for a paging-buffer submission, the driver should enforce this alignment by padding the operations that it writes to the paging buffer. Before the <a href="https://msdn.microsoft.com/d315ff53-4a9f-46a3-ad74-d65a5eb72de1">DxgkDdiBuildPagingBuffer</a> function returns, the driver should update <b>pDmaBuffer</b> to point past the last byte that is written to the paging buffer.

`DmaSize`

[in/out] The size, in bytes, of the paging buffer that <b>pDmaBuffer</b> specifies.

`pDmaBufferPrivateData`

[in/out] A pointer to a driver-resident private data structure that is associated with the direct memory access (DMA) buffer (that is, paging buffer) that <b>pDmaBuffer</b> specifies.

`DmaBufferPrivateDataSize`

[in/out] The number of bytes that remain in the private data structure that <b>pDmaBufferPrivateData</b> points to for the current operation.

`Operation`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/dn906827">DXGK_BUILDPAGINGBUFFER_OPERATION</a>-typed value that indicates the type of memory operation to perform.

`MultipassOffset`

[in/out] A UINT value that specifies the progress of the paging operation if multiple paging buffers are required. The driver sets this value to indicate a split into multiple paging buffers for more than one transfer operation. For example, the driver can store the page number that was last transferred for a paged-based transfer.

`hSystemContext`

[in] A handle to the system context for the paging operation.

`DmaBufferGpuVirtualAddress`



`DmaBufferWriteOffset`



## Remarks
MDL is defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565698">Windows Driver Model (WDM)</a> documentation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows Vista. Supported starting with Windows Vista. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451242">DXGKARGCB_CREATECONTEXTALLOCATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557559">DXGKARG_CREATEALLOCATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894164">DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894166">DXGK_BUILDPAGINGBUFFER_FILLVIRTUAL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894167">DXGK_BUILDPAGINGBUFFER_FLUSHTLB</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894168">DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894169">DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894170">DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894171">DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561055">DXGK_DISCARDCONTENTFLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561139">DXGK_MAPAPERTUREFLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562066">DXGK_TRANSFERFLAGS</a>



<a href="https://msdn.microsoft.com/b6b142a4-20eb-4368-bd7f-8a25f4fe48ca">DxgkCbCreateContextAllocation</a>



<a href="https://msdn.microsoft.com/d315ff53-4a9f-46a3-ad74-d65a5eb72de1">DxgkDdiBuildPagingBuffer</a>



<a href="https://msdn.microsoft.com/a28287d6-4dfa-4db4-92df-bbcd9379a5b2">DxgkDdiCreateAllocation</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554414">MDL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554537">MmGetMdlPfnArray</a>



<a href="https://msdn.microsoft.com/69022797-432a-410b-8cbf-e1ef7111e7ea">pfnLockCb</a>