---
UID : NC:d3d12umddi.PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030
title : PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030
author : windows-driver-content
description : Used to set a protected resource session.
old-location : display\pfnd3d12ddi_setprotectedresourcesession_0030_.htm
old-project : display
ms.assetid : 1AF1FA8A-3A7E-4277-B6BE-C41A5C4416B6
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.pfnd3d12ddi_setprotectedresourcesession_0030_, PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030 callback function [Display Devices], PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030, d3d12umddi/PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d12umddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
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
req.typenames : D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030 callback function
Used to set a protected resource session.

## Syntax

```
PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030 Pfnd3d12ddiSetprotectedresourcesession0030;

void Pfnd3d12ddiSetprotectedresourcesession0030(
   D3D12DDI_HCOMMANDLIST,
   D3D12DDI_HPROTECTEDRESOURCESESSION_0030
)
{...}
```

## Parameters

`D3D12DDI_HCOMMANDLIST`



`D3D12DDI_HPROTECTEDRESOURCESESSION_0030`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h |