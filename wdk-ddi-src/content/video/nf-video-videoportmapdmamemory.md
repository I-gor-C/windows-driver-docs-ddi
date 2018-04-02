---
UID: NF:video.VideoPortMapDmaMemory
title: VideoPortMapDmaMemory function
author: windows-driver-content
description: The VideoPortMapDmaMemory function is obsolete in Windows 2000 and later.VideoPortMapDmaMemory maps a range of memory for use in DMA transfers.
old-location: display\videoportmapdmamemory.htm
old-project: display
ms.assetid: 51148c26-c10d-4c57-9e3e-c7d82d6a1c79
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: VideoPortMapDmaMemory, VideoPortMapDmaMemory function [Display Devices], VideoPort_Functions_f2a97e55-d165-4884-a121-52e98f8f46cd.xml, display.videoportmapdmamemory, video/VideoPortMapDmaMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Videoprt.sys
api_name:
-	VideoPortMapDmaMemory
product: Windows
targetos: Windows
req.typenames: VIDEO_PORT_SERVICES
req.product: Windows 10 or later.
---


# VideoPortMapDmaMemory function
The <b>VideoPortMapDmaMemory</b> function is <b>obsolete</b> in Windows 2000 and later.

<b>VideoPortMapDmaMemory</b> maps a range of memory for use in DMA transfers.

## Syntax

```
VIDEOPORT_API PDMA VideoPortMapDmaMemory(
  IN PVOID                 HwDeviceExtension,
  IN PVIDEO_REQUEST_PACKET pVrp,
  IN PHYSICAL_ADDRESS      BoardAddress,
  IN PULONG                Length,
  IN PULONG                InIoSpace,
  IN PVOID                 MappedUserEvent,
  IN PVOID                 DisplayDriverEvent,
  IN OUT PVOID             *VirtualAddress
);
```

## Parameters

`HwDeviceExtension`

Pointer to the miniport driver's device extension.

`pVrp`

Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570547">VIDEO_REQUEST_PACKET</a>.

`BoardAddress`

Specifies the adapter's beginning address.

`Length`

Specifies the length, in bytes, of the range of memory.

`InIoSpace`

Indicates the location of the range. This parameter can be one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
VIDEO_MEMORY_SPACE_DENSE

</td>
<td>
Memory is densely mapped and linear.

</td>
</tr>
<tr>
<td>
VIDEO_MEMORY_SPACE_IO

</td>
<td>
The range is in system I/O space. Should not be set by the display driver.

</td>
</tr>
<tr>
<td>
VIDEO_MEMORY_SPACE_MEMORY

</td>
<td>
The range is in memory space. Should not be set by the display driver.

</td>
</tr>
<tr>
<td>
VIDEO_MEMORY_SPACE_P6CACHE

</td>
<td>
P6 MTRR caching, which is equivalent to write-combine caching. (kernel and user mode).

</td>
</tr>
<tr>
<td>
VIDEO_MEMORY_SPACE_USER_MODE

</td>
<td>
Memory pointer for application use.

</td>
</tr>
</table>

`MappedUserEvent`

Is reserved for system use.

`DisplayDriverEvent`

Is reserved for system use.

`VirtualAddress`

Is reserved for system use.


## Return Value

<b>VideoPortMapDmaMemory</b> always returns <b>NULL</b>.

## Remarks

See <a href="https://msdn.microsoft.com/fe6c2e16-d222-4948-b1df-34ed8d57d9d8">Bus-Master DMA in Video Miniport Drivers</a> for information about packet-based and common-buffer DMA transfers.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 2000 and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | video.h (include Video.h) |
| **Library** | Videoprt.lib |
| **DLL** | Videoprt.sys |