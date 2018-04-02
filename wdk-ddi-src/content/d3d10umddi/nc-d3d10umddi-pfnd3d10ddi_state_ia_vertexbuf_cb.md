---
UID: NC:d3d10umddi.PFND3D10DDI_STATE_IA_VERTEXBUF_CB
title: PFND3D10DDI_STATE_IA_VERTEXBUF_CB
author: windows-driver-content
description: The pfnStateIaVertexBufCb function causes the Microsoft Direct3D 10 runtime to refresh the set of vertex buffers that are bound to the input assembler.
old-location: display\pfnstateiavertexbufcb.htm
old-project: display
ms.assetid: 15068932-b769-4027-986f-195b569a23eb
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D10DDI_STATE_IA_VERTEXBUF_CB, d3d10state_functions_b08135a0-2a61-4823-9153-bf89ea24e0fa.xml, d3d10umddi/pfnStateIaVertexBufCb, display.pfnstateiavertexbufcb, pfnStateIaVertexBufCb, pfnStateIaVertexBufCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
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
-	UserDefined
api_location:
-	d3d10umddi.h
api_name:
-	pfnStateIaVertexBufCb
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_STATE_IA_VERTEXBUF_CB callback function
The <b>pfnStateIaVertexBufCb</b> function causes the Microsoft Direct3D 10 runtime to refresh the set of vertex buffers that are bound to the input assembler.

## Syntax

```
PFND3D10DDI_STATE_IA_VERTEXBUF_CB Pfnd3d10ddiStateIaVertexbufCb;

void Pfnd3d10ddiStateIaVertexbufCb(
   D3D10DDI_HRTCORELAYER,
   UINT,
   UINT
)
{...}
```

## Parameters

`D3D10DDI_HRTCORELAYER`



`UINT`



`UINT`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541820">D3D10DDI_CORELAYER_DEVICECALLBACKS</a>