---
UID: NS:d3dkmthk._D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2
title: "_D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2"
author: windows-driver-content
description: The D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 structure contains information about the synchronization events that the D3DKMTWaitForSynchronizationObject2 function waits for to occur.
old-location: display\d3dkmt_waitforsynchronizationobject2.htm
old-project: display
ms.assetid: 934bfe32-b54b-477c-a5f8-714caa97f233
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2, D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 structure [Display Devices], OpenGL_Structs_fb1ca5e1-799c-49c7-844d-25954fd0db64.xml, _D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2, d3dkmthk/D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2, display.d3dkmt_waitforsynchronizationobject2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 is supported beginning with the Windows 7 operating system.
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
-	D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2
---

# _D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 structure
The D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 structure contains information about the synchronization events that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547262">D3DKMTWaitForSynchronizationObject2</a> function waits for to occur.

## Syntax
```
typedef struct _D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 {
  D3DKMT_HANDLE hContext;
  UINT          ObjectCount;
  D3DKMT_HANDLE ObjectHandleArray[D3DDDI_MAX_OBJECT_WAITED_ON];
  union {
    struct {
      UINT64 FenceValue;
    } Fence;
    UINT64 Reserved[8];
  };
} D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2;
```

## Members


`hContext`

[in] A kernel-mode handle to the context stream in which a wait for the synchronization events in the array that the <b>ObjectHandleArray</b> member specifies is inserted.

`ObjectCount`

[in] The number of synchronization events in the <b>ObjectHandleArray</b> array.

`ObjectHandleArray`

[in] An array of kernel-mode handles to the synchronization events that the context that is specified by the <b>hContext</b> member waits for. The D3DDDI_MAX_OBJECT_WAITED_ON constant, which is defined as 32, indicates the maximum number of synchronization events that the context can wait for.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 is supported beginning with the Windows 7 operating system. D3DKMT_WAITFORSYNCHRONIZATIONOBJECT2 is supported beginning with the Windows 7 operating system. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff547262">D3DKMTWaitForSynchronizationObject2</a>