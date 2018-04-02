---
UID: NC:d3d10umddi.PFND3DWDDM2_0DDI_CHECKVIDEOPROCESSORFORMATCONVERSION
title: PFND3DWDDM2_0DDI_CHECKVIDEOPROCESSORFORMATCONVERSION
author: windows-driver-content
description: Indicates whether the driver supports a specific format/color-space conversion combination. This function must be implemented by Windows Display Driver Model (WDDM) 2.0 or later drivers.
old-location: display\checkvideoprocessorformatconversion.htm
old-project: display
ms.assetid: 70A741CC-9D1B-4ECC-BB3A-6ACF6893691A
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CheckVideoProcessorFormatConversion, CheckVideoProcessorFormatConversion callback function [Display Devices], d3d10umddi/CheckVideoProcessorFormatConversion, display.checkvideoprocessorformatconversion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
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
-	CheckVideoProcessorFormatConversion
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3DWDDM2_0DDI_CHECKVIDEOPROCESSORFORMATCONVERSION callback function
Indicates whether the driver supports a specific format/color-space conversion combination. This function must be implemented by Windows Display Driver Model (WDDM) 2.0 or later drivers.

## Syntax

```
PFND3DWDDM2_0DDI_CHECKVIDEOPROCESSORFORMATCONVERSION Pfnd3dwddm20DdiCheckvideoprocessorformatconversion;

void Pfnd3dwddm20DdiCheckvideoprocessorformatconversion(
  D3D10DDI_HDEVICE hDevice,
  D3D11_1DDI_HVIDEOPROCESSORENUM hProcessorEnum,
  D3DWDDM2_0DDI_CHECK_VIDEO_PROCESSOR_FORMAT_CONVERSION *pConversion
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context). The Direct3D runtime passed the user-mode driver this handle as the <b>hDevice</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542931">D3DDDIARG_CREATEDEVICE</a> structure at device creation.

`hProcessorEnum`

A handle to a video processor enumeration object that was created through a call to the <a href="https://msdn.microsoft.com/38c27502-7e8a-45a1-8a7c-315300502480">CreateVideoProcessorEnum</a> function.

`*pConversion`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn894604">D3DWDDM2_0DDI_CHECK_VIDEO_PROCESSOR_FORMAT_CONVERSION</a> structure that contains the input and output format/color-space combination.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/38c27502-7e8a-45a1-8a7c-315300502480">CreateVideoProcessorEnum</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542931">D3DDDIARG_CREATEDEVICE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn894604">D3DWDDM2_0DDI_CHECK_VIDEO_PROCESSOR_FORMAT_CONVERSION</a>