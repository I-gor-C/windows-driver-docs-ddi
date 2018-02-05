---
UID : NC:d3dumddi.PFND3DDDI_CHECKCOUNTERINFO
title : PFND3DDDI_CHECKCOUNTERINFO
author : windows-driver-content
description : Called by the Microsoft Direct3D runtime to determine global information that's related to manipulating counters. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers.
old-location : display\pfncheckcounterinfo.htm
old-project : display
ms.assetid : 98B8EE79-18D2-4C57-964B-74DB550C1330
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.pfncheckcounterinfo, pfnCheckCounterInfo callback function [Display Devices], pfnCheckCounterInfo, PFND3DDDI_CHECKCOUNTERINFO, PFND3DDDI_CHECKCOUNTERINFO, d3dumddi/pfnCheckCounterInfo
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dumddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8.1
req.target-min-winversvr : Windows Server 2012 R2
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
req.typenames : DXGK_PTE
---


# PFND3DDDI_CHECKCOUNTERINFO callback function
Called by the Microsoft Direct3D runtime to determine global information that's related to manipulating counters. Must be implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers.

## Syntax

```
PFND3DDDI_CHECKCOUNTERINFO Pfnd3dddiCheckcounterinfo;

void Pfnd3dddiCheckcounterinfo(
  HANDLE hDevice,
  D3DDDIARG_COUNTER_INFO *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

This function should behave similarly to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_checkcounterinfo.md">CheckCounterInfo</a> function that supports Microsoft Direct3D 10 and later.

If the user-mode display driver does not support any of the concepts that are represented in the members of the <a href="..\d3dumddi\ns-d3dumddi-d3dddiarg_counter_info.md">D3DDDIARG_COUNTER_INFO</a> structure, it can populate the members of <b>D3DDDIARG_COUNTER_INFO</b> with zeros.

The driver's <i>pfnCheckCounterInfo</i> function cannot call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set the <b>D3DDDIERR_DEVICEREMOVED</b> error code because <i>pfnCheckCounterInfo</i> is a capability-check type of function. The driver must ensure that it has enough information after device creation to respond to a call to <i>pfnCheckCounterInfo</i>, even in the presence of <b>D3DDDIERR_DEVICEREMOVED</b>. <i>pfnCheckCounterInfo</i> should not encounter any errors. However, <i>pfnCheckCounterInfo</i> might call <b>pfnSetErrorCb</b> for critical errors.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>

<a href="..\d3dumddi\ns-d3dumddi-d3dddiarg_counter_info.md">D3DDDIARG_COUNTER_INFO</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_checkcounterinfo.md">CheckCounterInfo</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_CHECKCOUNTERINFO callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>