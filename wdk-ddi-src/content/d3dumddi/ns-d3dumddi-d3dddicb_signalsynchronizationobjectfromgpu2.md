---
UID: NS:d3dumddi.D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2
title: D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2
author: windows-driver-content
description: D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2 is used with pfnSignalSynchronizationObjectFromGpu2Cb to signal a monitored fence.
old-location: display\d3dddicb_signalsynchronizationobjectfromgpu2.htm
old-project: display
ms.assetid: 077BFCCB-4963-40CF-B56E-EAA08681ED5F
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2, D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2 structure [Display Devices], d3dumddi/D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2, display.d3dddicb_signalsynchronizationobjectfromgpu2
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
-	D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2
product:
- Windows
targetos: Windows
req.typenames: D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2
---

# D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2 structure
<b>D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2</b> is used with <a href="https://msdn.microsoft.com/03F9E47D-A3CA-44A1-A136-8236309D3D36">pfnSignalSynchronizationObjectFromGpu2Cb</a> to signal a monitored fence.

## Syntax
```
typedef struct D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU2 {
  UINT                 ObjectCount;
  const D3DKMT_HANDLE  *ObjectHandleArray;
  D3DDDICB_SIGNALFLAGS Flags;
  ULONG                BroadcastContextCount;
  const HANDLE         *BroadcastContextArray;
  union {
    HANDLE       CpuEventHandle;
    UINT64       FenceValue;
    const UINT64 *MonitoredFenceValueArray;
    UINT64       Reserved[8];
  };
};
```

## Members


`ObjectCount`

[in] The number of synchronization events in the <b>ObjectHandleArray</b> array and fence values in <b>MonitoredFenceValueArray</b> arrays.

`ObjectHandleArray`

[in] An array of kernel-mode handles to the synchronization events that the context that is specified by the <b>hContext</b> member waits for.

`Flags`

[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544271">D3DDDICB_SIGNALFLAGS</a> structure that indicates, in bit-field flags, signaling behavior.

`BroadcastContextCount`

[in] The number of contexts this signal operation will be broadcast to.

`BroadcastContextArray`

[in] An array of kernel-mode handles to the context streams in which a signal for the synchronization events in the array that the <b>ObjectHandleArray</b> member specifies is inserted. The synchronization events are considered signaled only when all broadcast contexts reach the signal insertion point.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544271">D3DDDICB_SIGNALFLAGS</a>



<a href="https://msdn.microsoft.com/03F9E47D-A3CA-44A1-A136-8236309D3D36">pfnSignalSynchronizationObjectFromGpu2Cb</a>