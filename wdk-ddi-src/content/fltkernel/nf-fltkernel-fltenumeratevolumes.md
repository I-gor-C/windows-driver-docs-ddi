---
UID: NF.fltkernel.FltEnumerateVolumes
title: FltEnumerateVolumes
author: windows-driver-content
description: The FltEnumerateVolumes routine enumerates all volumes in the system.
old-location: ifsk\fltenumeratevolumes.htm
old-project: ifsk
ms.assetid: 67038ff5-c450-460b-b158-f5d817fdc972
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltEnumerateVolumes
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
req.alt-api: FltEnumerateVolumes
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

# FltEnumerateVolumes function



## -description
<p>The <b>FltEnumerateVolumes</b> routine enumerates all volumes in the system. </p>


## -syntax

````
NTSTATUS FltEnumerateVolumes(
  _In_  PFLT_FILTER Filter,
  _Out_ PFLT_VOLUME *VolumeList,
  _In_  ULONG       VolumeListSize,
  _Out_ PULONG      NumberVolumesReturned
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>Opaque filter pointer for the caller. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>VolumeList</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer that receives an array of opaque volume pointers. This parameter is optional and can be <b>NULL</b> if <i>VolumeListSize</i> is zero. If <i>VolumeListSize</i> is zero on input and <i>VolumeList</i> is <b>NULL</b>, <i>NumberVolumesReturned</i> receives the number of volumes found.</p>
</dd>

### -param <i>VolumeListSize</i> [in]

<dd>
<p>Number of opaque filter pointers that the buffer that <i>VolumeList</i> points to can hold. This parameter is optional and can be zero. If <i>VolumeListSize</i> is zero on input and <i>VolumeList</i> is <b>NULL</b>, <i>NumberVolumesReturned</i> receives the number of volumes found.</p>
</dd>

### -param <i>NumberVolumesReturned</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives the number of opaque volume pointers returned in the array that <i>VolumeList </i>points to. If <i>VolumeListSize</i> is too small and <i>VolumeList</i> is non-<b>NULL</b> on input, <b>FltEnumerateVolumes</b> returns STATUS_BUFFER_TOO_SMALL and sets <i>NumberVolumesReturned</i> to point to the number of volumes found. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>FltEnumerateVolumes</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer that the <i>VolumeList</i> parameter points to is not large enough to store the requested information. This is an error code. </p>

<p> </p>

## -remarks
<p>Because the contents of the filter manager's volume list can change at any time, two calls to <b>FltEnumerateVolumes</b> are not guaranteed to return the same result. </p>

<p><b>FltEnumerateVolumes</b> adds a rundown reference to each of the opaque volume pointers returned in the array that <i>VolumeList </i>points to. When these pointers are no longer needed, the caller must release them by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a> on each one. Thus every successful call to <b>FltEnumerateVolumes</b> must be matched by a subsequent call to <b>FltObjectDereference</b> for each returned volume pointer. </p>

<p>To convert one or more opaque volume pointers returned by the <i>VolumeList</i> parameter into volume information, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543238">FltGetVolumeInformation</a>.</p>

<p>To list volume information for all volumes that are known to the filter manager, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542091">FltEnumerateVolumeInformation</a>. </p>

<p>To enumerate all registered minifilter drivers, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542064">FltEnumerateFilters</a>. </p>

<p>To enumerate all minifilter driver instances, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542090">FltEnumerateInstances</a>. </p>

<p>To enumerate all minifilter driver instances on a given volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>. </p>

<p>Because the contents of the filter manager's volume list can change at any time, two calls to <b>FltEnumerateVolumes</b> are not guaranteed to return the same result. </p>

<p><b>FltEnumerateVolumes</b> adds a rundown reference to each of the opaque volume pointers returned in the array that <i>VolumeList </i>points to. When these pointers are no longer needed, the caller must release them by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a> on each one. Thus every successful call to <b>FltEnumerateVolumes</b> must be matched by a subsequent call to <b>FltObjectDereference</b> for each returned volume pointer. </p>

<p>To convert one or more opaque volume pointers returned by the <i>VolumeList</i> parameter into volume information, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543238">FltGetVolumeInformation</a>.</p>

<p>To list volume information for all volumes that are known to the filter manager, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542091">FltEnumerateVolumeInformation</a>. </p>

<p>To enumerate all registered minifilter drivers, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542064">FltEnumerateFilters</a>. </p>

<p>To enumerate all minifilter driver instances, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542090">FltEnumerateInstances</a>. </p>

<p>To enumerate all minifilter driver instances on a given volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542064">FltEnumerateFilters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542090">FltEnumerateInstances</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542091">FltEnumerateVolumeInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543238">FltGetVolumeInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543378">FltObjectDereference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltEnumerateVolumes routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
