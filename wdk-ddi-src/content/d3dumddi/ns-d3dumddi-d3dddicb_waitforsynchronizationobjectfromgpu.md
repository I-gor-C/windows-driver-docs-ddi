---
UID: NS:d3dumddi.D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU
title: D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU
author: windows-driver-content
description: D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU is used with pfnWaitForSynchronizationObjectFromGpuCb to wait for a monitored fence to reach a certain value.
old-location: display\d3dddicb_waitforsynchronizationobjectfromgpu.htm
old-project: display
ms.assetid: 2A441CEE-C138-4FF0-8865-04ABFB0F029C
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU, D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU structure [Display Devices], d3dumddi/D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU, display.d3dddicb_waitforsynchronizationobjectfromgpu
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
-	D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU
product: Windows
targetos: Windows
req.typenames: D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU
---

# D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU structure
<b>D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU</b> is used with <a href="https://msdn.microsoft.com/49023D25-D57E-418F-AD10-133377B90493">pfnWaitForSynchronizationObjectFromGpuCb</a> to wait for a monitored fence to reach a certain value.

## Syntax
```
typedef struct D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMGPU {
  HANDLE              hContext;
  UINT                ObjectCount;
  const D3DKMT_HANDLE *ObjectHandleArray;
  union {
    UINT64       FenceValue;
    const UINT64 *MonitoredFenceValueArray;
    UINT64       Reserved[8];
  };
};
```

## Members


`hContext`

[in] A kernel-mode handle to the context stream in which a wait for the synchronization events in the array that the <b>ObjectHandleArray</b> member specifies is inserted.

`ObjectCount`

[in] The number of synchronization events in the <b>ObjectHandleArray</b> array and fence values in <b>MonitoredFenceValueArray</b> arrays.

`ObjectHandleArray`

[in] An array of kernel-mode handles to the synchronization events that the context that is specified by the <b>hContext</b> member waits for.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/49023D25-D57E-418F-AD10-133377B90493">pfnWaitForSynchronizationObjectFromGpuCb</a>