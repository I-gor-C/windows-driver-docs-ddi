---
UID: NF.ks.KsSetTargetDeviceObject
title: KsSetTargetDeviceObject
author: windows-driver-content
description: The KsSetTargetDeviceObject function sets the target device object of an object. The function adds the object header to a list of object headers that have target devices.
old-location: stream\kssettargetdeviceobject.htm
old-project: stream
ms.assetid: 0d90f70d-8cbe-4c95-ae54-494ff404631a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsSetTargetDeviceObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsSetTargetDeviceObject
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsSetTargetDeviceObject function



## -description
<p>The <b>KsSetTargetDeviceObject</b> function sets the target device object of an object. The function adds the object header to a list of object headers that have target devices. </p>


## -syntax

````
VOID KsSetTargetDeviceObject(
  _In_     KSOBJECT_HEADER Header,
  _In_opt_ PDEVICE_OBJECT  TargetDevice
);
````


## -parameters
<dl>

### -param <i>Header</i> [in]

<dd>
<p>Points to a header previously allocated by <a href="https://msdn.microsoft.com/library/windows/hardware/ff560972">KsAllocateObjectHeader</a>.</p>
</dd>

### -param <i>TargetDevice</i> [in, optional]

<dd>
<p>Optionally contains the target device object that will be used when recalculating the stack depth for the underlying device object. If the value is <b>NULL</b>, any current setting is removed. If the value is any setting other than <b>NULL</b>, the current setting is replaced.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>KsSetTargetDeviceObject</b> function assumes that the caller has previously allocated a device header on the underlying device object with the <b>KsAllocateDeviceHeader</b> function. The presence of the device header allows future calls to the function <b>KsRecalculateStackDepth</b>, and the device header is used when the object will be forwarding IRPs through a connection to another device and needs to keep track of the stack depth.</p>

<p>If <b>KsSetDevicePnpAndBaseObject</b> is also used to assign the PnP object stack, that device object will also be taken into account when recalculating stack depth.</p>

<p>The <b>KsSetTargetDeviceObject</b> function assumes that the caller has previously allocated a device header on the underlying device object with the <b>KsAllocateDeviceHeader</b> function. The presence of the device header allows future calls to the function <b>KsRecalculateStackDepth</b>, and the device header is used when the object will be forwarding IRPs through a connection to another device and needs to keep track of the stack depth.</p>

<p>If <b>KsSetDevicePnpAndBaseObject</b> is also used to assign the PnP object stack, that device object will also be taken into account when recalculating stack depth.</p>

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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566831">KsSetDevicePnpAndBaseObject</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksrecalculatestackdepth.md">KsRecalculateStackDepth</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560958">KsAllocateDeviceHeader</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560972">KsAllocateObjectHeader</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsSetTargetDeviceObject function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
