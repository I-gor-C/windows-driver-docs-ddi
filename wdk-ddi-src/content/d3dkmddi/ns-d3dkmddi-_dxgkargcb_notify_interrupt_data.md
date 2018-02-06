---
UID: NS:d3dkmddi._DXGKARGCB_NOTIFY_INTERRUPT_DATA
title: "_DXGKARGCB_NOTIFY_INTERRUPT_DATA"
author: windows-driver-content
description: The DXGKARGCB_NOTIFY_INTERRUPT_DATA structure describes notification information.
old-location: display\dxgkargcb_notify_interrupt_data.htm
old-project: display
ms.assetid: c71078fb-5666-4038-81a0-de9375bafb5c
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DmStructs_071ed85c-70d6-44d8-95e3-7f6609331f4f.xml, _DXGKARGCB_NOTIFY_INTERRUPT_DATA, *IN_CONST_PDXGKARGCB_NOTIFY_INTERRUPT_DATA, d3dkmddi/DXGKARGCB_NOTIFY_INTERRUPT_DATA, STATUS_SUCCESS, DXGKARGCB_NOTIFY_INTERRUPT_DATA structure [Display Devices], DXGKARGCB_NOTIFY_INTERRUPT_DATA, STATUS_INVALID_PARAMETER, STATUS_NO_MEMORY, display.dxgkargcb_notify_interrupt_data
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmddi.h
apiname:
-	DXGKARGCB_NOTIFY_INTERRUPT_DATA
product: Windows
targetos: Windows
req.typenames: DXGKARGCB_NOTIFY_INTERRUPT_DATA
---

# _DXGKARGCB_NOTIFY_INTERRUPT_DATA structure
The DXGKARGCB_NOTIFY_INTERRUPT_DATA structure describes notification information.

## Syntax
````
typedef struct _DXGKARGCB_NOTIFY_INTERRUPT_DATA {
  DXGK_INTERRUPT_TYPE                InterruptType;
  union {
    struct {
      UINT SubmissionFenceId;
      UINT NodeOrdinal;
      UINT EngineOrdinal;
    } DmaCompleted;
    struct {
      UINT PreemptionFenceId;
      UINT LastCompletedFenceId;
      UINT NodeOrdinal;
      UINT EngineOrdinal;
    } DmaPreempted;
    struct {
      UINT     FaultedFenceId;
      NTSTATUS Status;
      UINT     NodeOrdinal;
      UINT     EngineOrdinal;
    } DmaFaulted;
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId;
      PHYSICAL_ADDRESS               PhysicalAddress;
      UINT                           PhysicalAdapterMask;
    } CrtcVsync;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId;
    } DisplayOnlyVsync;
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID     VidPnTargetId;
      UINT                               PhysicalAdapterMask;
      UINT                               MultiPlaneOverlayVsyncInfoCount;
      DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO *pMultiPlaneOverlayVsyncInfo;
    } CrtcVsyncWithMultiPlaneOverlay;
    DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS DisplayOnlyPresentProgress;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId;
      DXGK_MIRACAST_CHUNK_INFO       ChunkInfo;
      PVOID                          pPrivateDriverData;
      UINT                           PrivateDataDriverSize;
      NTSTATUS                       Status;
    } MiracastEncodeChunkCompleted;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
    struct {
      UINT                       FaultedFenceId;
      UINT64                     FaultedPrimitiveAPISequenceNumber;
      DXGK_RENDER_PIPELINE_STAGE FaultedPipelineStage;
      UINT                       FaultedBindTableEntry;
      DXGK_PAGE_FAULT_FLAGS      PageFaultFlags;
      D3DGPU_VIRTUAL_ADDRESS     FaultedVirtualAddress;
      UINT                       NodeOrdinal;
      UINT                       EngineOrdinal;
      UINT                       PageTableLevel;
      DXGK_FAULT_ERROR_CODE      FaultErrorCode;
      HANDLE                     FaultedProcessHandle;
    } DmaPageFaulted;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
    D3DDDI_VIDEO_PRESENT_TARGET_ID         VidPnTargetId;
    UINT                                   PhysicalAdapterMask;
    UINT                                   MultiPlaneOverlayVsyncInfoCount;
    DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO2    *pMultiPlaneOverlayVsyncInfo;
    ULONGLONG                              GpuFrequency;
    ULONGLONG                              GpuClockCounter;
#endif 
    struct {
      UINT Reserved[16];
    } Reserved;
  };
  DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS Flags;
} DXGKARGCB_NOTIFY_INTERRUPT_DATA;
````

## Members


`Flags`

[in] A <a href="..\d3dkmddi\ns-d3dkmddi-_dxgkcb_notify_interrupt_data_flags.md">DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS</a> structure that indicates if the display miniport driver provides a physical adapter mask in a call to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb_notify_interrupt.md">DxgkCbNotifyInterrupt</a> function.

`InterruptType`

[in] A <a href="..\d3dkmddi\ne-d3dkmddi-_dxgk_interrupt_type.md">DXGK_INTERRUPT_TYPE</a>-typed value that indicates the type of interrupt that the display miniport driver notifies the GPU scheduler about.

## Remarks
Depending on the value in the <b>InterruptType</b> member, the display miniport driver should set the appropriate union member in the DXGKARGCB_NOTIFY_INTERRUPT_DATA structure. For example, for the end of a direct memory access (DMA) buffer fence, which corresponds to a value of DXGK_INTERRUPT_DMA_COMPLETED in <b>InterruptType</b>, the driver must set a value in the <b>SubmissionFenceId</b> member of the <b>DmaCompleted</b> member. This value should be the DMA buffer fence identifier, which the driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_submitcommand.md">DxgkDdiSubmitCommand</a> function assigned to the just completed DMA buffer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_submitcommand.md">DxgkDdiSubmitCommand</a>

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkcb_notify_interrupt_data_flags.md">DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS</a>

<a href="..\d3dukmdt\ns-d3dukmdt-dxgk_miracast_chunk_info.md">DXGK_MIRACAST_CHUNK_INFO</a>

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb_notify_interrupt.md">DxgkCbNotifyInterrupt</a>

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkargcb_present_displayonly_progress.md">DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS</a>

<a href="..\d3dkmddi\ne-d3dkmddi-_dxgk_interrupt_type.md">DXGK_INTERRUPT_TYPE</a>

<a href="..\d3dkmdt\ne-d3dkmdt-_dxgk_page_fault_flags.md">DXGK_PAGE_FAULT_FLAGS</a>

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_multiplane_overlay_vsync_info.md">DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO</a>

<a href="..\dispmprt\ns-dispmprt-_dxgk_miracast_caps.md">DXGK_MIRACAST_CAPS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARGCB_NOTIFY_INTERRUPT_DATA structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>