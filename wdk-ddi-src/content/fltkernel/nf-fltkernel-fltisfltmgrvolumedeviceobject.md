---
UID: NF.fltkernel.FltIsFltMgrVolumeDeviceObject
title: FltIsFltMgrVolumeDeviceObject
author: windows-driver-content
description: The FltIsFltMgrVolumeDeviceObject routine determines whether the given device object belongs to filter manager and if the device object is a volume device object.
old-location: ifsk\fltisfltmgrvolumedeviceobject.htm
old-project: ifsk
ms.assetid: c4165eab-c62e-436d-b4d4-a1f72ee9c1bd
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltIsFltMgrVolumeDeviceObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Vista or later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltIsFltMgrVolumeDeviceObject
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

# FltIsFltMgrVolumeDeviceObject function



## -description
<p>The <b>FltIsFltMgrVolumeDeviceObject</b> routine determines whether the given device object belongs to filter manager and if the device object is a volume device object.</p>


## -syntax

````
BOOLEAN FltIsFltMgrVolumeDeviceObject(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters
<dl>

### -param DeviceObject [in]

<dd>
<p>A pointer to the device object (<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>) to test.</p>
</dd>
</dl>

## -returns
<p>The <b>FltIsFltMgrVolumeDeviceObject</b> routine returns <b>TRUE</b> if <i>DeviceObject</i> is a filter manager volume device object; otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>None</p>

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
<p>Available in Vista or later versions of the Windows operating system.</p>
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
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltIsFltMgrVolumeDeviceObject routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
