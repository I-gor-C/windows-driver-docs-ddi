---
UID: NF:d3dkmthk.D3DKMTExtractBundleObject
title: D3DKMTExtractBundleObject function
author: windows-driver-content
description: Used to extract the bundle object.
old-location: display\d3dkmtextractbundleobject.htm
old-project: display
ms.assetid: f3193d5b-084f-4df1-9688-26ba5a964cca
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.d3dkmtextractbundleobject, d3dkmthk/D3DKMTExtractBundleObject, D3DKMTExtractBundleObject, D3DKMTExtractBundleObject method [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmthk.h
apiname:
-	D3DKMTExtractBundleObject
product: Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
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
| **Windows version** | Windows 10 Windows 10 |
| **Target Platform** | Windows |
| **Header** | d3dkmthk.h |
| **Library** | NtosKrnl.exe |