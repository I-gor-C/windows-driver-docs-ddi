---
UID: NN:wdtf.IWDTFNumbers2
title: IWDTFNumbers2
author: windows-driver-content
description: Defines operations and properties for a collection of numbers.
old-location: dtf\iwdtfnumbers2.htm
old-project: dtf
ms.assetid: 8cff3bc3-771f-47b7-bf4b-b7221f498252
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFNumbers2, IWDTFNumbers2 interface [Windows Device Testing Framework], IWDTFNumbers2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFNumbers2, dtf.iwdtfnumbers2, wdtf/IWDTFNumbers2
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
-	IWDTFNumbers2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFNumbers2 interface

Defines operations and properties for a collection of numbers.

## Methods

<p>The <b>IWDTFNumbers2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFNumbers2::Add](nf-wdtf-iwdtfnumbers2-add.md) | Adds a single number to the collection. |
| [IWDTFNumbers2::get__NewEnum](nf-wdtf-iwdtfnumbers2-get__newenum.md) | Gets a new iteration variable that the For Each loop structure implicitly uses. |
| [IWDTFNumbers2::get_Count](nf-wdtf-iwdtfnumbers2-get_count.md) | Gets the number of devices that are currently provided by the DeviceDepot. |
| [IWDTFNumbers2::get_Item](nf-wdtf-iwdtfnumbers2-get_item.md) | Gets an individual device in the DeviceDepot. |
| [IWDTFNumbers2::Remove](nf-wdtf-iwdtfnumbers2-remove.md) | Removes a number from the collection. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtf.h |