---
UID: NN:printerextension.IPrinterExtensionEvent
title: IPrinterExtensionEvent
author: windows-driver-content
description: The IPrinterExtensionEvent interface represents the event delegate implemented by desktop printer extensions for activation.
old-location: print\iprinterextensionevent_interface.htm
old-project: print
ms.assetid: A0F4DB51-D68E-4516-833A-7E984247796B
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterExtensionEvent, IPrinterExtensionEvent interface [Print Devices], IPrinterExtensionEvent interface [Print Devices], described, print.iprinterextensionevent_interface, printerextension/IPrinterExtensionEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
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
-	printerextension.h
api_name:
-	IPrinterExtensionEvent
product:
- Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterExtensionEvent interface

The IPrinterExtensionEvent interface represents the event delegate implemented by desktop printer extensions for activation.

## Methods

<p>The <b>IPrinterExtensionEvent</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrinterExtensionEvent::OnDriverEvent](nf-printerextension-iprinterextensionevent-ondriverevent.md) | Called when a driver event occurs. |
| [IPrinterExtensionEvent::OnPrinterQueuesEnumerated](nf-printerextension-iprinterextensionevent-onprinterqueuesenumerated.md) | Called when printer queues are enumerated. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | printerextension.h |