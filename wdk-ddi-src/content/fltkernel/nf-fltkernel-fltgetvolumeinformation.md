---
UID: NF.fltkernel.FltGetVolumeInformation
title: FltGetVolumeInformation
author: windows-driver-content
description: The FltGetVolumeInformation routine provides information about a given volume.
old-location: ifsk\fltgetvolumeinformation.htm
old-project: ifsk
ms.assetid: e25a7114-c1e5-4432-82a1-4c2e82d9fbc6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltGetVolumeInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetVolumeInformation
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
req.irql: <= APC_LEVEL
req.iface: 
---

# FltGetVolumeInformation function



## -description
<p>The <b>FltGetVolumeInformation</b> routine provides information about a given volume.</p>


## -syntax

````
NTSTATUS FltGetVolumeInformation(
  _In_  PFLT_VOLUME                     Volume,
  _In_  FILTER_VOLUME_INFORMATION_CLASS InformationClass,
  _Out_ PVOID                           Buffer,
  _In_  ULONG                           BufferSize,
  _Out_ PULONG                          BytesReturned
);
````


## -parameters
<dl>

### -param <i>Volume</i> [in]

<dd>
<p>Opaque pointer for the volume.  This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>InformationClass</i> [in]

<dd>
<p>Type of information requested. This parameter is required and must be one of the following values. </p>
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
<p>The <i>Buffer</i> parameter receives a <a href="..\fltuserstructures\ns-fltuserstructures--filter-volume-basic-information.md">FILTER_VOLUME_BASIC_INFORMATION</a> structure for the volume.</p>
</td>
</tr>
<tr>
<td>
<p><b>FilterVolumeStandardInformation</b></p>
</td>
<td>
<p>The <i>Buffer</i> parameter receives a <a href="..\fltuserstructures\ns-fltuserstructures--filter-volume-standard-information.md">FILTER_VOLUME_STANDARD_INFORMATION</a> structure for the volume.  This structure is available starting with Windows Vista.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer that receives the requested information. The type of the information returned in the buffer is defined by the <i>InformationClass</i> parameter.  This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Size, in bytes, of the buffer that the <i>Buffer</i> parameter points to. The caller should set this parameter according to the given <i>InformationClass</i> value.  This parameter is required.</p>
</dd>

### -param <i>BytesReturned</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the number of bytes returned in the buffer that <i>Buffer </i>points to. If the input value of <i>BufferSize</i> is too small, <b>FltGetVolumeInformation </b>returns STATUS_BUFFER_TOO_SMALL and sets this variable to the number of bytes required to store the requested information. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>FltGetVolumeInformation</b> returns STATUS_SUCCESS or an appropriate NTSTATUS status code, such as one of the following:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid value was specified for the <i>InformationClass</i> parameter.  For example, if <b>FilterVolumeStandardInformation</b> is specified on an operating system prior to Windows Vista, the routine will return STATUS_INVALID_PARAMETER.  This is an error code.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer that the <i>Buffer</i> parameter points to is not large enough to store the requested information. This is an error code.</p>

<p> </p>

## -remarks
<p>Given an opaque volume pointer, such as that returned by the <a href="..\fltkernel\nf-fltkernel-fltenumeratevolumes.md">FltEnumerateVolumes</a> routine, the <b>FltGetVolumeInformation</b> routine provides information about the volume pointed to by the opaque volume pointer, passed through the <i>Volume</i> parameter.  Note that the caller must eventually release the opaque volume pointer by calling the <a href="..\fltkernel\nf-fltkernel-fltobjectdereference.md">FltObjectDereference</a> routine.</p>

<p>The <b>FltGetVolumeInformation</b> routine returns information for a single volume.  However, given a list of opaque volume pointers, the routine can be iteratively used to create a list of corresponding volume information structures.  In such a list, it is possible for two or more of the structures to contain identical volume names.  For more information, see <a href="ifsk.understanding_volume_enumerations_with_duplicate_volume_names">Understanding Volume Enumerations with Duplicate Volume Names</a>.</p>

<p>To list volume information for all volumes that are known to the filter manager, call <a href="..\fltkernel\nf-fltkernel-fltenumeratevolumeinformation.md">FltEnumerateVolumeInformation</a>. </p>

<p>The following list contains related information, which may be of use:</p>

<p> To enumerate all registered minifilter drivers in the system, call the <a href="..\fltkernel\nf-fltkernel-fltenumeratefilters.md">FltEnumerateFilters</a> routine.</p>

<p> To obtain information about minifilter driver instances attached to a given volume, call the <a href="..\fltkernel\nf-fltkernel-fltenumerateinstanceinformationbyvolume.md">FltEnumerateInstanceInformationByVolume</a> routine.</p>

<p> To enumerate minifilter driver instances for a given minifilter driver or volume, call the <a href="..\fltkernel\nf-fltkernel-fltenumerateinstances.md">FltEnumerateInstances</a> routine.</p>

<p> To enumerate all volumes in the system, call the <a href="..\fltkernel\nf-fltkernel-fltenumeratevolumes.md">FltEnumerateVolumes</a> routine.</p>

<p> To obtain an opaque pointer for the volume represented by a given volume device object (VDO), call the <a href="..\fltkernel\nf-fltkernel-fltgetvolumefromdeviceobject.md">FltGetVolumeFromDeviceObject</a> routine.</p>

<p> To obtain an opaque pointer for the volume that a given file stream resides on, call the <a href="..\fltkernel\nf-fltkernel-fltgetvolumefromfileobject.md">FltGetVolumeFromFileObject</a> routine.</p>

<p> To obtain an opaque pointer for the volume that a given minifilter driver instance is attached to, call the <a href="..\fltkernel\nf-fltkernel-fltgetvolumefrominstance.md">FltGetVolumeFromInstance</a> routine.</p>

<p> To obtain an opaque pointer for the volume whose name matches a given volume name, call the <a href="..\fltkernel\nf-fltkernel-fltgetvolumefromname.md">FltGetVolumeFromName</a> routine.</p>

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
<p>This routine is available starting with Windows Vista.</p>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltuserstructures\ns-fltuserstructures--filter-volume-basic-information.md">FILTER_VOLUME_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\fltuserstructures\ns-fltuserstructures--filter-volume-standard-information.md">FILTER_VOLUME_STANDARD_INFORMATION</a>
</dt>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-related-objects.md">FLT_RELATED_OBJECTS</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltenumeratefilters.md">FltEnumerateFilters</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltenumerateinstanceinformationbyvolume.md">FltEnumerateInstanceInformationByVolume</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltenumerateinstances.md">FltEnumerateInstances</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltenumeratevolumeinformation.md">FltEnumerateVolumeInformation</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltenumeratevolumes.md">FltEnumerateVolumes</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetvolumefromdeviceobject.md">FltGetVolumeFromDeviceObject</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetvolumefromfileobject.md">FltGetVolumeFromFileObject</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetvolumefrominstance.md">FltGetVolumeFromInstance</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetvolumefromname.md">FltGetVolumeFromName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetVolumeInformation routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
