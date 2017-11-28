---
UID: NF.wdfdevice.WdfDeviceInitFree
title: WdfDeviceInitFree
author: windows-driver-content
description: The WdfDeviceInitFree method deallocates a WDFDEVICE_INIT structure.
old-location: wdf\wdfdeviceinitfree.htm
old-project: wdf
ms.assetid: 61540bd2-8496-4972-854c-968b53c90788
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceInitFree function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceInitFree</b> method deallocates a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure.</p>


## -syntax

````
VOID WdfDeviceInitFree(
  _In_ PWDFDEVICE_INIT DeviceInit
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If your driver receives a WDFDEVICE_INIT structure from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548786">WdfPdoInitAllocate</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841">WdfControlDeviceInitAllocate</a>, and if the driver subsequently encounters an error when it calls a <a href="wdf.wdfdevice_init">device object initialization method</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>, the driver must call <b>WdfDeviceInitFree</b>. </p>

<p>Your driver must not call <b>WdfDeviceInitFree</b> after it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> successfully.</p>

<p>Your driver does not need to call <b>WdfDeviceInitFree</b> if it received the WDFDEVICE_INIT structure as input to its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function, because the framework deletes the structure after the callback function returns.</p>

<p>For more information about calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>The following code example calls <b>WdfDeviceInitFree</b> if a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548802">WdfPdoInitAssignRawDevice</a> fails.</p>

<p>If your driver receives a WDFDEVICE_INIT structure from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548786">WdfPdoInitAllocate</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545841">WdfControlDeviceInitAllocate</a>, and if the driver subsequently encounters an error when it calls a <a href="wdf.wdfdevice_init">device object initialization method</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>, the driver must call <b>WdfDeviceInitFree</b>. </p>

<p>Your driver must not call <b>WdfDeviceInitFree</b> after it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> successfully.</p>

<p>Your driver does not need to call <b>WdfDeviceInitFree</b> if it received the WDFDEVICE_INIT structure as input to its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function, because the framework deletes the structure after the callback function returns.</p>

<p>For more information about calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>The following code example calls <b>WdfDeviceInitFree</b> if a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548802">WdfPdoInitAssignRawDevice</a> fails.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975072">DoubleDeviceInitFree</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547101">InitFreeDeviceCallback</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547104">InitFreeDeviceCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547109">InitFreeDeviceCreateType2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547119">InitFreeDeviceCreateType4</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547122">InitFreeNull</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550359">PdoInitFreeDeviceCallback</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550362">PdoInitFreeDeviceCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550366">PdoInitFreeDeviceCreateType2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550368">PdoInitFreeDeviceCreateType4</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitFree method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
