---
UID: NC.dbgeng.PDEBUG_EXTENSION_CALL
title: PDEBUG_EXTENSION_CALL
author: windows-driver-content
description: Callback functions of the type PDEBUG_EXTENSION_CALL are called by the engine to execute extension commands. You can give these functions any name you want, as long as it contains no uppercase letters.
old-location: debugger\pdebug_extension_call.htm
ms.assetid: 325af2f4-9fb7-4fb3-9294-cd6d20d803c6
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PDEBUG_EXTENSION_CALL
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
ms.keywords: DOT4_ACTIVITY, DOT4_ACTIVITY, *PDOT4_ACTIVITY
req.iface: 
---

# PDEBUG_EXTENSION_CALL callback



## -description
<p>Callback functions of the type <b>PDEBUG_EXTENSION_CALL</b> are called by the engine to execute <a href="debugger.anatomy_of_a_dbgeng_extension_dll#extension_commands#extension_commands">extension commands</a>. You can give these functions any name you want, as long as it contains no uppercase letters.</p>


## -prototype

````
typedef HRESULT ( CALLBACK *PDEBUG_EXTENSION_CALL)(
  _In_     PDEBUG_CLIENT Client,
  _In_opt_ PCSTR         Args
);
````


## -parameters
<dl>

### -param <i>Client</i> [in]

<dd>
<p>Specifies an interface pointer to the client.  This can be used to interact with the engine.  Typically, this is the client through which the extension command was issued.</p>
</dd>

### -param <i>Args</i> [in, optional]

<dd>
<p>Specifies the arguments passed to the extension command.  In particular, if the extension command was called from a command line, <i>Args</i> contains the rest of the command line.  It can be <b>NULL</b> or empty.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The function was successful.</p><dl>
<dt><b>DEBUG_EXTENSION_CONTINUE_SEARCH</b></dt>
</dl><p>Indicates that the function cannot handle the command, or that other implementations of the same command in other extension DLLs should also run.  The engine should continue searching other extension DLLs for another function to handle the command. For example, this can be used to have all help functions run if each one returns CONTINUE_SEARCH.</p>

<p> </p>

<p>All other return values are ignored by the engine.</p>

## -remarks
<p>The name of the function becomes the name of the extension command.  When executing an extension command, the engine searches through each of the loaded extension DLLs in turn, looking for an exported function that has the same name as the command.  For example, when executing the command <b>!stack</b>, the engine will look for an exported function named <b>stack</b> in each loaded extension DLL. For information about the order in which extension DLLs are searched, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560098">Using Debugger Extension Commands</a>.</p>

<p>The extension function should use the client that was passed to it in <i>Client</i> for all interaction with the engine, unless it has a specific reason to use another client.  The extension function should not maintain the pointer to the client object after it has finished.</p>

<p>The name of the function becomes the name of the extension command.  When executing an extension command, the engine searches through each of the loaded extension DLLs in turn, looking for an exported function that has the same name as the command.  For example, when executing the command <b>!stack</b>, the engine will look for an exported function named <b>stack</b> in each loaded extension DLL. For information about the order in which extension DLLs are searched, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560098">Using Debugger Extension Commands</a>.</p>

<p>The extension function should use the client that was passed to it in <i>Client</i> for all interaction with the engine, unless it has a specific reason to use another client.  The extension function should not maintain the pointer to the client object after it has finished.</p>

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
<dt>Dbgeng.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549827">IDebugClient</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20PDEBUG_EXTENSION_CALL function pointer%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
