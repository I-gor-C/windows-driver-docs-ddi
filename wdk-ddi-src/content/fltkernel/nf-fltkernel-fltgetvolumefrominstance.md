---
UID: NF.fltkernel.FltGetVolumeFromInstance
title: FltGetVolumeFromInstance
author: windows-driver-content
description: The FltGetVolumeFromInstance routine returns an opaque pointer for the volume that a given minifilter driver instance is attached to.
old-location: ifsk\fltgetvolumefrominstance.htm
old-project: ifsk
ms.assetid: 2c38ab6a-c583-45a5-93a5-6a5882411b6c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltGetVolumeFromInstance
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
req.alt-api: FltGetVolumeFromInstance
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

# FltGetVolumeFromInstance function



## -description
<p>The <b>FltGetVolumeFromInstance</b> routine returns an opaque pointer for the volume that a given minifilter driver instance is attached to. </p>


## -syntax

````
NTSTATUS FltGetVolumeFromInstance(
  _In_  PFLT_INSTANCE Instance,
  _Out_ PFLT_VOLUME   *RetVolume
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the instance. </p>
</dd>

### -param <i>RetVolume</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives an opaque pointer for the volume. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltGetVolumeFromInstance</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as the following: </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The volume that the minifilter driver instance is attached to is being torn down. This is an error code. </p>

<p> </p>

## -remarks
<p><b>FltGetVolumeFromInstance</b> adds a rundown reference to the opaque volume pointer returned in the <i>RetVolume</i> parameter. When this pointer is no longer needed, the caller must release it by calling <a href="..\fltkernel\nf-fltkernel-fltobjectdereference.md">FltObjectDereference</a>. Thus every successful call to <b>FltGetVolumeFromInstance</b> must be matched by a subsequent call to <b>FltObjectDereference</b>. </p>

<p>To get an opaque filter pointer for the minifilter driver that created a given instance, call <a href="..\fltkernel\nf-fltkernel-fltgetfilterfrominstance.md">FltGetFilterFromInstance</a>. </p>

<p>To get a pointer to the device object for a given volume, call <a href="..\fltkernel\nf-fltkernel-fltgetdeviceobject.md">FltGetDeviceObject</a>. </p>

<p>To get detailed information about the volume that a given instance is attached to, call <a href="..\fltkernel\nf-fltkernel-fltqueryvolumeinformation.md">FltQueryVolumeInformation</a>. </p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetdeviceobject.md">FltGetDeviceObject</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetfilterfrominstance.md">FltGetFilterFromInstance</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltobjectdereference.md">FltObjectDereference</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltqueryvolumeinformation.md">FltQueryVolumeInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetVolumeFromInstance routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
