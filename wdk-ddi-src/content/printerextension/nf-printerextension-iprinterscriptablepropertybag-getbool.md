---
UID: NF:printerextension.IPrinterScriptablePropertyBag.GetBool
title: IPrinterScriptablePropertyBag::GetBool method
author: windows-driver-content
description: Gets a specified boolean property.
old-location: print\iprinterscriptablepropertybag_getbool.htm
old-project: print
ms.assetid: EEBB916B-0E7B-4523-BB13-A4758F5491BB
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: GetBool method [Print Devices], GetBool method [Print Devices], IPrinterScriptablePropertyBag interface, GetBool,IPrinterScriptablePropertyBag.GetBool, IPrinterScriptablePropertyBag, IPrinterScriptablePropertyBag interface [Print Devices], GetBool method, IPrinterScriptablePropertyBag::GetBool, print.iprinterscriptablepropertybag_getbool, printerextension/IPrinterScriptablePropertyBag::GetBool
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
-	IPrinterScriptablePropertyBag.GetBool
product:
- Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---


# IPrinterScriptablePropertyBag::GetBool method
Gets a specified boolean property.

## Syntax

```
HRESULT GetBool(
  BSTR bstrName,
  BOOL *pbValue
);
```

## Parameters

`bstrName`

The name of the property.

`pbValue`

The returned property value.


## Return Value

This method returns an <b>HRESULT</b> value.

## Remarks

A call to <b>GetBool</b> will throw an exception, if the specified property is not found. We recommend that you use a try-catch statement around calls to this method, to allow your app to handle any failures gracefully.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh973217">IPrinterScriptablePropertyBag</a>