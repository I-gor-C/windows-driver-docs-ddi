---
UID: NF.dbgeng.IDebugEventCallbacks.LoadModule
title: IDebugEventCallbacks::LoadModule
author: windows-driver-content
description: The LoadModule callback method is called by the engine when a module-load debugging event occurs in the target.
old-location: debugger\idebugeventcallbacks_loadmodule.htm
old-project: debugger
ms.assetid: f4efcbf3-f78a-4e0e-9741-4f9b68814e5b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugEventCallbacks, LoadModule, IDebugEventCallbacks::LoadModule
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
req.alt-api: IDebugEventCallbacks.LoadModule
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
req.iface: IDebugEventCallbacks
---

# IDebugEventCallbacks::LoadModule method



## -description
<p>The <b>LoadModule</b> callback method is called by the engine when a module-load debugging event occurs in the target.</p>


## -syntax

````
HRESULT LoadModule(
  [in]           ULONG64 ImageFileHandle,
  [in]           ULONG64 BaseOffset,
  [in]           ULONG   ModuleSize,
  [in, optional] PCSTR   ModuleName,
  [in, optional] PCSTR   ImageName,
  [in]           ULONG   CheckSum,
  [in]           ULONG   TimeDateStamp
);
````


## -parameters
<dl>

### -param <i>ImageFileHandle</i> [in]

<dd>
<p>Specifies the handle to the module's image file.  If this information is not available, <i>ImageFileHandle</i> will be <b>NULL</b>. </p>
</dd>

### -param <i>BaseOffset</i> [in]

<dd>
<p>Specifies the base address of the module in the target's memory address space.  If this information is not available, <i>BaseOffset</i> will be <b>NULL</b>.</p>
</dd>

### -param <i>ModuleSize</i> [in]

<dd>
<p>Specifies the module's image size in bytes.  If this information is not available, <i>ModuleSize</i> will be <b>NULL</b>.</p>
</dd>

### -param <i>ModuleName</i> [in, optional]

<dd>
<p>Specifies the simplified module name that is used by the debugger engine.  In most cases, this matches the image file name excluding the extension.  If this information is not available, <i>ModuleName</i> will be <b>NULL</b>.</p>
</dd>

### -param <i>ImageName</i> [in, optional]

<dd>
<p>Specifies the module's image file name, which can include the path.  If this information is not available, <i>ImageName</i> will be <b>NULL</b>.</p>
</dd>

### -param <i>CheckSum</i> [in]

<dd>
<p>Specifies the checksum of the module's image file.  If this information is not available, <i>CheckSum</i> will be <b>NULL</b>.</p>
</dd>

### -param <i>TimeDateStamp</i> [in]

<dd>
<p>Specifies the time and date stamp of the module's image file.  If this information is not available, <i>TimeDateStamp</i> will be zero.</p>
</dd>
</dl>

## -returns
<p>This method returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541651">DEBUG_STATUS_XXX</a> value, which indicates how the execution of the target should proceed after the engine processes this event.  For details on how the engine treats this value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.</p>

## -remarks
<p>This method is only called by the engine if the DEBUG_EVENT_LOAD_MODULE flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550737">IDebugEventCallbacks::GetInterestMask</a>.</p>

<p>After calling this method, the engine will call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550692">IDebugEventCallbacks::ChangeSymbolState</a>, with the <i>Flags</i> parameter containing the bit flag DEBUG_CSS_LOADS.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>. </p>

<p>This method is only called by the engine if the DEBUG_EVENT_LOAD_MODULE flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550737">IDebugEventCallbacks::GetInterestMask</a>.</p>

<p>After calling this method, the engine will call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550692">IDebugEventCallbacks::ChangeSymbolState</a>, with the <i>Flags</i> parameter containing the bit flag DEBUG_CSS_LOADS.</p>

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