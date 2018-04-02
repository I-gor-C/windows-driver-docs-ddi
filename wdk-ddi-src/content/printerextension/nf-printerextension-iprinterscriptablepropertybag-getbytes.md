---
UID: NF:printerextension.IPrinterScriptablePropertyBag.GetBytes
title: IPrinterScriptablePropertyBag::GetBytes method
author: windows-driver-content
description: Gets a byte array property.
old-location: print\iprinterscriptablepropertybag_getbytes.htm
old-project: print
ms.assetid: 419BCBB6-634A-421D-A940-8690BCCF1AC6
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: GetBytes method [Print Devices], GetBytes method [Print Devices], IPrinterScriptablePropertyBag interface, GetBytes,IPrinterScriptablePropertyBag.GetBytes, IPrinterScriptablePropertyBag, IPrinterScriptablePropertyBag interface [Print Devices], GetBytes method, IPrinterScriptablePropertyBag::GetBytes, print.iprinterscriptablepropertybag_getbytes, printerextension/IPrinterScriptablePropertyBag::GetBytes
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
-	IPrinterScriptablePropertyBag.GetBytes
product:
- Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---


# IPrinterScriptablePropertyBag::GetBytes method
Gets a byte array property.

## Syntax

```
HRESULT GetBytes(
  BSTR      bstrName,
  IDispatch **ppArray
);
```

## Parameters

`bstrName`

The property to read.

`ppArray`




## Return Value

This method returns an <b>HRESULT</b> value.

## Remarks

A call to <b>GetBytes</b> will throw an exception, if the specified property is not found. We recommend that you use a try-catch statement around calls to this method, to allow your app to handle any failures gracefully.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh973217">IPrinterScriptablePropertyBag</a>