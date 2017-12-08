---
UID: NF.dbgeng.IDebugAdvanced2.GetSystemObjectInformation
title: IDebugAdvanced2::GetSystemObjectInformation
author: windows-driver-content
description: The GetSystemObjectInformation method returns information about operating system objects on the target.
old-location: debugger\getsystemobjectinformation.htm
old-project: debugger
ms.assetid: 7e95a16e-e62d-49df-9889-fab0a85f9cbc
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugAdvanced2, GetSystemObjectInformation, IDebugAdvanced2::GetSystemObjectInformation
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
req.alt-api: IDebugAdvanced2.GetSystemObjectInformation,IDebugAdvanced3.GetSystemObjectInformation
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
req.iface: IDebugAdvanced2
---

# IDebugAdvanced2::GetSystemObjectInformation method



## -description
<p>The <b>GetSystemObjectInformation</b> method returns information about operating system objects on the target.</p>


## -syntax

````
HRESULT GetSystemObjectInformation(
  [in]            ULONG   Which,
  [in]            ULONG64 Arg64,
  [in]            ULONG   Arg32,
  [out, optional] PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  InfoSize
);
````


## -parameters
<dl>

### -param Which [in]

<dd>
<p>Specifies the type of object and the type of information to return about that object.  <i>Which</i> can take the following value.</p>
<table>
<tr>
<th>Value</th>
<th>Information returned</th>
</tr>
<tr>
<td>
<p>DEBUG_SYSOBJINFO_THREAD_BASIC_INFORMATION</p>
</td>
<td>
<p>Returns details of the thread specified by engine thread ID.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param Arg64 [in]

<dd>
<p>Specifies a 64-bit argument.  This parameter has the following interpretations depending on the value of <i>Which</i>:</p>
<p></p>
<dl>

### -param DEBUG_SYSOBJINFO_THREAD_BASIC_INFORMATION

<dd>
<p>Not used.</p>
</dd>
</dl>
</dd>

### -param Arg32 [in]

<dd>
<p>Specifies a 32-bit argument.  This parameter has the following interpretations depending on the value of <i>Which</i>:</p>
<p></p>
<dl>

### -param DEBUG_SYSOBJINFO_THREAD_BASIC_INFORMATION

<dd>
<p>The engine thread ID of the desired thread.</p>
</dd>
</dl>
</dd>

### -param Buffer [out, optional]

<dd>
<p>Receives the requested information.  The type of data returned in <i>Buffer</i> depends on the value of <i>Which</i>.</p>
<table>
<tr>
<th>Value</th>
<th>Return type</th>
</tr>
<tr>
<td>
<p>DEBUG_SYSOBJINFO_THREAD_BASIC_INFORMATION</p>
</td>
<td>
<p>
<a href="..\dbgeng\ns-dbgeng--debug-thread-basic-information.md">DEBUG_THREAD_BASIC_INFORMATION</a>
</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param BufferSize [in]

<dd>
<p>Specifies the size, in bytes, of the buffer <i>Buffer</i>.</p>
</dd>

### -param InfoSize [out, optional]

<dd>
<p>Receives the size of the information that is returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, the information would not fit in the buffer <i>Buffer</i>, so the information was truncated.</p>

<p> </p>

## -remarks


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
<a href="..\dbgeng\nn-dbgeng-idebugadvanced2.md">IDebugAdvanced2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugadvanced3.md">IDebugAdvanced3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects.md">IDebugSystemObjects</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugAdvanced2::GetSystemObjectInformation method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
