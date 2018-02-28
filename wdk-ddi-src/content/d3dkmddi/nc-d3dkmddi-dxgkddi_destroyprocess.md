---
UID: NC:d3dkmddi.DXGKDDI_DESTROYPROCESS
title: DXGKDDI_DESTROYPROCESS
author: windows-driver-content
description: DxgkDdiDestroyProcess destroys a kernel mode driver process object.
old-location: display\dxgkddidestroyprocess.htm
old-project: display
ms.assetid: C5117F9B-876D-4F74-B528-47698666B44B
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: DXGKDDI_DESTROYPROCESS, DxgkDdiDestroyProcess, DxgkDdiDestroyProcess callback function [Display Devices], d3dkmddi/DxgkDdiDestroyProcess, display.dxgkddidestroyprocess, dispmprt/DxgkDdiDestroyProcess
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: 
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
-	dispmprt.h
-	d3dkmddi.h
api_name:
-	DxgkDdiDestroyProcess
product: Windows
targetos: Windows
req.typenames: DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_DESTROYPROCESS callback function
<b>DxgkDdiDestroyProcess</b> destroys a kernel mode driver process object.

## Syntax

```
DXGKDDI_DESTROYPROCESS DxgkddiDestroyprocess;

NTSTATUS DxgkddiDestroyprocess(
  IN_CONST_HANDLE hAdapter,
  IN_CONST_HANDLE hKmdProcess
)
{...}
```

## Parameters

`hAdapter`

A handle to the display adapter.

`hKmdProcess`

A handle to the kernel mode driver process.


## Return Value

Returns <b>STATUS_SUCCESS</b> if it succeeds. Otherwise, it returns one of the error codes defined in <b>Ntstatus.h</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Desktop |
| **Header** | d3dkmddi.h |