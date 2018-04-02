---
UID: NF:wiamdef.wiasSetValidListFloat
title: wiasSetValidListFloat function
author: windows-driver-content
description: The wiasSetValidListFloat function sets valid values for a WIA_PROP_LIST property of type VT_R4.
old-location: image\wiassetvalidlistfloat.htm
old-project: image
ms.assetid: e1a833aa-fc8b-4506-aba8-ba6dc9a375ba
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: image.wiassetvalidlistfloat, wiamdef/wiasSetValidListFloat, wiasFncs_ef1aa836-f63d-43e8-8378-22d37fbdc3a2.xml, wiasSetValidListFloat, wiasSetValidListFloat function [Imaging Devices]
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
-	wiasSetValidListFloat
product: Windows
targetos: Windows
req.typenames: DEVICEDIALOGDATA2, *LPDEVICEDIALOGDATA2, *PDEVICEDIALOGDATA2
req.product: Windows 10 or later.
---


# wiasSetValidListFloat function
The <b>wiasSetValidListFloat </b>function sets valid values for a WIA_PROP_LIST property of type VT_R4.

## Syntax

```
HRESULT wiasSetValidListFloat(
  BYTE   *pWiasContext,
  PROPID propid,
  ULONG  ulCount,
  FLOAT  fNom,
  FLOAT  *pfValues
);
```

## Parameters

`pWiasContext`

Pointer to a WIA item context.

`propid`

Specifies the identifier of the property to be updated.

`ulCount`

Specifies the number of items in the <i>plValues</i> array.

`fNom`

Specifies the property's nominal value.

`pfValues`

Pointer to the first element of an array of valid property values.


## Return Value

On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | wiamdef.h (include Wiamdef.h) |
| **Library** | Wiaservc.lib |
| **DLL** | Wiaservc.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549390">wiasSetValidFlag</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549409">wiasSetValidListGuid</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549414">wiasSetValidListLong</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549421">wiasSetValidListStr</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549425">wiasSetValidRangeFloat</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549434">wiasSetValidRangeLong</a>