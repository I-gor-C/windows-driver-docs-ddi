---
UID: NC:dispmprt.DXGKDDI_UNLOAD
title: DXGKDDI_UNLOAD
author: windows-driver-content
description: The DxgkDdiUnload function frees any resources allocated during execution of the display miniport driver's DriverEntry function.
old-location: display\dxgkddiunload.htm
old-project: display
ms.assetid: 336fa87a-6c3e-4337-90d9-b0ebeb355e68
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGKDDI_UNLOAD, DmFunctions_b7f60489-c7e7-4bd1-bf17-ff193bc7d614.xml, DxgkDdiUnload, DxgkDdiUnload callback function [Display Devices], display.dxgkddiunload, dispmprt/DxgkDdiUnload
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dispmprt.h
req.include-header: Dispmprt.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	Dispmprt.h
api_name:
-	DxgkDdiUnload
product: Windows
targetos: Windows
req.typenames: SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
---


# DXGKDDI_UNLOAD callback function
The <i>DxgkDdiUnload</i> function frees any resources allocated during execution of the display miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function.

## Syntax

```
DXGKDDI_UNLOAD DxgkddiUnload;

void DxgkddiUnload(

)
{...}
```

## Parameters

This function has no parameters.

## Return Value

This callback function does not return a value.

## Remarks

Typically, there will be nothing to do in <i>DxgkDdiUnload</i>.

<i>DxgkDdiUnload</i> should be made pageable.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | dispmprt.h (include Dispmprt.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff556157">DriverEntry of Display Miniport Driver</a>