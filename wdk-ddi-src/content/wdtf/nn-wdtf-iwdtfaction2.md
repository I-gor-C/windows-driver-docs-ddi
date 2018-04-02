---
UID: NN:wdtf.IWDTFAction2
title: IWDTFAction2
author: windows-driver-content
description: Defines operations and properties that can control an instance of the IWDTFTarget2 interface.
old-location: dtf\iwdtfaction2.htm
old-project: dtf
ms.assetid: 0ca56301-9e46-4082-a5a4-41a9c655fbd8
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFAction2, IWDTFAction2 interface [Windows Device Testing Framework], IWDTFAction2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFAction2, dtf.iwdtfaction2, wdtf/IWDTFAction2
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
-	IWDTFAction2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFAction2 interface

Defines operations and properties that can control an instance of the 
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439367">IWDTFTarget2</a> interface.

## Methods

<p>The <b>IWDTFAction2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFAction2::DisableObjectErrorLogging](nf-wdtf-iwdtfaction2-disableobjecterrorlogging.md) | Disables object error logging for the action. |
| [IWDTFAction2::DisableObjectLogging](nf-wdtf-iwdtfaction2-disableobjectlogging.md) | Disables object logging for the action. |
| [IWDTFAction2::EnableObjectErrorLogging](nf-wdtf-iwdtfaction2-enableobjecterrorlogging.md) | Enables object error logging for the action. |
| [IWDTFAction2::EnableObjectLogging](nf-wdtf-iwdtfaction2-enableobjectlogging.md) | Enables object logging for the action. |
| [IWDTFAction2::get_Target](nf-wdtf-iwdtfaction2-get_target.md) | Gets the target to which this action refers. |
| [IWDTFAction2::GetStatus](nf-wdtf-iwdtfaction2-getstatus.md) | Returns the status code for the last operation. |
| [IWDTFAction2::GetStatusString](nf-wdtf-iwdtfaction2-getstatusstring.md) | Returns the status for the last operation as a string. |
| [IWDTFAction2::IsStatusSuccess](nf-wdtf-iwdtfaction2-isstatussuccess.md) | Gets a value that indicates whether the last operation was successful. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtf.h |