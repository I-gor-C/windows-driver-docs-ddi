---
UID: NC:d3d10umddi.PFND3D10DDI_CHECKMULTISAMPLEQUALITYLEVELS
title: PFND3D10DDI_CHECKMULTISAMPLEQUALITYLEVELS
author: windows-driver-content
description: The CheckMultisampleQualityLevels function retrieves the number of quality levels that the device supports for the specified number of samples.
old-location: display\checkmultisamplequalitylevels.htm
old-project: display
ms.assetid: 2b6a0ab8-f197-48c3-baf2-305b77b7e8b5
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: CheckMultisampleQualityLevels, CheckMultisampleQualityLevels callback function [Display Devices], PFND3D10DDI_CHECKMULTISAMPLEQUALITYLEVELS, UserModeDisplayDriverDx10_Functions_d19bc4c0-49ba-4e1c-b19e-667905ceb391.xml, d3d10umddi/CheckMultisampleQualityLevels, display.checkmultisamplequalitylevels
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
-	CheckMultisampleQualityLevels
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_CHECKMULTISAMPLEQUALITYLEVELS callback function
The <b>CheckMultisampleQualityLevels</b> function retrieves the number of quality levels that the device supports for the specified number of samples.

## Syntax

```
PFND3D10DDI_CHECKMULTISAMPLEQUALITYLEVELS Pfnd3d10ddiCheckmultisamplequalitylevels;

void Pfnd3d10ddiCheckmultisamplequalitylevels(
   D3D10DDI_HDEVICE,
   DXGI_FORMAT,
   UINT,
  UINT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`DXGI_FORMAT`



`UINT`



`*`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. The driver can set E_INVALIDARG if the format in the <i>Format</i> parameter does not exist or the <i>pNumQualityLevels</i> parameter is <b>NULL</b>.

## Remarks

If the device does not support multiple sampling with the number of samples that is specified in the <i>SampleCount</i> parameter, the user-mode display driver should return 0 in the variable that the <i>pNumQualityLevels</i> parameter points to.

When the driver returns 1 or more in the variable that <i>pNumQualityLevels</i> points to, the driver indicates the number of device-specific sampling variations that are available with the given sample count. For example, if the driver returns 3, quality levels 0, 1, and 2 can be used to create resources with the given sample count. The device manufacturer defines these quality levels, which the Microsoft Direct3D runtime cannot query. However, different quality levels at a fixed sample count might refer to different spatial layouts of the sample locations or different methods of resolving.

If the driver receives 1 in <i>SampleCount</i>, the driver always returns 1 in the variable that <i>pNumQualityLevels</i> points to.

If the driver receives 0 or greater than 32 in <i>SampleCount</i>, the driver always returns 0 in the variable that <i>pNumQualityLevels</i> points to.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>