---
UID: NF.wdfdevice.WdfDeviceInitFree
title: WdfDeviceInitFree function
author: windows-driver-content
description: The WdfDeviceInitFree method deallocates a WDFDEVICE_INIT structure.
old-location: wdf\wdfdeviceinitfree.htm
old-project: wdf
ms.assetid: 61540bd2-8496-4972-854c-968b53c90788
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDeviceInitFree
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceInitFree
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DoubleDeviceInitFree, DriverCreate, InitFreeDeviceCallback, InitFreeDeviceCreate, InitFreeDeviceCreateType2, InitFreeDeviceCreateType4, InitFreeNull, KmdfIrql, KmdfIrql2, PdoInitFreeDeviceCallback, PdoInitFreeDeviceCreate, PdoInitFreeDeviceCreateType2, PdoInitFreeDeviceCreateType4
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceInitFree function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceInitFree</b> method deallocates a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.



## -syntax

````
VOID WdfDeviceInitFree(
  _In_ PWDFDEVICE_INIT DeviceInit
);
````


## -parameters

### -param DeviceInit [in]

A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.


## -returns
None


## -remarks
If your driver receives a WDFDEVICE_INIT structure from a call to <a href="wdf.wdfpdoinitallocate">WdfPdoInitAllocate</a> or <a href="wdf.wdfcontroldeviceinitallocate">WdfControlDeviceInitAllocate</a>, and if the driver subsequently encounters an error when it calls a <a href="wdf.wdfdevice_init">device object initialization method</a> or <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>, the driver must call <b>WdfDeviceInitFree</b>. 

Your driver must not call <b>WdfDeviceInitFree</b> after it calls <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a> successfully.

Your driver does not need to call <b>WdfDeviceInitFree</b> if it received the WDFDEVICE_INIT structure as input to its <a href="..\wdfdriver\nc-wdfdriver-evt_wdf_driver_device_add.md">EvtDriverDeviceAdd</a> callback function, because the framework deletes the structure after the callback function returns.

For more information about calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.

The following code example calls <b>WdfDeviceInitFree</b> if a call to <a href="wdf.wdfpdoinitassignrawdevice">WdfPdoInitAssignRawDevice</a> fails.


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
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
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
<a href="devtest.kmdf_doubledeviceinitfree">DoubleDeviceInitFree</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_initfreedevicecallback">InitFreeDeviceCallback</a>, <a href="devtest.kmdf_initfreedevicecreate">InitFreeDeviceCreate</a>, <a href="devtest.kmdf_initfreedevicecreatetype2">InitFreeDeviceCreateType2</a>, <a href="devtest.kmdf_initfreedevicecreatetype4">InitFreeDeviceCreateType4</a>, <a href="devtest.kmdf_initfreenull">InitFreeNull</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_pdoinitfreedevicecallback">PdoInitFreeDeviceCallback</a>, <a href="devtest.kmdf_pdoinitfreedevicecreate">PdoInitFreeDeviceCreate</a>, <a href="devtest.kmdf_pdoinitfreedevicecreatetype2">PdoInitFreeDeviceCreateType2</a>, <a href="devtest.kmdf_pdoinitfreedevicecreatetype4">PdoInitFreeDeviceCreateType4</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitFree method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

