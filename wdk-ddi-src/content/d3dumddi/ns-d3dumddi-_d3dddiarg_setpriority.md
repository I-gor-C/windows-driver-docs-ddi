---
UID: NS:d3dumddi._D3DDDIARG_SETPRIORITY
title: "_D3DDDIARG_SETPRIORITY"
author: windows-driver-content
description: The D3DDDIARG_SETPRIORITY structure describes the priority level to set for a managed texture.
old-location: display\d3dddiarg_setpriority.htm
old-project: display
ms.assetid: d3dd52de-6d28-4d71-9b64-ba79e17bd9ee
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDIARG_SETPRIORITY, D3DDDIARG_SETPRIORITY structure [Display Devices], UMDisplayDriver_param_Structs_e416cff1-5cad-4488-a3e2-ea0b42a7cd81.xml, _D3DDDIARG_SETPRIORITY, d3dumddi/D3DDDIARG_SETPRIORITY, display.d3dddiarg_setpriority
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
-	d3dumddi.h
api_name:
-	D3DDDIARG_SETPRIORITY
product: Windows
targetos: Windows
req.typenames: D3DDDIARG_SETPRIORITY
---

# _D3DDDIARG_SETPRIORITY structure
The D3DDDIARG_SETPRIORITY structure describes the priority level to set for a managed texture.

## Syntax
```
typedef struct _D3DDDIARG_SETPRIORITY {
  HANDLE hResource;
  UINT   Priority;
} D3DDDIARG_SETPRIORITY;
```

## Members


`hResource`

A handle to the resource that contains the texture.

`Priority`

The priority level to set for the texture that is contained in the <b>hResource</b> resource. A texture's priority value can be set anywhere in the range from 0 through 0xFFFFFFFF.

## Remarks
The driver receives only priority notifications for driver-managed textures.

The priority level at which a texture is set determines its eviction order from memory. A texture that is assigned a low priority is evicted before a texture with a high priority. If two textures have the same priority, the texture that was used more recently is kept in memory; the other texture is evicted.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/61ac2d28-7aed-4796-8d09-591db936013b">SetPriority</a>