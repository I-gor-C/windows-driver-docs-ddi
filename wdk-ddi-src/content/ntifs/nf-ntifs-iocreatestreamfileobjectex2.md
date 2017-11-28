---
UID: NF.ntifs.IoCreateStreamFileObjectEx2
title: IoCreateStreamFileObjectEx2
author: windows-driver-content
description: The IoCreateStreamFileObjectEx2 routine creates a new stream file object with create options for a target device object.
old-location: ifsk\iocreatestreamfileobjectex2.htm
old-project: ifsk
ms.assetid: 2F12F4E5-21C2-4DA8-9111-0087A16F0256
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IoCreateStreamFileObjectEx2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoCreateStreamFileObjectEx
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE
req.iface: 
---

# IoCreateStreamFileObjectEx2 function



## -description
<p>The <b>IoCreateStreamFileObjectEx2</b> routine creates a new stream file object with create options for a target device object. </p>


## -syntax

````
PFILE_OBJECT IoCreateStreamFileObjectEx(
  _In_      PIO_CREATE_STREAM_FILE_OPTIONS CreateOptions,
  _In_opt_  PFILE_OBJECT                   FileObject,
  _In_opt_  PDEVICE_OBJECT                 DeviceObject,
  _Out_     PDEVICE_OBJECT                 *StreamFileObject,
  _Out_opt_ PHANDLE                        FileHandle
);
````


## -parameters
<dl>

### -param <i>CreateOptions</i> [in]

<dd>
<p>Pointer a <b>IO_CREATE_STREAM_FILE_OPTIONS</b> structure containing the create options for the new stream file object.  <b>IO_CREATE_STREAM_FILE_OPTIONS</b> is defined in <i>ntifs.h</i> as the following.</p>
<pre class="syntax" xml:space="preserve"><code>typedef struct _IO_CREATE_STREAM_FILE_OPTIONS {
    USHORT Size;
    USHORT Flags;
    PDEVICE_OBJECT TargetDeviceObject;
} IO_CREATE_STREAM_FILE_OPTIONS, *PIO_CREATE_STREAM_FILE_OPTIONS;
</code></pre>
<p></p>
<dl>

### -param <a id="Size"></a><a id="size"></a><a id="SIZE"></a>Size

<dd>
<p>Size of the stream options structure. Set to <b>sizeof</b>(IO_CREATE_STREAM_FILE_OPTIONS).</p>
</dd>

### -param <a id="Flags"></a><a id="flags"></a><a id="FLAGS"></a>Flags

<dd>
<p>The flags for the stream file create options. This value can be one of the following.</p>
<p></p>
<table>
<tr>
<th>Term</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<p><a id="IO_CREATE_STREAM_FILE_RAISE_ON_ERROR"></a><a id="io_create_stream_file_raise_on_error"></a>IO_CREATE_STREAM_FILE_RAISE_ON_ERROR</p>
</td>
<td width="60%">
<p>On an error condition, <b>IoCreateStreamFileObjectEx2</b> will raise the error
        status as an exception instead of returning it.  This flag is specified to maintain error status behavior of the other stream file object creation routines.</p>
</td>
</tr>
<tr>
<td width="40%">
<p><a id="IO_CREATE_STREAM_FILE_LITE"></a><a id="io_create_stream_file_lite"></a>IO_CREATE_STREAM_FILE_LITE</p>
</td>
<td width="60%">
<p>A file object is created with out a file handle. No close operation is sent for the file object when it is deleted.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <a id="TargetDeviceObject"></a><a id="targetdeviceobject"></a><a id="TARGETDEVICEOBJECT"></a>TargetDeviceObject

<dd>
<p>A pointer to the device object to set as the target for operations on the file
        handle.  <b>TargetDeviceObject</b> must be in the same device stack as <i>DeviceObject</i> parameter.  This
        member is optional.</p>
</dd>
</dl>
</dd>

### -param <i>FileObject</i> [in, optional]

<dd>
<p>Pointer to the file object to which the new stream file is related. This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param <i>DeviceObject</i> [in, optional]

<dd>
<p>Pointer to a device object for the device on which the stream file is to be opened. If the caller specifies a non-<b>NULL</b> value for <i>FileObject</i>, the value of <i>DeviceObject</i> is ignored. Otherwise, the caller must specify a non-<b>NULL</b> value for <i>DeviceObject</i>. </p>
</dd>

### -param <i>StreamFileObject</i> [out]

<dd>
<p>Pointer to a device object pointer to receive the stream fille object.</p>
</dd>

### -param <i>FileHandle</i> [out, optional]

<dd>
<p>A pointer to a file handle for the stream on output. This parameter is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>IoCreateStreamFileObjectEx2</b> returns a pointer to the newly created stream file object.</p>

## -remarks
<p>File systems call <b>IoCreateStreamFileObjectEx2</b> to create a new stream file object. A <i>stream file object</i> is identical to an ordinary file object, except that the<b> FO_STREAM_FILE</b> file object flag is set.</p>

<p>A stream file object is commonly used to represent an internal stream for a volume mounted by the file system. This <i>virtual volume file</i> permits the file system to view, change, and cache the volume's on-disk structure as if it were an ordinary file. In this case, the <i>DeviceObject</i> parameter in the call to <b>IoCreateStreamFileObjectEx2</b> specifies the volume device object (VDO) for the volume.</p>

<p>A stream file object can also be used to represent an alternate data stream for accessing a file's metadata, such as extended attributes or security descriptors. In this case, the <i>FileObject</i> parameter in the call to <b>IoCreateStreamFileObjectEx2</b> specifies an existing file object for the file. The newly created stream file object permits the file system to view, change, and cache the file's metadata as if it were an ordinary file.</p>

<p>When the stream file object is no longer needed, the caller must decrement its reference count by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>. When the stream file object's reference count reaches zero, an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> request is sent to the file system driver stack for the volume.</p>

<p>File system filter driver writers should note that <b>IoCreateStreamFileObjectEx2</b> causes an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548608">IRP_MJ_CLEANUP</a> request to be sent to the file system driver stack for the volume. Because file systems often create stream file objects as a side effect of operations other than <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>, it is difficult for filter drivers to reliably detect stream file object creation. Thus a filter driver should expect to receive I<b>IRP_MJ_CLEANUP</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> requests for previously unseen file objects.</p>

<p>If a pool allocation failure occurs, <b>IoCreateStreamFileObjectEx2</b> raises a <b>STATUS_INSUFFICIENT_RESOURCES</b> exception.</p>

<p>File systems call <b>IoCreateStreamFileObjectEx2</b> to create a new stream file object. A <i>stream file object</i> is identical to an ordinary file object, except that the<b> FO_STREAM_FILE</b> file object flag is set.</p>

<p>A stream file object is commonly used to represent an internal stream for a volume mounted by the file system. This <i>virtual volume file</i> permits the file system to view, change, and cache the volume's on-disk structure as if it were an ordinary file. In this case, the <i>DeviceObject</i> parameter in the call to <b>IoCreateStreamFileObjectEx2</b> specifies the volume device object (VDO) for the volume.</p>

<p>A stream file object can also be used to represent an alternate data stream for accessing a file's metadata, such as extended attributes or security descriptors. In this case, the <i>FileObject</i> parameter in the call to <b>IoCreateStreamFileObjectEx2</b> specifies an existing file object for the file. The newly created stream file object permits the file system to view, change, and cache the file's metadata as if it were an ordinary file.</p>

<p>When the stream file object is no longer needed, the caller must decrement its reference count by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>. When the stream file object's reference count reaches zero, an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> request is sent to the file system driver stack for the volume.</p>

<p>File system filter driver writers should note that <b>IoCreateStreamFileObjectEx2</b> causes an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548608">IRP_MJ_CLEANUP</a> request to be sent to the file system driver stack for the volume. Because file systems often create stream file objects as a side effect of operations other than <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>, it is difficult for filter drivers to reliably detect stream file object creation. Thus a filter driver should expect to receive I<b>IRP_MJ_CLEANUP</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> requests for previously unseen file objects.</p>

<p>If a pool allocation failure occurs, <b>IoCreateStreamFileObjectEx2</b> raises a <b>STATUS_INSUFFICIENT_RESOURCES</b> exception.</p>

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
<p>Available starting with Windows 8.</p>
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
<p>PASSIVE</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548296">IoCreateStreamFileObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548303">IoCreateStreamFileObjectEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548306">IoCreateStreamFileObjectLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548608">IRP_MJ_CLEANUP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoCreateStreamFileObjectEx2 routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
