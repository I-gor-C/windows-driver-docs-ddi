---
UID : NF:d3dkmthk.D3DKMTSetMonitorColorSpaceTransform
title : D3DKMTSetMonitorColorSpaceTransform function
author : windows-driver-content
description : Used to set the color space transform for the selected monitor.
old-location : display\d3dkmtsetmonitorcolorspacetransform.htm
old-project : display
ms.assetid : cb831371-4684-4756-bc01-6c42e5af7e1b
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMTSetMonitorColorSpaceTransform
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
req.alt-api : D3DKMTSetMonitorColorSpaceTransform
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


# D3DKMTSetMonitorColorSpaceTransform function
Used to set the color space transform for the selected monitor.

## Syntax

````
NTSTATUS  D3DKMTSetMonitorColorSpaceTransform(
   D3DKMT_SET_COLORSPACE_TRANSFORM  D3dkmt_set_colorspace_transform
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