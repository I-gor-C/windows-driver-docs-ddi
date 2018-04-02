---
UID: NS:d3dumddi._D3DDDICB_SUBMITCOMMANDTOHWQUEUE
title: "_D3DDDICB_SUBMITCOMMANDTOHWQUEUE"
author: windows-driver-content
description: A structure that holds information to queue hardware flags.
old-location: display\d3dddicb_submitcommandtohwqueue.htm
old-project: display
ms.assetid: 5B650831-7AD7-4FEA-AC31-82F2B351BAD6
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDICB_SUBMITCOMMANDTOHWQUEUE, D3DDDICB_SUBMITCOMMANDTOHWQUEUE structure [Display Devices], _D3DDDICB_SUBMITCOMMANDTOHWQUEUE, d3dumddi/D3DDDICB_SUBMITCOMMANDTOHWQUEUE, display.d3dddicb_submitcommandtohwqueue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
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
-	d3dumddi.h
api_name:
-	D3DDDICB_SUBMITCOMMANDTOHWQUEUE
product:
- Windows
targetos: Windows
req.typenames: D3DDDICB_SUBMITCOMMANDTOHWQUEUE
---

# _D3DDDICB_SUBMITCOMMANDTOHWQUEUE structure
A structure that holds information to queue hardware flags.

## Syntax
```
typedef struct _D3DDDICB_SUBMITCOMMANDTOHWQUEUE {
  HANDLE                               hHwQueue;
  UINT64                               HwQueueProgressFenceId;
  D3DGPU_VIRTUAL_ADDRESS               Commands;
  UINT                                 CommandLength;
  D3DDDICB_SUBMITCOMMANDTOHWQUEUEFLAGS Flags;
  UINT                                 PrivateDriverDataSize;
  VOID                                 *pPrivateDriverData;
  UINT                                 NumPrimaries;
  D3DKMT_HANDLE                        *WrittenPrimaries;
} D3DDDICB_SUBMITCOMMANDTOHWQUEUE;
```

## Members


`hHwQueue`



`HwQueueProgressFenceId`



`Commands`



`CommandLength`



`Flags`



`PrivateDriverDataSize`



`pPrivateDriverData`



`NumPrimaries`



`WrittenPrimaries`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dumddi.h |