---
UID: NS:d3dkmthk._D3DKMT_SETQUEUEDLIMIT
title: "_D3DKMT_SETQUEUEDLIMIT"
author: windows-driver-content
description: The D3DKMT_SETQUEUEDLIMIT structure describes parameters for setting or retrieving the limit for the number of operations of the given type that can be queued for the given device.
old-location: display\d3dkmt_setqueuedlimit.htm
old-project: display
ms.assetid: 4fe525b1-9c06-4e2c-9e57-041164905efe
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: D3DKMT_SETQUEUEDLIMIT, display.d3dkmt_setqueuedlimit, d3dkmthk/D3DKMT_SETQUEUEDLIMIT, _D3DKMT_SETQUEUEDLIMIT, D3DKMT_SETQUEUEDLIMIT structure [Display Devices], OpenGL_Structs_3c7f7e33-f71a-4547-89ee-7dba69917a4f.xml
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmthk.h
apiname:
-	D3DKMT_SETQUEUEDLIMIT
product: Windows
targetos: Windows
req.typenames: D3DKMT_SETQUEUEDLIMIT
---

# _D3DKMT_SETQUEUEDLIMIT structure
The D3DKMT_SETQUEUEDLIMIT structure describes parameters for setting or retrieving the limit for the number of operations of the given type that can be queued for the given device.

## Syntax
````
typedef struct _D3DKMT_SETQUEUEDLIMIT {
  D3DKMT_HANDLE           hDevice;
  D3DKMT_QUEUEDLIMIT_TYPE Type;
  union {
    UINT   QueuedPresentLimit;
    struct {
      D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
      UINT                           QueuedPendingFlipLimit;
    };
  };
} D3DKMT_SETQUEUEDLIMIT;
````

## Members


`hDevice`

[in] A D3DKMT_HANDLE data type that represents the kernel-mode handle to the device to set or retrieve the limit of queued operations for.

`Type`

[in] A <a href="..\d3dkmthk\ne-d3dkmthk-_d3dkmt_queuedlimit_type.md">D3DKMT_QUEUEDLIMIT_TYPE</a>-typed value that indicates the type of operations to set or retrieve the queued limit for.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="..\d3dkmthk\ne-d3dkmthk-_d3dkmt_queuedlimit_type.md">D3DKMT_QUEUEDLIMIT_TYPE</a>

<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtsetqueuedlimit.md">D3DKMTSetQueuedLimit</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_SETQUEUEDLIMIT structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>