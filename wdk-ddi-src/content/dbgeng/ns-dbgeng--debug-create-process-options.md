---
UID: NS.dbgeng._DEBUG_CREATE_PROCESS_OPTIONS
title: DEBUG_CREATE_PROCESS_OPTIONS
author: windows-driver-content
description: The DEBUG_CREATE_PROCESS_OPTIONS structure specifies the process creation options to use when creating a new process.
old-location: debugger\debug_create_process_options.htm
old-project: debugger
ms.assetid: b4b279c2-d44a-442d-9f1d-0ac0d2304eb8
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DEBUG_CREATE_PROCESS_OPTIONS, DEBUG_CREATE_PROCESS_OPTIONS, *PDEBUG_CREATE_PROCESS_OPTIONS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_CREATE_PROCESS_OPTIONS
req.alt-loc: DbgEng.h
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

# DEBUG_CREATE_PROCESS_OPTIONS structure



## -description
<p>The DEBUG_CREATE_PROCESS_OPTIONS structure specifies the process creation options to use when creating a new process.</p>


## -syntax

````
typedef struct _DEBUG_CREATE_PROCESS_OPTIONS {
  ULONG CreateFlags;
  ULONG EngCreateFlags;
  ULONG VerifierFlags;
  ULONG Reserved;
} DEBUG_CREATE_PROCESS_OPTIONS, *PDEBUG_CREATE_PROCESS_OPTIONS;
````


## -struct-fields
<dl>

### -field <b>CreateFlags</b>

<dd>
<p>The flags to use when creating the process.   In addition to the flags described in the "Process Creation Flags" topic in the Platform SDK documentation, the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> uses the following flags when creating a process.</p>
<table>
<tr>
<th>Values</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_CREATE_PROCESS_NO_DEBUG_HEAP</p>
</td>
<td>
<p>(Microsoft Windows Server 2003 and later)  Prevents the debug heap from being used in the new process.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CREATE_PROCESS_THROUGH_RTL</p>
</td>
<td>
<p>The native NT RTL process creation routines should be used instead of Win32.  This is only meaningful for special processes that run as NT native processes. No Win32 process can be created with this flag.</p>
</td>
</tr>
</table>
<p> </p>
<p>When creating and attaching to a process through the debugger engine, set one of the Platform SDK's process creation flags: DEBUG_PROCESS or DEBUG_ONLY_THIS_PROCESS.</p>
</dd>

### -field <b>EngCreateFlags</b>

<dd>
<p>The engine specific flags used when creating the process.  <b>EngCreateFlags</b> is a combination of the following bit-flags:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_ECREATE_PROCESS_INHERIT_HANDLES</p>
</td>
<td>
<p>The new process will inherit system handles from the debugger or process server.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_ECREATE_PROCESS_USE_VERIFIER_FLAGS</p>
</td>
<td>
<p>(Windows Vista and later)  Use Application Verifier flags in the <b>VerifierFlags</b> field.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_ECREATE_PROCESS_USE_IMPLICIT_COMMAND_LINE</p>
</td>
<td>
<p>Use the debugger's or process server's implicit command line to start the process instead of a supplied command line.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>VerifierFlags</b>

<dd>
<p>The Application Verifier flags.  Only used if DEBUG_ECREATE_PROCESS_USE_VERIFIER_FLAGS is set in the <b>EngCreateFlags</b> field.  For possible values, see the <a href="NULL">Application Verifier</a> documentation. </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Set to zero.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>DbgEng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>