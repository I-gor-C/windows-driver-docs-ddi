---
UID: NF:printerextension.IPrinterScriptablePropertyBag.SetBool
title: IPrinterScriptablePropertyBag::SetBool method
author: windows-driver-content
description: Writes a specified boolean property value.
old-location: print\iprinterscriptablepropertybag_setbool.htm
old-project: print
ms.assetid: 8970833A-7CBA-40EB-85A8-60E7730C052F
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterScriptablePropertyBag, IPrinterScriptablePropertyBag interface [Print Devices], SetBool method, IPrinterScriptablePropertyBag::SetBool, SetBool method [Print Devices], SetBool method [Print Devices], IPrinterScriptablePropertyBag interface, SetBool,IPrinterScriptablePropertyBag.SetBool, print.iprinterscriptablepropertybag_setbool, printerextension/IPrinterScriptablePropertyBag::SetBool
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	COM
api_location:
-	Printerextension.h
api_name:
-	IPrinterScriptablePropertyBag.SetBool
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---


# IPrinterScriptablePropertyBag::SetBool method
Writes a specified boolean property value.

## Syntax

```
HRESULT SetBool(
  BSTR bstrName,
  BOOL bValue
);
```

## Parameters

`bstrName`

The property to set.

`bValue`

The value to set.


## Return Value

This method returns an <b>HRESULT</b> value.

## Remarks

A call to <b>SetBool</b> will throw an exception, if the specified property is not found. We recommend that you use a try-catch statement around calls to this method, to allow your app to handle any failures gracefully.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh973217">IPrinterScriptablePropertyBag</a>