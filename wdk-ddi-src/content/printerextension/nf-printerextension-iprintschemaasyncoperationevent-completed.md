---
UID: NF:printerextension.IPrintSchemaAsyncOperationEvent.Completed
title: IPrintSchemaAsyncOperationEvent::Completed method
author: windows-driver-content
description: Is called when asynchronous PrintSchema operation that is represented by an IPrintSchemaAsyncOperation context is completed.
old-location: print\iprintschemaasyncoperationevent_completed.htm
old-project: print
ms.assetid: B1599F21-D6DD-497D-9CD8-6C637ABAA33A
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: Completed method [Print Devices], Completed method [Print Devices], IPrintSchemaAsyncOperationEvent interface, Completed,IPrintSchemaAsyncOperationEvent.Completed, IPrintSchemaAsyncOperationEvent, IPrintSchemaAsyncOperationEvent interface [Print Devices], Completed method, IPrintSchemaAsyncOperationEvent::Completed, print.iprintschemaasyncoperationevent_completed, printerextension/IPrintSchemaAsyncOperationEvent::Completed
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
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
-	IPrintSchemaAsyncOperationEvent.Completed
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---


# Completed method
Is called when asynchronous PrintSchema operation that is represented by an <a href="..\printerextension\nn-printerextension-iprintschemaasyncoperation.md">IPrintSchemaAsyncOperation</a> context is completed.

## Syntax

````
HRESULT Completed(
  [in] IPrintSchemaTicket *pTicket,
  [in] HRESULT            hrOperation
);
````

## Parameters

`pTicket`

The print ticket.

`hrOperation`

The result of the completed operation.


## Return Value

This method returns an <b>HRESULT</b> value.

## Remarks

The print ticket passed to the <b>Completed</b> method is the final validated, merged, or committed print ticket.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8  |
| **Target Platform** | Desktop |
| **Header** | printerextension.h |

## See Also

<a href="..\printerextension\nn-printerextension-iprintschematicket.md">IPrintSchemaTicket</a>



<a href="..\printerextension\nn-printerextension-iprintschemaasyncoperationevent.md">IPrintSchemaAsyncOperationEvent</a>