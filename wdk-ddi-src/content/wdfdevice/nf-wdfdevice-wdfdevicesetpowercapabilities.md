---
UID: NF.wdfdevice.WdfDeviceSetPowerCapabilities
title: WdfDeviceSetPowerCapabilities function
author: windows-driver-content
description: The WdfDeviceSetPowerCapabilities method reports a device's power capabilities.
old-location: wdf\wdfdevicesetpowercapabilities.htm
old-project: wdf
ms.assetid: e04558e3-a95a-408b-961b-e8ea7ac9136d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDeviceSetPowerCapabilities
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceSetPowerCapabilities
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceSetPowerCapabilities function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDeviceSetPowerCapabilities</b> method reports a device's power capabilities.



## -syntax

````
VOID WdfDeviceSetPowerCapabilities(
  _In_ WDFDEVICE                      Device,
  _In_ PWDF_DEVICE_POWER_CAPABILITIES PowerCapabilities
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.


### -param PowerCapabilities [in]

A pointer to a driver-allocated <a href="wdf.wdf_device_power_capabilities">WDF_DEVICE_POWER_CAPABILITIES</a> structure.


## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.


## -remarks
A driver typically calls <b>WdfDeviceSetPowerCapabilities</b> from within one of the following callback functions:


<a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a>



<a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_prepare_hardware.md">EvtDevicePrepareHardware</a>



<a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_d0_entry.md">EvtDeviceD0Entry</a> (if the <i>PreviousState</i> parameter's value is <b>WdfPowerDeviceD3Final</b>) 


<a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_self_managed_io_init.md">EvtDeviceSelfManagedIoInit</a>



<a href="..\wdfchildlist\nc-wdfchildlist-evt_wdf_child_list_create_device.md">EvtChildListCreateDevice</a>


If more than one driver in the device's driver stack call <b>WdfDeviceSetPowerCapabilities</b>, the power manager uses the values that are supplied by the driver that is highest in the stack.

The following code example initializes a WDF_DEVICE_POWER_CAPABILITIES structure and then calls <b>WdfDeviceSetPowerCapabilities</b>.


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
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdevicesetpnpcapabilities">WdfDeviceSetPnpCapabilities</a>
</dt>
<dt>
<a href="wdf.wdf_device_power_capabilities">WDF_DEVICE_POWER_CAPABILITIES</a>
</dt>
<dt>
<a href="wdf.wdf_device_power_capabilities_init">WDF_DEVICE_POWER_CAPABILITIES_INIT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceSetPowerCapabilities method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

