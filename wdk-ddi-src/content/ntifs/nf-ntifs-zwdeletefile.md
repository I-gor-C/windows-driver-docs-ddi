---
UID: NF.ntifs.ZwDeleteFile
title: ZwDeleteFile
author: windows-driver-content
description: The ZwDeleteFile routine deletes the specified file.
old-location: kernel\zwdeletefile.htm
old-project: kernel
ms.assetid: e6ad3bc5-9e19-4d32-bc08-b894ac802f41
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ZwDeleteFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwDeleteFile,NtDeleteFile
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
---

# ZwDeleteFile function



## -description
<p>The <b>ZwDeleteFile</b> routine deletes the specified file.</p>


## -syntax

````
NTSTATUS ZwDeleteFile(
  _In_ POBJECT_ATTRIBUTES ObjectAttributes
);
````


## -parameters
<dl>

### -param <i>ObjectAttributes</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a> structure that contains the attributes supplied by the caller to be used for the file object. These attributes would include the <b>ObjectName</b> and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a>, for example. This parameter is initialized by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a> macro.</p>
</dd>
</dl>

## -returns
<p><b>ZwDeleteFile</b> returns STATUS_SUCCESS or an appropriate error status representing the final completion status of the operation. Possible error status codes include the following:</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A temporary buffer required by this function could not be allocated.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified <i>ObjectAttributes</i> parameter was a <b>NULL</b> pointer, not a valid pointer to an <b>OBJECT_ATTRIBUTES</b> structure, or some of the specified <i>ObjectAttributes</i> structure members were invalid.</p><dl>
<dt><b>STATUS_OBJECT_NAME_INVALID</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter contained an <b>ObjectName</b> in the <b>OBJECT_ATTRIBUTES</b> structure that was invalid because an empty string was found after the OBJECT_NAME_PATH_SEPARATOR character.</p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter contained an <b>ObjectName</b> member in the <b>OBJECT_ATTRIBUTES</b> structure that could not be found.</p><dl>
<dt><b>STATUS_OBJECT_PATH_NOT_FOUND</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter contained an <b>ObjectName</b> member in the <b>OBJECT_ATTRIBUTES</b> structure with an object path that could not be found.</p><dl>
<dt><b>STATUS_OBJECT_PATH_SYNTAX_BAD</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter did not contain a <b>RootDirectory</b> member, but the <b>ObjectName</b> member in the <b>OBJECT_ATTRIBUTES</b> structure was an empty string or did not contain an OBJECT_NAME_PATH_SEPARATOR character. This indicates incorrect syntax for the object path.</p>

<p> </p>

## -remarks
<p><b>ZwDeleteFile</b> deletes the specified file object. </p>

<p>The <b>ZwDeleteFile</b> function is called after the <b>InitializeAttributes</b> macro is used to set attributes in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a> structure for the file object to be deleted. </p>

<p>There are two alternate ways to specify the name of the file to be deleted with <b>ZwDeleteFile</b>:</p>

<p>As a fully qualified pathname, supplied in the <b>ObjectName</b> member of the input <i>ObjectAttributes</i></p>

<p>As pathname relative to the directory file represented by the handle in the <b>RootDirectory</b> member of the input <i>ObjectAttributes</i></p>

<p>Callers of <b>ZwDeleteFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p><b>ZwDeleteFile</b> deletes the specified file object. </p>

<p>The <b>ZwDeleteFile</b> function is called after the <b>InitializeAttributes</b> macro is used to set attributes in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a> structure for the file object to be deleted. </p>

<p>There are two alternate ways to specify the name of the file to be deleted with <b>ZwDeleteFile</b>:</p>

<p>As a fully qualified pathname, supplied in the <b>ObjectName</b> member of the input <i>ObjectAttributes</i></p>

<p>As pathname relative to the directory file represented by the handle in the <b>RootDirectory</b> member of the input <i>ObjectAttributes</i></p>

<p>Callers of <b>ZwDeleteFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

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
<p>Available starting with Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwDeleteFile routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
