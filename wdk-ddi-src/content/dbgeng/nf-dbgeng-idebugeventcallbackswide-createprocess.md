---
UID: NF.dbgeng.IDebugEventCallbacksWide.CreateProcess
title: IDebugEventCallbacksWide::CreateProcess
author: windows-driver-content
description: The CreateProcess callback method is called by the engine when a create-processdebugging event occurs in the target.
old-location: debugger\idebugeventcallbackswide_createprocess.htm
old-project: debugger
ms.assetid: d5378b35-da27-419f-a161-0c542aa4a9f9
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugEventCallbacksWide, CreateProcess, IDebugEventCallbacksWide::CreateProcess
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
req.alt-api: IDebugEventCallbacksWide.CreateProcess
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

# IDebugEventCallbacksWide::CreateProcess method



## -description
<p>The <b>CreateProcess</b> callback method is called by the engine when a create-processdebugging event occurs in the target.</p>


## -syntax

````
HRESULT CreateProcess(
  [in]           ULONG64 ImageFileHandle,
  [in]           ULONG64 Handle,
  [in]           ULONG64 BaseOffset,
  [in]           ULONG   ModuleSize,
  [in, optional] PCWSTR  ModuleName,
  [in, optional] PCWSTR  ImageName,
  [in]           ULONG   CheckSum,
  [in]           ULONG   TimeDateStamp,
  [in]           ULONG64 InitialThreadHandle,
  [in]           ULONG64 ThreadDataOffset,
  [in]           ULONG64 StartOffset
);
````


## -parameters
<dl>

### -param <i>ImageFileHandle</i> [in]

<dd>
<p>Specifies the handle to the process's image file.    If this information is not available, <i>ImageFileHandle</i> will be <b>NULL</b>.  </p>
</dd>

### -param <i>Handle</i> [in]

<dd>
<p>Specifies the handle to the process.  This parameter corresponds to the <b>hProcess</b> field in the CREATE_PROCESS_DEBUG_INFO structure.  If this information is not available, <i>ImageFileHandle</i> will be <b>NULL</b>.  </p>
</dd>

### -param <i>BaseOffset</i> [in]

<dd>
<p>Specifies the base address of the process's executable image in the target's memory address space.  If this information is not available, <i>BaseOffset</i> will be <b>NULL</b>.</p>
</dd>

### -param <i>ModuleSize</i> [in]

<dd>
<p>Specifies the process's executable image size in bytes.  If this information is not available, <i>ModuleSize</i> will be zero.</p>
</dd>

### -param <i>ModuleName</i> [in, optional]

<dd>
<p>Specifies the simplified module name that is used by the debugger engine.  In most cases, this matches the image file name excluding the extension. If this information is not available, <i>ModuleName</i> will be <b>NULL</b>.</p>
</dd>

### -param <i>ImageName</i> [in, optional]

<dd>
<p>Specifies the process's executable-image file name, which can include the path.   If this information is not available, <i>ImageName</i> will be <b>NULL</b>.</p>
</dd>

### -param <i>CheckSum</i> [in]

<dd>
<p>Specifies the checksum of the process's executable image.  If this information is not available, <i>CheckSum</i> will be zero.</p>
</dd>

### -param <i>TimeDateStamp</i> [in]

<dd>
<p>Specifies the time and date stamp of the process's executable-image file.  If this information is not available, <i>TimeDateStamp</i> will be zero.</p>
</dd>

### -param <i>InitialThreadHandle</i> [in]

<dd>
<p>Specifies the handle to the process's initial thread.  This parameter corresponds to the <b>hThread</b> field in the CREATE_PROCESS_DEBUG_INFO structure.  If this information is not available, <i>InitialThreadHandle</i> will be <b>NULL</b>. </p>
</dd>

### -param <i>ThreadDataOffset</i> [in]

<dd>
<p>Specifies a block of data that the operating system maintains for this thread.  The actual data in the block is operating system-specific.  If this information is not available, <i>ThreadDataOffset</i> will be <b>NULL</b>. </p>
</dd>

### -param <i>StartOffset</i> [in]

<dd>
<p>Specifies the starting address of the thread in the process's virtual address space.    If this information is not available, <i>StartOffset</i> will be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>This method returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541651">DEBUG_STATUS_XXX</a> value, which indicates how the execution of the target should proceed after the engine processes this event.  For details on how the engine treats this value, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.</p>

## -remarks
<p>This method is only called by the engine if the DEBUG_EVENT_CREATE_PROCESS flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550625">IDebugEventCallbacksWide::GetInterestMask</a>.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.  For information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

<p>This method is only called by the engine if the DEBUG_EVENT_CREATE_PROCESS flag is set in the mask returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550625">IDebugEventCallbacksWide::GetInterestMask</a>.</p>

<p>For more information about handling events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552239">Monitoring Events</a>.  For information about threads, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>.</p>

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