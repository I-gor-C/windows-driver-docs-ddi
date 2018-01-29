---
UID : NF:printerextension.IPrinterScriptablePropertyBag.SetBytes
title : IPrinterScriptablePropertyBag::SetBytes method
author : windows-driver-content
description : Writes a byte array property.
old-location : print\iprinterscriptablepropertybag_setbytes.htm
old-project : print
ms.assetid : 517CF135-A5D7-4C99-8592-59934E24DEE3
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : SetBytes method [Print Devices], IPrinterScriptablePropertyBag interface, IPrinterScriptablePropertyBag interface [Print Devices], SetBytes method, SetBytes, IPrinterScriptablePropertyBag::SetBytes, printerextension/IPrinterScriptablePropertyBag::SetBytes, IPrinterScriptablePropertyBag, print.iprinterscriptablepropertybag_setbytes, SetBytes method [Print Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : printerextension.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : printerextension.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PrintSchemaSelectionType
req.product : Windows 10 or later.
---


# SetBytes method
Writes a byte array property.

## Syntax

````
HRESULT SetBytes(
  [in] BSTR      bstrName,
  [in] IDispatch *pdispArray
);
````

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
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | printerextension.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\printerextension\nn-printerextension-iprinterscriptablepropertybag.md">IPrinterScriptablePropertyBag</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterScriptablePropertyBag::SetBytes method%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>