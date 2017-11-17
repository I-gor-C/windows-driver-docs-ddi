---
UID: NF.dbgeng.IDebugAdvanced3.GetSourceFileInformationWide
title: IDebugAdvanced3::GetSourceFileInformationWide
author: windows-driver-content
description: The GetSourceFileInformationWide method returns specified information about a source file.
old-location: debugger\getsourcefileinformationwide.htm
ms.assetid: 1b7b26be-b7be-4dc7-9863-413f7293707c
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
req.alt-api: IDebugAdvanced3.GetSourceFileInformationWide
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
ms.keywords: IDebugAdvanced3, GetSourceFileInformationWide, IDebugAdvanced3::GetSourceFileInformationWide
req.iface: IDebugAdvanced3
---

# IDebugAdvanced3::GetSourceFileInformationWide method



## -description
<p>The <b>GetSourceFileInformationWide</b> method returns specified information about a source file.</p>


## -syntax

````
HRESULT GetSourceFileInformationWide(
  [in]            ULONG   Which,
  [in]            PWSTR   SourceFile,
  [in]            ULONG64 Arg64,
  [in]            ULONG   Arg32,
  [out, optional] PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  InfoSize
);
````


## -parameters
<dl>

### -param <i>Which</i> [in]

<dd>
<p>Specifies the piece of information to return.  The <i>Which</i> parameter can take one of the values in the following table.</p>
<p></p>
<dl>

### -param <a id="DEBUG_SRCFILE_SYMBOL_TOKEN_"></a><a id="debug_srcfile_symbol_token_"></a>DEBUG_SRCFILE_SYMBOL_TOKEN 

<dd>
<p>Returns a token representing the specified source file on a source server.  This token can be passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545430">FindSourceFileAndToken</a> to retrieve information about the file. The token is returned to the <i>Buffer</i> buffer as an array of bytes.  The size of this token is a reflection of the size of the SrcSrv token. </p>
</dd>

### -param <a id="DEBUG_SRCFILE_SYMBOL_TOKEN_SOURCE_COMMAND_WIDE_"></a><a id="debug_srcfile_symbol_token_source_command_wide_"></a>DEBUG_SRCFILE_SYMBOL_TOKEN_SOURCE_COMMAND_WIDE 

<dd>
<p>Queries a source server for the command to extract the source file from source control.  This includes the name of the executable file and its command-line parameters. The command is returned to the <i>Buffer</i> buffer as a Unicode string. </p>
</dd>
</dl>
</dd>

### -param <i>SourceFile</i> [in]

<dd>
<p>Specifies the source file whose information is being requested.  The source file is looked up on all the source servers in the source path. </p>
</dd>

### -param <i>Arg64</i> [in]

<dd>
<p>Specifies a 64-bit argument.  The value of <i>Which</i> specifies the module whose symbol token is requested.  Regardless of the value of <i>Which</i>, <i>Arg64</i> is a location within the memory allocation of the module.  </p>
</dd>

### -param <i>Arg32</i> [in]

<dd>
<p>Specifies a 32-bit argument.  This parameter is currently unused.   </p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the requested symbol information.  The type of the data returned depends on the value of <i>Which</i>.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in bytes of the <i>Buffer</i> buffer. If <i>Buffer</i> is <b>NULL</b>, <i>BufferSize</i> must also be <b>NULL</b>.</p>
</dd>

### -param <i>InfoSize</i> [out, optional]

<dd>
<p>Specifies the size in bytes of the information returned to the <i>Buffer</i> buffer. This parameter can be NULL if the data is not required.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, the information would not fit in the <i>Buffer</i> buffer, so the information or name was truncated.</p>

<p> </p>

## -remarks
<p>For more information about source files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560141">Using Source Files</a>.</p>

<p>For more information about source files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560141">Using Source Files</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549807">IDebugAdvanced3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545430">FindSourceFileAndToken</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugAdvanced3::GetSourceFileInformationWide method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
