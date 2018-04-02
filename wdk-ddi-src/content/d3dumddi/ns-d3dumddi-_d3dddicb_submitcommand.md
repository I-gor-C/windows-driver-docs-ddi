---
UID: NS:d3dumddi._D3DDDICB_SUBMITCOMMAND
title: "_D3DDDICB_SUBMITCOMMAND"
author: windows-driver-content
description: The D3DDDICB_SUBMITCOMMAND structure is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing.
old-location: display\d3dddicb_submitcommand.htm
old-project: display
ms.assetid: 53D4890A-D075-4DF7-97E6-A8E8A174866B
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDICB_SUBMITCOMMAND, D3DDDICB_SUBMITCOMMAND structure [Display Devices], _D3DDDICB_SUBMITCOMMAND, d3dumddi/D3DDDICB_SUBMITCOMMAND, display.d3dddicb_submitcommand
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dumddi.h
api_name:
-	D3DDDICB_SUBMITCOMMAND
product:
- Windows
targetos: Windows
req.typenames: D3DDDICB_SUBMITCOMMAND
---

# _D3DDDICB_SUBMITCOMMAND structure
The <b>D3DDDICB_SUBMITCOMMAND</b> structure is used to submit command buffers on contexts that support graphics processing unit (GPU) virtual addressing.

## Syntax
```
typedef struct _D3DDDICB_SUBMITCOMMAND {
  D3DGPU_VIRTUAL_ADDRESS      Commands;
  UINT                        CommandLength;
  D3DDDICB_SUBMITCOMMANDFLAGS Flags;
  UINT                        BroadcastContextCount;
  HANDLE                      BroadcastContext[D3DDDI_MAX_BROADCAST_CONTEXT];
  VOID                        *pPrivateDriverData;
  UINT                        PrivateDriverDataSize;
  UINT                        NumPrimaries;
  D3DKMT_HANDLE               WrittenPrimaries[D3DDDI_MAX_WRITTEN_PRIMARIES];
  D3DDDI_MARKERLOGTYPE        MarkerLogType;
  UINT                        RenderCBSequence;
  UINT                        FirstAPISequenceNumberHigh;
  UINT                        CompletedAPISequenceNumberLow0Size;
  UINT                        CompletedAPISequenceNumberLow1Size;
  UINT                        BegunAPISequenceNumberLow0Size;
  UINT                        BegunAPISequenceNumberLow1Size;
  CONST UINT                  *pCompletedAPISequenceNumberLow0;
  CONST UINT                  *pCompletedAPISequenceNumberLow1;
  CONST UINT                  *pBegunAPISequenceNumberLow0;
  CONST UINT                  *pBegunAPISequenceNumberLow1;
  UINT                        Reserved;
  UINT                        NumHistoryBuffers;
  D3DKMT_HANDLE               *HistoryBufferArray;
  HANDLE                      hSyncToken;
  void                        *pReserved;
} D3DDDICB_SUBMITCOMMAND;
```

## Members


`Commands`

GPU virtual address to the commands being submitted to the context for execution. This information is provided to the kernel mode driver during command submission and is also used for debugging purposes.

`CommandLength`

Specifies the length, in bytes, of the commands being submitted to the GPU. This information is provided to the kernel  mode driver during command submission and is also used for debugging purposes.

`Flags`

An instance of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn914420">D3DDDICB_SUBMITCOMMANDFLAGS</a> structure.

`BroadcastContextCount`

Specifies the number of context these command should be submitted to. This count must be at least 1.

`BroadcastContext`

Specifies the handle of the context to execute the specified commands.

`pPrivateDriverData`

Pointer to driver private data to be passed to the kernel mode driver as part of this submission.

`PrivateDriverDataSize`

Size of the private driver data information being passed. This size must be smaller than the size requested by the kernel mode driver for submission private driver data.

`NumPrimaries`

Specifies the number of primaries and swapchain back buffers being written to by the submitted commands. This is equal to the number of allocations in the <b>WrittenPrimaries</b> array.

`WrittenPrimaries`

Arrays of handle to the primaries and swapchain back buffers being written to by the submitted commands.

`MarkerLogType`

A <a href="https://msdn.microsoft.com/library/windows/hardware/dn535966">D3DDDI_MARKERLOGTYPE</a> enumeration that indicates the type of marker in the Event Tracing for Windows (ETW) log that the user-mode display driver supports.

`RenderCBSequence`

A unique identifier for each <a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a> function call. Starts at a value of 1 for contexts associated with single-threaded user-mode DDIs and ranges to a value of 0x80000001 for contexts associated with free-threaded user mode DDIs. The user-mode display driver must increment the value for each <i>pfnRenderCb</i> call it makes on any engine.

`FirstAPISequenceNumberHigh`

Used by the driver to pass the context's API sequence number.

`CompletedAPISequenceNumberLow0Size`

Used by the driver to pass the context's API sequence number.

`CompletedAPISequenceNumberLow1Size`

Used by the driver to pass the context's API sequence number.

`BegunAPISequenceNumberLow0Size`

Used by the driver to pass the context's API sequence number.

`BegunAPISequenceNumberLow1Size`

Used by the driver to pass the context's API sequence number.

`pCompletedAPISequenceNumberLow0`

A pointer used by the driver to pass the context's API sequence number.

`pCompletedAPISequenceNumberLow1`

A pointer used by the driver to pass the context's API sequence number.

`pBegunAPISequenceNumberLow0`

A pointer used by the driver to pass the context's API sequence number.

`pBegunAPISequenceNumberLow1`

A pointer used by the driver to pass the context's API sequence number.

`Reserved`

This member is reserved and should be set to zero.

`NumHistoryBuffers`

The number of history buffers.

`HistoryBufferArray`

A pointer to the array of history buffers.

`hSyncToken`



`pReserved`



## Remarks
The <a href="https://msdn.microsoft.com/60300845-9050-4D0A-83D1-76A45EA823C1">pfnSubmitCommandCb</a> code path no longer provides an allocation list for the user mode driver to provide a list of allocations that will be read and written to during this command. However, it is necessary to synchronize some writes that would not normally be known without the allocation list. For this, a new small allocation list specifically for surfaces which will be written to and used for displaying content. The <b>WrittenPrimaries</b> array should be used to provide such allocations.


Despite the name, <b>WrittenPrimaries</b> must contain allocations that are considered <i>SwapChainBackBuffer</i> allocations according to the runtime in addition to the primaries. This is exposed to the user mode driver by a new flag in <a href="https://msdn.microsoft.com/library/windows/hardware/ff542004">D3D10_DDI_RESOURCE_MISC_FLAG</a>. The runtime will provide the <b>D3DWDDM2_0DDI_RESOURCE_MISC_DISPLAYABLE_SURFACE</b> flag to the user mode driver during calls to create a resource or heap that is created as a <i>FlipEx swapchain</i> or <i>primary</i>. The driver may use this flag to determine all allocations that should be put in the <b>WrittenPrimaries</b> list for Microsoft Direct3D 11. Other runtimes have not changed.


If the driver receives a call to <a href="https://msdn.microsoft.com/5b74c989-1a62-4415-a19a-dd0ba2fcff83">CreateResource</a> that has this flag, the allocation should be added to this list on every <a href="https://msdn.microsoft.com/60300845-9050-4D0A-83D1-76A45EA823C1">pfnSubmitCommandCb</a> call that writes to the surface.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542004">D3D10_DDI_RESOURCE_MISC_FLAG</a>



<a href="https://msdn.microsoft.com/f242162e-6237-469c-b178-5a51dcf69e32">pfnRenderCb</a>



<a href="https://msdn.microsoft.com/60300845-9050-4D0A-83D1-76A45EA823C1">pfnSubmitCommandCb</a>