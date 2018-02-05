---
UID : NS:d3dukmdt.D3DDDI_UPDATEALLOCPROPERTY_FLAGS
title : D3DDDI_UPDATEALLOCPROPERTY_FLAGS
author : windows-driver-content
description : The D3DDDI_UPDATEALLOCPROPERTY_FLAGS structure identifies how to update a property in an allocation.
old-location : display\d3dddi_updateallocproperty_flags.htm
old-project : display
ms.assetid : 377EC824-9D43-40CA-B5CA-A04402852EA3
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DDDI_UPDATEALLOCPROPERTY_FLAGS, d3dukmdt/D3DDDI_UPDATEALLOCPROPERTY_FLAGS, display.d3dddi_updateallocproperty_flags, d3dukmdt/PD3DDDI_UPDATEALLOCPROPERTY_FLAGS, PD3DDDI_UPDATEALLOCPROPERTY_FLAGS structure pointer [Display Devices], D3DDDI_UPDATEALLOCPROPERTY_FLAGS structure [Display Devices], PD3DDDI_UPDATEALLOCPROPERTY_FLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dukmdt.h
req.include-header : TBD
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
req.typenames : D3DDDI_UPDATEALLOCPROPERTY_FLAGS
---

# D3DDDI_UPDATEALLOCPROPERTY_FLAGS structure
The D3DDDI_UPDATEALLOCPROPERTY_FLAGS structure identifies how to update a property in an allocation.

## Syntax
````
typedef struct _D3DDDI_UPDATEALLOCPROPERTY_FLAGS {
  union {
    struct {
      UINT AccessedPhysically   :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  };
} D3DDDI_UPDATEALLOCPROPERTY_FLAGS, *PD3DDDI_UPDATEALLOCPROPERTY_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dukmdt.h (include TBD) |