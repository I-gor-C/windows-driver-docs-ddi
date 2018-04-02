---
UID: NF:printerextension.IPrinterScriptablePropertyBag.GetInt32
title: IPrinterScriptablePropertyBag::GetInt32 method
author: windows-driver-content
description: Gets an integer property.
old-location: print\iprinterscriptablepropertybag_getint32.htm
old-project: print
ms.assetid: 0E1089E4-5FE4-4769-A244-3E1979E4DE46
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: GetInt32 method [Print Devices], GetInt32 method [Print Devices], IPrinterScriptablePropertyBag interface, GetInt32,IPrinterScriptablePropertyBag.GetInt32, IPrinterScriptablePropertyBag, IPrinterScriptablePropertyBag interface [Print Devices], GetInt32 method, IPrinterScriptablePropertyBag::GetInt32, print.iprinterscriptablepropertybag_getint32, printerextension/IPrinterScriptablePropertyBag::GetInt32
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
-	IPrinterScriptablePropertyBag.GetInt32
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---


# IPrinterScriptablePropertyBag::GetInt32 method
Gets an integer property.

## Syntax

```
HRESULT GetInt32(
  BSTR bstrName,
  LONG *pnValue
);
```

## Parameters

`bstrName`

The property to read.

`pnValue`

The value read.


## Return Value

This method returns an <b>HRESULT</b> value.

## Remarks

A call to <b>GetInt32</b> will throw an exception, if the specified property is not found. We recommend that you use a try-catch statement around calls to this method, to allow your app to handle any failures gracefully.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh973217">IPrinterScriptablePropertyBag</a>