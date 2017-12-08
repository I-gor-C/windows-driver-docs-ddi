---
UID: NF.dbgeng.IDebugClient.GetRunningProcessDescription
title: IDebugClient::GetRunningProcessDescription
author: windows-driver-content
description: The GetRunningProcessDescription method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line.
old-location: debugger\getrunningprocessdescription.htm
old-project: debugger
ms.assetid: 1fdc4b85-d969-4433-8409-512f3f52cbbb
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugClient, GetRunningProcessDescription, IDebugClient::GetRunningProcessDescription
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
req.alt-api: IDebugClient.GetRunningProcessDescription,IDebugClient2.GetRunningProcessDescription,IDebugClient3.GetRunningProcessDescription,IDebugClient4.GetRunningProcessDescription,IDebugClient5.GetRunningProcessDescription
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
req.iface: IDebugClient
---

# IDebugClient::GetRunningProcessDescription method



## -description
<p>The <b>GetRunningProcessDescription</b>  method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line.</p>


## -syntax

````
HRESULT GetRunningProcessDescription(
  [in]            ULONG64 Server,
  [in]            ULONG   SystemId,
  [in]            ULONG   Flags,
  [out, optional] PSTR    ExeName,
  [in]            ULONG   ExeNameSize,
  [out, optional] PULONG  ActualExeNameSize,
  [out, optional] PSTR    Description,
  [in]            ULONG   DescriptionSize,
  [out, optional] PULONG  ActualDescriptionSize
);
````


## -parameters
<dl>

### -param Server [in]

<dd>
<p>Specifies the process server to query for the process description.  If <i>Server</i> is zero, the engine will query information about the local process directly.</p>
</dd>

### -param SystemId [in]

<dd>
<p>Specifies the process ID of the process whose description is desired.</p>
</dd>

### -param Flags [in]

<dd>
<p>Specifies a bit-set containing options that affect the behavior of this method.  <i>Flags</i> can contain the following bit flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_PROC_DESC_NO_PATHS</p>
</td>
<td>
<p>Return only file names without path names.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_PROC_DESC_NO_SERVICES</p>
</td>
<td>
<p>Do not look up service names.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_PROC_DESC_NO_MTS_PACKAGES</p>
</td>
<td>
<p>Do not look up MTS package names.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_PROC_DESC_NO_COMMAND_LINE</p>
</td>
<td>
<p>Do not retrieve the command line.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param ExeName [out, optional]

<dd>
<p>Receives the name of the executable file used to start the process.  If <i>ExeName</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param ExeNameSize [in]

<dd>
<p>Specifies the size in characters of the buffer <i>ExeNameSize</i>.</p>
</dd>

### -param ActualExeNameSize [out, optional]

<dd>
<p>Receives the size in characters of the executable file name.  If <i>ExeNameSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param Description [out, optional]

<dd>
<p>Receives extra information about the process, including service names, MTS package names, and the command line.  If <i>Description</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param DescriptionSize [in]

<dd>
<p>Specifies the size in characters of the buffer <i>Description</i>.</p>
</dd>

### -param ActualDescriptionSize [out, optional]

<dd>
<p>Receives the size in characters of the extra information.  If <i>ActualDescriptionSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  However, either <i>ExeNameSize</i> or <i>DescriptionSize</i> were smaller than the size of the respective string and the string was truncated to fit inside the buffer.</p>

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
<a href="debugger.getrunningprocesssystemidbyexecutablename">GetRunningProcessSystemIdByExecutableName</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::GetRunningProcessDescription method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
