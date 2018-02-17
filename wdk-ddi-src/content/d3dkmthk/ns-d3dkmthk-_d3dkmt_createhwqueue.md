---
UID: NS:d3dkmthk._D3DKMT_CREATEHWQUEUE
title: "_D3DKMT_CREATEHWQUEUE"
author: windows-driver-content
description: A structure holding information to create a hardware queue.
old-location: display\d3dkmt_createhwqueue.htm
old-project: display
ms.assetid: DBD99353-4798-4540-89DB-EA08521B276E
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: d3dkmthk/D3DKMT_CREATEHWQUEUE, _D3DKMT_CREATEHWQUEUE, display.d3dkmt_createhwqueue, D3DKMT_CREATEHWQUEUE, D3DKMT_CREATEHWQUEUE structure [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
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
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmthk.h
apiname:
-	D3DKMT_CREATEHWQUEUE
product: Windows
targetos: Windows
req.typenames: D3DKMT_CREATEHWQUEUE
---

# _D3DKMT_CREATEHWQUEUE structure
A structure holding information to create a hardware queue.

## Syntax
````
typedef struct _D3DKMT_CREATEHWQUEUE {
  D3DKMT_HANDLE             hHwContext;
  D3DDDI_CREATEHWQUEUEFLAGS Flags;
  UINT                      PrivateDriverDataSize;
  VOID                      *pPrivateDriverData;
  D3DKMT_HANDLE             hHwQueue;
  D3DKMT_HANDLE             hHwQueueProgressFence;
  VOID                      *HwQueueProgressFenceCPUVirtualAddress;
  D3DGPU_VIRTUAL_ADDRESS    HwQueueProgressFenceGPUVirtualAddress;
} D3DKMT_CREATEHWQUEUE;
````

## Members


`Flags`

Hardware queue creation flags.

`hHwContext`

Handle to the hardware context the queue is associated with.

`hHwQueue`

Handle to the hardware queue object to submit work to.

`hHwQueueProgressFence`

Handle to the monitored fence object used to monitor the queue progress.

`HwQueueProgressFenceCPUVirtualAddress`

Read-only mapping of the queue progress fence value for the CPU.

`HwQueueProgressFenceGPUVirtualAddress`

Read/write mapping of the queue progress fence value for the GPU.

`pPrivateDriverData`

Private driver data.

`PrivateDriverDataSize`

Size of private driver data.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmthk.h |