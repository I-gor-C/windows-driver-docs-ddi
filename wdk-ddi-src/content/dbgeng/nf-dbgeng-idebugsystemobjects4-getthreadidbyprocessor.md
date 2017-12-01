---
UID: NF.dbgeng.IDebugSystemObjects4.GetThreadIdByProcessor
title: IDebugSystemObjects4::GetThreadIdByProcessor
author: windows-driver-content
description: The GetThreadIdByProcessor method returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor.
old-location: debugger\getthreadidbyprocessor.htm
old-project: debugger
ms.assetid: c771a581-53ac-44a7-b307-b8a22ac97496
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects4, GetThreadIdByProcessor, IDebugSystemObjects4::GetThreadIdByProcessor
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
req.alt-api: IDebugSystemObjects.GetThreadIdByProcessor,IDebugSystemObjects2.GetThreadIdByProcessor,IDebugSystemObjects3.GetThreadIdByProcessor,IDebugSystemObjects4.GetThreadIdByProcessor
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

# IDebugSystemObjects4::GetThreadIdByProcessor method



## -description
<p>The <b>GetThreadIdByProcessor</b> method returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor.</p>


## -syntax

````
HRESULT GetThreadIdByProcessor(
  [in]  ULONG  Processor,
  [out] PULONG Id
);
````


## -parameters
<dl>

### -param <i>Processor</i> [in]

<dd>
<p>Specifies the processor corresponding to the desired thread.</p>
</dd>

### -param <i>Id</i> [out]

<dd>
<p>Receives the engine thread ID.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>This method is only available in kernel-mode debugging.</p>

<p>For more information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

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