---
UID : NS:d3dukmdt._D3DDDI_CREATEHWQUEUEFLAGS
title : _D3DDDI_CREATEHWQUEUEFLAGS
author : windows-driver-content
description : A structure used to create hardware queue flags.
old-location : display\d3dddi_createhwqueueflags_.htm
old-project : display
ms.assetid : 50318DEC-8EE4-4208-8E7D-E8BFEA4BA06B
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DDDI_CREATEHWQUEUEFLAGS structure [Display Devices], display.d3dddi_createhwqueueflags_, D3DDDI_CREATEHWQUEUEFLAGS, _D3DDDI_CREATEHWQUEUEFLAGS, d3dukmdt/D3DDDI_CREATEHWQUEUEFLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dukmdt.h
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
req.typenames : D3DDDI_CREATEHWQUEUEFLAGS
---

# _D3DDDI_CREATEHWQUEUEFLAGS structure
A structure used to create hardware queue flags.

## Syntax
````
typedef struct _D3DDDI_CREATEHWQUEUEFLAGS  {
  union {
    struct {
      UINT DisableGpuTimeout  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} D3DDDI_CREATEHWQUEUEFLAGS ;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dukmdt.h |