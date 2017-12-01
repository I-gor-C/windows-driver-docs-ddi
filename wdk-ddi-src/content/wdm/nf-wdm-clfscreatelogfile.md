---
UID: NF.wdm.ClfsCreateLogFile
title: ClfsCreateLogFile
author: windows-driver-content
description: The ClfsCreateLogFile routine creates or opens a CLFS stream. If necessary, ClfsCreateLogFile also creates the underlying physical log that holds the stream's records.
old-location: kernel\clfscreatelogfile.htm
old-project: kernel
ms.assetid: 297f7b03-efd0-4e9c-a758-1a3b5b89511d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ClfsCreateLogFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsCreateLogFile
req.alt-loc: Clfs.sys,Ext-MS-Win-fs-clfs-l1-1-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Clfs.lib
req.dll: Clfs.sys
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ClfsCreateLogFile function



## -description
<p>The <b>ClfsCreateLogFile</b> routine creates or opens a CLFS stream. If necessary, <b>ClfsCreateLogFile</b> also creates the underlying physical log that holds the stream's records.</p>


## -syntax

````
NTSTATUS ClfsCreateLogFile(
  _Out_    PPLOG_FILE_OBJECT    pplfoLog,
  _In_     PUNICODE_STRING      puszLogFileName,
  _In_     ACCESS_MASK          fDesiredAccess,
  _In_     ULONG                dwShareMode,
  _In_opt_ PSECURITY_DESCRIPTOR psdLogFile,
  _In_     ULONG                fCreateDisposition,
  _In_     ULONG                fCreateOptions,
  _In_     ULONG                fFlagsAndAttributes,
  _In_     ULONG                fLogOptionFlag,
  _In_opt_ PVOID                pvContext,
  _In_     ULONG                cbContext
);
````


## -parameters
<dl>

### -param <i>pplfoLog</i> [out]

<dd>
<p>A pointer to a variable that receives a pointer to a <a href="kernel.log_file_object">LOG_FILE_OBJECT</a> structure that represents an open instance of the stream.</p>
</dd>

### -param <i>puszLogFileName</i> [in]

<dd>
<p>A pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that supplies the name of the stream or the underlying physical log. </p>
<p>If the stream already exists and is the only stream of a dedicated log, the name has the form log:<i>physical log name</i>, where <i>physical log name</i> is the path name, on the underlying file system, of the existing physical log that contains the stream's records.</p>
<p>If the stream does not already exist and is to become the only stream of a dedicated log (that does not yet exist), the name has the form log:<i>physical log name</i>, where <i>physical log name</i> is the path name, on the underlying file system, of the physical log that will be created to hold the stream's records.</p>
<p>If the stream is (or is to become) one of the streams of a multiplexed log, the name has the form log:<i>physical log name</i>::<i>stream name</i>, where <i>physical log name</i> is the path name, on the underlying file system, of the physical log that holds the stream's records, and <i>stream name</i> is the name of a stream that shares (or will share) that physical log.</p>
<p>If you want to create a multiplexed log that has no streams for the moment, use a name of the form log:<i>physical log name</i>::, where <i>physical log name</i> is the path name, on the underlying file system, of the physical log to be created.</p>
<p>The following list gives some examples of valid names.</p>
<ul>
<li>
<p>"Log:c:\myLog" creates or opens a dedicated log and its one stream.</p>
</li>
<li>
<p>"Log:c:\myCommonLog::" creates a multiplexed log that does not yet have any streams.</p>
</li>
<li>
<p>"Log:c:\myCommonLog::Stream1" creates or opens one of the streams (Stream1) of a multiplexed log.</p>
</li>
</ul>
</dd>

### -param <i>fDesiredAccess</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> that supplies the type of access the client will have (by using the pointer returned in <i>pplfoLog</i>) to the stream. If this parameter is zero, clients can query the stream for its attributes, but cannot read from or write to the stream. This parameter can be zero or any combination of the following flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>GENERIC_READ</p>
</td>
<td>
<p>The client has read access to the stream.</p>
</td>
</tr>
<tr>
<td>
<p>GENERIC_WRITE</p>
</td>
<td>
<p>The client has write access to the stream.</p>
</td>
</tr>
<tr>
<td>
<p>DELETE</p>
</td>
<td>
<p>The client can mark the stream for deletion.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>dwShareMode</i> [in]

<dd>
<p>The sharing mode of the stream, which can be zero (not shared) or any combination of the following flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_SHARE_DELETE</p>
</td>
<td>
<p>Subsequent requests to open the stream with delete access will succeed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_SHARE_READ</p>
</td>
<td>
<p>Subsequent requests to open the stream with read access will succeed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_SHARE_WRITE</p>
</td>
<td>
<p>Subsequent requests to open the stream with write access will succeed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>psdLogFile</i> [in, optional]

<dd>
<p>A pointer to a <a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a> structure that supplies security attributes for the stream. This parameter can be <b>NULL</b>. </p>
</dd>

### -param <i>fCreateDisposition</i> [in]

<dd>
<p>The action to take that depends on whether the stream already exists. This parameter must be set to one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>CREATE_NEW</p>
</td>
<td>
<p>Create a new stream if the stream does not already exits. Fail if the stream already exists.</p>
</td>
</tr>
<tr>
<td>
<p>OPEN_EXISTING</p>
</td>
<td>
<p>Open an existing stream. Fail if the stream does not already exist.</p>
</td>
</tr>
<tr>
<td>
<p>OPEN_ALWAYS</p>
</td>
<td>
<p>Open an existing stream. Create the stream if it does not already exist.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>fCreateOptions</i> [in]

<dd>
<p>A set of flags that specify options to apply when creating or opening the stream. This parameter can be zero or a compatible combination of the following flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_NO_INTERMEDIATE_BUFFERING</p>
</td>
<td>
<p>The stream's records cannot be cached in a driver's internal buffers.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_SYNCHRONOUS_IO_ALERT</p>
</td>
<td>
<p>All operations on the stream are performed synchronously. Any wait on behalf of the caller is subject to premature termination from alerts. If this flag is set, the FILE_SYNCHRONOUS_IO_NONALERT flag must be cleared.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_SYNCHRONOUS_IO_NONALERT</p>
</td>
<td>
<p>All operations on the stream are performed synchronously. Waits in the system that synchronize I/O queuing and completion are not subject to alerts. If this flag is set, the FILE_SYNCHRONOUS_IO_ALERT flag must be cleared.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>fFlagsAndAttributes</i> [in]

<dd>
<p>A value that specifies whether the stream is opened for normal or read-only access. This parameter must be set to either </p>
<p>FILE_ATTRIBUTE_NORMAL or FILE_ATTRIBUTE_READONLY.</p>
</dd>

### -param <i>fLogOptionFlag</i> [in]

<dd>
<p>A hint about the relationship between CLFS and the component creating or opening the stream. This parameter must be set to one of the following values:
	 </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>CLFS_FLAG_NO_FLAGS</p>
</td>
<td>
<p>CLFS and the creating component have the standard, normal relationship. Kernel-mode components use this value unless they fall into one of the three other categories listed in this table. If <i>pvContext</i> is not <b>NULL</b>, CLFS verifies that <i>cbContext</i> is greater than zero. Otherwise, <i>pvContext</i> and <i>cbContext</i> are ignored.</p>
</td>
</tr>
<tr>
<td>
<p>CLFS_FLAG_REENTRANT_FILE_SYSTEM</p>
</td>
<td>
<p>The creating component is the file system that provides the underlying storage for CLFS. CLFS uses the file system for allocating containers, and the file system uses CLFS streams. In this case, it is possible for the file system to call CLFS and for CLFS to make calls back into the file system on the same thread or different threads. If <i>pvContext</i> is not <b>NULL</b>, CLFS verifies that <i>cbContext</i> is greater than zero. Otherwise, <i>pvContext</i> and <i>cbContext</i> are ignored.</p>
</td>
</tr>
<tr>
<td>
<p>CLFS_FLAG_NON_REENTRANT_FILTER</p>
</td>
<td>
<p>The creating component is a file system filter driver that sends all of its CLFS I/O to a specified level below itself on the filter stack. This option allows a filter driver to create a CLFS log without seeing its own logging I/O. The caller passes the non-<b>NULL</b> target device object in the <i>pvContext</i> parameter with <i>cbContext</i> set to the appropriate size. CLFS uses the <a href="..\ntddk\nf-ntddk-iocreatefilespecifydeviceobjecthint.md">IoCreateFileSpecifyDeviceObjectHint</a> routine to create containers at a targeted level in the I/O filter stack specified by the device object.</p>
</td>
</tr>
<tr>
<td>
<p>CLFS_FLAG_REENTRANT_FILTER</p>
</td>
<td>
<p>The creating component is a file system filter driver that sends all of its CLFS I/O to the top of the filter stack. The filter has a recursive relationship with CLFS because it filters its own logging I/O when CLFS performs any file system operation on its containers. The <i>pvContext</i> parameter provides a means for filters to associate a recognizable context with its CLFS containers as log I/O comes down the filter stack. The <i>cbContext</i> parameter specifies the size of the opaque context in bytes.</p>
</td>
</tr>
<tr>
<td>
<p>CLFS_FLAG_MINIFILTER_LEVEL</p>
</td>
<td>
<p>The creating component is a file system minifilter driver that sends all of its CLFS I/O to a specified level below itself on the filter stack. This option allows a minifilter to create a CLFS log  without seeing its own logging I/O. The caller passes the non-<b>NULL</b> minifilter context object in the <i>pvContext</i> parameter with <i>cbContext</i> set to the appropriate size. CLFS uses the <b>IoCreateFileSpecifyDeviceObjectHint</b> routine to create containers at an altitude (specified within the minifilter context) in the filter manager's minifilter stack. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pvContext</i> [in, optional]

<dd>
<p>A pointer to a context. The way the context is interpreted depends on the value passed to <i>fLogOptionsFlag</i>. </p>
</dd>

### -param <i>cbContext</i> [in]

<dd>
<p>The size, in bytes, of the context pointed to by <i>pvContext</i>. If <i>pvContext</i> is not <b>NULL</b>, this parameter must be greater than zero. </p>
</dd>
</dl>

## -returns
<p><b>ClfsCreateLogFile</b> returns STATUS_SUCCESS if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h.</p>

## -remarks
<p>When you create a CLFS stream, it is backed by an underlying physical CLFS log. The underlying log can be either dedicated (backs only one stream) or multiplexed (backs several streams). A dedicated log cannot be converted to a multiplexed log, and a multiplexed log cannot be converted to a dedicated log.</p>

<p>A physical CLFS log name does not include the .blf extension.</p>

<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.sys</dt>
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
<a href="..\wdm\nf-wdm-clfscloseandresetlogfile.md">ClfsCloseAndResetLogFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-clfscloselogfileobject.md">ClfsCloseLogFileObject</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-clfsdeletelogfile.md">ClfsDeleteLogFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-clfsdeletelogbypointer.md">ClfsDeleteLogByPointer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsCreateLogFile routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
