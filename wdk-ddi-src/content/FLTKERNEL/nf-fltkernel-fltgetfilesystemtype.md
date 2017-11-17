---
UID: NF.fltkernel.FltGetFileSystemType
title: FltGetFileSystemType
author: windows-driver-content
description: The FltGetFileSystemType function takes a volume or instance object and provides the file system type of the volume.
old-location: ifsk\fltgetfilesystemtype.htm
ms.assetid: 9e603d0f-74e7-4715-b3dc-4a9623f98dde
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetFileSystemType
req.alt-loc: FltMgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: FltMgr.sys
req.irql: <= APC_LEVEL
ms.keywords: FltGetFileSystemType
req.iface: 
---

# FltGetFileSystemType function



## -description
<p>The <b>FltGetFileSystemType</b> function takes a volume or instance object and provides the file system type of the volume.</p>


## -syntax

````
NTSTATUS FltGetFileSystemType(
  _In_  PVOID                FltObject,
  _Out_ PFLT_FILESYSTEM_TYPE FileSystemType
);
````


## -parameters
<dl>

### -param <i>FltObject</i> [in]

<dd>
<p>A pointer to a filter object. This can be a FLT_INSTANCE or FLT_VOLUME object. </p>
</dd>

### -param <i>FileSystemType</i> [out]

<dd>
<p>A pointer to a user allocated FLT_FILESYSTEM_TYPE object that receives the file system type for <i>FltObject</i>. </p>
</dd>
</dl>

## -returns
<p><b>FltGetFileSystemType</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>FltObject</i> object was not a FLT_INSTANCE  or FLT_VOLUME  object. </p>

<p> </p>

## -remarks
<p>If an instance is passed as the <i>FltObject</i>, <b>FltGetFileSystemType</b> provides the file system type for the volume referred to by the instance object. </p>

<p>If STATUS_INVALID_PARAMETER is returned, the <i>FileSystemType</i> parameter is set to FLT_FSTYPE_UNKNOWN. </p>

<p>If an instance is passed as the <i>FltObject</i>, <b>FltGetFileSystemType</b> provides the file system type for the volume referred to by the instance object. </p>

<p>If STATUS_INVALID_PARAMETER is returned, the <i>FileSystemType</i> parameter is set to FLT_FSTYPE_UNKNOWN. </p>

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
<dt>FltMgr.sys</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543206">FltGetVolumeFromFileObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543214">FltGetVolumeFromInstance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543220">FltGetVolumeFromName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543230">FltGetVolumeGuidName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543238">FltGetVolumeInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543239">FltGetVolumeInstanceFromName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543249">FltGetVolumeName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543254">FltGetVolumeProperties</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543361">FltIsVolumeWritable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetFileSystemType function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
