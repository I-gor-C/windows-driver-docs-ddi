---
UID : NS:d3dkmthk._D3DKMT_MPO3DDI_SUPPORT
title : _D3DKMT_MPO3DDI_SUPPORT
author : windows-driver-content
description : A structure that holds the support status.
old-location : display\d3dkmt_mpo3ddi_support.htm
old-project : display
ms.assetid : 993E0BC3-DE46-48B9-A346-386E49CE28CE
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DKMT_MPO3DDI_SUPPORT, D3DKMT_MPO3DDI_SUPPORT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmthk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMT_MPO3DDI_SUPPORT
req.alt-loc : d3dkmthk.h
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
req.typenames : D3DKMT_MPO3DDI_SUPPORT
---

# _D3DKMT_MPO3DDI_SUPPORT structure
A structure that holds the support status.

## Syntax
````
typedef struct _D3DKMT_MPO3DDI_SUPPORT {
  BOOL Supported;
} D3DKMT_MPO3DDI_SUPPORT;
````

## Members

        
            `Supported`

            Indicates whether support exists.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h |