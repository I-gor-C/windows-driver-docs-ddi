---
UID: NN:wdtf.IWDTFCONFIG2
title: IWDTFCONFIG2
author: windows-driver-content
description: Defines operations that control WDTF objects within a test script.
old-location: dtf\iwdtfconfig2.htm
old-project: dtf
ms.assetid: 7cc3775e-d116-4852-9b1a-606d909d878b
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFCONFIG2, IWDTFCONFIG2 interface [Windows Device Testing Framework], IWDTFCONFIG2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFCONFIG2, dtf.iwdtfconfig2, wdtf/IWDTFCONFIG2
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
-	IWDTFCONFIG2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFCONFIG2 interface

Defines operations that control <b>WDTF</b> objects within a test script.

## Methods

<p>The <b>IWDTFCONFIG2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFCONFIG2::DisableObjectErrorLogging](nf-wdtf-iwdtfconfig2-disableobjecterrorlogging.md) | Disables object error logging for all objects. |
| [IWDTFCONFIG2::DisableObjectLogging](nf-wdtf-iwdtfconfig2-disableobjectlogging.md) | Disables object logging for all objects. |
| [IWDTFCONFIG2::EnableObjectErrorLogging](nf-wdtf-iwdtfconfig2-enableobjecterrorlogging.md) | Enables object error logging for all objects. |
| [IWDTFCONFIG2::EnableObjectLogging](nf-wdtf-iwdtfconfig2-enableobjectlogging.md) | Enables object logging for all objects. |

## Remarks
<b>WDTF</b> object logging defaults to disabled. If object logging is enabled, 
each <b>WDTF</b> object writes to the test scripts log. If object logging is enabled, 
object error logging is enabled by default.

The following example shows the logging output for a call to 
<b>DeviceDepot.Query("Volume::")</b> when logging is enabled for an example system.

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>
[ Ouput ]

WDTF_TARGETS    : INFO  :  - Query("Volume::")
WDTF_TARGETS    : INFO  :          Target: Generic volume
WDTF_TARGETS    : INFO  :          Target: Generic volume
WDTF_TARGETS    : INFO  :          Target: HL-DT-ST RW/DVD MU10N ATA Device
WDTF_TARGETS    : INFO  :          Target: Generic volume
WDTF_TARGETS    : INFO  :          Target: Generic volume
WDTF_TARGETS    : INFO  :          Target: Generic volume
</pre>
</td>
</tr>
</table></span></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtf.h |