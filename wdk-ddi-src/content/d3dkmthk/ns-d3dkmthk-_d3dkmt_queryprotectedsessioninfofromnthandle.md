---
UID: NS:d3dkmthk._D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE
title: "_D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE"
author: windows-driver-content
description: Used to query information on the protected session.
old-location: display\d3dkmt-queryprotectedsessioninfofromnthandle.htm
old-project: display
ms.assetid: e08d27e7-e9b7-45e7-9bbd-dcb9aa8f85ed
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.d3dkmt-queryprotectedsessioninfofromnthandle, D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE structure [Display Devices], D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE, _D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE, d3dkmthk/D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmthk.h
apiname:
-	D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE
product: Windows
targetos: Windows
req.typenames: D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE
---

# _D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE structure
Used to query information on the protected session.

## Syntax
````
typedef struct _D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE {
  HANDLE     hNtHandle;
  const VOID *pPrivateDriverData;
  UINT       PrivateDriverDataSize;
  const VOID *pPrivateRuntimeData;
  UINT       PrivateRuntimeDataSize;
} D3DKMT_QUERYPROTECTEDSESSIONINFOFROMNTHANDLE;
````

## Members


`hNtHandle`

The protected NT session handle.

`pPrivateDriverData`

The private driver data.

`pPrivateRuntimeData`

The private runtime data.

`PrivateDriverDataSize`

The size of the private driver data.

`PrivateRuntimeDataSize`

The size of the private runtime data.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmthk.h |