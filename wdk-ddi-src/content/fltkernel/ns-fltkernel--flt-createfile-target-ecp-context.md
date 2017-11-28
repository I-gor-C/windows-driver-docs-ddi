---
UID: NS.fltkernel._FLT_CREATEFILE_TARGET_ECP_CONTEXT
title: FLT_CREATEFILE_TARGET_ECP_CONTEXT
author: windows-driver-content
description: The FLT_CREATEFILE_TARGET_ECP_CONTEXT structure is an extra create parameter (ECP) used to return reparse target information back to the caller of FltCreateFileEx2.
old-location: ifsk\flt_createfile_target_ecp_context.htm
old-project: ifsk
ms.assetid: 95BDB715-E476-48EF-9867-112CF665B66D
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FLT_CREATEFILE_TARGET_ECP_CONTEXT, FLT_CREATEFILE_TARGET_ECP_CONTEXT, *PFLT_CREATEFILE_TARGET_ECP_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FLT_CREATEFILE_TARGET_ECP_CONTEXT
req.alt-loc: fltkernel.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FLT_CREATEFILE_TARGET_ECP_CONTEXT structure



## -description
<p>The <b>FLT_CREATEFILE_TARGET_ECP_CONTEXT</b> structure is an extra create parameter (ECP) used to return reparse target information back to the caller of <a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a>.</p>


## -syntax

````
typedef struct _FLT_CREATEFILE_TARGET_ECP_CONTEXT {
  PFLT_INSTANCE               Instance;
  PFLT_VOLUME                 Volume;
  PFLT_FILE_NAME_INFORMATION  FileNameInformation;
  FLT_CREATEFILE_TARGET_FLAGS Flags;
} FLT_CREATEFILE_TARGET_ECP_CONTEXT, *PFLT_CREATEFILE_TARGET_ECP_CONTEXT;
````


## -struct-fields
<dl>

### -field <b>Instance</b>

<dd>
<p>The filter instance attached to the adjusted target.</p>
</dd>

### -field <b>Volume</b>

<dd>
<p>The adjusted target volume.</p>
</dd>

### -field <b>FileNameInformation</b>

<dd>
<p>The file information for the adjusted target.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags controlling the reparse operation. This value can be either 0 or the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="FLTTCFL_AUTO_REPARSE"></a><a id="flttcfl_auto_reparse"></a><dl>

### -field <b>FLTTCFL_AUTO_REPARSE</b>

</dl>
</td>
<td width="60%">
<p>Request that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a> attempt a reparse operation when a target is not found with the original file information.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>When a caller of <a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a> wishes to  enable reparsing for a volume target, a <b>FLT_CREATEFILE_TARGET_ECP_CONTEXT</b> can be included as an ECP to the ECP list in the <i>DriverContext</i> parameter.  If this ECP is present, <b>FltCreateFileEx2</b> will adjust the target device for the create operation and attempt for find a filtered instance  of a volume appropriate for the given file information. If filter manager does not find a corresponding instance for the caller on the target volume, it will set the <b>Volume</b> and  <b>FileNameInformation</b> members of <b>FLT_CREATEFILE_TARGET_ECP_CONTEXT</b> for the new target. The caller can then use this information to decide how best to proceed.</p>

<p>If the caller of <a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a> intends to handle the reparse operation itself, the <b>FLTTCFL_AUTO_REPARSE</b> flag is cleared from the <b>Flags</b> member. In this case, <b>FltCreateFileEx2</b> will place the initial target adjustment information in the ECP and then will return, ending the file create attempt.</p>

<p> If  the values in <b>Instance</b>, <b>Volume</b>, or <b>FileNameInformation</b> are set in an acknowledged ECP, they are referenced objects. A caller of <a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a> is responsible for calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a> for <b>Instance</b> and <b>Volume</b>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff544320">FltReleaseFileNameInformation</a> for <b>FileNameInformation</b>.</p>

<p>The following example routine demonstrates how a minifilter can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a> with <b>FLT_CREATEFILE_TARGET_ECP_CONTEXT</b> to handle a reparse to a different volume when required to find a file target.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available starting with Windows 8. </p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544320">FltReleaseFileNameInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FLT_CREATEFILE_TARGET_ECP_CONTEXT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
