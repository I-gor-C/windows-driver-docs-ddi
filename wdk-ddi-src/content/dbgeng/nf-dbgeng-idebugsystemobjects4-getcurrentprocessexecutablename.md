---
UID: NF.dbgeng.IDebugSystemObjects4.GetCurrentProcessExecutableName
title: IDebugSystemObjects4::GetCurrentProcessExecutableName
author: windows-driver-content
description: The GetCurrentProcessExecutableName method returns the name of executable file loaded in the current process.
old-location: debugger\getcurrentprocessexecutablename.htm
old-project: debugger
ms.assetid: ea968316-a53d-4ab1-966a-5c699ffb8f2a
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects4, GetCurrentProcessExecutableName, IDebugSystemObjects4::GetCurrentProcessExecutableName
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
req.alt-api: IDebugSystemObjects.GetCurrentProcessExecutableName,IDebugSystemObjects2.GetCurrentProcessExecutableName,IDebugSystemObjects3.GetCurrentProcessExecutableName,IDebugSystemObjects4.GetCurrentProcessExecutableName
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
req.iface: IDebugSystemObjects4
---

# IDebugSystemObjects4::GetCurrentProcessExecutableName method



## -description
<p>The <b>GetCurrentProcessExecutableName</b>  method returns the name of executable file loaded in the current process.</p>


## -syntax

````
HRESULT GetCurrentProcessExecutableName(
  [out, optional] PSTR   Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG ExeSize
);
````


## -parameters
<dl>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the name of the executable file.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in characters of the buffer <i>Buffer</i>.</p>
</dd>

### -param <i>ExeSize</i> [out, optional]

<dd>
<p>Receives the size in characters of the name of the executable file.  If <i>ExeSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, the buffer was not large enough to hold the name of the executable file and it was truncated.</p>

<p> </p>

## -remarks
<p>These methods are only available in user-mode debugging.</p>

<p>If the engine cannot determine the name of the executable file, it writes the string "?NoImage?" to the buffer.</p>

<p>For more information about processes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

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