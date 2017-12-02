---
UID: NF.fltkernel.FltSetQuotaInformationFile
title: FltSetQuotaInformationFile
author: windows-driver-content
description: The FltSetQuotaInformationFile routine modifies quota entries for a file object.
old-location: ifsk\fltsetquotainformationfile.htm
old-project: ifsk
ms.assetid: 89EC9F5C-24AE-4340-99CF-05323F99B465
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltSetQuotaInformationFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltSetQuotaInformationFile
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

# FltSetQuotaInformationFile function



## -description
<p>The <b>FltSetQuotaInformationFile</b> routine modifies quota entries for a file object. </p>


## -syntax

````
NTSTATUS FltSetQuotaInformationFile(
  _In_ PFLT_INSTANCE Instance,
  _In_ PFILE_OBJECT  FileObject,
  _In_ PVOID         Buffer,
  _In_ ULONG         Length
);
````


## -parameters
<dl>

### -param Instance [in]

<dd>
<p>An opaque instance pointer for the minifilter driver instance that the operation is to be sent to. The instance must be attached to the volume where the file resides. </p>
</dd>

### -param FileObject [in]

<dd>
<p>The file object pointer for the file. </p>
</dd>

### -param Buffer [in]

<dd>
<p>A pointer to a caller-supplied, <a href="..\ntifs\ns-ntifs--file-get-quota-information.md">FILE_GET_QUOTA_INFORMATION</a>-structured input buffer that contains the quota information entries to be set. </p>
</dd>

### -param Length [in]

<dd>
<p>The length, in bytes, of the buffer that the <i>Buffer</i> parameter points to. </p>
</dd>
</dl>

## -returns
<p><b>FltSetQuotaInformationFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following. </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The instance or volume is being torn down. This is an error code. </p>

<p> </p>

## -remarks


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
<p>Available starting with  Windows 8.</p>
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
<a href="..\ntifs\ns-ntifs--file-get-quota-information.md">FILE_GET_QUOTA_INFORMATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltqueryquotainformationfile.md">FltQueryQuotaInformationFile</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwsetquotainformationfile.md">ZwSetQuotaInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSetQuotaInformationFile function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
