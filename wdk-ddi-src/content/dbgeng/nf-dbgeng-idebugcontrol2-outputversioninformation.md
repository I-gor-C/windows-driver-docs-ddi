---
UID: NF.dbgeng.IDebugControl2.OutputVersionInformation
title: IDebugControl2::OutputVersionInformation
author: windows-driver-content
description: The OutputVersionInformation method prints version information about the debugger engine to the debugger console.
old-location: debugger\outputversioninformation.htm
old-project: debugger
ms.assetid: cbf688b4-a174-4ab0-af98-2c0db1b2ab3a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl2, OutputVersionInformation, IDebugControl2::OutputVersionInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.OutputVersionInformation,IDebugControl2.OutputVersionInformation,IDebugControl3.OutputVersionInformation
req.alt-loc: dbgeng.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IDebugControl2
---

# IDebugControl2::OutputVersionInformation method



## -description
<p>The <b>OutputVersionInformation</b> method prints version information about the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> to the debugger console.</p>


## -syntax

````
HRESULT OutputVersionInformation(
  [in] ULONG OutputControl
);
````


## -parameters
<dl>

### -param OutputControl [in]

<dd>
<p>Specifies where to send the output.  For possible values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541517">DEBUG_OUTCTL_XXX</a>.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values, including error values caused by the engine being busy.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The information that is sent to the output can include the mode of the debugger, the path and version of the debugger DLLs, the extension DLL search path, the extension DLL chain, and the version of the operating system that is running on the host computer.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558860">Target Information</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>