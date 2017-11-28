---
UID: NF.fltkernel.FltEnumerateVolumeInformation
title: FltEnumerateVolumeInformation
author: windows-driver-content
description: The FltEnumerateVolumeInformation routine provides information about volumes that are known to the filter manager.
old-location: ifsk\fltenumeratevolumeinformation.htm
old-project: ifsk
ms.assetid: cdec7faa-299c-4a4e-a037-9900bc3cffa1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltEnumerateVolumeInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltEnumerateVolumeInformation
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
req.iface: 
---

# FltEnumerateVolumeInformation function



## -description
<p>The <b>FltEnumerateVolumeInformation</b> routine provides information about volumes that are known to the filter manager.</p>


## -syntax

````
NTSTATUS FltEnumerateVolumeInformation(
  _In_  PFLT_FILTER                     Filter,
  _In_  ULONG                           Index,
  _In_  FILTER_VOLUME_INFORMATION_CLASS InformationClass,
  _Out_ PVOID                           Buffer,
  _In_  ULONG                           BufferSize,
  _Out_ PULONG                          BytesReturned
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>Opaque filter pointer for the minifilter driver. This pointer uniquely identifies the minifilter driver and remains constant as long as the minifilter driver is loaded.</p>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>Zero-based index of the volume for which the information is requested.</p>
</dd>

### -param <i>InformationClass</i> [in]

<dd>
<p>Type of information requested. This parameter can have one of the following values. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>FilterVolumeBasicInformation</b></p>
</td>
<td>
<p>The <i>Buffer </i>parameter receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541631">FILTER_VOLUME_BASIC_INFORMATION</a> structure for the volume. </p>
</td>
</tr>
<tr>
<td>
<p><b>FilterVolumeStandardInformation</b></p>
</td>
<td>
<p>The <i>Buffer</i> parameter receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541647">FILTER_VOLUME_STANDARD_INFORMATION</a> structure for the volume.  This structure is available starting with Windows Vista.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer that receives the requested information. The type of the information returned in the buffer is defined by the <i>InformationClass</i> parameter.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Size, in bytes, of the buffer that the <i>Buffer</i> parameter points to. The caller should set this parameter according to the given <i>InformationClass</i> value.</p>
</dd>

### -param <i>BytesReturned</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the number of bytes returned in the buffer that <i>Buffer </i>points to. If the input value of <i>BufferSize</i> is too small, <b>FltEnumerateVolumeInformation</b> returns STATUS_BUFFER_TOO_SMALL and sets this variable to the number of bytes required to store the requested information. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>FltEnumerateVolumeInformation</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as one of the following: </p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer that the <i>Buffer</i> parameter points to is not large enough to store the requested information. This is an error code. </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>A matching volume was found, but it is being torn down. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid value was specified for the <i>InformationClass</i> parameter. For example, if <b>FilterVolumeStandardInformation</b> is specified on an operating system prior to Windows Vista, the routine returns STATUS_INVALID_PARAMETER.  This is an error code. </p><dl>
<dt><b>STATUS_NO_MORE_ENTRIES</b></dt>
</dl><p>There are no more entries in the global list of volumes. This is a warning code. </p>

<p> </p>

## -remarks
<p>Using the <i>Index</i> parameter is simply a way for the <b>FltEnumerateVolumeInformation</b> routine to select among volumes in the filter manager's global list of volumes. Two calls to <b>FltEnumerateVolumeInformation</b> with the same value of the <i>Index</i> parameter do not necessarily return the same result because volumes can be mounted or dismounted at any time. </p>

<p>If <b>FltEnumerateVolumeInformation</b> is used to create a list of volume information structures, it is possible for two or more of these structures to contain identical volume names.  For more information, see <a href="ifsk.understanding_volume_enumerations_with_duplicate_volume_names">Understanding Volume Enumerations with Duplicate Volume Names</a>.</p>

<p>To enumerate all registered minifilter drivers, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542064">FltEnumerateFilters</a>. </p>

<p>To enumerate all volumes that are known to the filter manager, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542092">FltEnumerateVolumes</a>. </p>

<p>To list filter information for all registered minifilter drivers, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542060">FltEnumerateFilterInformation</a>. </p>

<p>To get filter information for a given minifilter driver, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543053">FltGetFilterInformation</a>. </p>

<p>To enumerate all instances of a given minifilter driver, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542071">FltEnumerateInstanceInformationByFilter</a>. </p>

<p>To enumerate all minifilter driver instances on a given volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>. </p>

<p>To enumerate instances of all minifilter drivers on all volumes, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542090">FltEnumerateInstances</a>. </p>

<p>Using the <i>Index</i> parameter is simply a way for the <b>FltEnumerateVolumeInformation</b> routine to select among volumes in the filter manager's global list of volumes. Two calls to <b>FltEnumerateVolumeInformation</b> with the same value of the <i>Index</i> parameter do not necessarily return the same result because volumes can be mounted or dismounted at any time. </p>

<p>If <b>FltEnumerateVolumeInformation</b> is used to create a list of volume information structures, it is possible for two or more of these structures to contain identical volume names.  For more information, see <a href="ifsk.understanding_volume_enumerations_with_duplicate_volume_names">Understanding Volume Enumerations with Duplicate Volume Names</a>.</p>

<p>To enumerate all registered minifilter drivers, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542064">FltEnumerateFilters</a>. </p>

<p>To enumerate all volumes that are known to the filter manager, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542092">FltEnumerateVolumes</a>. </p>

<p>To list filter information for all registered minifilter drivers, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542060">FltEnumerateFilterInformation</a>. </p>

<p>To get filter information for a given minifilter driver, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543053">FltGetFilterInformation</a>. </p>

<p>To enumerate all instances of a given minifilter driver, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542071">FltEnumerateInstanceInformationByFilter</a>. </p>

<p>To enumerate all minifilter driver instances on a given volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>. </p>

<p>To enumerate instances of all minifilter drivers on all volumes, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542090">FltEnumerateInstances</a>. </p>

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
<dt>Fltkernel.h (include FltKernel.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541631">FILTER_VOLUME_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541647">FILTER_VOLUME_STANDARD_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542060">FltEnumerateFilterInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542064">FltEnumerateFilters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542071">FltEnumerateInstanceInformationByFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542090">FltEnumerateInstances</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542092">FltEnumerateVolumes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543053">FltGetFilterInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltEnumerateVolumeInformation routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
