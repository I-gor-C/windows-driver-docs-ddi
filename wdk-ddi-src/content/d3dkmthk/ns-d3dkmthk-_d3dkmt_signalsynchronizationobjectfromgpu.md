---
UID: NS:d3dkmthk._D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU
title: "_D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU"
author: windows-driver-content
description: D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU is used with D3DKMTSignalSynchronizationObjectFromGpu to signal a monitored fence.
old-location: display\d3dkmt_signalsynchronizationobjectfromgpu.htm
old-project: display
ms.assetid: 09190DCC-5F88-4C49-89B3-9063707E3F15
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU, D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU structure [Display Devices], _D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU, d3dkmthk/D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU, display.d3dkmt_signalsynchronizationobjectfromgpu
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
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
-	d3dkmthk.h
api_name:
-	D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU
---

# _D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU structure
<b>D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU</b> is used with <a href="https://msdn.microsoft.com/library/windows/hardware/dn906784">D3DKMTSignalSynchronizationObjectFromGpu</a> to signal a monitored fence.

## Syntax
```
typedef struct _D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU {
  D3DKMT_HANDLE       hContext;
  UINT                ObjectCount;
  const D3DKMT_HANDLE *ObjectHandleArray;
  union {
    const UINT64 *MonitoredFenceValueArray;
    UINT64       Reserved[8];
  };
} D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMGPU;
```

## Members


`hContext`

[in] A kernel-mode handle to the context stream.

`ObjectCount`

[in] The number of synchronization events in the <b>ObjectHandleArray</b> array and fence values in <b>MonitoredFenceValueArray</b> arrays.

`ObjectHandleArray`

[in] An array of kernel-mode handles to the synchronization events that the <b>hContext</b> member signals.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn906784">D3DKMTSignalSynchronizationObjectFromGpu</a>