---
UID: NF.gpioclx.GPIO_CLX_ProcessAddDevicePreDeviceCreate
title: GPIO_CLX_ProcessAddDevicePreDeviceCreate
author: windows-driver-content
description: The GPIO_CLX_ProcessAddDevicePreDeviceCreate method loads initialization information into two structures that are passed as input parameters to the WdfDeviceCreate method.
old-location: gpio\gpio_clx_processadddevicepredevicecreate.htm
old-project: GPIO
ms.assetid: 8492CCCB-2BA9-419D-A22F-DE06D08D4CC7
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.keywords: GPIO_CLX_ProcessAddDevicePreDeviceCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: gpioclx.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GPIO_CLX_ProcessAddDevicePreDeviceCreate
req.alt-loc: Msgpioclxstub.lib,Msgpioclxstub.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Msgpioclxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# GPIO_CLX_ProcessAddDevicePreDeviceCreate function



## -description
<p>The <b>GPIO_CLX_ProcessAddDevicePreDeviceCreate</b> method loads initialization information into two structures that are passed as input parameters to the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a> method.</p>


## -syntax

````
NTSTATUS GPIO_CLX_ProcessAddDevicePreDeviceCreate(
  _In_    WDFDRIVER              Driver,
  _Inout_ PWDFDEVICE_INIT        DeviceInit,
  _Out_   PWDF_OBJECT_ATTRIBUTES FdoAttributes
);
````


## -parameters
<dl>

### -param <i>Driver</i> [in]

<dd>
<p>A WDFDRIVER handle to the framework driver object for the GPIO controller driver.</p>
</dd>

### -param <i>DeviceInit</i> [in, out]

<dd>
<p>A pointer to a framework-allocated <a href="kmdf.wdfdevice_init">WDFDEVICE_INIT</a> structure. This method loads initialization information into this structure. On return, this structure is ready to be used as an input parameter to the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a> method.</p>
</dd>

### -param <i>FdoAttributes</i> [out]

<dd>
<p>A pointer to a caller-allocated <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure. This method loads initialization information into this structure. On return, this structure is ready to be used as an input parameter to the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a> method.</p>
</dd>
</dl>

## -returns
<p><b>GPIO_CLX_ProcessAddDevicePreDeviceCreate</b> returns STATUS_SUCCESS if the call is successful. Possible return values include the following error codes.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The caller is not a registered client of GpioClx.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Out of memory.</p>

<p> </p>

## -remarks
<p>Your GPIO controller driver must call this method in its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function, before the call to the <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a> method that creates the device object (FDO) that represents the GPIO controller. Otherwise, the GPIO framework extension (GpioClx) cannot handle I/O requests or process interrupts for the new framework device object.</p>

<p>The following code example shows the <i>EvtDriverDeviceAdd</i> callback function in the GPIO controller driver for an "XYZ" GPIO controller device.</p>

<p>In the preceding code example, the <b>WdfDeviceCreate</b> call creates the framework device object that represents the GPIO controller device. The two input parameters for this call point to <a href="kmdf.wdfdevice_init">WDFDEVICE_INIT</a> and <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structures. These structures are modified by the  <b>GPIO_CLX_ProcessAddDevicePreDeviceCreate</b> call, which precedes the <b>WdfDeviceCreate</b> call. The output parameter, <i>Device</i>, from the <b>WdfDeviceCreate</b> call is an input parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439484">GPIO_CLX_ProcessAddDevicePostDeviceCreate</a> call, which follows the <b>WdfDeviceCreate</b> call.</p>

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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Gpioclx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Msgpioclxstub.lib</dt>
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
<a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439484">GPIO_CLX_ProcessAddDevicePostDeviceCreate</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>
</dt>
<dt>
<a href="kmdf.wdfdevice_init">WDFDEVICE_INIT</a>
</dt>
<dt>
<a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20GPIO_CLX_ProcessAddDevicePreDeviceCreate method%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
