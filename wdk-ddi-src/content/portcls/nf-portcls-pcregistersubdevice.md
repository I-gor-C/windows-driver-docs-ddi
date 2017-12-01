---
UID: NF.portcls.PcRegisterSubdevice
title: PcRegisterSubdevice
author: windows-driver-content
description: The PcRegisterSubdevice function registers a subdevice to make it available for use by clients.
old-location: audio\pcregistersubdevice.htm
old-project: audio
ms.assetid: 97461adf-053b-484b-9425-b23ac6deb1bd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcRegisterSubdevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcRegisterSubdevice function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcRegisterSubdevice
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PcRegisterSubdevice function



## -description
<p>The <b>PcRegisterSubdevice</b> function registers a subdevice to make it available for use by clients. </p>


## -syntax

````
NTSTATUS PcRegisterSubdevice(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PWSTR          Name,
  _In_ PUNKNOWN       Unknown
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the adapter driver's device object. This is a system structure of type <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>.</p>
</dd>

### -param <i>Name</i> [in]

<dd>
<p>Pointer to a null-terminated Unicode string that specifies the name of the subdevice. The string buffer that the <i>Name</i> parameter points to must remain valid for the lifetime of the device object. The string contains a short name that distinguishes the subdevice from any other subdevices registered on the same device. Each of the device's subdevices must have a unique name.</p>
</dd>

### -param <i>Unknown</i> [in]

<dd>
<p>Pointer to the <a href="..\portcls\nn-portcls-iport.md">IPort</a> interface of the port driver object that is bound to the subdevice.</p>
</dd>
</dl>

## -returns
<p><b>PcRegisterSubdevice</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>The function registers the device interface instance for a filter object that represents a subdevice on an audio adapter. The I/O manager appends the string specified by the <i>Name</i> parameter to the reference string that it uses to identify the instance. The modified reference string is useful for distinguishing among the subdevices in the audio adapter. For more information about reference strings, see <a href="..\wdm\nf-wdm-ioregisterdeviceinterface.md">IoRegisterDeviceInterface</a>.</p>

<p>For more information about the role of the <b>PcRegisterSubdevice</b> function in registering a subdevice, see <a href="NULL">Subdevice Creation</a>.</p>

<p>An adapter driver can call the <a href="audio.iunregistersubdevice_unregistersubdevice">IUnregisterSubdevice::UnregisterSubdevice</a> method to delete the registration of a physical connection that was registered by a previous call to <b>PcRegisterSubdevice</b>. For more information, see <a href="NULL">Dynamic Audio Subdevices</a>. </p>

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
<p>The PortCls system driver implements the PcRegisterSubdevice function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
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
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iport.md">IPort</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-ioregisterdeviceinterface.md">IoRegisterDeviceInterface</a>
</dt>
<dt>
<a href="audio.iunregistersubdevice_unregistersubdevice">IUnregisterSubdevice::UnregisterSubdevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcRegisterSubdevice function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
