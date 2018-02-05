---
UID : NC:d3d12umddi.PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023
title : PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023
author : windows-driver-content
description : The pfnCalcPrivateCommandQueueSize callback function is used to calculate the size of a private command queue.
old-location : display\pfnd3d12ddi_calcprivatecommandqueuesize_0023.htm
old-project : display
ms.assetid : 70A81285-97CD-4526-8EB0-F00908B2D331
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.pfnd3d12ddi_calcprivatecommandqueuesize_0023, pfnCalcPrivateCommandQueueSize callback function [Display Devices], pfnCalcPrivateCommandQueueSize, PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023, PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023, d3d12umddi/pfnCalcPrivateCommandQueueSize
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


# PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023 callback function
The <i>pfnCalcPrivateCommandQueueSize</i> callback function is used to calculate the size of a private command queue.

## Syntax

```
PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023 Pfnd3d12ddiCalcprivatecommandqueuesize0023;

SIZE_T Pfnd3d12ddiCalcprivatecommandqueuesize0023(
   D3D12DDI_HDEVICE,
  CONST D3D12DDIARG_CREATECOMMANDQUEUE_0023 *
)
{...}
```

## Parameters

`D3D12DDI_HDEVICE`



`*`




## Return Value

The size of the queue.

## Remarks

Access this callback function by using a device functions core structure, such as the <b>D3D12DDI_DEVICE_FUNCS_CORE_0003</b> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |