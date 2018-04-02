---
UID: NN:printerextension.IPrinterExtensionManager
title: IPrinterExtensionManager
author: windows-driver-content
description: The IPrinterExtensionManager interface is retrieved by CoCreating the PrinterExtensionManager class.
old-location: print\iprinterextensionmanager_interface.htm
old-project: print
ms.assetid: 918AE3F6-2AC4-42AD-9581-E87AD7E79BAD
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterExtensionManager, IPrinterExtensionManager interface [Print Devices], IPrinterExtensionManager interface [Print Devices], described, print.iprinterextensionmanager_interface, printerextension/IPrinterExtensionManager
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
-	IPrinterExtensionManager
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterExtensionManager interface

The <b>IPrinterExtensionManager</b> interface is retrieved by CoCreating the <b>PrinterExtensionManager</b> class.

## Methods

<p>The <b>IPrinterExtensionManager</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrinterExtensionManager::DisableEvents](nf-printerextension-iprinterextensionmanager-disableevents.md) | Disallows events to be generated. |
| [IPrinterExtensionManager::EnableEvents](nf-printerextension-iprinterextensionmanager-enableevents.md) | The EnableEvents method allows events to be generated for the specified printer driver until DisableEvents is called. |

## Remarks
Any event sink that implements <a href="https://msdn.microsoft.com/A0F4DB51-D68E-4516-833A-7E984247796B">IPrinterExtensionEvent</a> is connected to the associated event source, <b>IPrinterExtensionManager</b>, via the <b>IConnectionPoint</b> mechanism. You must retrieve a pointer to the <b>IConnectionPoint</b> interface by invoking <b>QueryInterface</b> on the <b>IPrinterExtensionManager</b> object.

<div class="alert"><b>Note</b>  It is mandatory to implement <b>IDispatch::Invoke</b> on the event sink that implements <b>IPrinterExtensionEvent</b>, since that is the mechanism via which events are raised. It is sufficient to provide stub implementations of the other methods on the <b>IDispatch</b> interface.</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | printerextension.h |