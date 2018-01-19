---
UID : NF:d3dkmthk.D3DKMTGetProcessDeviceLostSupport
title : D3DKMTGetProcessDeviceLostSupport function
author : windows-driver-content
description : Used to get the indicated process.
old-location : display\d3dkmtgetprocessdevicelostsupport.htm
old-project : display
ms.assetid : 7127b6ff-164b-4645-a602-3969f87a47d0
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMTGetProcessDeviceLostSupport
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
req.alt-api : D3DKMTGetProcessDeviceLostSupport
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


# D3DKMTGetProcessDeviceLostSupport function
Used to get the indicated process.

## Syntax

````
NTSTATUS  D3DKMTGetProcessDeviceLostSupport(
  _Inout_ D3DKMT_GETPROCESSDEVICELOSTSUPPORT  *D3dkmt_getprocessdevicelostsupport
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