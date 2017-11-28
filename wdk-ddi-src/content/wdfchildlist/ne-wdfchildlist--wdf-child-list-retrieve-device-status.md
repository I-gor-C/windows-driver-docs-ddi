---
UID: NE.wdfchildlist._WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS
title: WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS
author: windows-driver-content
description: The WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS enumeration defines device status values that the framework stores in a driver's WDF_CHILD_RETRIEVE_INFO structure.
old-location: wdf\wdf_child_list_retrieve_device_status.htm
old-project: wdf
ms.assetid: 103f0c51-a7c9-4308-8ae2-d878daf0ff1c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDBGEXTS_THREAD_OS_INFO, WDBGEXTS_THREAD_OS_INFO, *PWDBGEXTS_THREAD_OS_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS
req.alt-loc: wdfchildlist.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS</b> enumeration defines device status values that the framework stores in a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a> structure.</p>


## -syntax

````
typedef enum _WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS { 
  WdfChildListRetrieveDeviceUndefined      = 0,
  WdfChildListRetrieveDeviceSuccess        = 1,
  WdfChildListRetrieveDeviceNotYetCreated  = 2,
  WdfChildListRetrieveDeviceNoSuchDevice   = 3
} WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS, *PWDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS;
````


## -enum-fields
<dl>

### -field <a id="WdfChildListRetrieveDeviceUndefined"></a><a id="wdfchildlistretrievedeviceundefined"></a><a id="WDFCHILDLISTRETRIEVEDEVICEUNDEFINED"></a><b>WdfChildListRetrieveDeviceUndefined</b>

<dd></dd>

### -field <a id="WdfChildListRetrieveDeviceSuccess"></a><a id="wdfchildlistretrievedevicesuccess"></a><a id="WDFCHILDLISTRETRIEVEDEVICESUCCESS"></a><b>WdfChildListRetrieveDeviceSuccess</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545663">WdfChildListRetrievePdo</a> method successfully retrieved a child device, and a framework device object exists for the device. </p>
</dd>

### -field <a id="WdfChildListRetrieveDeviceNotYetCreated"></a><a id="wdfchildlistretrievedevicenotyetcreated"></a><a id="WDFCHILDLISTRETRIEVEDEVICENOTYETCREATED"></a><b>WdfChildListRetrieveDeviceNotYetCreated</b>

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545663">WdfChildListRetrievePdo</a> successfully retrieved a child device, but a framework device object has not been created for the device (because the framework has not called the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md">EvtChildListCreateDevice</a> callback function).</p>
</dd>

### -field <a id="WdfChildListRetrieveDeviceNoSuchDevice"></a><a id="wdfchildlistretrievedevicenosuchdevice"></a><a id="WDFCHILDLISTRETRIEVEDEVICENOSUCHDEVICE"></a><b>WdfChildListRetrieveDeviceNoSuchDevice</b>

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545663">WdfChildListRetrievePdo</a> was not able to retrieve a child device that matched the search criteria.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS</b> enumeration is used to specify the <b>Status</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a> structure.</p>

<p>The <b>WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS</b> enumeration is used to specify the <b>Status</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a> structure.</p>

<p>The <b>WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS</b> enumeration is used to specify the <b>Status</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a> structure.</p>

## -requirements
<table>
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
<dt>Wdfchildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md">EvtChildListCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551234">WDF_CHILD_RETRIEVE_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545663">WdfChildListRetrievePdo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
