---
UID: NS:d3dumddi._D3DDDICB_RENDER
title: "_D3DDDICB_RENDER"
author: windows-driver-content
description: The D3DDDICB_RENDER structure describes the current command buffer to be rendered.
old-location: display\d3dddicb_render.htm
old-project: display
ms.assetid: 7a2bf1a8-d416-46bc-a9ba-9122407ea2a2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDICB_RENDER, D3DDDICB_RENDER structure [Display Devices], D3D_param_Structs_62df043b-dbd7-4faf-a911-683ab12ba79b.xml, _D3DDDICB_RENDER, d3dumddi/D3DDDICB_RENDER, display.d3dddicb_render
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dumddi.h
api_name:
-	D3DDDICB_RENDER
product:
- Windows
targetos: Windows
req.typenames: D3DDDICB_RENDER
---

# _D3DDDICB_RENDER structure
The D3DDDICB_RENDER structure describes the current command buffer to be rendered.

## Syntax
```
typedef struct _D3DDDICB_RENDER {
  UINT                     CommandLength;
  UINT                     CommandOffset;
  UINT                     NumAllocations;
  UINT                     NumPatchLocations;
  VOID                     *pNewCommandBuffer;
  UINT                     NewCommandBufferSize;
  D3DDDI_ALLOCATIONLIST    *pNewAllocationList;
  UINT                     NewAllocationListSize;
  D3DDDI_PATCHLOCATIONLIST *pNewPatchLocationList;
  UINT                     NewPatchLocationListSize;
  D3DDDICB_RENDERFLAGS     Flags;
  HANDLE                   hContext;
  UINT                     BroadcastContextCount;
  HANDLE                   BroadcastContext[D3DDDI_MAX_BROADCAST_CONTEXT];
  ULONG                    QueuedBufferCount;
  D3DGPU_VIRTUAL_ADDRESS   NewCommandBuffer;
  VOID                     *pPrivateDriverData;
  UINT                     PrivateDriverDataSize;
  D3DDDI_MARKERLOGTYPE     MarkerLogType;
  UINT                     RenderCBSequence;
  UINT                     FirstAPISequenceNumberHigh;
  UINT                     CompletedAPISequenceNumberLow0Size;
  UINT                     CompletedAPISequenceNumberLow1Size;
  UINT                     BegunAPISequenceNumberLow0Size;
  UINT                     BegunAPISequenceNumberLow1Size;
  CONST UINT               *pCompletedAPISequenceNumberLow0;
  CONST UINT               *pCompletedAPISequenceNumberLow1;
  CONST UINT               *pBegunAPISequenceNumberLow0;
  CONST UINT               *pBegunAPISequenceNumberLow1;
} D3DDDICB_RENDER;
```

## Members


`CommandLength`

[in] The size, in bytes, of the command buffer, starting from offset zero.

`CommandOffset`

[in] The offset, in bytes, to the first command in the command buffer.

`NumAllocations`

[in] The number of elements in the allocation list.

`NumPatchLocations`

[in] The number of elements in the patch-location list.

`pNewCommandBuffer`

[out] A pointer to a command buffer that the user-mode display driver receives to use in its next call to the <a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a> function.

`NewCommandBufferSize`

[in/out] The size, in bytes, that the user-mode display driver requests for the next command buffer.

The driver receives the size, in bytes, of the next command buffer to use.

`pNewAllocationList`

[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544375">D3DDDI_ALLOCATIONLIST</a> structures that the user-mode display driver receives to use as the allocation list in its next call to the <a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a> function.

`NewAllocationListSize`

[in/out] The number of elements that the user-mode display driver requests for the next allocation list. 

The driver receives the number of elements for the allocation list that will be available when the next command buffer is submitted.

`pNewPatchLocationList`

[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544630">D3DDDI_PATCHLOCATIONLIST</a> structures that the user-mode display driver receives to use as the patch-location list in its next call to the <a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a> function.

`NewPatchLocationListSize`

[in/out] The number of elements that the user-mode display driver requests for the next patch-location list.

The driver receives the number of elements for the patch-location list that will be available when the next command buffer is submitted.

`Flags`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544247">D3DDDICB_RENDERFLAGS</a> structure that indicates information about a command buffer to be rendered.

`hContext`

[in] A handle to the context that the driver submits the rendering operation to. The user-mode display driver previously created this context by calling the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function.

`BroadcastContextCount`

[in] The number of additional contexts in the array that the <b>BroadcastContext</b> member specifies.

`BroadcastContext`

[in] An array of handles to the additional contexts to broadcast the current command buffer to. The D3DDDI_MAX_BROADCAST_CONTEXT constant, which is defined as 64, defines the maximum number of additional contexts that the user-mode display driver can broadcast the current command buffer to.

The original context that the <b>hContext</b> member specifies and that owns the command buffer is not an element in the <b>BroadcastContext</b> array. For example, if the <b>BroadcastContext</b> array contains one element, the user-mode display driver sends the command buffer to the owning context (<b>hContext</b>) and broadcasts to that one additional context.

`QueuedBufferCount`

[out] The number of DMA buffers that are queued to the context that the <b>hContext</b> member specifies after the current submission occurs.

`NewCommandBuffer`

This member is reserved and should be set to zero.

This member is available beginning with Windows 7.

`pPrivateDriverData`

[in] This member is reserved and should be set to zero.

This member is available beginning with Windows 7.

`PrivateDriverDataSize`

[in] This member is reserved and should be set to zero.

This member is available beginning with Windows 7.

`MarkerLogType`



`RenderCBSequence`



`FirstAPISequenceNumberHigh`



`CompletedAPISequenceNumberLow0Size`



`CompletedAPISequenceNumberLow1Size`



`BegunAPISequenceNumberLow0Size`



`BegunAPISequenceNumberLow1Size`



`pCompletedAPISequenceNumberLow0`



`pCompletedAPISequenceNumberLow1`



`pBegunAPISequenceNumberLow0`



`pBegunAPISequenceNumberLow1`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544247">D3DDDICB_RENDERFLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544375">D3DDDI_ALLOCATIONLIST</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544630">D3DDDI_PATCHLOCATIONLIST</a>



<a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a>