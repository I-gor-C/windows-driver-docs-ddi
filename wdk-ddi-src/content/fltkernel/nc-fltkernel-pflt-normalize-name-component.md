---
UID: NC.fltkernel.PFLT_NORMALIZE_NAME_COMPONENT
title: PFLT_NORMALIZE_NAME_COMPONENT
author: windows-driver-content
description: A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_NORMALIZE_NAME_COMPONENT as the minifilter driver's NormalizeNameComponentCallback routine.
old-location: ifsk\pflt_normalize_name_component.htm
old-project: ifsk
ms.assetid: 7050e872-3976-4842-9d16-50caf415acbc
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IXpsPartIterator, Reset, IXpsPartIterator::Reset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NormalizeNameComponentCallback
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
req.iface: IXpsPartIterator
---

# PFLT_NORMALIZE_NAME_COMPONENT callback



## -description
<p>A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_NORMALIZE_NAME_COMPONENT as the minifilter driver's <i>NormalizeNameComponentCallback</i> routine. </p>


## -prototype

````
PFLT_NORMALIZE_NAME_COMPONENT NormalizeNameComponentCallback;

NTSTATUS NormalizeNameComponentCallback(
  _In_    PFLT_INSTANCE            Instance,
  _In_    PCUNICODE_STRING         ParentDirectory,
  _In_    USHORT                   VolumeNameLength,
  _In_    PCUNICODE_STRING         Component,
  _Out_   PFILE_NAMES_INFORMATION  ExpandComponentName,
  _In_    ULONG                    ExpandComponentNameLength,
  _In_    FLT_NORMALIZE_NAME_FLAGS Flags,
  _Inout_ PVOID                    *NormalizationContext
)
{ ... }
````


## -parameters
<dl>

### -param Instance [in]

<dd>
<p>Opaque instance pointer for the minifilter driver instance that this callback routine is registered for. </p>
</dd>

### -param ParentDirectory [in]

<dd>
<p>Pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains the name of the parent directory for this name component. </p>
</dd>

### -param VolumeNameLength [in]

<dd>
<p>Length, in bytes, of the parent directory name stored in the structure that the <i>ParentDirectory</i> parameter points to. </p>
</dd>

### -param Component [in]

<dd>
<p>Pointer to a UNICODE_STRING structure that contains the name component to be expanded. </p>
</dd>

### -param ExpandComponentName [out]

<dd>
<p>Pointer to a <a href="..\ntifs\ns-ntifs--file-names-information.md">FILE_NAMES_INFORMATION</a> structure that receives the expanded (normalized) file name information for the name component. </p>
</dd>

### -param ExpandComponentNameLength [in]

<dd>
<p>Length, in bytes, of the buffer that the <i>ExpandComponentName</i> parameter points to. </p>
</dd>

### -param Flags [in]

<dd>
<p>Name normalization flags.  FLTFL_NORMALIZE_NAME_CASE_SENSITIVE specifies that the name to be normalized is case-sensitive.  FLTFL_NORMALIZE_NAME_DESTINATION_FILE_NAME specifies that the callback routine has been called to service a <a href="..\fltkernel\nf-fltkernel-fltgetdestinationfilenameinformation.md">FltGetDestinationFileNameInformation</a> routine call.</p>
</dd>

### -param NormalizationContext [in, out]

<dd>
<p>Pointer to minifilter driver-provided context information to be passed in any subsequent calls to this callback routine that are made to normalize the remaining components in the same file name path. </p>
</dd>
</dl>

## -returns
<p>This callback routine returns STATUS_SUCCESS or an appropriate NTSTATUS value. If the name component that the <i>Component</i> parameter specifies does not exist in the parent directory that the <i>ParentDirectory</i> parameter specifies, this callback routine should return STATUS_NO_SUCH_FILE. If this callback routine issues an IRP_MN_QUERY_DIRECTORY (FileNamesInformation) request to the parent directory, the file system returns the correct status code. In this situation, this callback can simply return the status code that the file system returns.</p>

## -remarks
<p>A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_NORMALIZE_NAME_COMPONENT as the minifilter driver's <i>NormalizeNameComponentCallback</i> routine. </p>

<p>To register this callback routine, the minifilter driver stores the address of a routine of type PFLT_NORMALIZE_NAME_COMPONENT in the <b>NormalizeNameComponentCallback</b> member of the <a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a> structure that the minifilter driver passes as a parameter to <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>. </p>

<p>The filter manager calls this callback routine to query the minifilter driver for the normalized names for components in the file name path whose names the minifilter driver has modified. If the file name path contains more than one such component, the filter manager can call this callback routine multiple times in the process of normalizing all the components in the path. The minifilter driver can use the <i>NormalizationContext</i> parameter to pass context information to subsequent calls to this callback routine. </p>

<p>If the minifilter driver uses the <i>NormalizationContext</i> parameter, it should also register a normalization context cleanup callback routine. For more information, see the reference entry for <a href="..\fltkernel\nc-fltkernel-pflt-normalize-context-cleanup.md">PFLT_NORMALIZE_CONTEXT_CLEANUP</a>. </p>

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
<a href="..\ntifs\ns-ntifs--file-names-information.md">FILE_NAMES_INFORMATION</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-generate-file-name.md">PFLT_GENERATE_FILE_NAME</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-normalize-context-cleanup.md">PFLT_NORMALIZE_CONTEXT_CLEANUP</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-normalize-name-component-ex.md">PFLT_NORMALIZE_NAME_COMPONENT_EX</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_NORMALIZE_NAME_COMPONENT routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
