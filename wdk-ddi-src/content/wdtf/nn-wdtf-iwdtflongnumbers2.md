---
UID: NN:wdtf.IWDTFLongNumbers2
title: IWDTFLongNumbers2
author: windows-driver-content
description: Defines operations and properties for a collection of long numbers.
old-location: dtf\iwdtflongnumbers2.htm
old-project: dtf
ms.assetid: 2a6c4cf7-179e-4e20-bab4-a4181a0ee64c
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFLongNumbers2, IWDTFLongNumbers2 interface [Windows Device Testing Framework], IWDTFLongNumbers2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFLongNumbers2, dtf.iwdtflongnumbers2, wdtf/IWDTFLongNumbers2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtf.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTF.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTF.Interop.metadata_dll
req.type-library: 
req.lib: wdtf.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WDTF.Interop.metadata_dll.dll
api_name:
-	IWDTFLongNumbers2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFLongNumbers2 interface

Defines operations and properties for a collection of long numbers.

## Methods

<p>The <b>IWDTFLongNumbers2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFLongNumbers2::Add](nf-wdtf-iwdtflongnumbers2-add.md) | Adds a single long number to the collection. |
| [IWDTFLongNumbers2::get__NewEnum](nf-wdtf-iwdtflongnumbers2-get__newenum.md) | Gets a new iteration variable that the For Each loop structure implicitly uses. |
| [IWDTFLongNumbers2::get_Count](nf-wdtf-iwdtflongnumbers2-get_count.md) | Gets the number of devices that are currently provided by the DeviceDepot. |
| [IWDTFLongNumbers2::get_Item](nf-wdtf-iwdtflongnumbers2-get_item.md) | Gets an individual device in the DeviceDepot. |
| [IWDTFLongNumbers2::Remove](nf-wdtf-iwdtflongnumbers2-remove.md) | Removes a long number from the collection. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtf.h |