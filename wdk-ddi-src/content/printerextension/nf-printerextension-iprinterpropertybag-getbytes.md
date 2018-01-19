---
UID : NF:printerextension.IPrinterPropertyBag.GetBytes
title : IPrinterPropertyBag::GetBytes method
author : windows-driver-content
description : Reads a byte array property.
old-location : print\iprinterpropertybag_getbytes.htm
old-project : print
ms.assetid : F75E182D-90FA-4597-95E0-60A6326CF68D
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IPrinterPropertyBag, IPrinterPropertyBag::GetBytes, GetBytes
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : printerextension.h
req.include-header : Printerextension.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IPrinterPropertyBag.GetBytes
req.alt-loc : Printerextension.h
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
req.typenames : PrintSchemaSelectionType
req.product : Windows 10 or later.
---


# GetBytes method
Reads a byte array property.

The <a href="..\printerextension\nn-printerextension-iprinterpropertybag.md">IPrinterPropertyBag</a> interface is used by all the printer property bags, including driver property bag, user property bag, queue property bag, and DEVMODE property bag.

## Syntax

````
HRESULT GetBytes(
  [in]  BSTR  bstrName,
  [out] DWORD *pcbValue,
  [out] BYTE  *rgbValue
);
````

## Parameters

`bstrName`

The property to read.

`pcbValue`

The number of bytes read.

`ppValue`




## Return Value

This method returns an <b>HRESULT</b> value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | printerextension.h (include Printerextension.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterpropertybag.md">IPrinterPropertyBag</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterPropertyBag::GetBytes method%20 RELEASE:%20(1/8/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>