---
UID: NS:d3dukmdt._D3DDDICB_SIGNALFLAGS
title: "_D3DDDICB_SIGNALFLAGS"
author: windows-driver-content
description: The D3DDDICB_SIGNALFLAGS structure describes signaling behavior in a call to the pfnSignalSynchronizationObjectCb or pfnSignalSynchronizationObject2Cb functions.
old-location: display\d3dddicb_signalflags.htm
old-project: display
ms.assetid: 1efe98c4-021b-4312-bbcc-52267e528b5f
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: D3DDDICB_SIGNALFLAGS structure [Display Devices], D3D_other_Structs_3165168a-bcae-409c-8ca2-741675016ba8.xml, d3dukmdt/D3DDDICB_SIGNALFLAGS, _D3DDDICB_SIGNALFLAGS, D3DDDICB_SIGNALFLAGS, display.d3dddicb_signalflags
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dukmdt.h
apiname:
-	D3DDDICB_SIGNALFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDICB_SIGNALFLAGS
---

# _D3DDDICB_SIGNALFLAGS structure
The D3DDDICB_SIGNALFLAGS structure describes signaling behavior in a call to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_signalsynchronizationobjectcb.md">pfnSignalSynchronizationObjectCb</a> or <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_signalsynchronizationobject2cb.md">pfnSignalSynchronizationObject2Cb</a> functions.

## Syntax
````
typedef struct _D3DDDICB_SIGNALFLAGS {
  union {
    struct {
      UINT SignalAtSubmission  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
      UINT EnqueueCpuEvent  :1;
      UINT Reserved  :30;
#else 
      UINT Reserved  :31;
#endif 
    };
    UINT Value;
  };
} D3DDDICB_SIGNALFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_signalsynchronizationobject2cb.md">pfnSignalSynchronizationObject2Cb</a>

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_signalsynchronizationobjectcb.md">pfnSignalSynchronizationObjectCb</a>

<a href="..\d3dumddi\ns-d3dumddi-_d3dddicb_signalsynchronizationobject.md">D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT</a>

<a href="..\d3dumddi\ns-d3dumddi-_d3dddicb_signalsynchronizationobject2.md">D3DDDICB_SIGNALSYNCHRONIZATIONOBJECT2</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_SIGNALFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>