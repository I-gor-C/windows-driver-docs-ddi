---
UID : NS:d3dkmddi._DXGK_INTEGRATEDDISPLAYFLAGS
title : _DXGK_INTEGRATEDDISPLAYFLAGS
author : windows-driver-content
description : Flags which describe simple properties of an integrated display.
old-location : display\dxgk_integrateddisplayflags.htm
old-project : display
ms.assetid : 4671B6C1-358A-4CC2-A6FC-0FBA0F26DB07
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_INTEGRATEDDISPLAYFLAGS, *PDXGK_INTEGRATEDDISPLAYFLAGS, DXGK_INTEGRATEDDISPLAYFLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_INTEGRATEDDISPLAYFLAGS
req.alt-loc : d3dkmddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PDXGK_INTEGRATEDDISPLAYFLAGS, DXGK_INTEGRATEDDISPLAYFLAGS"
---

# _DXGK_INTEGRATEDDISPLAYFLAGS structure
Flags which describe simple properties of an integrated display.

## Syntax
````
typedef union _DXGK_INTEGRATEDDISPLAYFLAGS {
  struct {
    DXGK_DISPLAYPANELORIENTATION UndockedOrientation  :2;
    DXGK_DISPLAYPANELORIENTATION DockedOrientation  :2;
    UINT                         Reserved  :28;
  };
  UINT Value;
} DXGK_INTEGRATEDDISPLAYFLAGS;
````

## Members

        
            `Value`

            UINT used to operate on the combined bit-fields.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h |