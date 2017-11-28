---
UID: NF.wdbgexts.SetThreadForOperation
title: SetThreadForOperation
author: windows-driver-content
description: The SetThreadForOperation function sets the thread to use for the next StackTrace call.
old-location: debugger\setthreadforoperation.htm
old-project: debugger
ms.assetid: b5bae644-6c8d-4346-87bd-211efcf27748
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SetThreadForOperation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetThreadForOperation
req.alt-loc: wdbgexts.h
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
req.iface: 
req.product: Windows 10 or later.
---

# SetThreadForOperation function



## -description
<p>The <b>SetThreadForOperation</b> function sets the thread to use for the next <a href="https://msdn.microsoft.com/library/windows/hardware/ff558794">StackTrace</a> call.</p>


## -syntax

````
__inline VOID SetThreadForOperation(
   ULONG_PTR *Thread
);
````


## -parameters
<dl>

### -param <i>Thread</i> 

<dd>
<p>Points to a thread object to be used for the next stack trace.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If you are writing 64-bit code, you should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff556832">SetThreadForOperation64</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.</p>

<p>For a WdbgExts extension, include Wdbgexts.h. For a DbgEng extension, include Wdbgexts.h before Dbgeng.h. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details.</p>

<p>If you are writing 64-bit code, you should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff556832">SetThreadForOperation64</a> instead. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff537780">32-Bit Pointers and 64-Bit Pointers</a> for details.</p>

<p>For a WdbgExts extension, include Wdbgexts.h. For a DbgEng extension, include Wdbgexts.h before Dbgeng.h. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details.</p>

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
<dt>Wdbgexts.h (include Wdbgexts.h, Wdbgexts.h, or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>