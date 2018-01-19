---
UID : NS:d3dukmdt._D3DDDI_CREATEHWCONTEXTFLAGS
title : _D3DDDI_CREATEHWCONTEXTFLAGS
author : windows-driver-content
description : A structure used to create hardware context flags.
old-location : display\d3dddi_createhwcontextflags.htm
old-project : display
ms.assetid : 429A1C54-14F0-4E50-B0D6-BB73FCFD1904
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DDDI_CREATEHWCONTEXTFLAGS, D3DDDI_CREATEHWCONTEXTFLAGS
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
req.alt-api : D3DDDI_CREATEHWCONTEXTFLAGS
req.alt-loc : d3dukmdt.h
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
req.typenames : D3DDDI_CREATEHWCONTEXTFLAGS
---

# _D3DDDI_CREATEHWCONTEXTFLAGS structure
A structure used to create hardware context flags.

## Syntax
````
typedef struct _D3DDDI_CREATEHWCONTEXTFLAGS {
  union {
    struct {
      UINT Reserved  :32;
    };
    UINT Value;
  };
} D3DDDI_CREATEHWCONTEXTFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dukmdt.h |