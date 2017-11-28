---
UID: NC.fltkernel.PFLT_GENERATE_FILE_NAME
title: PFLT_GENERATE_FILE_NAME
author: windows-driver-content
description: A minifilter driver that provides file names for the filter manager's name cache can register a routine of type PFLT_GENERATE_FILE_NAME as the minifilter driver's GenerateFileNameCallback routine.
old-location: ifsk\pflt_generate_file_name.htm
old-project: ifsk
ms.assetid: 04e7e4db-2cf6-4312-8964-2c69c96953a3
ms.author: windowsdriverdev
ms.date: 11/14/2017
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
req.alt-api: GenerateFileNameCallback
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

# PFLT_GENERATE_FILE_NAME callback



## -description
<p>A minifilter driver that provides file names for the filter manager's name cache can register a routine of type <i>PFLT_GENERATE_FILE_NAME</i> as the minifilter driver's <i>GenerateFileNameCallback</i> routine. </p>


## -prototype

````
PFLT_GENERATE_FILE_NAME GenerateFileNameCallback;

NTSTATUS GenerateFileNameCallback(
  _In_     PFLT_INSTANCE         Instance,
  _In_     PFILE_OBJECT          FileObject,
  _In_opt_ PFLT_CALLBACK_DATA    CallbackData,
  _In_     FLT_FILE_NAME_OPTIONS NameOptions,
  _Out_    PBOOLEAN              CacheFileNameInformation,
  _Out_    PFLT_NAME_CONTROL     FileName
)
{ ... }
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the minifilter driver instance that this callback routine is registered for. </p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>A pointer to a file object for the file whose name is being requested. </p>
</dd>

### -param <i>CallbackData</i> [in, optional]

<dd>
<p>A pointer to the callback data structure for the operation during which this name is being requested. This parameter is <b>NULL</b> when <a href="https://msdn.microsoft.com/library/windows/hardware/ff543035">FltGetFileNameInformationUnsafe</a> is called to retrieve the name of the file.</p>
</dd>

### -param <i>NameOptions</i> [in]

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544636">FLT_FILE_NAME_OPTIONS</a> value that specifies the name format, query method, and flags for this file name information query. </p>
</dd>

### -param <i>CacheFileNameInformation</i> [out]

<dd>
<p>A pointer to a Boolean value specifying whether this name can be cached. Set to <b>TRUE</b> on output if the name can be cached; set to <b>FALSE</b> otherwise. </p>
</dd>

### -param <i>FileName</i> [out]

<dd>
<p>A pointer to a filter manager-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff544665">FLT_NAME_CONTROL</a> structure to receive the file name on output. </p>
</dd>
</dl>

## -returns
<p>This callback routine returns STATUS_SUCCESS or an appropriate NTSTATUS value. </p>

## -remarks
<p>A minifilter driver that provides file names for the filter manager's name cache can register a routine of type <i>PFLT_GENERATE_FILE_NAME</i> as the minifilter driver's <i>GenerateFileNameCallback</i> routine. </p>

<p>To register this callback routine, the minifilter driver stores the address of a routine of type <i>PFLT_GENERATE_FILE_NAME</i> in the <i>GenerateFileNameCallback</i> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> structure that the minifilter driver passes as a parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>. </p>

<p>The filter manager calls this callback routine to allow the minifilter driver to intercept file name requests by other minifilter drivers above it in the minifilter driver instance stack. Using this callback routine and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a> callback routine, the minifilter driver can provide its own file name information. </p>

<p>To determine which file name format is being requested, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543030">FltGetFileNameFormat</a> on the <i>NameOptions</i> parameter. </p>

<p>Prior to Windows 8, this callback routine is called only for opened file names and short file names. When the filter manager receives a request for a normalized file name, it calls this callback routine to request the opened file name. Then it calls the minifilter driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a> callback to normalize each component in the file name.
</p>

<p>Starting with Windows 8, this callback routine is also called for normalized names.  When the filter manager receives a request for a normalized file name, it calls this callback routine with FLT_FILE_NAME_NORMALIZED specified in the <i>NameOptions</i> parameter.  If the minifilter returns STATUS_SUCCESS from this callback, the minifilter’s <a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a> callback will not be called.  If the minifilter returns a failure code (such as STATUS_NOT_SUPPORTED), the filter manager will call this callback routine again, requesting the opened file name.  The filter manager will then call the minifilter driver’s <i>PFLT_NORMALIZE_NAME_COMPONENT</i> callback to normalize each component in the file name.
</p>

<p>When this callback routine is invoked, the minifilter driver generates its own file name information, based on the file system's file name information for the file. To get the file system's file name information for a file, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543032">FltGetFileNameInformation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543035">FltGetFileNameInformationUnsafe</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff543003">FltGetDestinationFileNameInformation</a>. </p>

<p>For opened file names, the generated file name information should include volume information. For a remote file, it should include share information as well. </p>

<p>The following is an example of an opened file name for a remote file: </p>

<p>For more information about file name formats, see the reference entries for <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a>. </p>

<p>After it generates the file name information, the minifilter driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541829">FltCheckAndGrowNameControl</a> to check whether the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544665">FLT_NAME_CONTROL</a> structure that the <i>FileName</i> parameter points to contains a name buffer that is large enough to hold the generated file name. If the name buffer is too small, <b>FltCheckAndGrowNameControl</b> replaces it with a larger one. The minifilter driver then stores the file name information into the name buffer and returns. </p>

<p>A minifilter driver that provides file names for the filter manager's name cache can register a routine of type <i>PFLT_GENERATE_FILE_NAME</i> as the minifilter driver's <i>GenerateFileNameCallback</i> routine. </p>

<p>To register this callback routine, the minifilter driver stores the address of a routine of type <i>PFLT_GENERATE_FILE_NAME</i> in the <i>GenerateFileNameCallback</i> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> structure that the minifilter driver passes as a parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>. </p>

<p>The filter manager calls this callback routine to allow the minifilter driver to intercept file name requests by other minifilter drivers above it in the minifilter driver instance stack. Using this callback routine and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a> callback routine, the minifilter driver can provide its own file name information. </p>

<p>To determine which file name format is being requested, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543030">FltGetFileNameFormat</a> on the <i>NameOptions</i> parameter. </p>

<p>Prior to Windows 8, this callback routine is called only for opened file names and short file names. When the filter manager receives a request for a normalized file name, it calls this callback routine to request the opened file name. Then it calls the minifilter driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a> callback to normalize each component in the file name.
</p>

<p>Starting with Windows 8, this callback routine is also called for normalized names.  When the filter manager receives a request for a normalized file name, it calls this callback routine with FLT_FILE_NAME_NORMALIZED specified in the <i>NameOptions</i> parameter.  If the minifilter returns STATUS_SUCCESS from this callback, the minifilter’s <a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a> callback will not be called.  If the minifilter returns a failure code (such as STATUS_NOT_SUPPORTED), the filter manager will call this callback routine again, requesting the opened file name.  The filter manager will then call the minifilter driver’s <i>PFLT_NORMALIZE_NAME_COMPONENT</i> callback to normalize each component in the file name.
</p>

<p>When this callback routine is invoked, the minifilter driver generates its own file name information, based on the file system's file name information for the file. To get the file system's file name information for a file, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543032">FltGetFileNameInformation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543035">FltGetFileNameInformationUnsafe</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff543003">FltGetDestinationFileNameInformation</a>. </p>

<p>For opened file names, the generated file name information should include volume information. For a remote file, it should include share information as well. </p>

<p>The following is an example of an opened file name for a remote file: </p>

<p>For more information about file name formats, see the reference entries for <a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a>. </p>

<p>After it generates the file name information, the minifilter driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541829">FltCheckAndGrowNameControl</a> to check whether the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544665">FLT_NAME_CONTROL</a> structure that the <i>FileName</i> parameter points to contains a name buffer that is large enough to hold the generated file name. If the name buffer is too small, <b>FltCheckAndGrowNameControl</b> replaces it with a larger one. The minifilter driver then stores the file name information into the name buffer and returns. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544633">FLT_FILE_NAME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544636">FLT_FILE_NAME_OPTIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544665">FLT_NAME_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541829">FltCheckAndGrowNameControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543003">FltGetDestinationFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543030">FltGetFileNameFormat</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543032">FltGetFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543035">FltGetFileNameInformationUnsafe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543040">FltGetFileNameQueryMethod</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543413">FltParseFileName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543417">FltParseFileNameInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543431">FltPurgeFileNameInformationCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551100">PFLT_NORMALIZE_CONTEXT_CLEANUP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551102">PFLT_NORMALIZE_NAME_COMPONENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551105">PFLT_NORMALIZE_NAME_COMPONENT_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_GENERATE_FILE_NAME routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
