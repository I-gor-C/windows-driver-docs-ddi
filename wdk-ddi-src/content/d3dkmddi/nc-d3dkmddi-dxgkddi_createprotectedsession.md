---
UID : NC:d3dkmddi.DXGKDDI_CREATEPROTECTEDSESSION
title : DXGKDDI_CREATEPROTECTEDSESSION
author : windows-driver-content
description : Used to create a protected session.
old-location : display\dxgkddi_createprotectedsession.htm
old-project : display
ms.assetid : 0FAE7AA0-839D-4D21-BC10-46B2B651979F
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.dxgkddi_createprotectedsession, DXGKDDI_CREATEPROTECTEDSESSION callback function [Display Devices], DXGKDDI_CREATEPROTECTEDSESSION, d3dkmddi/DXGKDDI_CREATEPROTECTEDSESSION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dkmddi.h
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
req.irql : requires_(PASSIVE_LEVEL)
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_CREATEPROTECTEDSESSION function
Used to create a protected session.

## Syntax

```
DXGKDDI_CREATEPROTECTEDSESSION DxgkddiCreateprotectedsession;

NTSTATUS DxgkddiCreateprotectedsession(
  IN_CONST_HANDLE hAdapter,
  INOUT_PDXGKARG_CREATEPROTECTEDSESSION pCreateProtectedSession
)
{...}
```

## Parameters

`hAdapter`

A handle to the adapter.

`pCreateProtectedSession`

A pointer to the arguments used to create a protected session.


## Return Value

Returns STATUS_SUCCESS if completed successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h |
| **Library** |  |
| **IRQL** | requires_(PASSIVE_LEVEL) |
| **DDI compliance rules** |  |