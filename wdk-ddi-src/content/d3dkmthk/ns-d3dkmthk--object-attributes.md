---
UID: NS.d3dkmthk._OBJECT_ATTRIBUTES
title: OBJECT_ATTRIBUTES
author: windows-driver-content
description: The OBJECT_ATTRIBUTES structure specifies attributes that can be applied to objects or object handles by routines that create objects and/or return handles to objects.
old-location: kernel\object_attributes.htm
old-project: kernel
ms.assetid: 08f5a141-abce-4890-867c-5fe8c4239905
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: OBJECT_ATTRIBUTES,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: Ntdef.h, Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OBJECT_ATTRIBUTES
req.alt-loc: d3dkmthk.h
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
req.iface: 
---

# OBJECT_ATTRIBUTES structure



## -description
<p>The <b>OBJECT_ATTRIBUTES</b> structure specifies attributes that can be applied to objects or object handles by routines that create objects and/or return handles to objects.</p>


## -syntax

````
typedef struct _OBJECT_ATTRIBUTES {
  ULONG           Length;
  HANDLE          RootDirectory;
  PUNICODE_STRING ObjectName;
  ULONG           Attributes;
  PVOID           SecurityDescriptor;
  PVOID           SecurityQualityOfService;
}  OBJECT_ATTRIBUTES, *POBJECT_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>The number of bytes of data contained in this structure. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a> macro sets this member to <b>sizeof</b>(<b>OBJECT_ATTRIBUTES</b>).</p>
</dd>

### -field <b>RootDirectory</b>

<dd>
<p>Optional handle to the root object directory for the path name specified by the <b>ObjectName</b> member. If <b>RootDirectory</b> is <b>NULL</b>, <b>ObjectName</b> must point to a fully qualified object name that includes the full path to the target object. If <b>RootDirectory</b> is non-<b>NULL</b>, <b>ObjectName</b> specifies an object name relative to the <b>RootDirectory</b> directory. The <b>RootDirectory</b> handle can refer to a file system directory or an object directory in the object manager namespace.</p>
</dd>

### -field <b>ObjectName</b>

<dd>
<p>Pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">Unicode string</a> that contains the name of the object for which a handle is to be opened. This must either be a fully qualified object name, or a relative path name to the directory specified by the <b>RootDirectory</b> member.</p>
</dd>

### -field <b>Attributes</b>

<dd>
<p>Bitmask of flags that specify object handle attributes. This member can contain one or more of the flags in the following table.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>OBJ_INHERIT </p>
</td>
<td>
<p>This handle can be inherited by child processes of the current process.</p>
</td>
</tr>
<tr>
<td>
<p>OBJ_PERMANENT</p>
</td>
<td>
<p>This flag only applies to objects that are named within the object manager. By default, such objects are deleted when all open handles to them are closed. If this flag is specified, the object is not deleted when all open handles are closed. Drivers can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566477">ZwMakeTemporaryObject</a> routine to make a permanent object non-permanent.</p>
</td>
</tr>
<tr>
<td>
<p>OBJ_EXCLUSIVE </p>
</td>
<td>
<p>If this flag is set and the <b>OBJECT_ATTRIBUTES</b> structure is passed to a routine that creates an object, the object can be accessed exclusively. That is, once a process opens such a handle to the object, no other processes can open handles to this object.</p>
<p>If this flag is set and the <b>OBJECT_ATTRIBUTES</b> structure is passed to a routine that creates an object handle, the caller is requesting exclusive access to the object for the process context that the handle was created in. This request can be granted only if the OBJ_EXCLUSIVE flag was set when the object was created.</p>
</td>
</tr>
<tr>
<td>
<p>OBJ_CASE_INSENSITIVE </p>
</td>
<td>
<p>If this flag is specified, a case-insensitive comparison is used when matching the name pointed to by the <b>ObjectName</b> member against the names of existing objects. Otherwise, object names are compared using the default system settings.</p>
</td>
</tr>
<tr>
<td>
<p>OBJ_OPENIF </p>
</td>
<td>
<p>If this flag is specified, by using the object handle, to a routine that creates objects and if that object already exists, the routine should open that object. Otherwise, the routine creating the object returns an NTSTATUS code of STATUS_OBJECT_NAME_COLLISION.</p>
</td>
</tr>
<tr>
<td>
<p>OBJ_OPENLINK </p>
</td>
<td>
<p>If an object handle, with this flag set, is passed to a routine that opens objects and if the object is a symbolic link object, the routine should open the symbolic link object itself, rather than the object that the symbolic link refers to (which is the default behavior).</p>
</td>
</tr>
<tr>
<td>
<p>OBJ_KERNEL_HANDLE </p>
</td>
<td>
<p>The handle is created in system process context and can only be accessed from kernel mode.</p>
</td>
</tr>
<tr>
<td>
<p>OBJ_FORCE_ACCESS_CHECK</p>
</td>
<td>
<p>The routine that opens the handle should enforce all access checks for the object, even if the handle is being opened in kernel mode.</p>
</td>
</tr>
<tr>
<td>
<p>OBJ_VALID_ATTRIBUTES</p>
</td>
<td>
<p>Reserved.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>SecurityDescriptor</b>

<dd>
<p>Specifies a security descriptor (<a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a>) for the object when the object is created. If this member is <b>NULL</b>, the object will receive default security settings.</p>
</dd>

### -field <b>SecurityQualityOfService</b>

<dd>
<p>Optional quality of service to be applied to the object when it is created. Used to indicate the security impersonation level and context tracking mode (dynamic or static). Currently, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a> macro sets this member to <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a> macro to initialize the members of the <b>OBJECT_ATTRIBUTES</b> structure. Note that <b>InitializeObjectAttributes</b> initializes the <b>SecurityQualityOfService</b> member to <b>NULL</b>. If you must specify a non-<b>NULL</b> value, set the <b>SecurityQualityOfService</b> member after initialization.</p>

<p>To apply the attributes contained in this structure to an object or object handle, pass a pointer to this structure to a routine that accesses objects or returns object handles, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff566421">ZwCreateDirectoryObject</a>.</p>

<p>All members of this structure are read-only. If a member of this structure is a pointer, the object that this member points to is read-only as well. Read-only members and objects can be used to acquire relevant information but must not be modified. To set the members of this structure, use the <b>InitializeObjectAttributes</b> macro.</p>

<p>Driver routines that run in a process context other than that of the system process must set the OBJ_KERNEL_HANDLE flag for the <b>Attributes</b> member (by using the <b>InitializeObjectAttributes</b> macro). This restricts the use of a handle opened for that object to processes running only in kernel mode. Otherwise, the handle can be accessed by the process in whose context the driver is running.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include Ntdef.h, Wdm.h, Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541931">FltCreateCommunicationPort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541935">FltCreateFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541937">FltCreateFileEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548418">IoCreateFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548283">IoCreateFileEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548289">IoCreateFileSpecifyDeviceObjectHint</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566421">ZwCreateDirectoryObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20OBJECT_ATTRIBUTES structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
