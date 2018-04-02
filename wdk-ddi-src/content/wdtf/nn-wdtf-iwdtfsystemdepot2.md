---
UID: NN:wdtf.IWDTFSystemDepot2
title: IWDTFSystemDepot2
author: windows-driver-content
description: Defines operations and properties for the SystemDepot - the object that represents the local computer.
old-location: dtf\iwdtfsystemdepot2.htm
old-project: dtf
ms.assetid: 7e6e5d35-66c3-4f69-8ac0-0c1100baa5c6
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFSystemDepot2, IWDTFSystemDepot2 interface [Windows Device Testing Framework], IWDTFSystemDepot2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFSystemDepot2, dtf.iwdtfsystemdepot2, wdtf/IWDTFSystemDepot2
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
-	IWDTFSystemDepot2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFSystemDepot2 interface

Defines operations and properties for the SystemDepot - the object that represents the 
local computer.

## Methods

<p>The <b>IWDTFSystemDepot2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFSystemDepot2::get_ThisSystem](nf-wdtf-iwdtfsystemdepot2-get_thissystem.md) | Gets an IWDTFTarget2 value that represents the local computer. |
| [IWDTFSystemDepot2::get_WDTF](nf-wdtf-iwdtfsystemdepot2-get_wdtf.md) | Gets the main WDTF aggregation object. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtf.h |