---
UID: NC:d3d10umddi.PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM
title: PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM
author: windows-driver-content
description: Releases resources for the video processor enumeration object that were created through a call to the CreateVideoProcessorEnum function.
old-location: display\destroyvideoprocessorenum.htm
old-project: display
ms.assetid: a4325993-aa87-466e-8e89-40bede1e0306
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM, d3d10umddi/pfnDestroyVideoProcessorEnum, display.destroyvideoprocessorenum, pfnDestroyVideoProcessorEnum, pfnDestroyVideoProcessorEnum callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	D3d10umddi.h
api_name:
-	pfnDestroyVideoProcessorEnum
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM callback function
Releases resources for the video processor enumeration object that were created through a call to the <a href="https://msdn.microsoft.com/38c27502-7e8a-45a1-8a7c-315300502480">CreateVideoProcessorEnum</a> function.

## Syntax

```
PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM Pfnd3d111DdiDestroyvideoprocessorenum;

void Pfnd3d111DdiDestroyvideoprocessorenum(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSORENUM
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSORENUM`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/38c27502-7e8a-45a1-8a7c-315300502480">CreateVideoProcessorEnum</a>