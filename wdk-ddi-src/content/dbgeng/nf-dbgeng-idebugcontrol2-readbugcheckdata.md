---
UID: NF.dbgeng.IDebugControl2.ReadBugCheckData
title: IDebugControl2::ReadBugCheckData
author: windows-driver-content
description: The ReadBugCheckData method reads the kernel bug check code and related parameters.
old-location: debugger\readbugcheckdata.htm
old-project: debugger
ms.assetid: 3ede32f5-9671-4f38-a33f-96536300267b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl2, ReadBugCheckData, IDebugControl2::ReadBugCheckData
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
req.alt-api: IDebugControl.ReadBugCheckData,IDebugControl2.ReadBugCheckData,IDebugControl3.ReadBugCheckData
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

# IDebugControl2::ReadBugCheckData method



## -description
<p>The <b>ReadBugCheckData</b> method reads the kernel bug check code and related parameters.</p>


## -syntax

````
HRESULT ReadBugCheckData(
  [out] PULONG   Code,
  [out] PULONG64 Arg1,
  [out] PULONG64 Arg2,
  [out] PULONG64 Arg3,
  [out] PULONG64 Arg4
);
````


## -parameters
<dl>

### -param <i>Code</i> [out]

<dd>
<p>Receives the bug check code.</p>
</dd>

### -param <i>Arg1</i> [out]

<dd>
<p>Receives the first parameter associated with the bug check.  The interpretation of this parameter depends on the bug check code.</p>
</dd>

### -param <i>Arg2</i> [out]

<dd>
<p>Receives the second parameter associated with the bug check.  The interpretation of this parameter depends on the bug check code.</p>
</dd>

### -param <i>Arg3</i> [out]

<dd>
<p>Receives the third parameter associated with the bug check.  The interpretation of this parameter depends on the bug check code.</p>
</dd>

### -param <i>Arg4</i> [out]

<dd>
<p>Receives the fourth parameter associated with the bug check.  The interpretation of this parameter depends on the bug check code.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>This method is only available in kernel-mode debugging.</p>

<p>For more information about bug checks, including a list of bug check codes and their interpretations, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh450912">Bug Checks (Blue Screens)</a>.</p>

<p>This method is only available in kernel-mode debugging.</p>

<p>For more information about bug checks, including a list of bug check codes and their interpretations, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh450912">Bug Checks (Blue Screens)</a>.</p>

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