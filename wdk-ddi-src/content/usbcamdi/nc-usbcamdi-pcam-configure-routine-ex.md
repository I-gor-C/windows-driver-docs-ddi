---
UID: NC.usbcamdi.PCAM_CONFIGURE_ROUTINE_EX
title: PCAM_CONFIGURE_ROUTINE_EX
author: windows-driver-content
description: A camera minidriver's CamConfigureEx callback function configures the isochronous streaming interface.
old-location: stream\camconfigureex.htm
old-project: stream
ms.assetid: ec9fd207-4ed8-4bc9-b240-b5214e8c7f67
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: USBC_FUNCTION_DESCRIPTOR, USBC_FUNCTION_DESCRIPTOR, *PUSBC_FUNCTION_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CamConfigureEx
req.alt-loc: usbcamdi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# PCAM_CONFIGURE_ROUTINE_EX callback



## -description
<p>A camera minidriver's <b>CamConfigureEx</b> callback function configures the isochronous streaming interface.</p>


## -prototype

````
PCAM_CONFIGURE_ROUTINE_EX CamConfigureEx;

NTSTATUS CamConfigureEx(
   PDEVICE_OBJECT                  BusDeviceObject,
   PVOID                           DeviceContext,
   PUSBD_INTERFACE_INFORMATION     Interface,
   PUSB_CONFIGURATION_DESCRIPTOR   ConfigurationDescriptor,
   ULONG                           PipeConfigListSize,
   PUSBCAMD_Pipe_Config_Descriptor PipeConfig,
   PUSB_DEVICE_DESCRIPTOR          DeviceDescriptor
)
{ ... }
````


## -parameters
<dl>

### -param <i>BusDeviceObject</i> 

<dd>
<p>Pointer to the camera minidriver's device object created by the USB hub.</p>
</dd>

### -param <i>DeviceContext</i> 

<dd>
<p>Pointer to the camera minidriver's device context.</p>
</dd>

### -param <i>Interface</i> 

<dd>
<p>Pointer to the <a href="..\usb\ns-usb--usbd-interface-information.md">USBD_INTERFACE_INFORMATION</a> structure initialized with the proper values for a SELECT_INTERFACE URB request. This interface structure corresponds to a single isochronous interface on the device.</p>
</dd>

### -param <i>ConfigurationDescriptor</i> 

<dd>
<p>Pointer to the <a href="..\usbspec\ns-usbspec--usb-configuration-descriptor.md">USB_CONFIGURATION_DESCRIPTOR</a> for this device.</p>
</dd>

### -param <i>PipeConfigListSize</i> 

<dd>
<p>Specifies the number of elements in the <i>PipeConfig</i> array.</p>
</dd>

### -param <i>PipeConfig</i> 

<dd>
<p>Pointer to a <a href="stream.usbcamd_pipe_config_descriptor">USBCAMD_Pipe_Config_Descriptor</a> array describing the association between pipes and streams.</p>
</dd>

### -param <i>DeviceDescriptor</i> 

<dd>
<p>Pointer to the <a href="..\usbspec\ns-usbspec--usb-device-descriptor.md">USB_DEVICE_DESCRIPTOR</a> for this device.</p>
</dd>
</dl>

## -returns
<p><b>CamConfigureEx</b> returns STATUS_SUCCESS or an appropriate error code.</p>

## -remarks
<p>Camera minidrivers use <b>CamConfigureEx</b> to inform USBCAMD about the relationship between discovered pipes and streams.</p>

<p>USBCAMD calls the <b>CamConfigureEx</b> callback function to configure the isochronous streaming interface. After this function returns, USBCAMD can be notified of which interface and which alternate setting within the USB video streaming interface to use for the idle state.</p>

<p>USBCAMD requires that the camera must have a single USB configuration description, and all alternate settings within the USB video streaming interface must have the same number and type of pipes.</p>

<p>The original USBCAMD does not call <b>CamConfigureEx</b>.</p>

<p>This function is required.</p>

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
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbcamdi\ns-usbcamdi--usbcamd-device-data2.md">USBCAMD_DEVICE_DATA2</a>
</dt>
<dt>
<a href="..\usb\ns-usb--usbd-interface-information.md">USBD_INTERFACE_INFORMATION</a>
</dt>
<dt>
<a href="..\usbspec\ns-usbspec--usb-configuration-descriptor.md">USB_CONFIGURATION_DESCRIPTOR</a>
</dt>
<dt>
<a href="stream.usbcamd_pipe_config_descriptor">USBCAMD_Pipe_Config_Descriptor</a>
</dt>
<dt>
<a href="..\usbspec\ns-usbspec--usb-device-descriptor.md">USB_DEVICE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20CamConfigureEx routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
