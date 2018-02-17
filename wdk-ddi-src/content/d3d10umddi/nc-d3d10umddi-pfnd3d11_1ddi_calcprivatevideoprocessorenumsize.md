---
UID: NC:d3d10umddi.PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE
title: PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE
author: windows-driver-content
description: Returns the number of bytes that the driver requires to store private data for the video processor enumeration state.
old-location: display\calcprivatevideoprocessorenumsize.htm
old-project: display
ms.assetid: d468c892-6635-40a5-ad52-cbcc86555419
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.calcprivatevideoprocessorenumsize, CalcPrivateVideoProcessorEnumSize callback function [Display Devices], CalcPrivateVideoProcessorEnumSize, PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE, PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE, d3d10umddi/CalcPrivateVideoProcessorEnumSize
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	D3d10umddi.h
apiname:
-	CalcPrivateVideoProcessorEnumSize
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE callback function
Returns the number of bytes that the driver requires to store private data for the video processor enumeration state.

## Syntax

```
PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE Pfnd3d111DdiCalcprivatevideoprocessorenumsize;

SIZE_T Pfnd3d111DdiCalcprivatevideoprocessorenumsize(
   D3D10DDI_HDEVICE,
  CONST D3D11_1DDIARG_CREATEVIDEOPROCESSORENUM *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

The required number of bytes for the video processor enumeration state.

## Remarks

This function is not expected to fail.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessorenum.md">CreateVideoProcessorEnum</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddiarg_createvideoprocessorenum.md">D3D11_1DDIARG_CREATEVIDEOPROCESSORENUM</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_CALCPRIVATEVIDEOPROCESSORENUMSIZE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>