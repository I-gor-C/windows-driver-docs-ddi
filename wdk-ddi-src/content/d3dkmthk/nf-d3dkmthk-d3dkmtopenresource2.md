---
UID : NF:d3dkmthk.D3DKMTOpenResource2
title : D3DKMTOpenResource2 function
author : windows-driver-content
description : Reserved for system use. Do not use in your driver.
old-location : display\d3dkmtopenresource2.htm
old-project : display
ms.assetid : 7D496443-F68D-41E6-B377-BC9E6F6ABB83
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMTOpenResource2, D3DKMTOpenResource2 function [Display Devices], d3dkmthk/D3DKMTOpenResource2, display.d3dkmtopenresource2
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : d3dkmthk.h
req.include-header : D3dkmthk.h
req.target-type : Universal
req.target-min-winverclnt : Available in Windows 7 and later versions of the Windows operating systems.
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
req.lib : Gdi32.lib
req.dll : Gdi32.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3DKMT_DRIVERVERSION
---


# D3DKMTOpenResource2 function
Reserved for system use. Do not use in your driver.

## Syntax

````
NTSTATUS D3DKMTOpenResource2(
  _Inout_ D3DKMT_OPENRESOURCE *pData
);
````

## Parameters

This function has no parameters.

## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |