---
UID: NS:d3dukmdt._D3DDDICB_SIGNALFLAGS
title: "_D3DDDICB_SIGNALFLAGS"
author: windows-driver-content
description: The D3DDDICB_SIGNALFLAGS structure describes signaling behavior in a call to the pfnSignalSynchronizationObjectCb or pfnSignalSynchronizationObject2Cb functions.
old-location: display\d3dddicb_signalflags.htm
old-project: display
ms.assetid: 1efe98c4-021b-4312-bbcc-52267e528b5f
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDICB_SIGNALFLAGS, D3DDDICB_SIGNALFLAGS structure [Display Devices], D3D_other_Structs_3165168a-bcae-409c-8ca2-741675016ba8.xml, _D3DDDICB_SIGNALFLAGS, d3dukmdt/D3DDDICB_SIGNALFLAGS, display.d3dddicb_signalflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
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
-	d3dukmdt.h
api_name:
-	D3DDDICB_SIGNALFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDICB_SIGNALFLAGS
---

# _D3DDDICB_SIGNALFLAGS structure
The D3DDDICB_SIGNALFLAGS structure describes signaling behavior in a call to the <a href="https://msdn.microsoft.com/12ffa230-2c26-4cd3-ae83-f753a0b6ba38">pfnSignalSynchronizationObjectCb</a> or <a href="https://msdn.microsoft.com/01B5E793-D075-42B5-9ADF-D033249AEE9F">pfnSignalSynchronizationObject2Cb</a> functions.

## Syntax
```
typedef struct _D3DDDICB_SIGNALFLAGS {
  union {
    struct {
      UINT  : 1  SignalAtSubmission;
      UINT  : 1  EnqueueCpuEvent;
      UINT  : 1  AllowFenceRewind;
#if ...
      UINT  : 28 Reserved;
      UINT  : 1  DXGK_SIGNAL_FLAG_INTERNAL0;
#elif
      UINT  : 30 Reserved;
#else
      UINT  : 31 Reserved;
#endif
    };
    UINT Value;
  };
} D3DDDICB_SIGNALFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544274">D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451164">D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT2</a>



<a href="https://msdn.microsoft.com/01B5E793-D075-42B5-9ADF-D033249AEE9F">pfnSignalSynchronizationObject2Cb</a>



<a href="https://msdn.microsoft.com/12ffa230-2c26-4cd3-ae83-f753a0b6ba38">pfnSignalSynchronizationObjectCb</a>