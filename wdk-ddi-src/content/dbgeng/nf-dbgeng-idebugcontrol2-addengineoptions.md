---
UID: NF.dbgeng.IDebugControl2.AddEngineOptions
title: IDebugControl2::AddEngineOptions
author: windows-driver-content
description: The AddEngineOptions method turns on some of the debugger engine's options.
old-location: debugger\addengineoptions.htm
old-project: debugger
ms.assetid: 088036f5-13cb-47ba-953c-a71c923f028e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl2, AddEngineOptions, IDebugControl2::AddEngineOptions
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
req.alt-api: IDebugControl.AddEngineOptions,IDebugControl2.AddEngineOptions,IDebugControl3.AddEngineOptions
req.alt-loc: Dbgeng.h
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

# IDebugControl2::AddEngineOptions method



## -description
<p>The <b>AddEngineOptions</b> method turns on some of the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>'s options.</p>


## -syntax

````
HRESULT AddEngineOptions(
  [in] ULONG Options
);
````


## -parameters
<dl>

### -param <i>Options</i> [in]

<dd>
<p>Specifies engine options to turn on.  <i>Options</i> is a bit-set that will be combined with the existing engine options using the bitwise-OR operator.  For a description of the engine options, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541475">DEBUG_ENGOPT_XXX</a>.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p>

## -remarks
<p>After the engine options have been changed, the engine sends out notification to each client's <a href="debugger.e#event_callback_objects#event_callback_objects">event callback object</a> by passing the DEBUG_CES_ENGINE_OPTIONS flag to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550683">IDebugEventCallbacks::ChangeEngineState</a> method.</p>

<p>After the engine options have been changed, the engine sends out notification to each client's <a href="debugger.e#event_callback_objects#event_callback_objects">event callback object</a> by passing the DEBUG_CES_ENGINE_OPTIONS flag to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550683">IDebugEventCallbacks::ChangeEngineState</a> method.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546598">GetEngineOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554491">RemoveEngineOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556670">SetEngineOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::AddEngineOptions method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
