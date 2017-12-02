---
UID: NF.fltkernel.FltParseFileName
title: FltParseFileName
author: windows-driver-content
description: FltParseFileName parses the extension, stream, and final component from a file name string.
old-location: ifsk\fltparsefilename.htm
old-project: ifsk
ms.assetid: 8d91390b-22a1-4e0b-8c9e-78c0872e7b21
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltParseFileName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP with Service Pack 2 (SP2) and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltParseFileName
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
req.iface: 
---

# FltParseFileName function



## -description
<p><b>FltParseFileName</b> parses the extension, stream, and final component from a file name string. </p>


## -syntax

````
NTSTATUS FltParseFileName(
  _In_    PCUNICODE_STRING FileName,
  _Inout_ PUNICODE_STRING  Extension,
  _Inout_ PUNICODE_STRING  Stream,
  _Inout_ PUNICODE_STRING  FinalComponent
);
````


## -parameters
<dl>

### -param FileName [in]

<dd>
<p>Pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains the string to parse as a file name. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param Extension [in, out]

<dd>
<p>Pointer to a UNICODE_STRING structure that receives the extension parsed from the <i>FileName</i> string. If no extension is found, <b>FltParseFileName</b> sets <i>Extension.Buffer</i> to <b>NULL</b> and <i>Extension.Length</i> to zero. Otherwise, <i>Extension.Buffer</i> receives a pointer to the beginning of the extension in <i>FileName.Buffer</i>, and <i>Extension.Length</i> receives the length, in bytes, of the extension. This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param Stream [in, out]

<dd>
<p>Pointer to a UNICODE_STRING structure that receives the stream name parsed from the <i>FileName</i> string. If no stream name is found, <b>FltParseFileName</b> sets <i>Stream.Buffer</i> to <b>NULL</b> and <i>Stream.Length</i> to zero. Otherwise, <i>Stream.Buffer</i> receives a pointer to the beginning of the stream name in <i>FileName.Buffer</i>, and <i>Stream.Length</i> receives the length, in bytes, of the stream name. This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param FinalComponent [in, out]

<dd>
<p>Pointer to a UNICODE_STRING structure that receives the final name component parsed from the <i>FileName</i> string. If no final component is found, <b>FltParseFileName</b> sets <i>FinalComponent.Buffer</i> to <b>NULL</b> and <i>FinalComponent.Length</i> to zero. Otherwise, <i>FinalComponent.Buffer</i> receives a pointer to the beginning of the final component in <i>FileName.Buffer</i>, and <i>FinalComponent.Length</i> receives the length, in bytes, of the final component. This parameter is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltParseFileName</b> returns STATUS_SUCCESS or an appropriate NTSTATUS error code. </p>

## -remarks
<p><b>FltParseFileName</b> parses the extension, stream name, and final component from a file name string. The file name is not required to be normalized or a full path name. If the file name is a short file name, <b>FltParseFileName</b> parses only the extension. </p>

<p>The following is an example of a normalized name for a local file: </p>

<p><b>FltParseFileName</b> parses this normalized name as follows: </p>

<p><i>Extension</i>: "txt" </p>

<p><i>Stream</i>: ":stream1" </p>

<p><i>FinalComponent</i>: "Test Results.txt:stream1" </p>

<p>The following is an example of a short name for a file: </p>

<p><b>FltParseFileName</b> parses this short name as follows: </p>

<p><i>Stream</i>: <b>NULL</b></p>

<p><i>FinalComponent</i>: "TestRe~1.txt" </p>

<p>For more information about file name normalization and file name parsing, see <a href="..\fltkernel\ns-fltkernel--flt-file-name-information.md">FLT_FILE_NAME_INFORMATION</a>. </p>

<p>To parse the contents of a FLT_FILE_NAME_INFORMATION structure, call <a href="..\fltkernel\nf-fltkernel-fltparsefilenameinformation.md">FltParseFileNameInformation</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP with Service Pack 2 (SP2) and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-file-name-information.md">FLT_FILE_NAME_INFORMATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltparsefilenameinformation.md">FltParseFileNameInformation</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltParseFileName function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
