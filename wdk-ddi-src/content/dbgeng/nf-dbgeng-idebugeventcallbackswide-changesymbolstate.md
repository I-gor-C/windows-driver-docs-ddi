---
UID: NF.dbgeng.IDebugEventCallbacksWide.ChangeSymbolState
title: IDebugEventCallbacksWide::ChangeSymbolState
author: windows-driver-content
description: The ChangeSymbolState callback method is called by the engine when the symbol state changes.
old-location: debugger\idebugeventcallbackswide_changesymbolstate.htm
old-project: debugger
ms.assetid: ea331612-5c48-4320-a658-101c3d93e7be
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugEventCallbacksWide, ChangeSymbolState, IDebugEventCallbacksWide::ChangeSymbolState
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
req.alt-api: IDebugEventCallbacksWide.ChangeSymbolState
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
req.iface: IDebugEventCallbacksWide
---

# IDebugEventCallbacksWide::ChangeSymbolState method



## -description
<p>The <b>ChangeSymbolState</b> callback method is called by the engine when the symbol state changes. </p>


## -syntax

````
HRESULT ChangeSymbolState(
  [in] ULONG   Flags,
  [in] ULONG64 Argument
);
````


## -parameters
<dl>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies a bit-set indicating the nature of the change to the symbol state.  The following bit flags might be set.</p>
<table>
<tr>
<th>Value</th>
<th>Description </th>
</tr>
<tr>
<td>
<p>DEBUG_CSS_LOADS</p>
</td>
<td>
<p>The engine has loaded some module symbols.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CSS_UNLOADS</p>
</td>
<td>
<p>The engine has unloaded some module symbols.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CSS_SCOPE</p>
</td>
<td>
<p>The current symbol scope has changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CSS_PATHS</p>
</td>
<td>
<p>The executable image, source , or symbol search paths have changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CSS_SYMBOL_OPTIONS</p>
</td>
<td>
<p>The symbol options have changed.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CSS_TYPE_OPTIONS</p>
</td>
<td>
<p>The type options have changed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Argument</i> [in]

<dd>
<p>Provides additional information about the change to the symbol state.   If more than one bit flag is set in the <i>Flags</i> parameter, the <i>Argument</i> parameter is not used.  Otherwise, the value of <i>Argument</i> depends on the value of <i>Flags</i>:</p>
<p></p>
<dl>

### -param <a id="DEBUG_CSS_LOADS"></a><a id="debug_css_loads"></a>DEBUG_CSS_LOADS

<dd>
<p>The value of <i>Argument</i> is the base location (in the target's memory address space) of the module image that the engine loaded symbols for.</p>
</dd>

### -param <a id="DEBUG_CSS_UNLOADS"></a><a id="debug_css_unloads"></a>DEBUG_CSS_UNLOADS

<dd>
<p>The value of <i>Argument</i> is the base location (in the target's memory address space) of the module image that the engine unloaded symbols for.  If the engine unloaded symbols for more than one image, the value of <i>Argument</i> is zero.</p>
</dd>

### -param <a id="DEBUG_CSS_SCOPE"></a><a id="debug_css_scope"></a>DEBUG_CSS_SCOPE

<dd>
<p>The value of <i>Argument</i> is zero.</p>
</dd>

### -param <a id="DEBUG_CSS_PATHS"></a><a id="debug_css_paths"></a>DEBUG_CSS_PATHS

<dd>
<p>The value of <i>Argument</i> is zero.</p>
</dd>

### -param <a id="DEBUG_CSS_SYMBOL_OPTIONS"></a><a id="debug_css_symbol_options"></a>DEBUG_CSS_SYMBOL_OPTIONS

<dd>
<p>The value of <i>Argument</i> is the symbol options.</p>
</dd>

### -param <a id="DEBUG_CSS_TYPE_OPTIONS"></a><a id="debug_css_type_options"></a>DEBUG_CSS_TYPE_OPTIONS

<dd>
<p>The value of <i>Argument</i> is zero.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>The return value is ignored by the engine unless it indicates a remote procedure call error; in this case the client, with which this <b>IDebugEventCallbacksWide</b> object is registered, is disabled.</p>

## -remarks
<p>This method is only called by the engine if the DEBUG_EVENT_CHANGE_SYMBOL_STATE flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550625">IDebugEventCallbacksWide::GetInterestMask</a>.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>. </p>

<p>This method is only called by the engine if the DEBUG_EVENT_CHANGE_SYMBOL_STATE flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550625">IDebugEventCallbacksWide::GetInterestMask</a>.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>. </p>

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