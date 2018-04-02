---
UID: NS:d3dkmddi._DXGKARG_SUBMITCOMMANDVIRTUAL
title: "_DXGKARG_SUBMITCOMMANDVIRTUAL"
author: windows-driver-content
description: DXGKARG_SUBMITCOMMANDVIRTUAL is used to submit a direct memory access (DMA) buffer to a context that supports virtual addressing with the DxgkDdiSubmitCommandVirtualdevice driver interface (DDI).
old-location: display\dxgkarg_submitcommandvirtual.htm
old-project: display
ms.assetid: 7BBB4BEC-82F1-44B9-A0C2-1073517A4116
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGKARG_SUBMITCOMMANDVIRTUAL, DXGKARG_SUBMITCOMMANDVIRTUAL structure [Display Devices], _DXGKARG_SUBMITCOMMANDVIRTUAL, d3dkmddi/DXGKARG_SUBMITCOMMANDVIRTUAL, display.dxgkarg_submitcommandvirtual
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	DXGKARG_SUBMITCOMMANDVIRTUAL
product: Windows
targetos: Windows
req.typenames: DXGKARG_SUBMITCOMMANDVIRTUAL
---

# _DXGKARG_SUBMITCOMMANDVIRTUAL structure
<b>DXGKARG_SUBMITCOMMANDVIRTUAL</b> is used to submit a direct memory access (DMA) buffer to a context that supports virtual addressing with the  <a href="https://msdn.microsoft.com/7A55FB51-BDC2-4215-895E-3250579BEAF0">DxgkDdiSubmitCommandVirtual</a>device driver interface (DDI).

## Syntax
```
typedef struct _DXGKARG_SUBMITCOMMANDVIRTUAL {
  HANDLE                         hContext;
  D3DGPU_VIRTUAL_ADDRESS         DmaBufferVirtualAddress;
  UINT                           DmaBufferSize;
  VOID                           *pDmaBufferPrivateData;
  UINT                           DmaBufferPrivateDataSize;
  UINT                           DmaBufferUmdPrivateDataSize;
  UINT                           SubmissionFenceId;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  D3DDDI_FLIPINTERVAL_TYPE       FlipInterval;
  DXGK_SUBMITCOMMANDFLAGS        Flags;
  UINT                           EngineOrdinal;
  UINT                           NodeOrdinal;
} DXGKARG_SUBMITCOMMANDVIRTUAL;
```

## Members


`hContext`

The handle returned from <a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a>.

`DmaBufferVirtualAddress`

The virtual address for the DMA buffer in the context of the submitting process.

`DmaBufferSize`

The size of the DMA buffer in bytes.

`pDmaBufferPrivateData`

A pointer to the driver-private data buffer.

`DmaBufferPrivateDataSize`

The size of the driver-private data buffer in bytes.

`DmaBufferUmdPrivateDataSize`

Size of the private driver data, in bytes, that was set by the user mode driver in <b>SubmitCommandCb</b>. When <b>SubmitCommandCb</b> is called, the DirectX graphics kernel allocates a buffer for the private driver data with the size equal to <a href="https://msdn.microsoft.com/library/windows/hardware/ff561019">DXGK_CONTEXTINFO</a>::<b>DmaBufferPrivateDataSize</b>. This size was reported by the kernel mode driver in the <a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a> call. The DirectX graphics kernel copies the driver private data from the <b>SubmitCommandCb</b> to the allocated buffer.

`SubmissionFenceId`

A unique identifier that the driver can write into the fence command in the ring buffer, which is the buffer where DMA buffers are queued for the GPU to run. For more information about these types of identifiers, see <a href="https://msdn.microsoft.com/0ec8a4eb-c441-47ae-b5de-d86e6065ffd4">Supplying Fence Identifiers</a>.

`VidPnSourceId`

The zero-based identification number of the video present source in a path of a video present network (VidPN) topology for a flip operation. This member is valid only when the <b>Flip</b> or <b>FlipWithNoWait</b> bit-field flag is set in the <b>Flags</b> member.

`FlipInterval`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>-typed value that indicates the flip interval (that is, if the flip occurs after zero, one, two, three, or four vertical syncs). <b>FlipInterval</b> is valid only if the <b>Flip</b> bit-field flag is set (that is, <b>TRUE</b>) in the <b>Flags</b> member.

`Flags`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562058">DXGK_SUBMITCOMMANDFLAGS</a> structure that identifies information about the DMA buffer to submit.

`EngineOrdinal`

Reserved for future use.

`NodeOrdinal`

The zero-based index of the node that the context is created for. Identifies the node when the context is <b>NULL</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561019">DXGK_CONTEXTINFO</a>



<a href="https://msdn.microsoft.com/aea21a36-f3d5-4541-bd2d-aa026668c562">DxgkDdiCreateContext</a>



<a href="https://msdn.microsoft.com/7A55FB51-BDC2-4215-895E-3250579BEAF0">DxgkDdiSubmitCommandVirtual</a>



<a href="https://msdn.microsoft.com/0ec8a4eb-c441-47ae-b5de-d86e6065ffd4">Supplying Fence Identifiers</a>