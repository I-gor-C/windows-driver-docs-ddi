---
UID: NC:video.PINT10_FREE_BUFFER
title: PINT10_FREE_BUFFER
author: windows-driver-content
description: The Int10FreeBuffer function frees a buffer previously allocated by Int10AllocateBuffer.
old-location: display\int10freebuffer.htm
old-project: display
ms.assetid: feb7dd98-8c44-405e-8e98-ffd6246cf0ee
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: Int10FreeBuffer, Int10FreeBuffer callback function [Display Devices], PINT10_FREE_BUFFER, VideoPort_Functions_607fc1f2-1d9a-48eb-97c2-a2cd510e3d78.xml, display.int10freebuffer, video/Int10FreeBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
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
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	video.h
api_name:
-	Int10FreeBuffer
product: Windows
targetos: Windows
req.typenames: VHF_CONFIG, *PVHF_CONFIG
req.product: Windows 10 or later.
---


# PINT10_FREE_BUFFER callback function
The <i>Int10FreeBuffer</i> function frees a buffer previously allocated by <i>Int10AllocateBuffer</i>.

## Syntax

```
PINT10_FREE_BUFFER Pint10FreeBuffer;

VP_STATUS Pint10FreeBuffer(
  IN PVOID Context,
  IN USHORT Seg,
  IN USHORT Off
)
{...}
```

## Parameters

`Context`

Pointer to a video port driver-defined context for the interface. This should be the same as the value in the <b>Context</b> member of the <a href="..\video\ns-video-_video_port_int10_interface.md">VIDEO_PORT_INT10_INTERFACE</a> structure after <a href="..\video\nf-video-videoportqueryservices.md">VideoPortQueryServices</a> returns.

`Seg`

Specifies the segment address of the buffer to be freed.

`Off`

Specifies the offset within the segment indicated by the <i>Seg</i> parameter.


## Return Value

The <i>Int10FreeBuffer</i> function returns NO_ERROR upon success. Otherwise, the function returns an appropriate error code.

## Remarks

The video port implements this function, which can be accessed through a pointer in the <a href="..\video\ns-video-_video_port_int10_interface.md">VIDEO_PORT_INT10_INTERFACE</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 2000 and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | video.h (include Video.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\video\ns-video-_video_port_int10_interface.md">VIDEO_PORT_INT10_INTERFACE</a>