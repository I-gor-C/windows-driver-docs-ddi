---
UID: NS:d3dkmddi._DXGKARGCB_NOTIFY_INTERRUPT_DATA
title: "_DXGKARGCB_NOTIFY_INTERRUPT_DATA"
author: windows-driver-content
description: The DXGKARGCB_NOTIFY_INTERRUPT_DATA structure describes notification information.
old-location: display\dxgkargcb_notify_interrupt_data.htm
old-project: display
ms.assetid: c71078fb-5666-4038-81a0-de9375bafb5c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*IN_CONST_PDXGKARGCB_NOTIFY_INTERRUPT_DATA, DXGKARGCB_NOTIFY_INTERRUPT_DATA, DXGKARGCB_NOTIFY_INTERRUPT_DATA structure [Display Devices], DmStructs_071ed85c-70d6-44d8-95e3-7f6609331f4f.xml, STATUS_INVALID_PARAMETER, STATUS_NO_MEMORY, STATUS_SUCCESS, _DXGKARGCB_NOTIFY_INTERRUPT_DATA, d3dkmddi/DXGKARGCB_NOTIFY_INTERRUPT_DATA, display.dxgkargcb_notify_interrupt_data"
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
-	DXGKARGCB_NOTIFY_INTERRUPT_DATA
product: Windows
targetos: Windows
req.typenames: DXGKARGCB_NOTIFY_INTERRUPT_DATA
---

# _DXGKARGCB_NOTIFY_INTERRUPT_DATA structure
The DXGKARGCB_NOTIFY_INTERRUPT_DATA structure describes notification information.

## Syntax
```
typedef struct _DXGKARGCB_NOTIFY_INTERRUPT_DATA {
  DXGK_INTERRUPT_TYPE                InterruptType;
  union {
    DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS DisplayOnlyPresentProgress;
    struct {
      UINT SubmissionFenceId;
      UINT NodeOrdinal;
      UINT EngineOrdinal;
    } DmaCompleted;
    struct {
      UINT PreemptionFenceId;
      UINT LastCompletedFenceId;
      UINT NodeOrdinal;
      UINT EngineOrdinal;
    } DmaPreempted;
    struct {
      UINT     FaultedFenceId;
      NTSTATUS Status;
      UINT     NodeOrdinal;
      UINT     EngineOrdinal;
    } DmaFaulted;
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId;
      PHYSICAL_ADDRESS               PhysicalAddress;
      UINT                           PhysicalAdapterMask;
    } CrtcVsync;
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId;
    } DisplayOnlyVsync;
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID     VidPnTargetId;
      UINT                               PhysicalAdapterMask;
      UINT                               MultiPlaneOverlayVsyncInfoCount;
      DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO *pMultiPlaneOverlayVsyncInfo;
    } CrtcVsyncWithMultiPlaneOverlay;
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId;
      DXGK_MIRACAST_CHUNK_INFO       ChunkInfo;
      PVOID                          pPrivateDriverData;
      UINT                           PrivateDataDriverSize;
      NTSTATUS                       Status;
    } MiracastEncodeChunkCompleted;
    struct {
      UINT                       FaultedFenceId;
      UINT64                     FaultedPrimitiveAPISequenceNumber;
      DXGK_RENDER_PIPELINE_STAGE FaultedPipelineStage;
      UINT                       FaultedBindTableEntry;
      DXGK_PAGE_FAULT_FLAGS      PageFaultFlags;
      D3DGPU_VIRTUAL_ADDRESS     FaultedVirtualAddress;
      UINT                       NodeOrdinal;
      UINT                       EngineOrdinal;
      UINT                       PageTableLevel;
      DXGK_FAULT_ERROR_CODE      FaultErrorCode;
      HANDLE                     FaultedProcessHandle;
    } DmaPageFaulted;
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID      VidPnTargetId;
      UINT                                PhysicalAdapterMask;
      UINT                                MultiPlaneOverlayVsyncInfoCount;
      DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO2 *pMultiPlaneOverlayVsyncInfo;
      ULONGLONG                           GpuFrequency;
      ULONGLONG                           GpuClockCounter;
    } CrtcVsyncWithMultiPlaneOverlay2;
    struct {
      UINT NodeOrdinal;
      UINT EngineOrdinal;
    } MonitoredFenceSignaled;
    struct {
      UINT   NodeOrdinal;
      UINT   EngineOrdinal;
      UINT64 ContextSwitchFence;
    } HwContextListSwitchCompleted;
    struct {
      UINT64                     FaultedFenceId;
      D3DGPU_VIRTUAL_ADDRESS     FaultedVirtualAddress;
      UINT64                     FaultedPrimitiveAPISequenceNumber;
      union {
        HANDLE FaultedHwContext;
        HANDLE FaultedHwQueue;
        HANDLE FaultedProcessHandle;
      };
      UINT                       NodeOrdinal;
      UINT                       EngineOrdinal;
      DXGK_RENDER_PIPELINE_STAGE FaultedPipelineStage;
      UINT                       FaultedBindTableEntry;
      DXGK_PAGE_FAULT_FLAGS      PageFaultFlags;
      UINT                       PageTableLevel;
      DXGK_FAULT_ERROR_CODE      FaultErrorCode;
    } HwQueuePageFaulted;
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId;
      UINT                           NotificationID;
    } PeriodicMonitoredFenceSignaled;
    struct {
      UINT Reserved[16];
    } Reserved;
  };
  DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS Flags;
} DXGKARGCB_NOTIFY_INTERRUPT_DATA;
```

## Members


`InterruptType`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561136">DXGK_INTERRUPT_TYPE</a>-typed value that indicates the type of interrupt that the display miniport driver notifies the GPU scheduler about.

`Flags`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff559579">DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS</a> structure that indicates if the display miniport driver provides a physical adapter mask in a call to the <a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a> function.

## Remarks
Depending on the value in the <b>InterruptType</b> member, the display miniport driver should set the appropriate union member in the DXGKARGCB_NOTIFY_INTERRUPT_DATA structure. For example, for the end of a direct memory access (DMA) buffer fence, which corresponds to a value of DXGK_INTERRUPT_DMA_COMPLETED in <b>InterruptType</b>, the driver must set a value in the <b>SubmissionFenceId</b> member of the <b>DmaCompleted</b> member. This value should be the DMA buffer fence identifier, which the driver's <a href="https://msdn.microsoft.com/de1925ab-e444-4cf6-acd9-8fdab26afcec">DxgkDdiSubmitCommand</a> function assigned to the just completed DMA buffer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451245">DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559579">DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561136">DXGK_INTERRUPT_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn322054">DXGK_MIRACAST_CAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn322056">DXGK_MIRACAST_CHUNK_INFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh780309">DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn906831">DXGK_PAGE_FAULT_FLAGS</a>



<a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a>



<a href="https://msdn.microsoft.com/de1925ab-e444-4cf6-acd9-8fdab26afcec">DxgkDdiSubmitCommand</a>