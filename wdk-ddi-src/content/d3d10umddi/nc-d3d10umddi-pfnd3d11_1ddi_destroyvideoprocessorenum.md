---
UID : NC:d3d10umddi.PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM
title : PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM
author : windows-driver-content
description : Releases resources for the video processor enumeration object that were created through a call to the CreateVideoProcessorEnum function.
old-location : display\destroyvideoprocessorenum.htm
old-project : display
ms.assetid : a4325993-aa87-466e-8e89-40bede1e0306
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.destroyvideoprocessorenum, pfnDestroyVideoProcessorEnum callback function [Display Devices], pfnDestroyVideoProcessorEnum, PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM, PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM, d3d10umddi/pfnDestroyVideoProcessorEnum
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
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
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM callback function
Releases resources for the video processor enumeration object that were created through a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessorenum.md">CreateVideoProcessorEnum</a> function.

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
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessorenum.md">CreateVideoProcessorEnum</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_DESTROYVIDEOPROCESSORENUM callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>