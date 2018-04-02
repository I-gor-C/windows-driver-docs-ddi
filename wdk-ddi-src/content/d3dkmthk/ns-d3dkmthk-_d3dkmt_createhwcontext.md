---
UID: NS:d3dkmthk._D3DKMT_CREATEHWCONTEXT
title: "_D3DKMT_CREATEHWCONTEXT"
author: windows-driver-content
description: A structure holding information to create a hardware context.
old-location: display\d3dkmt_createhwcontext.htm
old-project: display
ms.assetid: 9B6EA552-B576-45F3-A0BD-7EB721638D7F
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_CREATEHWCONTEXT, D3DKMT_CREATEHWCONTEXT structure [Display Devices], _D3DKMT_CREATEHWCONTEXT, d3dkmthk/D3DKMT_CREATEHWCONTEXT, display.d3dkmt_createhwcontext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
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
-	D3DKMT_CREATEHWCONTEXT
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_CREATEHWCONTEXT
---

# _D3DKMT_CREATEHWCONTEXT structure
A structure holding information to create a hardware context.

## Syntax
```
typedef struct _D3DKMT_CREATEHWCONTEXT {
  D3DKMT_HANDLE               hDevice;
  UINT                        NodeOrdinal;
  UINT                        EngineAffinity;
  D3DDDI_CREATEHWCONTEXTFLAGS Flags;
  UINT                        PrivateDriverDataSize;
  VOID                        *pPrivateDriverData;
  D3DKMT_HANDLE               hHwContext;
} D3DKMT_CREATEHWCONTEXT;
```

## Members


`hDevice`

Handle to the device owning this context.

`NodeOrdinal`

Identifier for the node targetted by this context.

`EngineAffinity`

Engine affinity within the specified node.

`Flags`

Context creation flags.

`PrivateDriverDataSize`

Size of private driver data.

`pPrivateDriverData`

Private driver data.

`hHwContext`

Handle of the created context.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmthk.h |