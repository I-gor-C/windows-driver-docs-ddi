---
UID: NS:d3dkmthk._D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2
title: "_D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2"
author: windows-driver-content
description: The D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 structure contains information about the synchronization events that the D3DKMTSignalSynchronizationObject2 function signals.
old-location: display\d3dkmt_signalsynchronizationobject2.htm
old-project: display
ms.assetid: a4bdafeb-310a-4ceb-966e-a1e3660fc5f2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2, D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 structure [Display Devices], OpenGL_Structs_ac490d8c-5ab9-4a1f-8908-5c2e7786b65b.xml, _D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2, d3dkmthk/D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2, display.d3dkmt_signalsynchronizationobject2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 is supported beginning with the Windows 7 operating system.
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
-	D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2
product: Windows
targetos: Windows
req.typenames: D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2
---

# _D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 structure
The D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 structure contains information about the synchronization events that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547227">D3DKMTSignalSynchronizationObject2</a> function signals.

## Syntax
```
typedef struct _D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 {
  D3DKMT_HANDLE        hContext;
  UINT                 ObjectCount;
  D3DKMT_HANDLE        ObjectHandleArray[D3DDDI_MAX_OBJECT_SIGNALED];
  D3DDDICB_SIGNALFLAGS Flags;
  ULONG                BroadcastContextCount;
  D3DKMT_HANDLE        BroadcastContext[D3DDDI_MAX_BROADCAST_CONTEXT];
  union {
    HANDLE CpuEventHandle;
    struct {
      UINT64 FenceValue;
    } Fence;
    UINT64 Reserved[8];
  };
} D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2;
```

## Members


`hContext`

[in] A kernel-mode handle to a context that signals the synchronization events in the array that the <b>ObjectHandleArray</b> member specifies.

`ObjectCount`

[in] The number of synchronization events in the <b>ObjectHandleArray</b> array.

`ObjectHandleArray`

[in] An array of kernel-mode handles to the synchronization events that the context that is specified by the <b>hContext</b> member signals. The D3DDDI_MAX_OBJECT_SIGNALED constant, which is defined as 32, indicates the maximum number of synchronization events that the context can signal.

`Flags`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544271">D3DDDICB_SIGNALFLAGS</a> structure that indicates, in bit-field flags, signaling behavior.

`BroadcastContextCount`

[in] The number of additional contexts in the array that <b>BroadcastContext</b> specifies.

`BroadcastContext`

[in] An array of D3DKMT_HANDLE data types that represent kernel-mode handles to the additional contexts to broadcast the event to. The D3DDDI_MAX_BROADCAST_CONTEXT constant, which is defined as 64, defines the maximum number of contexts that the OpenGL ICD can broadcast the event to.

The original context that the <b>hContext</b> member specifies and that owns the event is not an element in the <b>BroadcastContext</b> array. For example, if the <b>BroadcastContext</b> array contains one element, the OpenGL ICD sends the event to the owning context (<b>hContext</b>) and broadcasts to that one additional context.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 is supported beginning with the Windows 7 operating system. D3DKMT_SIGNALSYNCHRONIZATIONOBJECT2 is supported beginning with the Windows 7 operating system. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544271">D3DDDICB_SIGNALFLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547227">D3DKMTSignalSynchronizationObject2</a>