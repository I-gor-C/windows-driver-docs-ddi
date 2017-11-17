---
UID: NF.fltkernel.FltParseFileNameInformation
title: FltParseFileNameInformation
author: windows-driver-content
description: FltParseFileNameInformation parses the contents of a FLT_FILE_NAME_INFORMATION structure.
old-location: ifsk\fltparsefilenameinformation.htm
ms.assetid: f588f59b-5efa-4783-bb45-935b91c69cb5
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP SP2 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltParseFileNameInformation
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
ms.keywords: FltParseFileNameInformation
req.iface: 
---

# FltParseFileNameInformation function



## -description
<p><b>FltParseFileNameInformation</b> parses the contents of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a> structure. </p>


## -syntax

````
NTSTATUS FltParseFileNameInformation(
  _Inout_ PFLT_FILE_NAME_INFORMATION FileNameInformation
);
````


## -parameters
<dl>

### -param <i>FileNameInformation</i> [in, out]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a> structure returned by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543003">FltGetDestinationFileNameInformation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543032">FltGetFileNameInformation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543035">FltGetFileNameInformationUnsafe</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff543177">FltGetTunneledName</a>. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltParseFileNameInformation</b> returns STATUS_SUCCESS or an appropriate NTSTATUS error code. </p>

## -remarks
<p><b>FltParseFileNameInformation</b> parses the <b>Name</b> member of a FLT_FILE_NAME_INFORMATION structure and uses the results to set the values of the <b>Volume</b>, <b>Share</b>, <b>Extension</b>, <b>Stream</b>, <b>FinalComponent</b>, <b>ParentDir</b>, and <b>NamesParsed</b> members of this structure. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a>. </p>

<p>The following is an example of a normalized name for a remote file: </p>

<p><b>FltParseFileNameInformation</b> parses this normalized name as follows: </p>

<p><b>Volume</b>: "\Device\LanManRedirector" </p>

<p><b>Share</b>: "\MyServer\MyShare" </p>

<p><b>Extension</b>: "txt" </p>

<p><b>Stream</b>: ":stream1" </p>

<p><b>FinalComponent</b>: "Test Results.txt:stream1" </p>

<p><b>ParentDir</b>: "\Documents and Settings\MyUser\My Documents\" </p>

<p>The following is an example of an opened name for a local file: </p>

<p><b>FltParseFileNameInformation</b> parses this opened name as follows: </p>

<p><b>Volume</b>: "\Device\HarddiskVolume1" </p>

<p><b>Share</b>: <b>NULL</b></p>

<p><b>Extension</b>: "txt" </p>

<p><b>Stream</b>: ":stream1:$DATA" </p>

<p><b>FinalComponent</b>: "TestRe~1.txt:stream1:$DATA" </p>

<p><b>ParentDir</b>: "\Docume~1\MyUser\My Documents\" </p>

<p>The following is an example of a short name for a file: </p>

<p><b>FltParseFileNameInformation</b> parses this short name as follows: </p>

<p><b>Volume</b>: <b>NULL</b></p>

<p><b>Share</b>: <b>NULL</b></p>

<p><b>Extension</b>: "txt" </p>

<p><b>Stream</b>: <b>NULL</b></p>

<p><b>FinalComponent</b>: "TestRe~1.txt" </p>

<p><b>ParentDir</b>: <b>NULL</b></p>

<p>The caller must not modify the contents of the <i>FileNameInformation</i> structure, because the Filter Manager caches this structure so that all minifilter drivers can use it. </p>

<p><b>FltParseFileNameInformation</b> parses the <b>Name</b> member of a FLT_FILE_NAME_INFORMATION structure and uses the results to set the values of the <b>Volume</b>, <b>Share</b>, <b>Extension</b>, <b>Stream</b>, <b>FinalComponent</b>, <b>ParentDir</b>, and <b>NamesParsed</b> members of this structure. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a>. </p>

<p>The following is an example of a normalized name for a remote file: </p>

<p><b>FltParseFileNameInformation</b> parses this normalized name as follows: </p>

<p><b>Volume</b>: "\Device\LanManRedirector" </p>

<p><b>Share</b>: "\MyServer\MyShare" </p>

<p><b>Extension</b>: "txt" </p>

<p><b>Stream</b>: ":stream1" </p>

<p><b>FinalComponent</b>: "Test Results.txt:stream1" </p>

<p><b>ParentDir</b>: "\Documents and Settings\MyUser\My Documents\" </p>

<p>The following is an example of an opened name for a local file: </p>

<p><b>FltParseFileNameInformation</b> parses this opened name as follows: </p>

<p><b>Volume</b>: "\Device\HarddiskVolume1" </p>

<p><b>Share</b>: <b>NULL</b></p>

<p><b>Extension</b>: "txt" </p>

<p><b>Stream</b>: ":stream1:$DATA" </p>

<p><b>FinalComponent</b>: "TestRe~1.txt:stream1:$DATA" </p>

<p><b>ParentDir</b>: "\Docume~1\MyUser\My Documents\" </p>

<p>The following is an example of a short name for a file: </p>

<p><b>FltParseFileNameInformation</b> parses this short name as follows: </p>

<p><b>Volume</b>: <b>NULL</b></p>

<p><b>Share</b>: <b>NULL</b></p>

<p><b>Extension</b>: "txt" </p>

<p><b>Stream</b>: <b>NULL</b></p>

<p><b>FinalComponent</b>: "TestRe~1.txt" </p>

<p><b>ParentDir</b>: <b>NULL</b></p>

<p>The caller must not modify the contents of the <i>FileNameInformation</i> structure, because the Filter Manager caches this structure so that all minifilter drivers can use it. </p>

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
<p>Available in Windows XP SP2 and later versions of the Windows operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543003">FltGetDestinationFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543032">FltGetFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543035">FltGetFileNameInformationUnsafe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543177">FltGetTunneledName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543413">FltParseFileName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltParseFileNameInformation function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
