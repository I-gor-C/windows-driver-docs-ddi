---
UID : NF:d3dkmthk.D3DKMTDestroyProtectedSession
title : D3DKMTDestroyProtectedSession function
author : windows-driver-content
description : Used to destroy a protected session.
old-location : display\d3dkmtdestroyprotectedsession.htm
old-project : display
ms.assetid : e27ab1db-647d-447c-b79d-2553aa088398
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMTDestroyProtectedSession
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : d3dkmthk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMTDestroyProtectedSession
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
req.typenames : D3DKMT_DRIVERVERSION
---


# D3DKMTDestroyProtectedSession function
Used to destroy a protected session.

## Syntax

````
NTSTATUS  D3DKMTDestroyProtectedSession(
  _Inout_ D3DKMT_DESTROYPROTECTEDSESSION  *D3dkmt_destroyprotectedsession
);
````

## Parameters

This function has no parameters.

## Return Value

Returns STATUS_SUCCESS if completed successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |