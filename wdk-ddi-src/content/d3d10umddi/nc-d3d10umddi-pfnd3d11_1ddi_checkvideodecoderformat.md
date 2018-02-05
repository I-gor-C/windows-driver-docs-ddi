---
UID : NC:d3d10umddi.PFND3D11_1DDI_CHECKVIDEODECODERFORMAT
title : PFND3D11_1DDI_CHECKVIDEODECODERFORMAT
author : windows-driver-content
description : Determines whether a specified format can be used as a video decoder output format for a specified DirectX Video Acceleration (DXVA) profile.
old-location : display\checkvideodecoderformat.htm
old-project : display
ms.assetid : 6bde6e00-70ba-4fa5-9cc0-9884ce7381ed
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.checkvideodecoderformat, CheckVideoDecoderFormat callback function [Display Devices], CheckVideoDecoderFormat, PFND3D11_1DDI_CHECKVIDEODECODERFORMAT, PFND3D11_1DDI_CHECKVIDEODECODERFORMAT, d3d10umddi/CheckVideoDecoderFormat
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


# PFND3D11_1DDI_CHECKVIDEODECODERFORMAT callback function
Determines whether a specified format can be used as a video decoder output format for a specified DirectX Video Acceleration (DXVA) profile.

## Syntax

```
PFND3D11_1DDI_CHECKVIDEODECODERFORMAT Pfnd3d111DdiCheckvideodecoderformat;

void Pfnd3d111DdiCheckvideodecoderformat(
   D3D10DDI_HDEVICE,
  CONST GUID *,
   DXGI_FORMAT,
  BOOL *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`DXGI_FORMAT`



`*`




## Return Value

This callback function does not return a value.

## Remarks

This function is not expected to fail.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |