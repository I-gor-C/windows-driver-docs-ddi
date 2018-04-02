---
UID: NC:d3d10umddi.PFND3D10DDI_CREATEQUERY
title: PFND3D10DDI_CREATEQUERY
author: windows-driver-content
description: The CreateQuery(D3D10) function creates a query.
old-location: display\createquery_d3d10_.htm
old-project: display
ms.assetid: abe6a82f-1613-4c74-9e81-01939db74bfd
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateQuery, CreateQuery callback function [Display Devices], PFND3D10DDI_CREATEQUERY, UserModeDisplayDriverDx10_Functions_faa26999-d692-40b4-81ef-99c730879b49.xml, d3d10umddi/CreateQuery, display.createquery_d3d10_
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
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
-	d3d10umddi.h
api_name:
-	CreateQuery
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_CREATEQUERY callback function
The <b>CreateQuery(D3D10)</b> function creates a query.

## Syntax

```
PFND3D10DDI_CREATEQUERY Pfnd3d10ddiCreatequery;

void Pfnd3d10ddiCreatequery(
   D3D10DDI_HDEVICE,
  CONST D3D10DDIARG_CREATEQUERY *,
   D3D10DDI_HQUERY,
   D3D10DDI_HRTQUERY
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HQUERY`



`D3D10DDI_HRTQUERY`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver might run out of memory or be unable to create queries because of their exclusive nature. Therefore, the driver can pass E_OUTOFMEMORY, DXGI_DDI_ERR_NONEXCLUSIVE, or D3DDDIERR_DEVICEREMOVED in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="https://msdn.microsoft.com/74bb85df-6d64-49e8-b431-2f4a9954eff2">DestroyQuery(D3D10)</a> function to destroy the handle that the <i>hQuery</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/59a59aa8-085e-4bf8-8a6f-e08f2aecd894">CalcPrivateQuerySize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541685">D3D10DDIARG_CREATEQUERY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/74bb85df-6d64-49e8-b431-2f4a9954eff2">DestroyQuery(D3D10)</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>