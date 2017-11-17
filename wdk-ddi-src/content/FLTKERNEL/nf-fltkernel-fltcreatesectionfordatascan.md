---
UID: NF.fltkernel.FltCreateSectionForDataScan
title: FltCreateSectionForDataScan
author: windows-driver-content
description: The FltCreateSectionForDataScan routine creates a section object for a file. The filter manager can optionally synchronize I/O with the section created.
old-location: ifsk\fltcreatesectionfordatascan.htm
ms.assetid: D1215495-C737-45B6-BECD-8CB430C71DE8
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: The FltCreateSectionForDataScan routine is available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltCreateSectionForDataScan
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: FltCreateSectionForDataScan
req.iface: 
---

# FltCreateSectionForDataScan function



## -description
<p>The <b>FltCreateSectionForDataScan</b> routine creates a section object for a file. The filter manager can optionally synchronize I/O with the section created.</p>


## -syntax

````
NTSTATUS FltCreateSectionForDataScan(
  _In_      PFLT_INSTANCE      Instance,
  _In_      PFILE_OBJECT       FileObject,
  _In_      PFLT_CONTEXT       SectionContext,
  _In_      ACCESS_MASK        DesiredAccess,
  _In_opt_  POBJECT_ATTRIBUTES ObjectAttributes,
  _In_opt_  PLARGE_INTEGER     MaximumSize,
  _In_      ULONG              SectionPageProtection,
  _In_      ULONG              AllocationAttributes,
  _In_      ULONG              Flags,
  _Out_     PHANDLE            SectionHandle,
  _Out_     PVOID              *SectionObject,
  _Out_opt_ PLARGE_INTEGER     SectionFileSize
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>The opaque instance pointer for the minifilter driver instance whose context is to be retrieved. </p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>The file object for an open file.  The section object will be backed by the specified file. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>SectionContext</i> [in]

<dd>
<p>A pointer to a previously allocated section context. </p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>The type  of access for the section object as one or more of the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> flags. </p>
<table>
<tr>
<th><i>DesiredAccess</i> flag</th>
<th>Allows caller to </th>
</tr>
<tr>
<td>
<p>SECTION_MAP_READ</p>
</td>
<td>
<p>Read views of the section.</p>
</td>
</tr>
<tr>
<td>
<p>SECTION_MAP_WRITE</p>
</td>
<td>
<p>Write views of the section.</p>
</td>
</tr>
<tr>
<td>
<p>SECTION_QUERY</p>
</td>
<td>
<p>Query the section object for information about the section. Drivers should set this flag.</p>
</td>
</tr>
<tr>
<td>
<p>SECTION_ALL_ACCESS</p>
</td>
<td>
<p>All actions defined by the previous flags as well as that defined by STANDARD_RIGHTS_REQUIRED. (For more information about STANDARD_RIGHTS_REQUIRED, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>.) </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>ObjectAttributes</i> [in, optional]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff557749">OBJECT_ATTRIBUTES</a> structure that specifies the object name and other attributes. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547804">InitializeObjectAttributes</a> macro to initialize this structure. Because <b>FltCreateSectionForDataScan</b> inserts this object into the process handle table, the caller must specify the OBJ_KERNEL_HANDLE attribute when it calls <b>InitializeObjectAttributes</b>.</p>
</dd>

### -param <i>MaximumSize</i> [in, optional]

<dd>
<p>This parameter is reserved for future use.</p>
</dd>

### -param <i>SectionPageProtection</i> [in]

<dd>
<p>The protection to place on each page in the section. Specify one of the following values. This parameter is required and cannot be zero. </p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>PAGE_READONLY</p>
</td>
<td>
<p>Enables read-only access to the committed region of pages. An attempt to write to the committed region results in an access violation. If the system differentiates between read-only access and execute access, an attempt to execute code in the committed region results in an access violation.</p>
</td>
</tr>
<tr>
<td>
<p>PAGE_READWRITE</p>
</td>
<td>
<p>Enables both read and write access to the committed region of pages.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>AllocationAttributes</i> [in]

<dd>
<p>Bitmasks of the SEC_<i>XXX</i> flags determine the allocation attributes of the section. Specify one or more of the following values. This parameter is required and cannot be zero. </p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SEC_COMMIT</p>
</td>
<td>
<p>Allocates physical storage in memory or in the paging file on disk for all pages of a section. This is the default setting. Note that this flag is required and cannot be omitted.</p>
</td>
</tr>
<tr>
<td>
<p>SEC_FILE</p>
</td>
<td>
<p>The file specified by the <i>FileObject</i> parameter is a mapped file.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>This parameter is reserved for future use.</p>
</dd>

### -param <i>SectionHandle</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives an opaque handle to the section handle. </p>
</dd>

### -param <i>SectionObject</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives an opaque pointer to the section object.</p>
</dd>

### -param <i>SectionFileSize</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated variable that receives the size, in bytes, of the file at the time the section object was created. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>FltCreateSectionForDataScan</b> returns <b>STATUS_SUCCESS</b> or an appropriate <b>NTSTATUS</b> value, such as one of the following.</p><dl>
<dt><b>STATUS_END_OF_FILE</b></dt>
</dl><p>The size of the file specified by the <i>FileObject</i> parameter is zero.</p><dl>
<dt><b> 
STATUS_FILE_LOCK_CONFLICT</b></dt>
</dl><p> 
The file specified by the <i>FileObject</i> parameter is locked.</p><dl>
<dt><b> 
STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>FltCreateSectionForDataScan</b> encountered a pool allocation failure.</p><dl>
<dt><b>STATUS_INVALID_FILE_FOR_SECTION</b></dt>
</dl><p>The file specified by the <i>FileObject</i> parameter does not support sections.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The minifilter is not registered.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_8</b></dt>
</dl><p>The value specified for the <i>SectionPageProtection</i> parameter is invalid.</p><dl>
<dt><b> 
STATUS_INVALID_PARAMETER_9</b></dt>
</dl><p> 
The caller specified an invalid value for the <i>AllocationAttributes</i> parameter.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The volume attached to this instance does not support section contexts.</p><dl>
<dt><b>STATUS_PRIVILEGE_NOT_HELD</b></dt>
</dl><p>
The caller did not have the required privileges to create a section object with the access specified in the <i>DesiredAccess</i> parameter.</p><dl>
<dt><b>STATUS_FILE_IS_A_DIRECTORY</b></dt>
</dl><p>
The file specified by the <i>FileObject</i> parameter is a directory.</p><dl>
<dt><b>STATUS_FLT_CONTEXT_ALREADY_DEFINED</b></dt>
</dl><p>The filter instance specified by <i>Instance</i> already has an open section for the stream. Only one section per stream, and therefore, per instance is supported.</p>

<p> </p>

## -remarks
<p>Prior to calling <b>FltCreateSectionForDataScan</b>, a minifilter must  first register its volume for data scanning by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451038">FltRegisterForDataScan</a>. As with other filter context elements, <i>SectionContext</i> is first allocated with <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>Certain situations can occur where holding a section open is incompatible with current file I/O. In particular, file I/O that triggers a cache purge can cause cache incoherency if the cache purge is prevented because of an open section.  A minifilter can provide an optional callback routine for notifications of these events. The minifilter driver implements a <a href="https://msdn.microsoft.com/library/windows/hardware/hh439452">PFLT_SECTION_CONFLICT_NOTIFICATION_CALLBACK</a> to receive these notifications. Conflict notifications are enabled if the <b>SectionNotificationCallback</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> is set to this callback routine when the minifilter is registered. When a notification is received, the section can be closed to allow the conflicting I/O operation to continue. </p>

<p>When the section object created by this routine is no longer necessary, be sure to close the section object's handle (<i>SectionHandle</i>) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> routine and dereference the section object itself (<i>SectionObject</i>) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> routine.</p>

<p>For overview  information on creating mapped sections and views of memory, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563684">Section Objects and Views</a>. Also, see the documentation for the <b>CreateFileMapping</b> routine in the Microsoft Windows SDK. </p><p class="note">Minifilters must not explicitly delete a section context passed to <b>FltCreateSectionForDataScan</b>. Do not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a> after a section context is passed to  <b>FltCreateSectionForDataScan</b>. A section context is deallocated and removed from a stream  by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh406456">FltCloseSectionForDataScan</a> in this case.</p><p class="note">In general, sections should be created as read-only. In particular, if a read-only file is in a transaction  and a minifilter does not create a read-only section, a write to the section is discarded and is not included as part of the transaction.</p>

<p>Prior to calling <b>FltCreateSectionForDataScan</b>, a minifilter must  first register its volume for data scanning by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451038">FltRegisterForDataScan</a>. As with other filter context elements, <i>SectionContext</i> is first allocated with <a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>. </p>

<p>Certain situations can occur where holding a section open is incompatible with current file I/O. In particular, file I/O that triggers a cache purge can cause cache incoherency if the cache purge is prevented because of an open section.  A minifilter can provide an optional callback routine for notifications of these events. The minifilter driver implements a <a href="https://msdn.microsoft.com/library/windows/hardware/hh439452">PFLT_SECTION_CONFLICT_NOTIFICATION_CALLBACK</a> to receive these notifications. Conflict notifications are enabled if the <b>SectionNotificationCallback</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> is set to this callback routine when the minifilter is registered. When a notification is received, the section can be closed to allow the conflicting I/O operation to continue. </p>

<p>When the section object created by this routine is no longer necessary, be sure to close the section object's handle (<i>SectionHandle</i>) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> routine and dereference the section object itself (<i>SectionObject</i>) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a> routine.</p>

<p>For overview  information on creating mapped sections and views of memory, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563684">Section Objects and Views</a>. Also, see the documentation for the <b>CreateFileMapping</b> routine in the Microsoft Windows SDK. </p><p class="note">Minifilters must not explicitly delete a section context passed to <b>FltCreateSectionForDataScan</b>. Do not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541960">FltDeleteContext</a> after a section context is passed to  <b>FltCreateSectionForDataScan</b>. A section context is deallocated and removed from a stream  by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh406456">FltCloseSectionForDataScan</a> in this case.</p><p class="note">In general, sections should be created as read-only. In particular, if a read-only file is in a transaction  and a minifilter does not create a read-only section, a write to the section is discarded and is not included as part of the transaction.</p>

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
<p>The <b>FltCreateSectionForDataScan</b> routine is available starting with  Windows 8.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539188">CcPurgeCacheSection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541710">FltAllocateContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406456">FltCloseSectionForDataScan</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451038">FltRegisterForDataScan</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557724">ObDereferenceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439452">PFLT_SECTION_CONFLICT_NOTIFICATION_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566428">ZwCreateSection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCreateSectionForDataScan routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
