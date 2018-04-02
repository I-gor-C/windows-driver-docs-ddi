---
UID: NN:wdtf.IWDTFTargets2
title: IWDTFTargets2
author: windows-driver-content
description: Defines properties and operations for the collection.
old-location: dtf\iwdtftargets2.htm
old-project: dtf
ms.assetid: b8d091e1-464c-43a7-b8fe-a9fa79be31c3
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFTargets2, IWDTFTargets2 interface [Windows Device Testing Framework], IWDTFTargets2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFTargets2, dtf.iwdtftargets2, wdtf/IWDTFTargets2
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
req.lib: 
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
-	IWDTFTargets2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFTargets2 interface

Defines properties and operations for the collection.

## Methods

<p>The <b>IWDTFTargets2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFTargets2::Add](nf-wdtf-iwdtftargets2-add.md) | Add a single item to the collection. |
| [IWDTFTargets2::Clear](nf-wdtf-iwdtftargets2-clear.md) | Removes all items from the collection. |
| [IWDTFTargets2::Eval](nf-wdtf-iwdtftargets2-eval.md) | Evaluates whether all items in the collection match an SDEL statement. |
| [IWDTFTargets2::get__NewEnum](nf-wdtf-iwdtftargets2-get__newenum.md) | Gets a new iteration variable that the For Each loop structure implicitly uses. |
| [IWDTFTargets2::get_Count](nf-wdtf-iwdtftargets2-get_count.md) | Gets the number of items in this collection. |
| [IWDTFTargets2::get_Item](nf-wdtf-iwdtftargets2-get_item.md) | Gets an individual item in the collection. |
| [IWDTFTargets2::get_WDTF](nf-wdtf-iwdtftargets2-get_wdtf.md) | Gets the main WDTF aggregation object. |
| [IWDTFTargets2::GetInterfaces](nf-wdtf-iwdtftargets2-getinterfaces.md) | Returns a collection of actions that support the interface - one IWDTFAction2 for each item that has one. |
| [IWDTFTargets2::GetInterfacesIfExist](nf-wdtf-iwdtftargets2-getinterfacesifexist.md) | Returns a collection of actions that support the interface - one IWDTFAction2 for each item that has one. |
| [IWDTFTargets2::Query](nf-wdtf-iwdtftargets2-query.md) | Returns a subset of the items in the collection. |
| [IWDTFTargets2::QuerySingle](nf-wdtf-iwdtftargets2-querysingle.md) | Returns a single item from the collection. |
| [IWDTFTargets2::Remove](nf-wdtf-iwdtftargets2-remove.md) | Removes an item from the collection. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtf.h |