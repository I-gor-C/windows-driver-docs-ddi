---
UID: NF.fltkernel.FltCreateMailslotFile
title: FltCreateMailslotFile
author: windows-driver-content
description: Minifilter drivers call FltCreateMailslotFile to create a new pipe or open an existing mailslot.
old-location: ifsk\fltcreatemailslotfile.htm
old-project: ifsk
ms.assetid: A727CDC1-A17A-4ABE-92AC-7CAEC11B78D1
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltCreateMailslotFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltCreateMailslotFile
req.alt-loc: Fltmgr.lib,Fltmgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fltmgr.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FltCreateMailslotFile function



## -description
<p>Minifilter drivers call <b>FltCreateMailslotFile</b> to create a new pipe or open an existing mailslot.</p>


## -syntax

````
NTSTATUS FltCreateMailslotFile(
  _In_      PFLT_FILTER               Filter,
  _In_opt_  PFLT_INSTANCE             Instance,
  _Out_     PHANDLE                   FileHandle,
  _Out_opt_ PFILE_OBJECT              *FileObject,
  _In_      ACCESS_MASK               DesiredAccess,
  _In_      POBJECT_ATTRIBUTES        ObjectAttributes,
  _Out_     PIO_STATUS_BLOCK          IoStatusBlock,
  _In_      ULONG                     CreateOptions,
  _In_      ULONG                     MailslotQuota,
  _In_      ULONG                     MaximumMessageSize,
  _In_      PLARGE_INTEGER            ReadTimeout,
  _In_opt_  PIO_DRIVER_CREATE_CONTEXT DriverContext
);
````


## -parameters
<dl>

### -param Filter [in]

<dd>
<p>An opaque filter pointer for the caller. </p>
</dd>

### -param Instance [in, optional]

<dd>
<p>An opaque instance pointer for the minifilter driver instance that the create request is to be sent to. The instance must be attached to the volume for the mailslot file system. This parameter is optional and can be <b>NULL</b>. If this parameter is <b>NULL</b>, the request is sent to the device object at the top of the file system driver stack for the volume. If it is non-<b>NULL</b>, the request is sent only to minifilter driver instances that are attached below the specified instance. </p>
</dd>

### -param FileHandle [out]

<dd>
<p>A pointer to a caller-allocated variable that receives the file handle if the call to  <b>FltCreateMailslotFile</b> is successful. </p>
</dd>

### -param FileObject [out, optional]

<dd>
<p>A pointer to a caller-allocated variable that receives the file object pointer if the call to <b>FltCreateMailslotFile</b> is successful. This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param DesiredAccess [in]

<dd>
<p>A bitmask of flags that specify the type of access that the caller requires to the file or directory. The set of system-defined <i>DesiredAccess</i> flags determines the following specific access rights for file objects. </p>
<table>
<tr>
<th>DesiredAccess Flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_READ_DATA</p>
</td>
<td>
<p>Data can be read from the named mailslot.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_READ_ATTRIBUTES</p>
</td>
<td>
<p><i>FileAttributes</i> flags can be read.  For additional information, see the table of valid flag values in the <i>FileAttributes</i> parameter of <a href="..\fltkernel\nf-fltkernel-fltcreatefileex2.md">FltCreateFileEx2</a>.</p>
</td>
</tr>
<tr>
<td>
<p>READ_CONTROL</p>
</td>
<td>
<p>The access control list (<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>) and ownership information associated with the mailslot can be read.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_WRITE_DATA</p>
</td>
<td>
<p>Data can be written to the mailslot.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_WRITE_ATTRIBUTES</p>
</td>
<td>
<p><i>FileAttributes</i> flags can be written.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_APPEND_DATA</p>
</td>
<td>
<p>Data can be appended to the mailslot.</p>
</td>
</tr>
<tr>
<td>
<p>WRITE_DAC </p>
</td>
<td>
<p>The discretionary access control list (<a href="..\ntifs\ns-ntifs--acl.md">DACL</a>) associated with the mailslot can be written.</p>
</td>
</tr>
<tr>
<td>
<p>WRITE_OWNER </p>
</td>
<td>
<p>Ownership information associated with the mailslot can be written.</p>
</td>
</tr>
<tr>
<td>
<p>ACCESS_SYSTEM_SECURITY</p>
</td>
<td>
<p>The caller will have write access to the mailslot's SACL</p>
</td>
</tr>
<tr>
<td>
<p>SYNCHRONIZE</p>
</td>
<td>
<p>The caller can synchronize the completion of an I/O operation by waiting for the returned <i>FileHandle</i> to be set to the Signaled state. This flag must be set if the <i>CreateOptions</i> FILE_SYNCHRONOUS_IO_ALERT or FILE_SYNCHRONOUS_IO_NONALERT flag is set. </p>
</td>
</tr>
</table>
<p> </p>
<p>Alternatively, for any file object that does not represent a directory, you can specify one or more of the following generic <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> flags. (The STANDARD_RIGHTS_<i>XXX</i> flags are predefined system values that are used to enforce security on system objects.) You can also combine these generic flags with additional flags from the preceding table. </p>
<table>
<tr>
<th>DesiredAccess to File Values</th>
<th>Maps to <i>DesiredAccess</i> Flags</th>
</tr>
<tr>
<td>
<p>GENERIC_READ</p>
</td>
<td>
<p>STANDARD_RIGHTS_READ, FILE_READ_DATA, and SYNCHRONIZE. </p>
</td>
</tr>
<tr>
<td>
<p>GENERIC_WRITE</p>
</td>
<td>
<p>STANDARD_RIGHTS_WRITE, FILE_WRITE_DATA, FILE_APPEND_DATA, and SYNCHRONIZE. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param ObjectAttributes [in]

<dd>
<p>A pointer to an opaque <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> structure that is already initialized with <a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a>. If the caller is running in the system process context, this parameter can be <b>NULL</b>. Otherwise, the caller must set the OBJ_KERNEL_HANDLE attribute in the call to <b>InitializeObjectAttributes</b>. Members of this structure for a file object are listed in the following table. </p>
<table>
<tr>
<th>Member</th>
<th>Value</th>
</tr>
<tr>
<td>
<p><b>ULONG </b><b>Length</b></p>
</td>
<td>
<p>The number of bytes of data that are contained in the structure pointed to by <i>ObjectAttributes</i>. This value must be at least <b>sizeof</b>(OBJECT_ATTRIBUTES).</p>
</td>
</tr>
<tr>
<td>
<p><b>PUNICODE_STRING </b><b>ObjectName</b></p>
</td>
<td>
<p>A pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains the name of the mailslot to be created or opened. This name must be a fully qualified file specification or the name of a device object unless it is the name of a file relative to the directory specified by <b>RootDirectory</b>. For example, "\Device\Mailslot\myslot" or "\??\mailslot\myslot" could both be valid file specifications. (Note: "\??" replaces "\DosDevices" as the name of the Win32 object namespace. "\DosDevices" still works, but "\??" is translated faster by the object manager.)</p>
</td>
</tr>
<tr>
<td>
<p><b>HANDLE </b><b>RootDirectory</b></p>
</td>
<td>
<p>An optional handle to a directory, obtained by a preceding call to <a href="..\fltkernel\nf-fltkernel-fltcreatefileex2.md">FltCreateFileEx2</a>. If this value is <b>NULL</b>, the <i>ObjectName</i>member must be a fully qualified file specification that includes the full path to the target mailslot. If this value is non-<b>NULL</b>, the <i>ObjectName</i> member specifies a mailslot name that is relative to this directory.</p>
</td>
</tr>
<tr>
<td>
<p><b>PSECURITY_DESCRIPTOR </b><b>SecurityDescriptor</b></p>
</td>
<td>
<p>An optional security descriptor (<a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a>) to be applied to a mailslot. <a href="..\ntifs\ns-ntifs--acl.md">ACLs</a> specified by such a security descriptor are only applied to the mailslot when it is created. If the value is <b>NULL</b> when a mailslot is created, the ACL placed on the mailslot is dependant on the mailslot file system and may allow a client with any access to create an instance.</p>
</td>
</tr>
<tr>
<td>
<p><b>ULONG </b><b>Attributes</b></p>
</td>
<td>
<p>A set of flags that controls the file object attributes. If the caller is running in the system process context, this parameter can be zero. Otherwise, the caller must set the OBJ_KERNEL_HANDLE flag. The caller can also optionally set the OBJ_CASE_INSENSITIVE flag, which indicates that name-lookup code should ignore the case of <i>ObjectName</i> rather than performing an exact-match search. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param IoStatusBlock [out]

<dd>
<p>A pointer to an <a href="..\wdm\ns-wdm--io-status-block.md">IO_STATUS_BLOCK</a> structure that receives the final completion status and information about the requested operation. On return from <b>FltCreateMailslotFile</b>, the <b>Information</b> member of the variable contains one of the following values:</p>
<dl>
<dd>
<p>FILE_CREATED</p>
</dd>
<dd>
<p>FILE_OPENED</p>
</dd>
</dl>
</dd>

### -param CreateOptions [in]

<dd>
<p>The options to be applied when creating or opening the mailslot, as a compatible combination of the following flags. </p>
<table>
<tr>
<th><i>CreateOptions</i> flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_WRITE_THROUGH</p>
</td>
<td>
<p>System services, file systems, and drivers that write data to the mailslot must actually transfer the data into the mailslot before any requested write operation is considered complete. This flag is automatically set if the <i>CreateOptions</i> flag FILE_NO_INTERMEDIATE_BUFFERING is set.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_SYNCHRONOUS_IO_ALERT</p>
</td>
<td>
<p>All operations on the mailslot are performed synchronously. Any wait on behalf of the caller is subject to premature termination from alerts. This flag also causes the I/O system to maintain the mailslot position context. If this flag is set, the <i>DesiredAccess</i> SYNCHRONIZE flag also must be set so that the I/O Manager uses the file object as a synchronization object. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_SYNCHRONOUS_IO_NONALERT</p>
</td>
<td>
<p>All operations on the mailslot are performed synchronously. Waits in the system to synchronize I/O queuing and completion are not subject to alerts. This flag also causes the I/O system to maintain the file position context. If this flag is set, the <i>DesiredAccess</i> SYNCHRONIZE flag also must be set so that the I/O Manager uses the file object as a synchronization object.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param MailslotQuota [in]

<dd>
<p>The size, in bytes, of the buffer for writes to the mailslot.</p>
</dd>

### -param MaximumMessageSize [in]

<dd>
<p>The maximum size, in bytes, of a message to write to the mailslot. A message of any size is specified by the value 0.</p>
</dd>

### -param ReadTimeout [in]

<dd>
<p>The time a read operation waits for a message to be available in the mailslot. The default timeout is expressed in 100-nanosecond increments as a negative integer. For example, 250 milliseconds is specified as –10 * 1000 * 250. Additionally, the following values have special meanings.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -param 0

</dl>
</td>
<td width="60%">
<p>Returns immediately if no message is present.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -param -1

</dl>
</td>
<td width="60%">
<p>Waits forever for a message.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param DriverContext [in, optional]

<dd>
<p>Optional pointer to an <a href="..\ntddk\ns-ntddk--io-driver-create-context.md">IO_DRIVER_CREATE_CONTEXT</a> structure already initialized by <a href="..\ntddk\nf-ntddk-ioinitializedrivercreatecontext.md">IoInitializeDriverCreateContext</a>.</p>
</dd>
</dl>

## -returns
<p><b>FltCreateMailslotFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following. </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The filter or instance specified in the <i>Filter</i> or <i>Instance</i> parameters is being torn down. This status code can be received if the open request crosses a volume mount point and the <i>Instance</i> parameter is non-<b>NULL</b>. This is an error code. </p><dl>
<dt><b>STATUS_OBJECT_PATH_SYNTAX_BAD</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter did not contain a <b>RootDirectory</b> member, but the <b>ObjectName</b> member in the OBJECT_ATTRIBUTES structure was an empty string or did not contain an OBJECT_NAME_PATH_SEPARATOR character. This error code indicates incorrect syntax for the object path. </p>

<p> </p>

## -remarks
<p>The <b>FltCreateMailslotFile</b> function allows minifilter drivers to create or open mailslot instances. This is useful for creating virtual mailslots or for creating a mailslot group that distributes to several other mailslots.</p>

<p>The <i>instance</i> parameter is either <b>NULL</b> or is previously set by attaching to the mailslot volume. A volume pointer is obtained by passing "\Device\Mailslot" as the volume name to <a href="..\fltkernel\nf-fltkernel-fltgetvolumefromname.md">FltGetVolumeFromName</a>.</p>

<p>To specify an extra create parameter (ECP) as part of a create operation, initialize the <b>ExtraCreateParameter</b> member of the <a href="..\ntddk\ns-ntddk--io-driver-create-context.md">IO_DRIVER_CREATE_CONTEXT</a> structure with the <a href="..\fltkernel\nf-fltkernel-fltallocateextracreateparameterlist.md">FltAllocateExtraCreateParameterList</a> routine.  If ECPs are used, they must be allocated, initialized, and freed using their associated support routines.  Upon returning from the call of <b>FltCreateMailslotFile</b>, the ECP list is unchanged and may be passed to additional calls of <b>FltCreateMailslotFile</b> for other create operations.  The ECP list structure is not automatically deallocated. The caller of <b>FltCreateMailslotFile</b> must deallocate this structure by calling the <a href="..\fltkernel\nf-fltkernel-fltfreeextracreateparameterlist.md">FltFreeExtraCreateParameterList</a> routine.</p>

<p>
     If <i>Instance</i> is not <b>NULL</b>, the create request from <b>FltCreateMailslotFile</b> is sent only to the instances attached below the specified minifilter driver instance and to the mailslot file system. The specified instance and the instances attached above it do not receive the create request. If no instance is specified, the request goes to the top of the stack and is received by all instances and the mailslot file system.</p>

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
<p>Available in Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include FltKernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.lib</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltfreeextracreateparameterlist.md">FltFreeExtraCreateParameterList</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltallocateextracreateparameterlist.md">FltAllocateExtraCreateParameterList</a>
</dt>
<dt>
<a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--io-driver-create-context.md">IO_DRIVER_CREATE_CONTEXT</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-ioinitializedrivercreatecontext.md">IoInitializeDriverCreateContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCreateMailslotFile function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
