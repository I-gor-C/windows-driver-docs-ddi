---
UID: NF:wiamdef.wiasIsPropChanged
title: wiasIsPropChanged function
author: windows-driver-content
description: The wiasIsPropChanged function tests whether a specified property has been changed by an application.
old-location: image\wiasispropchanged.htm
old-project: image
ms.assetid: 4b8f140c-ca4f-48fd-bee4-35d5a7beea52
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: image.wiasispropchanged, wiamdef/wiasIsPropChanged, wiasFncs_11e49124-0147-4140-ba56-879ae3fcbf46.xml, wiasIsPropChanged, wiasIsPropChanged function [Imaging Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamdef.h
req.include-header: Wiamdef.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.
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
req.lib: Wiaservc.lib
req.dll: Wiaservc.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Wiaservc.dll
api_name:
-	wiasIsPropChanged
product: Windows
targetos: Windows
req.typenames: DEVICEDIALOGDATA2, *LPDEVICEDIALOGDATA2, *PDEVICEDIALOGDATA2
req.product: Windows 10 or later.
---


# wiasIsPropChanged function
The <b>wiasIsPropChanged </b>function tests whether a specified property has been changed by an application.

## Syntax

```
HRESULT wiasIsPropChanged(
  PROPID               propid,
  WIA_PROPERTY_CONTEXT *pContext,
  BOOL                 *pbChanged
);
```

## Parameters

`propid`

TBD

`pContext`

Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552749">WIA_PROPERTY_CONTEXT</a> structure that contains the current property context.

`pbChanged`

Pointer to a memory location that receives a BOOL value. The BOOL value is <b>TRUE</b> if the property changed, and <b>FALSE</b> if the property did not change.


## Return Value

On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).

## Remarks

This function determines whether a property is being changed by looking at the <b>bChanged</b> member value in the property's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552749">WIA_PROPERTY_CONTEXT</a> structure. Minidrivers typically use this function to check when an independent property has been changed so that its dependents can be updated.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | wiamdef.h (include Wiamdef.h) |
| **Library** | Wiaservc.lib |
| **DLL** | Wiaservc.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552749">WIA_PROPERTY_CONTEXT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549200">wiasGetChangedValueFloat</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549211">wiasGetChangedValueGuid</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549214">wiasGetChangedValueLong</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549219">wiasGetChangedValueStr</a>