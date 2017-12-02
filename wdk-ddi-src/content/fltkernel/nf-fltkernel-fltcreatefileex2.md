---
UID: NF.fltkernel.FltCreateFileEx2
title: FltCreateFileEx2
author: windows-driver-content
description: Minifilter drivers call FltCreateFileEx2 to create a new file or open an existing file. This routine also includes an optional create context parameter.
old-location: ifsk\fltcreatefileex2.htm
old-project: ifsk
ms.assetid: e662472d-4d72-449e-91d7-119bd59e0943
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltCreateFileEx2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltCreateFileEx2
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

# FltCreateFileEx2 function



## -description
<p>Minifilter drivers call <b>FltCreateFileEx2</b> to create a new file or open an existing file.  This routine also includes an optional create context parameter.</p>


## -syntax

````
NTSTATUS FltCreateFileEx2(
  _In_      PFLT_FILTER               Filter,
  _In_opt_  PFLT_INSTANCE             Instance,
  _Out_     PHANDLE                   FileHandle,
  _Out_opt_ PFILE_OBJECT              *FileObject,
  _In_      ACCESS_MASK               DesiredAccess,
  _In_      POBJECT_ATTRIBUTES        ObjectAttributes,
  _Out_     PIO_STATUS_BLOCK          IoStatusBlock,
  _In_opt_  PLARGE_INTEGER            AllocationSize,
  _In_      ULONG                     FileAttributes,
  _In_      ULONG                     ShareAccess,
  _In_      ULONG                     CreateDisposition,
  _In_      ULONG                     CreateOptions,
  _In_opt_  PVOID                     EaBuffer,
  _In_      ULONG                     EaLength,
  _In_      ULONG                     Flags,
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
<p>An opaque instance pointer for the minifilter driver instance that the create request is to be sent to. The instance must be attached to the volume where the file or directory resides. This parameter is optional and can be <b>NULL</b>. If this parameter is <b>NULL</b>, the request is sent to the device object at the top of the file system driver stack for the volume. If this parameter is non-<b>NULL</b>, the request is sent only to minifilter driver instances that are attached below the specified instance. </p>
</dd>

### -param FileHandle [out]

<dd>
<p>A pointer to a caller-allocated variable that receives the file handle if the call to <b>FltCreateFileEx2</b> is successful. </p>
</dd>

### -param FileObject [out, optional]

<dd>
<p>A pointer to a caller-allocated variable that receives the file object pointer if the call to <b>FltCreateFileEx2</b> is successful. This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param DesiredAccess [in]

<dd>
<p>A bitmask of flags that specify the type of access that the caller requires to the file or directory. The set of system-defined <i>DesiredAccess</i> flags determines the following specific access rights for file objects. </p>
<div class="alert"><b>Note</b>  Do not specify FILE_READ_DATA, FILE_WRITE_DATA, FILE_EXECUTE, or FILE_APPEND_DATA when creating or opening a directory.</div>
<div> </div>
<table>
<tr>
<th><i>DesiredAccess</i> flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DELETE</p>
</td>
<td>
<p>The file can be deleted.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_READ_DATA</p>
</td>
<td>
<p>Data can be read from the file.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_READ_ATTRIBUTES</p>
</td>
<td>
<p><i>FileAttributes</i> flags can be read.  For additional information, see the table of valid flag values in the <i>FileAttributes</i> parameter description below.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_READ_EA</p>
</td>
<td>
<p>Extended attributes that are associated with the file can be read. </p>
</td>
</tr>
<tr>
<td>
<p>READ_CONTROL</p>
</td>
<td>
<p>The access control list (<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>) and ownership information that is associated with the file can be read.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_WRITE_DATA</p>
</td>
<td>
<p>Data can be written to the file.</p>
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
<p>FILE_WRITE_EA </p>
</td>
<td>
<p>Extended attributes that are associated with the file can be written. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_APPEND_DATA</p>
</td>
<td>
<p>Data can be appended to the file.</p>
</td>
</tr>
<tr>
<td>
<p>WRITE_DAC </p>
</td>
<td>
<p>The discretionary access control list (<a href="..\ntifs\ns-ntifs--acl.md">DACL</a>) that is associated with the file can be written.</p>
</td>
</tr>
<tr>
<td>
<p>WRITE_OWNER </p>
</td>
<td>
<p>Ownership information that is associated with the file can be written.</p>
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
<tr>
<td>
<p>FILE_EXECUTE</p>
</td>
<td>
<p>Use system paging I/O to read data from the file into system memory. </p>
</td>
</tr>
</table>
<p> </p>
<p>Alternatively, for any file object that does not represent a directory, you can specify one or more of the following generic <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> flags. The following table illustrates that a flag value in the left column is equivalent to the set of flag values in the right column. (The STANDARD_RIGHTS_<i>XXX</i> flags are predefined system values that are used to enforce security on system objects.) You can also combine these generic flags with additional flags from the preceding table. </p>
<table>
<tr>
<th><i>DesiredAccess</i> values</th>
<th>Maps to <i>DesiredAccess</i> flags</th>
</tr>
<tr>
<td>
<p>GENERIC_READ</p>
</td>
<td>
<p>STANDARD_RIGHTS_READ, FILE_READ_DATA, FILE_READ_ATTRIBUTES, FILE_READ_EA, and SYNCHRONIZE </p>
</td>
</tr>
<tr>
<td>
<p>GENERIC_WRITE</p>
</td>
<td>
<p>STANDARD_RIGHTS_WRITE, FILE_WRITE_DATA, FILE_WRITE_ATTRIBUTES, FILE_WRITE_EA, FILE_APPEND_DATA, and SYNCHRONIZE </p>
</td>
</tr>
<tr>
<td>
<p>GENERIC_EXECUTE</p>
</td>
<td>
<p>STANDARD_RIGHTS_EXECUTE, SYNCHRONIZE, FILE_READ_ATTRIBUTES, and FILE_EXECUTE </p>
</td>
</tr>
</table>
<p> </p>
<p>For directories, you can specify one or more of the following ACCESS_MASK flags, which you can also combine with any compatible flags that were described in the preceding tables. </p>
<table>
<tr>
<th><i>DesiredAccess</i> flags - for directories</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_LIST_DIRECTORY</p>
</td>
<td>
<p>Files in the directory can be listed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_TRAVERSE</p>
</td>
<td>
<p>The directory can be traversed: that is, it can be part of the pathname of a file.</p>
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
<p>A pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains the name of the file to be created or opened. This name must be a fully qualified file specification or the name of a device object unless it is the name of a file relative to the directory specified by <b>RootDirectory</b>. For example, "\Device\Floppy1\myfile.dat" or "\??\B:\myfile.dat" could both be valid file specifications, if the floppy driver and overlying file system are already loaded. (Note: "\??" replaces "\DosDevices" as the name of the Win32 object namespace. "\DosDevices" still works, but "\??" is translated faster by the object manager.)</p>
</td>
</tr>
<tr>
<td>
<p><b>HANDLE </b><b>RootDirectory</b></p>
</td>
<td>
<p>An optional handle to a directory, obtained by a preceding call to <b>FltCreateFileEx2</b>. If this value is <b>NULL</b>, the <i>ObjectName</i>member must be a fully qualified file specification that includes the full path to the target file. If this value is non-<b>NULL</b>, the <i>ObjectName</i> member specifies a file name that is relative to this directory.</p>
</td>
</tr>
<tr>
<td>
<p><b>PSECURITY_DESCRIPTOR </b><b>SecurityDescriptor</b></p>
</td>
<td>
<p>An optional security descriptor (<a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a>) to be applied to a file. <a href="..\ntifs\ns-ntifs--acl.md">ACLs</a> specified by such a security descriptor are only applied to the file when it is created. If the value is <b>NULL</b> when a file is created, the ACL placed on the file is file-system-dependent. Most file systems propagate some part of such an ACL from the parent directory file combined with the caller's default ACL. </p>
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
<p>A pointer to an <a href="..\wdm\ns-wdm--io-status-block.md">IO_STATUS_BLOCK</a> structure that receives the final completion status and information about the requested operation. On return from <b>FltCreateFileEx2</b>, the <b>Information</b> member of the variable contains one of the following values.</p>
<dl>
<dd>
<p>FILE_CREATED</p>
</dd>
<dd>
<p>FILE_OPENED</p>
</dd>
<dd>
<p>FILE_OVERWRITTEN</p>
</dd>
<dd>
<p>FILE_SUPERSEDED</p>
</dd>
<dd>
<p>FILE_EXISTS</p>
</dd>
<dd>
<p>FILE_DOES_NOT_EXIST</p>
</dd>
</dl>
</dd>

### -param AllocationSize [in, optional]

<dd>
<p>Optionally specifies the initial allocation size, in bytes, for the file stream. A nonzero value has no effect unless the file is being created, overwritten, or superseded. </p>
</dd>

### -param FileAttributes [in]

<dd>
<p>Specifies one or more of the following FILE_ATTRIBUTE_<i>XXX</i> flags, which represent the file attributes to set if you are creating, superseding, or overwriting a file. Normally, you specify FILE_ATTRIBUTE_NORMAL, which sets the default attributes. </p>
<table>
<tr>
<th><i>FileAttributes</i> flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_ATTRIBUTE_NORMAL</p>
</td>
<td>
<p>A file with standard attributes should be created.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_ATTRIBUTE_READONLY</p>
</td>
<td>
<p>A read-only file should be created.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_ATTRIBUTE_HIDDEN</p>
</td>
<td>
<p>A hidden file should be created.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_ATTRIBUTE_SYSTEM</p>
</td>
<td>
<p>A system file should be created.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_ATTRIBUTE_ARCHIVE</p>
</td>
<td>
<p>An archive file should be created. This attribute is used to mark files for backup or removal.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_ATTRIBUTE_TEMPORARY</p>
</td>
<td>
<p>A temporary file should be created.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param ShareAccess [in]

<dd>
<p>Specifies the type of share access to the file that the caller requires, as zero or one, or a combination of the following flags. If the IO_IGNORE_SHARE_ACCESS_CHECK flag is specified in the <i>Flags</i> parameter, the I/O manager ignores this parameter. However, the file system might still perform access checks. Thus, it is important to specify the sharing mode you would like for this parameter, even when using the IO_IGNORE_SHARE_ACCESS_CHECK flag. For the greatest chance of avoiding sharing violation errors, specify all of the following share access flags. </p>
<table>
<tr>
<th><i>ShareAccess</i> flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_SHARE_READ</p>
</td>
<td>
<p>The file can be opened for read access by other threads' calls to <b>FltCreateFileEx2</b>.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_SHARE_WRITE</p>
</td>
<td>
<p>The file can be opened for write access by other threads' calls to <b>FltCreateFileEx2</b>.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_SHARE_DELETE</p>
</td>
<td>
<p>The file can be opened for delete access by other threads' calls to <b>FltCreateFileEx2</b>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param CreateDisposition [in]

<dd>
<p>Specifies a value that determines the action to be taken, depending on whether the file already exists. The value can be any of those described in the following table. </p>
<table>
<tr>
<th><i>CreateDisposition</i> values</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_SUPERSEDE</p>
</td>
<td>
<p>If the file already exists, replace it with the given file. If it does not, create the given file. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_CREATE </p>
</td>
<td>
<p>If the file already exists, fail the request and do not create or open the given file. If it does not, create the given file.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_OPEN </p>
</td>
<td>
<p>If the file already exists, open it instead of creating a new file. If it does not, fail the request and do not create a new file.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_OPEN_IF</p>
</td>
<td>
<p>If the file already exists, open it. If it does not, create the given file.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_OVERWRITE</p>
</td>
<td>
<p>If the file already exists, open it and overwrite it. If it does not, fail the request.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_OVERWRITE_IF</p>
</td>
<td>
<p>If the file already exists, open it and overwrite it. If it does not, create the given file.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param CreateOptions [in]

<dd>
<p>Specifies the options to be applied when creating or opening the file, as a compatible combination of the following flags. </p>
<table>
<tr>
<th><i>CreateOptions</i> flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_DIRECTORY_FILE</p>
</td>
<td>
<p>The file that is being created or opened is a directory file. With this flag, the <i>CreateDisposition</i> parameter must be set to one of FILE_CREATE, FILE_OPEN, or FILE_OPEN_IF. With this flag, other compatible <i>CreateOptions</i> flags include only the following: FILE_SYNCHRONOUS_IO_ALERT, FILE_SYNCHRONOUS_IO_NONALERT, FILE_WRITE_THROUGH, FILE_OPEN_FOR_BACKUP_INTENT, and FILE_OPEN_BY_FILE_ID. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_NON_DIRECTORY_FILE</p>
</td>
<td>
<p>The file that is being opened must not be a directory file or this call fails. The file object that is being opened can represent a data file; a logical, virtual, or physical device; or a volume. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_WRITE_THROUGH</p>
</td>
<td>
<p>System services, file systems, and drivers that write data to the file must actually transfer the data into the file before any requested write operation is considered complete. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_SEQUENTIAL_ONLY</p>
</td>
<td>
<p>All accesses to the file will be sequential.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_RANDOM_ACCESS</p>
</td>
<td>
<p>Accesses to the file can be random, so no sequential read-ahead operations should be performed on the file by file systems or the operating system.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NO_INTERMEDIATE_BUFFERING</p>
</td>
<td>
<p>The file cannot be cached or buffered in a driver's internal buffers. This flag is incompatible with the <i>DesiredAccess</i>FILE_APPEND_DATA flag. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_SYNCHRONOUS_IO_ALERT</p>
</td>
<td>
<p>All operations on the file are performed synchronously. Any wait on behalf of the caller is subject to premature termination from alerts. This flag also causes the I/O system to maintain the file position context. If this flag is set, the <i>DesiredAccess</i> SYNCHRONIZE flag also must be set so that the I/O Manager uses the file object as a synchronization object. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_SYNCHRONOUS_IO_NONALERT</p>
</td>
<td>
<p>All operations on the file are performed synchronously. Waits in the system to synchronize I/O queuing and completion are not subject to alerts. This flag also causes the I/O system to maintain the file position context. If this flag is set, the <i>DesiredAccess</i> SYNCHRONIZE flag also must be set so that the I/O Manager uses the file object as a synchronization object.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_CREATE_TREE_CONNECTION</p>
</td>
<td>
<p>Create a tree connection for this file in order to open it over the network. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_COMPLETE_IF_OPLOCKED</p>
</td>
<td>
<p>Complete this operation immediately with an alternate success code if the target file is oplocked, rather than blocking the caller's thread. If the file is oplocked, another caller already has access to the file over the network. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_NO_EA_KNOWLEDGE</p>
</td>
<td>
<p>If the extended attributes on an existing file that is being opened indicate that the caller must understand extended attributes to properly interpret the file, fail this request because the caller does not understand how to deal with extended attributes. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_OPEN_REPARSE_POINT</p>
</td>
<td>
<p>Open a file with a reparse point and bypass normal reparse point processing for the file.  For more information, see the following Remarks section.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_DELETE_ON_CLOSE </p>
</td>
<td>
<p>Delete the file when the last handle to it is passed to <a href="..\fltkernel\nf-fltkernel-fltclose.md">FltClose</a>. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_OPEN_BY_FILE_ID</p>
</td>
<td>
<p>The file is being opened by ID. The file name contains the name of a device and a 64-bit ID to be used to open the file. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_OPEN_FOR_BACKUP_INTENT</p>
</td>
<td>
<p>The file is being opened for backup intent. Therefore, the system should check for certain access rights and grant the caller the appropriate accesses to the file before checking the input <i>DesiredAccess</i> against the file's security descriptor. </p>
</td>
</tr>
<tr>
<td>
<p>FILE_OPEN_REQUIRING_OPLOCK </p>
</td>
<td>
<p>The file is being opened and an opportunistic lock (oplock) on the file is being requested as a single atomic operation. The file system checks for oplocks before it performs the create operation, and the create will fail with a return code of STATUS_CANNOT_BREAK_OPLOCK if the create would break an existing oplock. </p>
<div class="alert"><b>Note</b>    The FILE_OPEN_REQUIRING_OPLOCK flag is available in Windows 7, Windows Server 2008 R2 and later Windows operating systems.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>FILE_RESERVE_OPFILTER </p>
</td>
<td>
<p>This flag allows an application to request a Filter opportunistic lock (oplock) to prevent other applications from getting share violations.  If there are already open handles, the create request will fail with STATUS_OPLOCK_NOT_GRANTED.  For more information, see the following Remarks section.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param EaBuffer [in, optional]

<dd>
<p>A pointer to a caller-supplied <a href="..\wdm\ns-wdm--file-full-ea-information.md">FILE_FULL_EA_INFORMATION</a> buffer that contains extended attribute (EA) information to be applied to the file. </p>
</dd>

### -param EaLength [in]

<dd>
<p>Length, in bytes, of <i>EaBuffer</i>. </p>
</dd>

### -param Flags [in]

<dd>
<p>Specifies options to be used during the creation of the create request. The following table lists the available options. </p>
<table>
<tr>
<th>Options flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>IO_FORCE_ACCESS_CHECK</p>
</td>
<td>
<p>Indicates that the I/O manager must check the create request against the file's security descriptor.</p>
</td>
</tr>
<tr>
<td>
<p>IO_IGNORE_SHARE_ACCESS_CHECK</p>
</td>
<td>
<p>Indicates that the I/O manager should not perform share-access checks on the file object after it is created. However, the file system might still perform these checks. </p>
</td>
</tr>
<tr>
<td>
<p>IO_STOP_ON_SYMLINK</p>
</td>
<td>
<p>The I/O manager or the file system will return STATUS_STOPPED_ON_SYMLINK if a symbolic link is encountered while opening or creating the file.</p>
</td>
</tr>
<tr>
<td>
<p>IO_NO_PARAMETER_CHECKING</p>
</td>
<td>
<p>Indicates that the parameters for this call should not be validated before attempting to issue the create request. Minifilter writers should use this flag with caution as certain invalid parameters can cause a system failure. For more information, see Remarks.</p>
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
<p><b>FltCreateFileEx2</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The filter or instance specified in the <i>Filter</i> or <i>Instance</i> parameters is being torn down. This status code can be received if the open request crosses a volume mount point and the <i>Instance</i> parameter is non-<b>NULL</b>. This is an error code. </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>FltCreateFileEx2</b> encountered a pool allocation failure. This is an error code. </p><dl>
<dt><b>STATUS_MOUNT_POINT_NOT_RESOLVED</b></dt>
</dl><p>The file or directory name contains a mount point that resolves to a volume other than the one that the specified minifilter driver instance is attached to. This is an error code. </p><dl>
<dt><b>STATUS_OBJECT_PATH_SYNTAX_BAD</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter did not contain a <b>RootDirectory</b> member, but the <b>ObjectName</b> member in the OBJECT_ATTRIBUTES structure was an empty string or did not contain an OBJECT_NAME_PATH_SEPARATOR character. This error code indicates incorrect syntax for the object path. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This value will be returned if the <i>DriverContext</i> parameter points to a valid IO_DRIVER_CREATE_CONTEXT structure and the <b>DeviceObjectHint</b> member of this structure is not <b>NULL</b>. This is an error code.</p>

<p> </p>

## -remarks
<p><b>FltCreateFileEx2</b> is similar to <a href="..\fltkernel\nf-fltkernel-fltcreatefile.md">FltCreateFile</a> and <a href="..\fltkernel\nf-fltkernel-fltcreatefileex.md">FltCreateFileEx</a>, except that it supports the new <i>DriverContext</i> input parameter.</p>

<p>To specify an extra create parameter (ECP) as part of a create operation, initialize the <b>ExtraCreateParameter</b> member of the IO_DRIVER_CREATE_CONTEXT structure with the <a href="..\fltkernel\nf-fltkernel-fltallocateextracreateparameterlist.md">FltAllocateExtraCreateParameterList</a> routine.  If ECPs are used, they must be created, manipulated, and freed using the appropriate routines - the following <i>See Also</i> section lists these routines.  Upon returning from the call of <b>FltCreateFileEx2</b>, the ECP list is unchanged and may be passed to additional calls of <b>FltCreateFileEx2</b> for other create operations.  Note that the operating system does not automatically deallocate the ECP list structure - the caller of <b>FltCreateFileEx2</b> must deallocate this structure by calling the <a href="..\fltkernel\nf-fltkernel-fltfreeextracreateparameterlist.md">FltFreeExtraCreateParameterList</a> routine.</p>

<p>To create/open a file in the context of a transaction, set the <b>TxnParameters</b> member of the IO_DRIVER_CREATE_CONTEXT structure to the value returned by the <a href="..\ntddk\nf-ntddk-iogettransactionparameterblock.md">IoGetTransactionParameterBlock</a> routine.</p>

<p>For additional information regarding transactions, see <a href="http://go.microsoft.com/fwlink/p/?linkid=66161">Transaction Management (TxF)</a>.</p>

<p><b>FltCreateFileEx2</b> sends the create request only to the instances attached below the specified minifilter driver instance and to the file system. The specified instance and the instances attached above it do not receive the create request. If no instance is specified, the request goes to the top of the stack and is received by all instances and the file system. </p>

<p>There are two alternate ways to specify the name of the file to be created or opened with <b>FltCreateFileEx2</b>: </p>

<p>As a fully qualified pathname, supplied in the <b>ObjectName</b> member of the input <i>ObjectAttributes</i>. </p>

<p>As a pathname that is relative to the directory file represented by the handle in the <b>RootDirectory</b> member of the input <i>ObjectAttributes</i>. </p>

<p>Any <i>FileHandle</i> that is obtained from <b>FltCreateFileEx2</b> must eventually be released by calling <a href="..\fltkernel\nf-fltkernel-fltclose.md">FltClose</a>. In addition, any returned <i>FileObject</i> pointer must be dereferenced when it is no longer needed by calling <a href="..\wdm\nf-wdm-obdereferenceobject.md">ObDereferenceObject</a>. </p>

<p>Driver routines that do not run in the system process context must set the OBJ_KERNEL_HANDLE attribute for the <i>ObjectAttributes</i> parameter of <b>FltCreateFileEx2</b>. Setting this attribute restricts the use of the handle that is returned by <b>FltCreateFileEx2</b> to processes running in kernel mode. Otherwise, the handle can be accessed by the process in whose context the driver is running. </p>

<p>Certain <i>DesiredAccess</i> flags and combinations of flags have the following effects: </p>

<p>For a caller to synchronize an I/O completion by waiting for the returned <i>FileHandle</i> to be set to the Signaled state, the SYNCHRONIZE flag must be set. </p>

<p>If only the FILE_APPEND_DATA and SYNCHRONIZE flags are set, the caller can write only to the end of the file, and any offset information about write requests to the file is ignored. However, the file is automatically extended as necessary for this type of write operation. </p>

<p>Setting the FILE_WRITE_DATA flag for a file also allows write requests beyond the end of the file to occur. The file is automatically extended for this type of write request, as well. </p>

<p>If only the FILE_EXECUTE and SYNCHRONIZE flags are set, the caller cannot use the handle returned in the <i>FileHandle</i> parameter to directly read or write any data to or from the file. That is, all operations on the file must use system paging I/O to read or write file data. </p>

<p>The <i>ShareAccess</i> parameter determines whether separate threads can access the same file, possibly simultaneously. If both file openers have the privilege to access a file in the specified manner, the file can be successfully opened and shared. If the original caller of <b>FltCreateFileEx2</b> does not specify FILE_SHARE_READ, FILE_SHARE_WRITE, or FILE_SHARE_DELETE, no other open operations can be performed on the file because the original caller is given exclusive access to the file. </p>

<p>For a shared file to be successfully opened, the requested <i>DesiredAccess</i> to the file must be compatible with both the <i>DesiredAccess</i> and <i>ShareAccess</i> specifications of all preceding open requests that have not yet been released with <a href="..\fltkernel\nf-fltkernel-fltclose.md">FltClose</a>. That is, the <i>DesiredAccess</i> parameter that is specified to <b>FltCreateFileEx2</b> for a given file must not conflict with the accesses that other openers of the file have disallowed. </p>

<p>The <i>CreateDisposition</i> value FILE_SUPERSEDE requires that the caller have DELETE access to an existing file object. If so, a successful call to <b>FltCreateFileEx2</b> with FILE_SUPERSEDE on an existing file effectively deletes that file and then recreates it. This implies that if the file has already been opened by another thread, it opened the file by specifying a <i>ShareAccess</i>parameter with the FILE_SHARE_DELETE flag set. Note that this type of disposition is consistent with the POSIX style of overwriting files. </p>

<p>The <i>CreateDisposition</i> values FILE_OVERWRITE_IF and FILE_SUPERSEDE are similar. If <b>FltCreateFileEx2</b> is called with an existing file and either of these <i>CreateDisposition</i> values, the file is replaced. </p>

<p>Overwriting a file is semantically equivalent to a supersede operation, except for the following: </p>

<p>The caller must have write access to the file, rather than delete access. This implies that, if the file has already been opened by another thread, it opened the file with the FILE_SHARE_WRITE flag set in the input <i>ShareAccess</i> parameter. </p>

<p>The specified file attributes are combined with those attributes that are already applied to the file by using a bitwise OR operation. This implies that if the file has already been opened by another thread, a subsequent caller of <b>FltCreateFileEx2</b> cannot disable existing <i>FileAttributes</i> flags but can enable additional flags for the same file. Note that this style of overwriting files is consistent with MS-DOS, Windows 3.1, and OS/2.</p>

<p>The <i>CreateOptions</i> FILE_DIRECTORY_FILE value specifies that the file to be created or opened is a directory file. When a directory file is created, the file system creates an appropriate structure on the disk to represent an empty directory for that particular file system's on-disk structure. If this option was specified and the given file to be opened is not a directory file or if the caller specified an inconsistent <i>CreateOptions</i> or <i>CreateDisposition</i> value, the call to <b>FltCreateFileEx2</b> fails. </p>

<p>The <i>CreateOptions</i> FILE_NO_INTERMEDIATE_BUFFERING flag prevents the file system from performing any intermediate buffering on behalf of the caller. Specifying this value places certain restrictions on the caller's parameters to other <b>Flt..File</b> routines or <b>Zw..File</b> routines, including the following: </p>

<p>Any byte offset value passed to the <i>ByteOffset</i> parameter of <a href="..\fltkernel\nf-fltkernel-fltreadfile.md">FltReadFile</a>, <a href="..\wdm\nf-wdm-zwreadfile.md">ZwReadFile</a>, <a href="..\fltkernel\nf-fltkernel-fltwritefile.md">FltWriteFile</a>, or <a href="..\wdm\nf-wdm-zwwritefile.md">ZwWriteFile</a> must be a multiple of the sector size. </p>

<p>The <i>Length</i> parameter passed to <a href="..\fltkernel\nf-fltkernel-fltreadfile.md">FltReadFile</a>, <a href="..\wdm\nf-wdm-zwreadfile.md">ZwReadFile</a>, <a href="..\fltkernel\nf-fltkernel-fltwritefile.md">FltWriteFile</a>, or <a href="..\wdm\nf-wdm-zwwritefile.md">ZwWriteFile</a> must be a multiple of the sector size. Note that specifying a read operation to a buffer whose length is exactly the sector size might result in fewer significant bytes being transferred to that buffer if the end of the file was reached during the transfer.</p>

<p>Buffers must be aligned in accordance with the alignment requirement of the underlying storage device. This information can be obtained by calling <b>FltCreateFileEx2</b> to get a handle for the file object that represents the physical device and then calling <a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a> with that handle, specifying <b>FileAlignmentInformation</b> as the value for <i>FileInformationClass</i> parameter. For more information about the system FILE_<i>XXX</i>_ALIGNMENT values, which are defined in <i>Ntifs.h</i>, see <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff547807">Initializing a Device Object</a>. </p>

<p>Calls to <a href="..\fltkernel\nf-fltkernel-fltsetinformationfile.md">FltSetInformationFile</a> or <a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a> with the <i>FileInformationClass</i> parameter set to <b>FilePositionInformation</b> must specify an offset that is a multiple of the sector size.</p>

<p>The <i>CreateOptions</i> FILE_SYNCHRONOUS_IO_ALERT and FILE_SYNCHRONOUS_IO_NONALERT flags, which are mutually exclusive as their names suggest, specify that the file is being opened for synchronous I/O. This means that all I/O operations on the file are to be synchronous as long as they occur through the file object that the returned <i>FileHandle</i> refers to. All I/O on such a file is serialized across all threads by using the returned handle. With either of these <i>CreateOptions</i> flags set, the I/O Manager maintains the current file position offset in the file object's <b>CurrentByteOffset</b> field. This offset can be used in calls to <a href="..\wdm\nf-wdm-zwreadfile.md">ZwReadFile</a> and <a href="..\wdm\nf-wdm-zwwritefile.md">ZwWriteFile</a>. It can also be queried or set by calling <a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a> or <a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>. </p>

<p>If the <i>CreateOptions</i> FILE_OPEN_REPARSE_POINT flag is <i>not</i> specified and <b>FltCreateFileEx2</b> attempts to open a file with a reparse point, normal reparse point processing occurs for the file.  If, on the other hand, the FILE_OPEN_REPARSE_POINT flag is specified, normal reparse processing does <i>not</i> occur and <b>FltCreateFileEx2</b> attempts to directly open the reparse point file.  In either case, if the open operation was successful, <b>FltCreateFileEx2</b> returns STATUS_SUCCESS; otherwise, the routine returns an NTSTATUS error code. <b>FltCreateFileEx2</b> never returns STATUS_REPARSE.</p>

<p>The <i>CreateOptions</i> FILE_OPEN_REQUIRING_OPLOCK flag eliminates the time between when you open the file and request an oplock that could potentially enable a third party to open the file and get a sharing violation. An application can use the FILE_OPEN_REQUIRING_OPLOCK flag on <b>FltCreateFileEx2</b> and then request any oplock. This ensures that an oplock owner will be notified of any later open request that causes a sharing violation. </p>

<p>In Windows 7, if other handles exist on the file when an application uses the FILE_OPEN_REQUIRING_OPLOCK flag, the create operation will fail with STATUS_OPLOCK_NOT_GRANTED. This restriction no longer exists starting with Windows 8.</p>

<p>If this create operation would break an oplock that already exists on the file, then setting the FILE_OPEN_REQUIRING_OPLOCK flag will cause the create operation to fail with STATUS_CANNOT_BREAK_OPLOCK. The existing oplock will not be broken by this create operation.</p>

<p> An application that uses this flag must request an oplock after this call succeeds, or all later attempts to open the file will be blocked without the benefit of typical oplock processing. Similarly, if this call succeeds but the later oplock request fails, an application that uses this flag must close its handle after it detects that the oplock request has failed.</p>

<p>The <i>CreateOptions</i> flag FILE_RESERVE_OPFILTER allows an application to request a level 1, batch, or filter oplock to prevent other applications from getting share violations. However, FILE_RESERVE_OPFILTER is only practically useful for filter oplocks. To use it, you must complete the following steps:</p>

<p> If the create request succeeds, request an oplock. </p>

<p> Open another handle to the file to do I/O.  </p>

<p>Step three makes this practical only for filter oplocks. The handle opened in step 3 can have a DesiredAccess that contains a maximum of FILE_READ_ATTRIBUTES | FILE_WRITE_ATTRIBUTES | FILE_READ_DATA | FILE_READ_EA | FILE_EXECUTE | SYNCHRONIZE | READ_CONTROL and still not break a filter oplock. However, any DesiredAccess greater than FILE_READ_ATTRIBUTES | FILE_WRITE_ATTRIBUTES | SYNCHRONIZE will break a level 1 or batch oplock and make the FILE_RESERVE_OPFILTER flag useless for those oplock types.</p>

<p>The <i>Options</i> IO_NO_PARAMETER_CHECKING flag can be useful if a kernel-mode create request is issued in the context of an operation initiated by a user-mode application. Because the request occurs within a user-mode context, the I/O manager, by default, probes the supplied parameter values, which can cause an access violation if the parameters are kernel-mode addresses. This flag enables the caller to override this default behavior and avoid the access violation.</p>

<p>NTFS is the only Microsoft file system that implements FILE_RESERVE_OPFILTER. </p>

<p>Minifilter drivers must use <a href="..\fltkernel\nf-fltkernel-fltsetinformationfile.md">FltSetInformationFile</a>, not <a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>, to rename a file. </p>

<p>FILE_READ_ATTRIBUTES</p>

<p>READ_CONTROL</p>

<p>WRITE_DAC</p>

<p>WRITE_OWNER</p>

<p>SYNCHRONIZE</p><p class="note">You must not use <b>FltCreateFileEx2</b> to open a handle with direct access to the storage device for the volume or you will leak system resources. If you want to open a handle with direct access to a storage device, call the <a href="..\ntddk\nf-ntddk-iocreatefileex.md">IoCreateFileEx</a>, <a href="..\ntddk\nf-ntddk-iocreatefilespecifydeviceobjecthint.md">IoCreateFileSpecifyDeviceObjectHint</a>, or <a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a> function instead.</p>

<p>When a caller of <b>FltCreateFileEx2</b> wishes to  enable reparsing for a volume target, a <a href="..\fltkernel\ns-fltkernel--flt-createfile-target-ecp-context.md">FLT_CREATEFILE_TARGET_ECP_CONTEXT</a> can be included as an ECP to the ECP list in the <i>DriverContext</i> parameter.  If this ECP is present, <b>FltCreateFileEx2</b> will adjust the target device for the create operation and attempt for find a filtered instance  of a volume appropriate for the given file information. Use of this ECP is available starting with Windows 8.</p>

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
<p>Available in starting with Windows Vista.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--acl.md">ACL</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--file-full-ea-information.md">FILE_FULL_EA_INFORMATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltacknowledgeecp.md">FltAcknowledgeEcp</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltallocateextracreateparameter.md">FltAllocateExtraCreateParameter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltallocateextracreateparameterlist.md">FltAllocateExtraCreateParameterList</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltclose.md">FltClose</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltfindextracreateparameter.md">FltFindExtraCreateParameter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltfreeextracreateparameter.md">FltFreeExtraCreateParameter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltfreeextracreateparameterlist.md">FltFreeExtraCreateParameterList</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetecplistfromcallbackdata.md">FltGetEcpListFromCallbackData</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetnextextracreateparameter.md">FltGetNextExtraCreateParameter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltinsertextracreateparameter.md">FltInsertExtraCreateParameter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltisecpacknowledged.md">FltIsEcpAcknowledged</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltisecpfromusermode.md">FltIsEcpFromUserMode</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltqueryinformationfile.md">FltQueryInformationFile</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreadfile.md">FltReadFile</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltremoveextracreateparameter.md">FltRemoveExtraCreateParameter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsetecplistintocallbackdata.md">FltSetEcpListIntoCallbackData</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsetinformationfile.md">FltSetInformationFile</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltwritefile.md">FltWriteFile</a>
</dt>
<dt>
<a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iocreatefile.md">IoCreateFile</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iocreatefilespecifydeviceobjecthint.md">IoCreateFileSpecifyDeviceObjectHint</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--io-driver-create-context.md">IO_DRIVER_CREATE_CONTEXT</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-ioinitializedrivercreatecontext.md">IoInitializeDriverCreateContext</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-obdereferenceobject.md">ObDereferenceObject</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwreadfile.md">ZwReadFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwwritefile.md">ZwWriteFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCreateFileEx2 routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
