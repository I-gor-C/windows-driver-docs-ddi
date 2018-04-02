---
UID: NN:wdtf.IWDTFStrings2
title: IWDTFStrings2
author: windows-driver-content
description: Defines operations and properties for a collection of strings.
old-location: dtf\iwdtfstrings2.htm
old-project: dtf
ms.assetid: ea7ebda9-9588-4c72-bac6-2bae1f80538e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFStrings2, IWDTFStrings2 interface [Windows Device Testing Framework], IWDTFStrings2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFStrings2, dtf.iwdtfstrings2, wdtf/IWDTFStrings2
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
-	IWDTFStrings2
product:
- Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFStrings2 interface

Defines operations and properties for a collection of strings.

## Methods

<p>The <b>IWDTFStrings2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFStrings2::Add](nf-wdtf-iwdtfstrings2-add.md) | Adds a single string to the collection. |
| [IWDTFStrings2::get__NewEnum](nf-wdtf-iwdtfstrings2-get__newenum.md) | Gets a new iteration variable that the For Each loop structure implicitly uses. |
| [IWDTFStrings2::get_Count](nf-wdtf-iwdtfstrings2-get_count.md) | Gets the number of strings in the collection. |
| [IWDTFStrings2::get_Item](nf-wdtf-iwdtfstrings2-get_item.md) | Gets an individual string in the collection. |
| [IWDTFStrings2::Remove](nf-wdtf-iwdtfstrings2-remove.md) | Removes a string from the collection. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtf.h |