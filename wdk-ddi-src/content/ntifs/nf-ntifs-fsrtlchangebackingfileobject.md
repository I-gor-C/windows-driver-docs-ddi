---
UID: NF.ntifs.FsRtlChangeBackingFileObject
title: FsRtlChangeBackingFileObject
author: windows-driver-content
description: The FsRtlChangeBackingFileObject routine replaces the current file object with a new file object.
old-location: ifsk\fsrtlchangebackingfileobject.htm
old-project: ifsk
ms.assetid: a3ef4644-8e17-4f67-ba7f-61d62c534c26
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlChangeBackingFileObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: The FsRtlChangeBackingFileObject routine is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlChangeBackingFileObject
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FsRtlChangeBackingFileObject function



## -description
<p>The <b>FsRtlChangeBackingFileObject</b> routine replaces the current file object with a new file object.</p>


## -syntax

````
NTSTATUS FsRtlChangeBackingFileObject(
  _In_opt_ PFILE_OBJECT              CurrentFileObject,
  _In_     PFILE_OBJECT              NewFileObject,
  _In_     FSRTL_CHANGE_BACKING_TYPE ChangeBackingType,
  _In_     ULONG                     Flags
);
````


## -parameters
<dl>

### -param <i>CurrentFileObject</i> [in, optional]

<dd>
<p>The current file object. If this object does not belong to the stream, the operation fails.</p>
</dd>

### -param <i>NewFileObject</i> [in]

<dd>
<p>The new file object.</p>
</dd>

### -param <i>ChangeBackingType</i> [in]

<dd>
<p>An <a href="..\ntifs\ne-ntifs--fsrtl-change-backing-type.md">FSRTL_CHANGE_BACKING_TYPE</a> enumeration value that indicates which internal memory area the new file object will designate.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -returns
<p>The <b>FsRtlChangeBackingFileObject</b> routine returns STATUS_SUCCESS if the operation succeeds. Otherwise, <b>FsRtlChangeBackingFileObject</b> returns the appropriate error code.The following table contains error codes that <b>FsRtlChangeBackingFileObject</b> might return.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The change operation failed because the file object that <i>NewFileObject</i> specifies does not represent the same stream as <i>CurrentFileObject</i>.  </p><dl>
<dt><b>STATUS_INVALID_PARAMETER_3</b></dt>
</dl><p>The change operation failed because the caller specified an invalid backing type in <i>ChangeBackingType</i>.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_4</b></dt>
</dl><p>The change operation failed because the caller specified an invalid value in <i>Flags</i>.</p><dl>
<dt><b>STATUS_NOT_SUPPORT</b></dt>
</dl><p>The change operation failed because the caller obtained the file object in a way that does not allow subsequent swapping of the file object. For example, if the caller obtained the file object with a call to <a href="..\ntifs\nf-ntifs-ccgetfileobjectfromsectionptrs.md">CcGetFileObjectFromSectionPtrs</a>, it is not safe to swap the file object.</p>

<p> </p>

## -remarks
<p>The <b>FsRtlChangeBackingFileObject</b> routine changes the file object for one of the following:</p>

<p>One of the memory manager's image control areas for the stream</p>

<p>The memory manager's data control area for the stream</p>

<p>The cache manager's shared cache map for the stream</p>

<p>The <b>FsRtlChangeBackingFileObject</b> routine is not synchronous. It processes the request for a change of file object and returns immediately. The cache manager and the memory manager synchronize the change of the file object and will not free the old file object until all incomplete operations that are associated with the old file object have finished. A return status of STATUS_SUCCESS from <b>FsRtlChangeBackingFileObject</b> does not mean that the operating system has already changed the file object.</p>

<p>However, after <b>FsRtlChangeBackingFileObject</b> runs successfully, the operating system associates all future operations with the new file object.</p>

<p>To change the file object for more than one backing type, the caller must call <b>FsRtlChangeBackingFileObject</b> multiple times, one time for each backing type to change.</p>

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
<p>The FsRtlChangeBackingFileObject routine is available starting with Windows Vista. </p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ne-ntifs--fsrtl-change-backing-type.md">FSRTL_CHANGE_BACKING_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlChangeBackingFileObject routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
