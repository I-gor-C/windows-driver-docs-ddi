---
UID: NS:d3dkmddi._DXGKARG_BUILDPAGINGBUFFER
title: "_DXGKARG_BUILDPAGINGBUFFER"
author: windows-driver-content
description: The DXGKARG_BUILDPAGINGBUFFER structure describes parameters for building a paging buffer that is used in a memory-transfer operation.
old-location: display\dxgkarg_buildpagingbuffer.htm
old-project: display
ms.assetid: dc0de06b-d495-4ce2-b0e2-a6fefd6c8e0c
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.dxgkarg_buildpagingbuffer, *IN_PDXGKARG_BUILDPAGINGBUFFER, DXGKARG_BUILDPAGINGBUFFER structure [Display Devices], DmStructs_06cb7ec2-482d-41ba-b550-3c4f27d36070.xml, _DXGKARG_BUILDPAGINGBUFFER, DXGKARG_BUILDPAGINGBUFFER, DXGK_BUILDPAGINGBUFFER_OPERATION, d3dkmddi/DXGKARG_BUILDPAGINGBUFFER, DXGKARG_BUILDPAGINGBUFFER_OPERATION
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmddi.h
apiname:
-	DXGKARG_BUILDPAGINGBUFFER
product: Windows
targetos: Windows
req.typenames: DXGKARG_BUILDPAGINGBUFFER
---

# _DXGKARG_BUILDPAGINGBUFFER structure
The <b>DXGKARG_BUILDPAGINGBUFFER</b> structure describes parameters for building a paging buffer that is used in a memory-transfer operation.

## Syntax
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

## Members


`DmaBufferGpuVirtualAddress`



`DmaBufferPrivateDataSize`

[in/out] The number of bytes that remain in the private data structure that <b>pDmaBufferPrivateData</b> points to for the current operation.

`DmaBufferWriteOffset`



`DmaSize`

[in/out] The size, in bytes, of the paging buffer that <b>pDmaBuffer</b> specifies.

`hSystemContext`

[in] A handle to the system context for the paging operation.

`MultipassOffset`

[in/out] A UINT value that specifies the progress of the paging operation if multiple paging buffers are required. The driver sets this value to indicate a split into multiple paging buffers for more than one transfer operation. For example, the driver can store the page number that was last transferred for a paged-based transfer.

`Operation`

[in] A <a href="..\d3dkmddi\ne-d3dkmddi-_dxgk_buildpagingbuffer_operation.md">DXGK_BUILDPAGINGBUFFER_OPERATION</a>-typed value that indicates the type of memory operation to perform.

`pDmaBuffer`

[in/out] A virtual address to the first available byte in the paging buffer. When the driver is first called with a new paging buffer, this virtual address is aligned on 4 KB. The driver tightly packs operations in the paging buffer until the paging buffer is full and then uses a new paging buffer. Therefore, if the graphics processing unit (GPU) requires a specific alignment for a paging-buffer submission, the driver should enforce this alignment by padding the operations that it writes to the paging buffer. Before the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_buildpagingbuffer.md">DxgkDdiBuildPagingBuffer</a> function returns, the driver should update <b>pDmaBuffer</b> to point past the last byte that is written to the paging buffer.

`pDmaBufferPrivateData`

[in/out] A pointer to a driver-resident private data structure that is associated with the direct memory access (DMA) buffer (that is, paging buffer) that <b>pDmaBuffer</b> specifies.

## Remarks
MDL is defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565698">Windows Driver Model (WDM)</a> documentation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows Vista. Supported starting with Windows Vista. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff554537">MmGetMdlPfnArray</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb_createcontextallocation.md">DxgkCbCreateContextAllocation</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_transferflags.md">DXGK_TRANSFERFLAGS</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_buildpagingbuffer_copypagetableentries.md">DXGK_BUILDPAGINGBUFFER_COPYPAGETABLEENTRIES</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_buildpagingbuffer_transfervirtual.md">DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL</a>



<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_lockcb.md">pfnLockCb</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createallocation.md">DxgkDdiCreateAllocation</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_buildpagingbuffer_updatecontextallocation.md">DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_buildpagingbuffer_notifyresidency.md">DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_mapapertureflags.md">DXGK_MAPAPERTUREFLAGS</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_buildpagingbuffer_fillvirtual.md">DXGK_BUILDPAGINGBUFFER_FILLVIRTUAL</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_buildpagingbuffer.md">DxgkDdiBuildPagingBuffer</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkargcb_createcontextallocation.md">DXGKARGCB_CREATECONTEXTALLOCATION</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_buildpagingbuffer_flushtlb.md">DXGK_BUILDPAGINGBUFFER_FLUSHTLB</a>



<a href="..\wdm\ns-wdm-_mdl.md">MDL</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_buildpagingbuffer_updatepagetable.md">DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_discardcontentflags.md">DXGK_DISCARDCONTENTFLAGS</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_allocationinfo.md">DXGK_ALLOCATIONINFO</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_createallocation.md">DXGKARG_CREATEALLOCATION</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_BUILDPAGINGBUFFER structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>