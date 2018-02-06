---
UID: NS:d3dkmthk._D3DKMT_CREATEPROTECTEDSESSION
title: "_D3DKMT_CREATEPROTECTEDSESSION"
author: windows-driver-content
description: Used to create a protected session.
old-location: display\d3dkmt-createprotectedsession.htm
old-project: display
ms.assetid: 4ec42f5a-df33-4da3-a959-64cb400f3177
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: "_D3DKMT_CREATEPROTECTEDSESSION, D3DKMT_CREATEPROTECTEDSESSION structure [Display Devices], d3dkmthk/D3DKMT_CREATEPROTECTEDSESSION, display.d3dkmt-createprotectedsession, D3DKMT_CREATEPROTECTEDSESSION"
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
-	D3DKMT_CREATEPROTECTEDSESSION
product: Windows
targetos: Windows
req.typenames: D3DKMT_CREATEPROTECTEDSESSION
---

# _D3DKMT_CREATEPROTECTEDSESSION structure
Used to create a protected session.

## Syntax
````
typedef struct _D3DKMT_CREATEPROTECTEDSESSION {
  D3DKMT_HANDLE hDevice;
  D3DKMT_HANDLE hSyncObject;
  const VOID    *pPrivateDriverData;
  UINT          PrivateDriverDataSize;
  const VOID    *pPrivateRuntimeData;
  UINT          PrivateRuntimeDataSize;
  D3DKMT_HANDLE hHandle;
} D3DKMT_CREATEPROTECTEDSESSION;
````

## Members


`hDevice`

A handle for the device.

`hHandle`

The protected session handle.

`hSyncObject`

A monitored fence handle associated with the session.

`pPrivateDriverData`

Private driver data.

`pPrivateRuntimeData`

Private runtime data.

`PrivateDriverDataSize`

Size of private driver data.

`PrivateRuntimeDataSize`

Size of private runtime data.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmthk.h |