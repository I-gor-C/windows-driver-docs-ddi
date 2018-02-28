---
UID: NC:d3dumddi.PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPUCB
title: PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPUCB
author: windows-driver-content
description: pfnWaitForSynchronizationObjectFromCpuCb waits for a monitored fence to reach a certain value before processing subsequent context commands.
old-location: display\pfnwaitforsynchronizationobjectfromcpucb.htm
old-project: display
ms.assetid: 304A5BCE-19E6-4F92-B840-FD3BE1CFB856
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPUCB, d3dumddi/pfnWaitForSynchronizationObjectFromCpuCb, display.pfnwaitforsynchronizationobjectfromcpucb, pfnWaitForSynchronizationObjectFromCpuCb, pfnWaitForSynchronizationObjectFromCpuCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
-	d3dumddi.h
api_name:
-	pfnWaitForSynchronizationObjectFromCpuCb
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPUCB callback function
<b>pfnWaitForSynchronizationObjectFromCpuCb</b> waits for a monitored fence to reach a certain value before processing subsequent context commands.

## Syntax

```
PFND3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPUCB Pfnd3dddiWaitforsynchronizationobjectfromcpucb;

HRESULT Pfnd3dddiWaitforsynchronizationobjectfromcpucb(
  HANDLE hDevice,
  CONST D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device.

`*`




## Return Value

If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |