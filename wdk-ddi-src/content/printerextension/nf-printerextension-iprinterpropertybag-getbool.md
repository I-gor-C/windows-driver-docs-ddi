---
UID: NF:printerextension.IPrinterPropertyBag.GetBool
title: IPrinterPropertyBag::GetBool method
author: windows-driver-content
description: Reads a specified boolean property.
old-location: print\iprinterpropertybag_getbool.htm
old-project: print
ms.assetid: 0C7ED962-F4E2-4F2F-B2CF-96DCFC71C4DD
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: GetBool method [Print Devices], GetBool method [Print Devices], IPrinterPropertyBag interface, GetBool,IPrinterPropertyBag.GetBool, IPrinterPropertyBag, IPrinterPropertyBag interface [Print Devices], GetBool method, IPrinterPropertyBag::GetBool, print.iprinterpropertybag_getbool, printerextension/IPrinterPropertyBag::GetBool
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: printerextension.h
req.include-header: Printerextension.h
req.target-type: Desktop
req.target-min-winverclnt: 
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
-	COM
api_location:
-	Printerextension.h
api_name:
-	IPrinterPropertyBag.GetBool
product:
- Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---


# IPrinterPropertyBag::GetBool method
Reads a specified boolean property.

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


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | printerextension.h (include Printerextension.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439547">IPrinterPropertyBag</a>