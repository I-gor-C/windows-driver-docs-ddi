---
UID: NF.wdfiotarget.WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE
title: WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE function
author: windows-driver-content
description: The WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so that the driver can open a remote I/O target by specifying a Windows Driver Model (WDM) device object.
old-location: wdf\wdf_io_target_open_params_init_existing_device.htm
old-project: wdf
ms.assetid: 41fc4479-98e4-4632-89a1-1638eff02279
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE
req.alt-loc: wdfiotarget.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.product: Windows 10 or later.
---

# WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE</b> function initializes a driver's <a href="wdf.wdf_io_target_open_params">WDF_IO_TARGET_OPEN_PARAMS</a> structure so that the driver can open a remote I/O target by specifying a Windows Driver Model (WDM) device object.


## -syntax

````
VOID WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE(
  _Out_ PWDF_IO_TARGET_OPEN_PARAMS Params,
  _In_  PDEVICE_OBJECT             DeviceObject
);
````


## -parameters

### -param Params [out]

A pointer to a driver-allocated <a href="wdf.wdf_io_target_open_params">WDF_IO_TARGET_OPEN_PARAMS</a> structure that the function initializes.

### -param DeviceObject [in]

A pointer to a <a href="kernel.device_object">DEVICE_OBJECT</a> structure, which is used as the value for the <b>DeviceObject</b> member of the <a href="wdf.wdf_io_target_open_params">WDF_IO_TARGET_OPEN_PARAMS</a> structure.

## -returns
None

## -remarks
The <a href="wdf.wdf_io_target_open_params">WDF_IO_TARGET_OPEN_PARAMS</a> structure is used as input to the <a href="wdf.wdfiotargetopen">WdfIoTargetOpen</a> method.

The <b>WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE</b> function initializes the <b>Size</b>, <b>Type</b>, and <b>TargetDeviceObject</b> members of the specified <a href="wdf.wdf_io_target_open_params">WDF_IO_TARGET_OPEN_PARAMS</a> structure. 

Typically, a driver sets the <b>TargetFileObject</b> member of the <a href="wdf.wdf_io_target_open_params">WDF_IO_TARGET_OPEN_PARAMS</a> structure after the driver has called <b>WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE</b>.

For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.

The following code example creates an I/O target object and opens the target by specifying a DEVICE_OBJECT structure. The sample driver obtains the DEVICE_OBJECT structure by calling <a href="netvista.ndismgetdeviceproperty">NdisMGetDeviceProperty</a> (not shown).

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfiotarget.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
Any level
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_io_target_open_params">WDF_IO_TARGET_OPEN_PARAMS</a>
</dt>
<dt>
<a href="wdf.wdf_io_target_open_params_init_create_by_name">WDF_IO_TARGET_OPEN_PARAMS_INIT_CREATE_BY_NAME</a>
</dt>
<dt>
<a href="wdf.wdf_io_target_open_params_init_open_by_name">WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_NAME</a>
</dt>
<dt>
<a href="wdf.wdfiotargetopen">WdfIoTargetOpen</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
