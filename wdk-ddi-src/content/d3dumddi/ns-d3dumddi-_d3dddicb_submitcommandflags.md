---
UID : NS:d3dumddi._D3DDDICB_SUBMITCOMMANDFLAGS
title : _D3DDDICB_SUBMITCOMMANDFLAGS
author : windows-driver-content
description : D3DDDICB_SUBMITCOMMANDFLAGS is used to indicate how to process command buffers on contexts that support graphics processing unit (GPU) virtual addressing.
old-location : display\d3dddicb_submitcommandflags.htm
old-project : display
ms.assetid : 415255A8-4D43-4677-B4B3-0425D6D57933
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DDDICB_SUBMITCOMMANDFLAGS, D3DDDICB_SUBMITCOMMANDFLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DDDICB_SUBMITCOMMANDFLAGS
req.alt-loc : d3dumddi.h
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
req.typenames : D3DDDICB_SUBMITCOMMANDFLAGS
---

# _D3DDDICB_SUBMITCOMMANDFLAGS structure
<b>D3DDDICB_SUBMITCOMMANDFLAGS</b> is used to indicate how to process command buffers on contexts that support graphics processing unit (GPU) virtual addressing.

## Syntax
````
typedef struct _D3DDDICB_SUBMITCOMMANDFLAGS {
  union {
    struct {
      UINT NullRendering  :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  };
} D3DDDICB_SUBMITCOMMANDFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |