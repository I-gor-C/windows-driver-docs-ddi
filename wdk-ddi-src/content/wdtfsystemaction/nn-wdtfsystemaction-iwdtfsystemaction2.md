---
UID: NN:wdtfsystemaction.IWDTFSystemAction2
title: IWDTFSystemAction2
author: windows-driver-content
description: Defines operations and properties that support driver testing.
old-location: dtf\iwdtfsystemaction2.htm
old-project: dtf
ms.assetid: 783ddaaa-f39f-4e66-85aa-4788bf7959a6
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFSystemAction2, IWDTFSystemAction2 interface [Windows Device Testing Framework], IWDTFSystemAction2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFSystemAction2, dtf.iwdtfsystemaction2, wdtfsystemaction/IWDTFSystemAction2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfsystemaction.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFSystemAction.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFSystemAction.Interop.dll
req.type-library: 
req.lib: wdtfsystemaction.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WDTFSystemAction.Interop.dll
api_name:
-	IWDTFSystemAction2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFSystemAction2 interface

Defines operations and properties that support driver testing.

## Methods

<p>The <b>IWDTFSystemAction2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFSystemAction2::ConnectedStandby](nf-wdtfsystemaction-iwdtfsystemaction2-connectedstandby.md) | Puts the system into Connected Standby state and exits Connected Standby state after the desired time has passed. This method only works on a computer that supports Always On Always Connected (AOAC). |
| [IWDTFSystemAction2::get_Critical](nf-wdtfsystemaction-iwdtfsystemaction2-get_critical.md) | Gets or sets a value that indicates whether the the system power state is critical. |
| [IWDTFSystemAction2::get_IsRestarted](nf-wdtfsystemaction-iwdtfsystemaction2-get_isrestarted.md) | Gets a value that indicates whether the test script restarted as a result of a call to RebootRestart or RebootRestartWithContext. |
| [IWDTFSystemAction2::get_SleepWakeTimeInSeconds](nf-wdtfsystemaction-iwdtfsystemaction2-get_sleepwaketimeinseconds.md) | Gets or sets the time in seconds when the system will wake from the sleep state. |
| [IWDTFSystemAction2::GetFirstSleepState](nf-wdtfsystemaction-iwdtfsystemaction2-getfirstsleepstate.md) | Returns the first supported sleep state. |
| [IWDTFSystemAction2::GetNextSleepState](nf-wdtfsystemaction-iwdtfsystemaction2-getnextsleepstate.md) | Returns the next supported sleep state. |
| [IWDTFSystemAction2::IsRestartedWithContext](nf-wdtfsystemaction-iwdtfsystemaction2-isrestartedwithcontext.md) | Gets a value that indicates whether the test script was restarted for a specific context. |
| [IWDTFSystemAction2::PowerAnalyzeTraceByFile](nf-wdtfsystemaction-iwdtfsystemaction2-poweranalyzetracebyfile.md) | Analyzes a power trace session that has already been collected and stored in the associated trace message (.etl) log file. This method will only work on Windows 8 and above. |
| [IWDTFSystemAction2::PowerTracingEnd](nf-wdtfsystemaction-iwdtfsystemaction2-powertracingend.md) | This method ends a power trace session. |
| [IWDTFSystemAction2::PowerTracingStart](nf-wdtfsystemaction-iwdtfsystemaction2-powertracingstart.md) | Starts a trace session for power state transitions and saves the trace message file (Wdtfpwr.etl) in the current working directory. This method is available starting with Windows 8. |
| [IWDTFSystemAction2::PowerTracingStartByFile](nf-wdtfsystemaction-iwdtfsystemaction2-powertracingstartbyfile.md) | Starts a trace session for power state transitions and saves the trace message file (.etl) using the specified path. This method is available starting with Windows 8. |
| [IWDTFSystemAction2::put_Critical](nf-wdtfsystemaction-iwdtfsystemaction2-put_critical.md) | Gets or sets a value that indicates whether the the system power state is critical. |
| [IWDTFSystemAction2::put_SleepWakeTimeInSeconds](nf-wdtfsystemaction-iwdtfsystemaction2-put_sleepwaketimeinseconds.md) | Gets or sets the time in seconds when the system will wake from the sleep state. |
| [IWDTFSystemAction2::RebootRestart](nf-wdtfsystemaction-iwdtfsystemaction2-rebootrestart.md) | Restart the system and the current test. |
| [IWDTFSystemAction2::RebootRestartWithContext](nf-wdtfsystemaction-iwdtfsystemaction2-rebootrestartwithcontext.md) | Reboots the system and restarts the test script with context data. |
| [IWDTFSystemAction2::Sleep](nf-wdtfsystemaction-iwdtfsystemaction2-sleep.md) | Puts the system into the desired sleep state. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtfsystemaction.h |