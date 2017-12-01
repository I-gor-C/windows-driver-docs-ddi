---
UID: NF.ntifs.ZwOpenDirectoryObject
title: ZwOpenDirectoryObject
author: windows-driver-content
description: The ZwOpenDirectoryObject routine opens an existing directory object.
old-location: kernel\zwopendirectoryobject.htm
old-project: kernel
ms.assetid: ddff6e6e-d22f-4e22-af13-aca889eee0d4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwOpenDirectoryObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntdef.h, Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwOpenDirectoryObject,NtCreateDirectoryObject
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# ZwOpenDirectoryObject function



## -description
<p>The <b>ZwOpenDirectoryObject</b> routine opens an existing directory object. </p>


## -syntax

````
NTSTATUS ZwOpenDirectoryObject(
  _Out_ PHANDLE            DirectoryHandle,
  _In_  ACCESS_MASK        DesiredAccess,
  _In_  POBJECT_ATTRIBUTES ObjectAttributes
);
````


## -parameters
<dl>

### -param <i>DirectoryHandle</i> [out]

<dd>
<p>Handle for the newly opened directory object. </p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> structure specifying the requested types of access being requested for this directory object. A caller can specify one or a combination of the following.</p>
<table>
<tr>
<th><i>DesiredAccess</i> Flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DIRECTORY_QUERY</p>
</td>
<td>
<p>Query access to the directory object</p>
</td>
</tr>
<tr>
<td>
<p>DIRECTORY_TRAVERSE</p>
</td>
<td>
<p>Name-lookup access to the directory object</p>
</td>
</tr>
<tr>
<td>
<p>DIRECTORY_CREATE_OBJECT</p>
</td>
<td>
<p>Name-creation access to the directory object</p>
</td>
</tr>
<tr>
<td>
<p>DIRECTORY_CREATE_SUBDIRECTORY</p>
</td>
<td>
<p>Subdirectory-creation access to the directory object</p>
</td>
</tr>
<tr>
<td>
<p>DIRECTORY_ALL_ACCESS</p>
</td>
<td>
<p>All of the preceding rights plus STANDARD_RIGHTS_REQUIRED.</p>
</td>
</tr>
</table>
<p> </p>
<p>These requested access types are compared with the object's discretionary access-control list (<a href="..\ntifs\ns-ntifs--acl.md">DACL</a>) to determine which accesses are granted or denied.</p>
</dd>

### -param <i>ObjectAttributes</i> [in]

<dd>
<p>Specified attributes for the directory object supplied by the caller. This parameter is initialized by calling the <b>InitializeObjectAttributes</b> macro. </p>
</dd>
</dl>

## -returns
<p><b>ZwOpenDirectoryObject</b> returns STATUS_SUCCESS or an appropriate error status. The most common error status codes include the following: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A temporary buffer required by this routine could not be allocated. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified <i>ObjectAttributes</i> parameter was a <b>NULL</b> pointer, not a valid pointer to an <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> structure, or some of the fields specified in the OBJECT_ATTRIBUTES structure were invalid. </p><dl>
<dt><b>STATUS_OBJECT_NAME_INVALID</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter contained an <b>ObjectName</b> field in the <b>OBJECT_ATTRIBUTES</b> structure that was invalid because an empty string was found after the OBJECT_NAME_PATH_SEPARATOR character. </p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter contained an <b>ObjectName</b> field in the <b>OBJECT_ATTRIBUTES</b> structure that could not be found. </p><dl>
<dt><b>STATUS_OBJECT_PATH_NOT_FOUND</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter contained an <b>ObjectName</b> field in the <b>OBJECT_ATTRIBUTES</b> structure with an object path that could not be found. </p><dl>
<dt><b>STATUS_OBJECT_PATH_SYNTAX_BAD</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter did not contain a <b>RootDirectory</b> field, but the <b>ObjectName</b> field in the <b>OBJECT_ATTRIBUTES</b> structure was an empty string or did not contain an OBJECT_NAME_PATH_SEPARATOR character. This indicates incorrect syntax for the object path. </p>

<p> </p>

<p>The <b>ZwOpenDirectoryObject</b> routine throws an exception if the <i>DirectoryHandle</i> parameter is an illegal pointer.</p>

## -remarks
<p><b>ZwOpenDirectoryObject</b> opens an existing directory object and returns a handle to the object. </p>

<p>The <b>ZwOpenDirectoryObject</b> routine is called after the <b>InitializeObjectAttributes</b> macro is used to initialize specific attributes of the <b>OBJECT_ATTRIBUTES</b> structure for the object to be opened. </p>

<p>A directory object is created using the <b>ZwCreateDirectoryObject </b>routine<b>. </b>Any handle obtained by calling <b>ZwOpenDirectoryObject</b> must eventually be released by calling <b>ZwClose</b>. </p>

<p>For more information about security and access control, see the documentation on these topics in the Windows SDK. </p>

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
<p>Available in Windows XP and later versions of Windows. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntdef.h, Ntifs.h, or Fltkernel.h)</dt>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>
</dt>
<dt>
<a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatedirectoryobject.md">ZwCreateDirectoryObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwOpenDirectoryObject routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
