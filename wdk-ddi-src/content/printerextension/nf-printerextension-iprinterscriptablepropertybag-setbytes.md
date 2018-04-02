---
UID: NF:printerextension.IPrinterScriptablePropertyBag.SetBytes
title: IPrinterScriptablePropertyBag::SetBytes method
author: windows-driver-content
description: Writes a byte array property.
old-location: print\iprinterscriptablepropertybag_setbytes.htm
old-project: print
ms.assetid: 517CF135-A5D7-4C99-8592-59934E24DEE3
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterScriptablePropertyBag, IPrinterScriptablePropertyBag interface [Print Devices], SetBytes method, IPrinterScriptablePropertyBag::SetBytes, SetBytes method [Print Devices], SetBytes method [Print Devices], IPrinterScriptablePropertyBag interface, SetBytes,IPrinterScriptablePropertyBag.SetBytes, print.iprinterscriptablepropertybag_setbytes, printerextension/IPrinterScriptablePropertyBag::SetBytes
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
-	IPrinterScriptablePropertyBag.SetBytes
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---


# IPrinterScriptablePropertyBag::SetBytes method
Writes a byte array property.

## Syntax

```
HRESULT SetBytes(
  BSTR      bstrName,
  IDispatch *pArray
);
```

## Parameters

`bstrName`

The array to write to.

`pArray`




## Return Value

This method returns an <b>HRESULT</b> value.

## Remarks

A call to <b>SetBytes</b> will throw an exception, if the specified property is not found. We recommend that you use a try-catch statement around calls to this method, to allow your app to handle any failures gracefully.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh973217">IPrinterScriptablePropertyBag</a>