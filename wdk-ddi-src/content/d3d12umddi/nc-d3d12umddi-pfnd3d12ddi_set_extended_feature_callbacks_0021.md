---
UID : NC:d3d12umddi.PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021
title : PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021
author : windows-driver-content
description : The pfnSetExtendedFeatureCallbacks callback function sets extended feature callbacks.
old-location : display\pfnd3d12ddi_set_extended_feature_callbacks_0021.htm
old-project : display
ms.assetid : 8380C972-D5A0-46D5-B32B-C31D5113BB95
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.pfnd3d12ddi_set_extended_feature_callbacks_0021, pfnSetExtendedFeatureCallbacks callback function [Display Devices], pfnSetExtendedFeatureCallbacks, PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021, PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021, d3d12umddi/pfnSetExtendedFeatureCallbacks
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d12umddi.h
req.include-header : D3d12umddi.h
req.target-type : Windows
req.target-min-winverclnt : 
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
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021 callback function
The <i>pfnSetExtendedFeatureCallbacks</i> callback function sets extended feature callbacks.

## Syntax

```
PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021 Pfnd3d12ddiSetExtendedFeatureCallbacks0021;

HRESULT Pfnd3d12ddiSetExtendedFeatureCallbacks0021(
  D3D12DDI_HDEVICE hDevice,
  D3D12DDI_TABLE_TYPE Table,
  const void *pTable,
  SIZE_T TableSize
)
{...}
```

## Parameters

`hDevice`

The handle of a device.

`Table`

A value for an implementation of video.

`*pTable`

A pointer to a table value.

`TableSize`

The size of the table.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |