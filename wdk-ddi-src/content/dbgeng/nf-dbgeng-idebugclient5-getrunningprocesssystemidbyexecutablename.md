---
UID: NF.dbgeng.IDebugClient5.GetRunningProcessSystemIdByExecutableName
title: IDebugClient5::GetRunningProcessSystemIdByExecutableName
author: windows-driver-content
description: The GetRunningProcessSystemIdByExecutableName method searches for a process with a given executable file name and return its process ID.
old-location: debugger\getrunningprocesssystemidbyexecutablename.htm
old-project: debugger
ms.assetid: 67e231b4-c693-4824-b895-b7f3085e6f4e
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient5, GetRunningProcessSystemIdByExecutableName, IDebugClient5::GetRunningProcessSystemIdByExecutableName
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
req.alt-api: IDebugClient.GetRunningProcessSystemIdByExecutableName,IDebugClient2.GetRunningProcessSystemIdByExecutableName,IDebugClient3.GetRunningProcessSystemIdByExecutableName,IDebugClient4.GetRunningProcessSystemIdByExecutableName,IDebugClient5.GetRunningProcessSystemIdByExecutableName
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
req.iface: IDebugClient5
---

# IDebugClient5::GetRunningProcessSystemIdByExecutableName method



## -description
<p>The <b>GetRunningProcessSystemIdByExecutableName</b>  method searches for a process with a given executable file name and return its process ID.</p>


## -syntax

````
HRESULT GetRunningProcessSystemIdByExecutableName(
  [in]  ULONG64 Server,
  [in]  PCSTR   ExeName,
  [in]  ULONG   Flags,
  [out] PULONG  Id
);
````


## -parameters
<dl>

### -param <i>Server</i> [in]

<dd>
<p>Specifies the process server to search for the executable name.  If <i>Server</i> is zero, the engine will search for the executable name among the processes running on the local computer.</p>
</dd>

### -param <i>ExeName</i> [in]

<dd>
<p>Specifies the executable file name for which to search.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies a bit-set that controls how the executable name is matched.  The following flags may be present:</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_GET_PROC_FULL_MATCH</p>
</td>
<td>
<p><i>ExeName</i> specifies the full path name of the executable file name.</p>
<p>If this flag is not set, this method will not use path names when searching for the process.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_GET_PROC_ONLY_MATCH</p>
</td>
<td>
<p>Require that only one process match the executable file name <i>ExeName</i>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Id</i> [out]

<dd>
<p>Receives the process ID of the first process to match <i>ExeName</i>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>More than one process matched the executable file name in <i>ExeName</i>, and DEBUG_GET_PROC_ONLY_MATCH was set in <i>Flags</i>.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>No process matched the executable file name in <i>ExeName</i>.</p>

<p> </p>

## -remarks
<p>This method is available only for live user-mode debugging.</p>

<p>For more information about creating and attaching to live user-mode targets, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552020">Live User-Mode Targets</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugclient.md">IDebugClient</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient2.md">IDebugClient2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
<dt>
<a href="debugger.getrunningprocesssystemids">GetRunningProcessSystemIds</a>
</dt>
<dt>
<a href="debugger.getrunningprocessdescription">GetRunningProcessDescription</a>
</dt>
<dt>
<a href="debugger.connectprocessserver">ConnectProcessServer</a>
</dt>
<dt>
<a href="debugger.attachprocess">AttachProcess</a>
</dt>
<dt>
<a href="debugger.createprocessandattach2">CreateProcessAndAttach2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::GetRunningProcessSystemIdByExecutableName method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
