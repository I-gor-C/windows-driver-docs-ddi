---
UID: NF:printerextension.IPrinterBidiSetRequestCallback.Completed
title: IPrinterBidiSetRequestCallback::Completed method
author: windows-driver-content
description: Invoked when the Bidi “Set”” operation is completed.
old-location: print\iprinterbidisetrequestcallback_completed.htm
old-project: print
ms.assetid: F086903F-2FCA-4B9F-948B-0F40F114E11D
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: Completed method [Print Devices], Completed method [Print Devices], IPrinterBidiSetRequestCallback interface, Completed,IPrinterBidiSetRequestCallback.Completed, IPrinterBidiSetRequestCallback, IPrinterBidiSetRequestCallback interface [Print Devices], Completed method, IPrinterBidiSetRequestCallback::Completed, print.iprinterbidisetrequestcallback_completed, printerextension/IPrinterBidiSetRequestCallback::Completed
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
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
-	IPrinterBidiSetRequestCallback.Completed
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---


# Completed method
Invoked when the Bidi “Set”” operation is completed.

## Syntax

````
HRESULT Completed(
  [in] BSTR    bstrResponse,
  [in] HRESULT hrStatus
);
````

## Parameters

`bstrResponse`

The received response.

`hrStatus`

An HRESULT value.


## Return Value

This method returns the appropriate <b>HRESULT</b> value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows Server 2012 R2 |
| **Target Platform** | Desktop |
| **Header** | printerextension.h |

## See Also

<a href="..\printerextension\nn-printerextension-iprinterbidisetrequestcallback.md">IPrinterBidiSetRequestCallback</a>