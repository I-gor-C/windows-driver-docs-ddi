---
UID : NC:drmk.PFNDRMCREATECONTENTMIXED
title : PFNDRMCREATECONTENTMIXED
author : windows-driver-content
description : This callback function is reserved for system use.
old-location : audio\pfndrmcreatecontentmixed.htm
old-project : audio
ms.assetid : A4BA818F-126F-4134-AEDA-F983ADFC4A07
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WDI_TX_METADATA, WDI_TX_METADATA, *PWDI_TX_METADATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : drmk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DRMCreateContentMixed
req.alt-loc : Drmk.h
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
req.typenames : WDI_TX_METADATA, *PWDI_TX_METADATA
---


# PFNDRMCREATECONTENTMIXED callback function
This callback function is reserved for system use.

## Syntax

```
PFNDRMCREATECONTENTMIXED Pfndrmcreatecontentmixed;

NTSTATUS Pfndrmcreatecontentmixed(
  PULONG paContentId,
  ULONG cContentId,
  PULONG pMixedContentId
)
{...}
```

## Parameters

`paContentId`

This parameter is reserved for system use.

`cContentId`

This parameter is reserved for system use.

`pMixedContentId`

This parameter is reserved for system use.


## Return Value

This return value is reserved for system use.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | drmk.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |