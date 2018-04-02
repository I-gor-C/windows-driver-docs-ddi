---
UID: NS:d3dkmthk._D3DKMT_SETQUEUEDLIMIT
title: "_D3DKMT_SETQUEUEDLIMIT"
author: windows-driver-content
description: The D3DKMT_SETQUEUEDLIMIT structure describes parameters for setting or retrieving the limit for the number of operations of the given type that can be queued for the given device.
old-location: display\d3dkmt_setqueuedlimit.htm
old-project: display
ms.assetid: 4fe525b1-9c06-4e2c-9e57-041164905efe
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_SETQUEUEDLIMIT, D3DKMT_SETQUEUEDLIMIT structure [Display Devices], OpenGL_Structs_3c7f7e33-f71a-4547-89ee-7dba69917a4f.xml, _D3DKMT_SETQUEUEDLIMIT, d3dkmthk/D3DKMT_SETQUEUEDLIMIT, display.d3dkmt_setqueuedlimit
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
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
-	d3dkmthk.h
api_name:
-	D3DKMT_SETQUEUEDLIMIT
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_SETQUEUEDLIMIT
---

# _D3DKMT_SETQUEUEDLIMIT structure
The D3DKMT_SETQUEUEDLIMIT structure describes parameters for setting or retrieving the limit for the number of operations of the given type that can be queued for the given device.

## Syntax
```
typedef struct _D3DKMT_SETQUEUEDLIMIT {
  D3DKMT_HANDLE           hDevice;
  D3DKMT_QUEUEDLIMIT_TYPE Type;
  union {
    UINT QueuedPresentLimit;
    struct {
      D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
      UINT                           QueuedPendingFlipLimit;
    };
  };
} D3DKMT_SETQUEUEDLIMIT;
```

## Members


`hDevice`

[in] A D3DKMT_HANDLE data type that represents the kernel-mode handle to the device to set or retrieve the limit of queued operations for.

`Type`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff548225">D3DKMT_QUEUEDLIMIT_TYPE</a>-typed value that indicates the type of operations to set or retrieve the queued limit for.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff547195">D3DKMTSetQueuedLimit</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548225">D3DKMT_QUEUEDLIMIT_TYPE</a>