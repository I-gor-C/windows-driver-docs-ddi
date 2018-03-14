---
UID: NN:wdtf.IWDTFActions2
title: IWDTFActions2
author: windows-driver-content
description: Defines operations and properties for the collection of actions that the IWDTFTargets::GetInterfaces method returns.
old-location: dtf\iwdtfactions2.htm
old-project: dtf
ms.assetid: cf78bd7f-7d92-421f-8f68-e56db5e7c7d4
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFActions2, IWDTFActions2 interface [Windows Device Testing Framework], IWDTFActions2 interface [Windows Device Testing Framework], described, dtf.iwdtfactions2, wdtf/IWDTFActions2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtf.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Wdtf.idl
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
-	wdtf.h
api_name:
-	IWDTFActions2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFActions2 interface

Defines operations and properties for the collection of actions that the IWDTFTargets::GetInterfaces 
method returns.

## Methods

<p>The <b>IWDTFActions2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFActions2::Add](nf-wdtf-iwdtfactions2-add.md) | Add a single action to the collection. |
| [IWDTFActions2::Clear](nf-wdtf-iwdtfactions2-clear.md) | Removes all items from the collection. |
| [IWDTFActions2::DisableObjectErrorLogging](nf-wdtf-iwdtfactions2-disableobjecterrorlogging.md) | Disable object error logging for all actions in the collection. |
| [IWDTFActions2::DisableObjectLogging](nf-wdtf-iwdtfactions2-disableobjectlogging.md) | Disable object logging for all actions in the collection. |
| [IWDTFActions2::EnableObjectErrorLogging](nf-wdtf-iwdtfactions2-enableobjecterrorlogging.md) | Enable object error logging for all actions in the collection. |
| [IWDTFActions2::EnableObjectLogging](nf-wdtf-iwdtfactions2-enableobjectlogging.md) | Enable object logging for all actions in the collection. |
| [IWDTFActions2::get__NewEnum](nf-wdtf-iwdtfactions2-get__newenum.md) | Gets a new iteration variable that the For Each loop structure implicitly uses. |
| [IWDTFActions2::get_Count](nf-wdtf-iwdtfactions2-get_count.md) | Gets the number of devices that are currently provided by the DeviceDepot. |
| [IWDTFActions2::get_Item](nf-wdtf-iwdtfactions2-get_item.md) | Gets an individual device in the DeviceDepot. |
| [IWDTFActions2::Remove](nf-wdtf-iwdtfactions2-remove.md) | Remove an action from the collection. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wdtf.h |