---
UID: NN:wdtf.IWDTFTarget2
title: IWDTFTarget2
author: windows-driver-content
description: Defines operations and properties for a testable item.
old-location: dtf\iwdtftarget2.htm
old-project: dtf
ms.assetid: fc75c201-a3ff-44f7-ba09-8e3554b1cf27
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFTarget2, IWDTFTarget2 interface [Windows Device Testing Framework], IWDTFTarget2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFTarget2, dtf.iwdtftarget2, wdtf/IWDTFTarget2
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
-	IWDTFTarget2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFTarget2 interface

Defines operations and properties for a testable item.

## Methods

<p>The <b>IWDTFTarget2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFTarget2::Eval](nf-wdtf-iwdtftarget2-eval.md) | Evaluate whether this target matches an SDEL statement. |
| [IWDTFTarget2::get_Context](nf-wdtf-iwdtftarget2-get_context.md) | Gets and sets a name-value pair that represents user data for the target. |
| [IWDTFTarget2::get_Type](nf-wdtf-iwdtftarget2-get_type.md) | Gets a value that identifies the depot that the target comes from. |
| [IWDTFTarget2::get_WDTF](nf-wdtf-iwdtftarget2-get_wdtf.md) | Gets the main WDTF aggregation object. |
| [IWDTFTarget2::GetInterface](nf-wdtf-iwdtftarget2-getinterface.md) | Returns an action for the target. |
| [IWDTFTarget2::GetRelations](nf-wdtf-iwdtftarget2-getrelations.md) | Returns a collection of related targets. |
| [IWDTFTarget2::GetValue](nf-wdtf-iwdtftarget2-getvalue.md) | Returns a value from the target that is associated with a specified attribute. |
| [IWDTFTarget2::GetValueBool](nf-wdtf-iwdtftarget2-getvaluebool.md) | Returns a boolean value from the target that is associated with a specified attribute. |
| [IWDTFTarget2::GetValueLongNumber](nf-wdtf-iwdtftarget2-getvaluelongnumber.md) | Returns a long number value from the target that is associated with a specified attribute. |
| [IWDTFTarget2::GetValueLongNumbers](nf-wdtf-iwdtftarget2-getvaluelongnumbers.md) | Returns a collection of long number values from the target that are associated with a specified attribute. |
| [IWDTFTarget2::GetValueNumber](nf-wdtf-iwdtftarget2-getvaluenumber.md) | Returns a number value from the target that is associated with a specified attribute. |
| [IWDTFTarget2::GetValueNumbers](nf-wdtf-iwdtftarget2-getvaluenumbers.md) | Returns a collection of number values from the target that are associated with a specified attribute. |
| [IWDTFTarget2::GetValueString](nf-wdtf-iwdtftarget2-getvaluestring.md) | Returns a string value from the target that is associated with a specified attribute. |
| [IWDTFTarget2::GetValueStrings](nf-wdtf-iwdtftarget2-getvaluestrings.md) | Returns a collection of string values from the target that are associated with a specified attribute. |
| [IWDTFTarget2::HasContext](nf-wdtf-iwdtftarget2-hascontext.md) | Determines whether a given context exists for the target. |
| [IWDTFTarget2::HasInterface](nf-wdtf-iwdtftarget2-hasinterface.md) | Determines whether the target supports a given interface. |
| [IWDTFTarget2::put_Context](nf-wdtf-iwdtftarget2-put_context.md) | Gets and sets a name-value pair that represents user data for the target. |

## Remarks
The <b>IWDTFTarget2</b> interface abstracts the notion of a testable item, 
which is the central focus of the WDTF object model.
You can retrieve instances of the <b>IWDTFTarget2</b> interface only 
through other interfaces (such as the 
<a href="..\wdtf\nn-wdtf-iwdtfdevicedepot2.md">IWDTFDeviceDepot2</a> interface or
the <a href="..\wdtf\nn-wdtf-iwdtfsystemdepot2.md">IWDTFSystemDepot2</a> interface). 

The lifetime of a target is tied to its creator; that is, if you retrieve a target 
from the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406304">DeviceDepot</a> property, 
the target will exist as long as the <b>DeviceDepot</b> 
property exists.

You cannot copy an instance of the <b>IWDTFTarget2</b> interface. 
Even if you add a target to a collection, you really just add a reference to the same instance.

<b>Implementation Details</b>

ProgID: (Use the <a href="https://msdn.microsoft.com/3034f790-471f-46c2-915a-15074ae72960">IWDTF</a> 
aggregation interface to instantiate)

TraceLevel Path: HKCR\WDTF.Target.1\

<div class="alert"><b>Note</b>  The implementation of this interface is not thread-safe.</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtf.h |