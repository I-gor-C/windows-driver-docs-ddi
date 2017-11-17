---
UID: NF.dbgeng.IDebugAdvanced3.Request
title: IDebugAdvanced3::Request
author: windows-driver-content
description: The Request method performs a variety of different operations.
old-location: debugger\request.htm
ms.assetid: efb3c93c-5405-418b-a063-afa8e5e9e59a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugAdvanced2.Request,IDebugAdvanced3.Request
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
ms.keywords: IDebugAdvanced3, Request, IDebugAdvanced3::Request
req.iface: IDebugAdvanced3
---

# IDebugAdvanced3::Request method



## -description
<p>The <b>Request</b> method performs a variety of different operations.</p>


## -syntax

````
HRESULT Request(
  [in]            ULONG  Request,
  [in, optional]  PVOID  InBuffer,
  [in]            ULONG  InBufferSize,
  [out, optional] PVOID  OutBuffer,
  [in]            ULONG  OutBufferSize,
  [out, optional] PULONG OutSize
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>Specifies which operation to perform.  <b>Request</b> can be one of the values in the following table.  Details of each operation can be found by following the link in the "Request" column.</p>
<table>
<tr>
<th>Request</th>
<th>Action</th>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541597">DEBUG_REQUEST_SOURCE_PATH_HAS_SOURCE_SERVER</a>
</p>
</td>
<td>
<p>Check the source path for a source server.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541606">DEBUG_REQUEST_TARGET_EXCEPTION_CONTEXT</a>
</p>
</td>
<td>
<p>Return the <a href="debugger.scopes_and_symbol_groups#thread_context#thread_context">thread context</a> for the stored event in a user-mode minidump file.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541623">DEBUG_REQUEST_TARGET_EXCEPTION_THREAD</a>
</p>
</td>
<td>
<p>Return the operating system thread ID for the stored event in a user-mode minidump file.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541616">DEBUG_REQUEST_TARGET_EXCEPTION_RECORD</a>
</p>
</td>
<td>
<p>Return the exception record for the stored event in a user-mode minidump file.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541553">DEBUG_REQUEST_GET_ADDITIONAL_CREATE_OPTIONS</a>
</p>
</td>
<td>
<p>Return the default process creation options.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541586">DEBUG_REQUEST_SET_ADDITIONAL_CREATE_OPTIONS</a>
</p>
</td>
<td>
<p>Set the default process creation options.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541563">DEBUG_REQUEST_GET_WIN32_MAJOR_MINOR_VERSIONS</a>
</p>
</td>
<td>
<p>Return the version of Windows that is currently running on the target.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541575">DEBUG_REQUEST_READ_USER_MINIDUMP_STREAM</a>
</p>
</td>
<td>
<p>Read a stream from a user-mode minidump target.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541602">DEBUG_REQUEST_TARGET_CAN_DETACH</a>
</p>
</td>
<td>
<p>Check to see if it is possible for the debugger engine to detach from the current process (leaving the process running but no longer being debugged).</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541592">DEBUG_REQUEST_SET_LOCAL_IMPLICIT_COMMAND_LINE</a>
</p>
</td>
<td>
<p>Set the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>'s implicit command line.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541561">DEBUG_REQUEST_GET_CAPTURED_EVENT_CODE_OFFSET</a>
</p>
</td>
<td>
<p>Return the current event's instruction pointer.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541572">DEBUG_REQUEST_READ_CAPTURED_EVENT_CODE_STREAM</a>
</p>
</td>
<td>
<p>Return up to 64 bytes of memory at the current event's instruction pointer.</p>
</td>
</tr>
<tr>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541547">DEBUG_REQUEST_EXT_TYPED_DATA_ANSI</a>
</p>
</td>
<td>
<p>Perform a variety of different operations that aid in the interpretation of typed data.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>InBuffer</i> [in, optional]

<dd>
<p>Specifies the input to this method.  The type and interpretation of the input depends on the <i>Request</i> parameter.</p>
</dd>

### -param <i>InBufferSize</i> [in]

<dd>
<p>Specifies the size of the input buffer <i>InBuffer</i>.  If the request requires no input, <i>InBufferSize</i> should be set to zero.</p>
</dd>

### -param <i>OutBuffer</i> [out, optional]

<dd>
<p>Receives the output from this method.  The type and interpretation of the output depends on the <i>Request</i> parameter.  If <i>OutBuffer</i> is <b>NULL</b>, the output is not returned.</p>
</dd>

### -param <i>OutBufferSize</i> [in]

<dd>
<p>Specifies the size of the output buffer <i>OutBufferSize</i>.  If the type of the output returned to <i>OutBuffer</i> has a known size, <i>OutBufferSize</i> is usually expected to be exactly that size, even if <i>OutBuffer</i> is set to <b>NULL</b>.</p>
</dd>

### -param <i>OutSize</i> [out, optional]

<dd>
<p>Receives the size of the output returned in the output buffer <i>OutBuffer</i>.  If <i>OutSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>The interpretation of the return value depends on the value of the <i>Request</i> parameter.  Unless otherwise stated, the following values may be returned.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  However, the output would not fit in the output buffer <i>OutBuffer</i>, so truncated output was returned.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The size of the input buffer <i>InBufferSize</i> or the size of the output buffer <i>OutBufferSize</i> was not the expected value.</p>

<p> </p>

<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549803">IDebugAdvanced2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549807">IDebugAdvanced3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541597">DEBUG_REQUEST_SOURCE_PATH_HAS_SOURCE_SERVER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541606">DEBUG_REQUEST_TARGET_EXCEPTION_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541623">DEBUG_REQUEST_TARGET_EXCEPTION_THREAD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541616">DEBUG_REQUEST_TARGET_EXCEPTION_RECORD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541553">DEBUG_REQUEST_GET_ADDITIONAL_CREATE_OPTIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541586">DEBUG_REQUEST_SET_ADDITIONAL_CREATE_OPTIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541563">DEBUG_REQUEST_GET_WIN32_MAJOR_MINOR_VERSIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541575">DEBUG_REQUEST_READ_USER_MINIDUMP_STREAM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541602">DEBUG_REQUEST_TARGET_CAN_DETACH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541592">DEBUG_REQUEST_SET_LOCAL_IMPLICIT_COMMAND_LINE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541561">DEBUG_REQUEST_GET_CAPTURED_EVENT_CODE_OFFSET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541572">DEBUG_REQUEST_READ_CAPTURED_EVENT_CODE_STREAM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugAdvanced2::Request method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
