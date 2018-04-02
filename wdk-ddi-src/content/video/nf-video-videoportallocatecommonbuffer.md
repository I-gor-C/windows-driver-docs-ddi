---
UID: NF:video.VideoPortAllocateCommonBuffer
title: VideoPortAllocateCommonBuffer function
author: windows-driver-content
description: The VideoPortAllocateCommonBuffer function allocates and maps system memory so that it is simultaneously accessible from both the processor and a device for common-buffer DMA operations.
old-location: display\videoportallocatecommonbuffer.htm
old-project: display
ms.assetid: 950c2509-688e-4aaa-a12d-4106bb722bbc
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: VideoPortAllocateCommonBuffer, VideoPortAllocateCommonBuffer function [Display Devices], VideoPort_Functions_bd747ea0-7963-4008-a91c-eb5598fc6bdd.xml, display.videoportallocatecommonbuffer, video/VideoPortAllocateCommonBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
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
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Videoprt.sys
api_name:
-	VideoPortAllocateCommonBuffer
product: Windows
targetos: Windows
req.typenames: VIDEO_PORT_SERVICES
req.product: Windows 10 or later.
---


# VideoPortAllocateCommonBuffer function
The <b>VideoPortAllocateCommonBuffer</b> function allocates and maps system memory so that it is simultaneously accessible from both the processor and a device for common-buffer DMA operations.

## Syntax

```
VIDEOPORT_API PVOID VideoPortAllocateCommonBuffer(
  IN PVOID              HwDeviceExtension,
  IN PVP_DMA_ADAPTER    VpDmaAdapter,
  IN ULONG              DesiredLength,
  OUT PPHYSICAL_ADDRESS LogicalAddress,
  IN BOOLEAN            CacheEnabled,
  OUT PVOID             Reserved
);
```

## Parameters

`HwDeviceExtension`

Pointer to the miniport driver's device extension.

`VpDmaAdapter`

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570570">VP_DMA_ADAPTER</a> structure that represents the bus-master adapter. This structure was returned by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff570312">VideoPortGetDmaAdapter</a>.

`DesiredLength`

Specifies the requested number of bytes of memory.

`LogicalAddress`

Pointer to a memory location that receives the logical address to be used by the adapter to access the allocated buffer.

`CacheEnabled`

Specifies whether the allocated memory can be cached.  For more information, see the description of the <i>CacheEnabled</i> parameter for <a href="https://msdn.microsoft.com/library/windows/hardware/ff540575">AllocateCommonBuffer</a>.

`Reserved`

Is currently ignored by the video port driver; should be set to <b>NULL</b>.


## Return Value

<b>VideoPortAllocateCommonBuffer</b> returns the base virtual address of the allocated buffer if successful; otherwise, it returns <b>NULL</b> if the buffer cannot be allocated.

## Remarks

When the buffer is no longer needed, the video miniport driver should release it by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff570355">VideoPortReleaseCommonBuffer</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | video.h (include Video.h) |
| **Library** | Videoprt.lib |
| **DLL** | Videoprt.sys |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540575">AllocateCommonBuffer</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff570570">VP_DMA_ADAPTER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff570312">VideoPortGetDmaAdapter</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff570355">VideoPortReleaseCommonBuffer</a>