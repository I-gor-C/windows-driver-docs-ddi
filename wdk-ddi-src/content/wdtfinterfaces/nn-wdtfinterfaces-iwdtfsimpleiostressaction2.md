---
UID: NN:wdtfinterfaces.IWDTFSimpleIOStressAction2
title: IWDTFSimpleIOStressAction2
author: windows-driver-content
description: Defines operations for a simple asynchronous I/O functionality test.
old-location: dtf\iwdtfsimpleiostressaction2.htm
old-project: dtf
ms.assetid: dc594873-2347-4ad8-9748-2d5a1fa4d8a7
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFSimpleIOStressAction2, IWDTFSimpleIOStressAction2 interface [Windows Device Testing Framework], IWDTFSimpleIOStressAction2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFSimpleIOStressAction2, dtf.iwdtfsimpleiostressaction2, wdtfinterfaces/IWDTFSimpleIOStressAction2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfinterfaces.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFInterfaces.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFInterfaces.Interop.dll
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
-	WDTFInterfaces.Interop.dll
api_name:
-	IWDTFSimpleIOStressAction2
product:
- Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFSimpleIOStressAction2 interface

Defines operations for a simple asynchronous I/O functionality test.

## Methods

<p>The <b>IWDTFSimpleIOStressAction2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFSimpleIOStressAction2::Continue](nf-wdtfinterfaces-iwdtfsimpleiostressaction2-continue.md) | Continues the I/O. |
| [IWDTFSimpleIOStressAction2::ContinueAsync](nf-wdtfinterfaces-iwdtfsimpleiostressaction2-continueasync.md) | Asynchronously signals the I/O to continue. |
| [IWDTFSimpleIOStressAction2::Pause](nf-wdtfinterfaces-iwdtfsimpleiostressaction2-pause.md) | Pauses the I/O. |
| [IWDTFSimpleIOStressAction2::Start](nf-wdtfinterfaces-iwdtfsimpleiostressaction2-start.md) | Opens the device. |
| [IWDTFSimpleIOStressAction2::StartAsync](nf-wdtfinterfaces-iwdtfsimpleiostressaction2-startasync.md) | Asynchronously signals a start event to occur. |
| [IWDTFSimpleIOStressAction2::Stop](nf-wdtfinterfaces-iwdtfsimpleiostressaction2-stop.md) | Stops the device. |
| [IWDTFSimpleIOStressAction2::StopAsync](nf-wdtfinterfaces-iwdtfsimpleiostressaction2-stopasync.md) | Asynchronously signals the stop event to occur. |
| [IWDTFSimpleIOStressAction2::WaitAsyncCompletion](nf-wdtfinterfaces-iwdtfsimpleiostressaction2-waitasynccompletion.md) | Waits for the completion of any of the asynchronous events. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtfinterfaces.h |