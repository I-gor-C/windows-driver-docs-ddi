---
UID: NF.dbgeng.IDebugClient4.GetDumpFileWide
title: IDebugClient4::GetDumpFileWide
author: windows-driver-content
description: The GetDumpFileWide method describes the files containing supporting information that were used when opening the current dump target.
old-location: debugger\getdumpfilewide.htm
old-project: debugger
ms.assetid: 42acd24e-5952-46b3-bb0b-1eb43125fccd
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugClient4, GetDumpFileWide, IDebugClient4::GetDumpFileWide
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
req.alt-api: IDebugClient4.GetDumpFileWide,IDebugClient5.GetDumpFileWide
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
req.iface: IDebugClient4
---

# IDebugClient4::GetDumpFileWide method



## -description
<p>The <b>GetDumpFileWide</b> method describes the files containing supporting information that were used when opening the current dump target.</p>


## -syntax

````
HRESULT GetDumpFileWide(
  [in]            ULONG    Index,
  [out, optional] PWSTR    Buffer,
  [in]            ULONG    BufferSize,
  [out, optional] PULONG   NameSize,
  [out, optional] PULONG64 Handle,
  [out]           PULONG   Type
);
````


## -parameters
<dl>

### -param Index [in]

<dd>
<p>Specifies which file to describe.  <i>Index</i> can take values between zero and the number of files minus one; the number of files can be found by using <a href="debugger.getnumberdumpfiles">GetNumberDumpFiles</a>.</p>
</dd>

### -param Buffer [out, optional]

<dd>
<p>Receives the file name.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param BufferSize [in]

<dd>
<p>Specifies the size in characters of the buffer <i>Buffer</i>.</p>
</dd>

### -param NameSize [out, optional]

<dd>
<p>Receives the size of the file name.  If <i>NameSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param Handle [out, optional]

<dd>
<p>Receives the file handle of the file.  If <i>Handle</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param Type [out]

<dd>
<p>Receives the type of the file.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about crash dump files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542783">Dump-File Targets</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
<dt>
<a href="debugger.getnumberdumpfiles">GetNumberDumpFiles</a>
</dt>
<dt>
<a href="debugger.adddumpinformationfilewide">AddDumpInformationFileWide</a>
</dt>
<dt>
<a href="debugger.adddumpinformationfile">AddDumpInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient4::GetDumpFileWide method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
