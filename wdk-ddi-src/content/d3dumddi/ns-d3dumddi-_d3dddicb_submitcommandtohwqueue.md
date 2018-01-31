---
UID : NS:d3dumddi._D3DDDICB_SUBMITCOMMANDTOHWQUEUE
title : "_D3DDDICB_SUBMITCOMMANDTOHWQUEUE"
author : windows-driver-content
description : A structure that holds information to queue hardware flags.
old-location : display\d3dddicb_submitcommandtohwqueue.htm
old-project : display
ms.assetid : 5B650831-7AD7-4FEA-AC31-82F2B351BAD6
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DDDICB_SUBMITCOMMANDTOHWQUEUE, display.d3dddicb_submitcommandtohwqueue, D3DDDICB_SUBMITCOMMANDTOHWQUEUE structure [Display Devices], d3dumddi/D3DDDICB_SUBMITCOMMANDTOHWQUEUE, _D3DDDICB_SUBMITCOMMANDTOHWQUEUE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dumddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3DDDICB_SUBMITCOMMANDTOHWQUEUE
---

# _D3DDDICB_SUBMITCOMMANDTOHWQUEUE structure
A structure that holds information to queue hardware flags.

## Syntax
````
typedef struct _D3DDDICB_SUBMITCOMMANDTOHWQUEUE {
  union {
    struct {
      UINT Reserved  :32;
    };
    UINT Value;
  };
} D3DDDICB_SUBMITCOMMANDTOHWQUEUE;
````

## Members


`CommandLength`



`Commands`



`Flags`



`hHwQueue`



`HwQueueProgressFenceId`



`NumPrimaries`



`pPrivateDriverData`



`PrivateDriverDataSize`



`WrittenPrimaries`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h |