---
UID: NF.wdfdevice.WdfDeviceInitSetPowerPolicyEventCallbacks
title: WdfDeviceInitSetPowerPolicyEventCallbacks function
author: windows-driver-content
description: The WdfDeviceInitSetPowerPolicyEventCallbacks method registers a driver's power policy event callback functions.
old-location: wdf\wdfdeviceinitsetpowerpolicyeventcallbacks.htm
old-project: wdf
ms.assetid: ae74d58c-3b36-4298-aa6f-4c272e7ff61c
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDeviceInitSetPowerPolicyEventCallbacks
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
req.alt-api: WdfDeviceInitSetPowerPolicyEventCallbacks
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: ChildDeviceInitAPI, DeviceInitAPI, DriverCreate, FDOPowerPolicyOwnerAPI, KmdfIrql, KmdfIrql2, NonFDONotPowerPolicyOwnerAPI, PdoDeviceInitAPI
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceInitSetPowerPolicyEventCallbacks function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDeviceInitSetPowerPolicyEventCallbacks</b> method registers a driver's power policy event callback functions.



## -syntax

````
VOID WdfDeviceInitSetPowerPolicyEventCallbacks(
  _In_ PWDFDEVICE_INIT                   DeviceInit,
  _In_ PWDF_POWER_POLICY_EVENT_CALLBACKS PowerPolicyEventCallbacks
);
````


## -parameters

### -param DeviceInit [in]

A caller-supplied pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.


### -param PowerPolicyEventCallbacks [in]

A pointer to a caller-initialized <a href="wdf.wdf_power_policy_event_callbacks">WDF_POWER_POLICY_EVENT_CALLBACKS</a> structure.


## -returns
None


## -remarks
If your driver calls <b>WdfDeviceInitSetPowerPolicyEventCallbacks</b>, it must do so before it calls <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>. For more information, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.

For more information about <b>WdfDeviceInitSetPowerPolicyEventCallbacks</b>, see <a href="wdf.power_policy_ownership">Power Policy Ownership</a>.

The following code example initializes a <a href="wdf.wdf_power_policy_event_callbacks">WDF_POWER_POLICY_EVENT_CALLBACKS</a> structure and then calls <b>WdfDeviceInitSetPowerPolicyEventCallbacks</b>.


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
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_childdeviceinitapi">ChildDeviceInitAPI</a>, <a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_fdopowerpolicyownerapi">FDOPowerPolicyOwnerAPI</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_nonfdonotpowerpolicyownerapi">NonFDONotPowerPolicyOwnerAPI</a>, <a href="devtest.kmdf_pdodeviceinitapi">PdoDeviceInitAPI</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_power_policy_event_callbacks_init">WDF_POWER_POLICY_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="wdf.wdfdeviceinitsetpnppowereventcallbacks">WdfDeviceInitSetPnpPowerEventCallbacks</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitSetPowerPolicyEventCallbacks method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

