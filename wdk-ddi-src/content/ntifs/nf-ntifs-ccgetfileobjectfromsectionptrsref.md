---
UID: NF.ntifs.CcGetFileObjectFromSectionPtrsRef
title: CcGetFileObjectFromSectionPtrsRef
author: windows-driver-content
description: When passed a pointer to a SECTION_OBJECT_POINTERS structure for a cached file, the CcGetFileObjectFromSectionPtrsRef routine returns a pointer to the file object that the cache manager is using for the cached file.
old-location: ifsk\ccgetfileobjectfromsectionptrsref.htm
old-project: ifsk
ms.assetid: 8afbd8df-95fc-453f-a1d8-400a993c286a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcGetFileObjectFromSectionPtrsRef
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcGetFileObjectFromSectionPtrsRef
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
req.irql: 
req.iface: 
---

# CcGetFileObjectFromSectionPtrsRef function



## -description
<p>When passed a pointer to a SECTION_OBJECT_POINTERS structure for a cached file, the <b>CcGetFileObjectFromSectionPtrsRef</b> routine returns a pointer to the file object that the cache manager is using for the cached file.</p>


## -syntax

````
PFILE_OBJECT CcGetFileObjectFromSectionPtrsRef(
  _In_ PSECTION_OBJECT_POINTERS SectionObjectPointer
);
````


## -parameters
<dl>

### -param <i>SectionObjectPointer</i> [in]

<dd>
<p>A pointer to the <a href="..\wdm\ns-wdm--section-object-pointers.md">SECTION_OBJECT_POINTERS</a> structure that is associated with the cached file.</p>
</dd>
</dl>

## -returns
<p>A pointer to the file object for the cached file, or <b>NULL</b> if the file is not cached or is no longer cached.</p>

## -remarks
<p>The file object is returned with a reference.  The caller is responsible for calling <a href="..\wdm\nf-wdm-obdereferenceobject.md">ObDereferenceObject</a> on the file object when it has finished using the file object.</p>

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
<p>Available in Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-ccgetfileobjectfromsectionptrs.md">CcGetFileObjectFromSectionPtrs</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-obdereferenceobject.md">ObDereferenceObject</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--section-object-pointers.md">SECTION_OBJECT_POINTERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcGetFileObjectFromSectionPtrsRef routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
