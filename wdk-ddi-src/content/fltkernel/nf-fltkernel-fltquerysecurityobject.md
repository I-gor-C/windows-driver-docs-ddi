---
UID: NF.fltkernel.FltQuerySecurityObject
title: FltQuerySecurityObject
author: windows-driver-content
description: FltQuerySecurityObject retrieves a copy of an object's security descriptor.
old-location: ifsk\fltquerysecurityobject.htm
old-project: ifsk
ms.assetid: 388dc11d-79cc-4e6b-bce0-b99cca556342
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltQuerySecurityObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltQuerySecurityObject
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FltQuerySecurityObject function



## -description
<p><b>FltQuerySecurityObject</b> retrieves a copy of an object's security 
   descriptor.</p>


## -syntax

````
NTSTATUS FltQuerySecurityObject(
  _In_      PFLT_INSTANCE        Instance,
  _In_      PFILE_OBJECT         FileObject,
  _In_      SECURITY_INFORMATION SecurityInformation,
  _Inout_   PSECURITY_DESCRIPTOR SecurityDescriptor,
  _In_      ULONG                Length,
  _Out_opt_ PULONG               LengthNeeded
);
````


## -parameters
<dl>

### -param Instance [in]

<dd>
<p>Opaque instance pointer for the caller. This parameter is required and cannot be 
      <b>NULL</b>.</p>
</dd>

### -param FileObject [in]

<dd>
<p>File object pointer for the object whose security descriptor is being queried. This parameter is required 
      and cannot be <b>NULL</b>.</p>
</dd>

### -param SecurityInformation [in]

<dd>
<p>
<a href="ifsk.security_information">SECURITY_INFORMATION</a> value. This parameter is 
       required and must be one of the following:</p>
<table>
<tr>
<th>SecurityInformation Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>OWNER_SECURITY_INFORMATION</p>
</td>
<td>
<p>The owner identifier of the object is being queried. Requires <b>READ_CONTROL</b> 
          access.</p>
</td>
</tr>
<tr>
<td>
<p>GROUP_SECURITY_INFORMATION</p>
</td>
<td>
<p>The primary group identifier of the object is being queried. Requires 
          <b>READ_CONTROL</b> access.</p>
</td>
</tr>
<tr>
<td>
<p>DACL_SECURITY_INFORMATION</p>
</td>
<td>
<p>The discretionary access control list (DACL) of the object is being queried. Requires 
          <b>READ_CONTROL</b> access.</p>
</td>
</tr>
<tr>
<td>
<p>SACL_SECURITY_INFORMATION</p>
</td>
<td>
<p>The system ACL (SACL) of the object is being queried. Requires 
          <b>ACCESS_SYSTEM_SECURITY</b> access.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param SecurityDescriptor [in, out]

<dd>
<p>Pointer to a caller-supplied output buffer that receives a copy of the security descriptor for the 
      specified object. The <a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a> 
      structure is returned in self-relative format. This parameter is optional and can be 
      <b>NULL</b>.</p>
</dd>

### -param Length [in]

<dd>
<p>Size, in bytes, of the <i>SecurityDescriptor</i> buffer.</p>
</dd>

### -param LengthNeeded [out, optional]

<dd>
<p>Pointer to a caller-allocated variable that receives the number of bytes required to store the copied 
      security descriptor returned in the buffer pointed to by the <i>SecurityDescriptor</i> 
      parameter. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>FltQuerySecurityObject</b> returns STATUS_SUCCESS or an appropriate 
      <b>NTSTATUS</b> value such as one of the following:</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The caller did not have the required access. This is an error code.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer is too small to contain the security descriptor. None of the security information was copied 
        to the buffer. This is an error code.</p>

<p> </p>

## -remarks
<p>A security descriptor can be in absolute or self-relative form. In self-relative form, all members of the 
     structure are located contiguously in memory. In absolute form, the structure contains only pointers to its 
     members.</p>

<p>The NTFS file system imposes a 64-KB limit on the size of the security descriptor that is written to disk for a 
     file. (The FAT file system does not support security descriptors for files.) Thus, a 64-KB buffer pointed to by 
     the <i>SecurityDescriptor</i> parameter is guaranteed to be large enough to hold the returned 
     <a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a> structure.</p>

<p>The object that the <i>FileObject</i> parameter points to can represent a named data stream. 
     For more information about named data streams, see 
     <a href="..\ntifs\ns-ntifs--file-stream-information.md">FILE_STREAM_INFORMATION</a>.</p>

<p>For more information about security and access control, see the Microsoft Windows SDK documentation.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ns-ntifs--file-stream-information.md">FILE_STREAM_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="ifsk.security_information">SECURITY_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltQuerySecurityObject function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
