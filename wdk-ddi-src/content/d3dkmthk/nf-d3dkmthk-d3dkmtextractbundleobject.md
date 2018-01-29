---
UID : NF:d3dkmthk.D3DKMTExtractBundleObject
title : D3DKMTExtractBundleObject function
author : windows-driver-content
description : Used to extract the bundle object.
old-location : display\d3dkmtextractbundleobject.htm
old-project : display
ms.assetid : f3193d5b-084f-4df1-9688-26ba5a964cca
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMTExtractBundleObject, D3DKMTExtractBundleObject method [Display Devices], d3dkmthk/D3DKMTExtractBundleObject, display.d3dkmtextractbundleobject
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3DKMT_DRIVERVERSION
---


# D3DKMTExtractBundleObject function
Used to extract the bundle object.

## Syntax

````
NTSTATUS  D3DKMTExtractBundleObject(
  _Inout_ D3DKMT_EXTRACTBUNDLEOBJECT  *D3dkmt_extractbundleobject
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