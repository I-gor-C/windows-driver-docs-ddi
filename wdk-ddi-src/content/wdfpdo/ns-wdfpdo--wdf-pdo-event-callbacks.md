---
UID: NS.wdfpdo._WDF_PDO_EVENT_CALLBACKS
title: WDF_PDO_EVENT_CALLBACKS
author: windows-driver-content
description: The WDF_PDO_EVENT_CALLBACKS structure is the dispatch table for a bus driver's event callback functions.
old-location: wdf\wdf_pdo_event_callbacks.htm
ms.assetid: 13cb1da1-0bb7-444e-a0e1-abcac7d0240d
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfpdo.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_PDO_EVENT_CALLBACKS
req.alt-loc: wdfpdo.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDF_PDO_EVENT_CALLBACKS, WDF_PDO_EVENT_CALLBACKS, *PWDF_PDO_EVENT_CALLBACKS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_PDO_EVENT_CALLBACKS structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_PDO_EVENT_CALLBACKS</b> structure is the dispatch table for a bus driver's event callback functions.</p>


## -syntax

````
typedef struct _WDF_PDO_EVENT_CALLBACKS {
  ULONG                                      Size;
  PFN_WDF_DEVICE_RESOURCES_QUERY             EvtDeviceResourcesQuery;
  PFN_WDF_DEVICE_RESOURCE_REQUIREMENTS_QUERY EvtDeviceResourceRequirementsQuery;
  PFN_WDF_DEVICE_EJECT                       EvtDeviceEject;
  PFN_WDF_DEVICE_SET_LOCK                    EvtDeviceSetLock;
  PFN_WDF_DEVICE_ENABLE_WAKE_AT_BUS          EvtDeviceEnableWakeAtBus;
  PFN_WDF_DEVICE_DISABLE_WAKE_AT_BUS         EvtDeviceDisableWakeAtBus;
  PFN_WDF_DEVICE_REPORTED_MISSING            EvtDeviceReportedMissing;
} WDF_PDO_EVENT_CALLBACKS, *PWDF_PDO_EVENT_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>EvtDeviceResourcesQuery</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/3210b28b-cbaa-4ad9-9ca8-3b5f03aee41e">EvtDeviceResourcesQuery</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceResourceRequirementsQuery</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/bacd7e7c-9f71-4dda-98ed-a8d813360943">EvtDeviceResourceRequirementsQuery</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceEject</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/fc3f3a15-9a79-4275-9ba4-b01ab8851390">EvtDeviceEject</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceSetLock</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/2ac42710-9f44-4982-a0d9-c49048870aeb">EvtDeviceSetLock</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceEnableWakeAtBus</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/902c9bdc-d83a-4bc2-802c-1aaba43c9e2e">EvtDeviceEnableWakeAtBus</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceDisableWakeAtBus</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/91ae9694-5020-42ee-b882-a753e9bbe919">EvtDeviceDisableWakeAtBus</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceReportedMissing</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/F64E2FFD-229F-4447-94C2-A5403E7893B7">EvtDeviceReportedMissing</a> event callback function, or <b>NULL</b>. The <b>EvtDeviceReportedMissing</b> member is available in version 1.11 and later versions of KMDF.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_PDO_EVENT_CALLBACKS</b> structure is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548805">WdfPdoInitSetEventCallbacks</a>.</p>

<p>Drivers must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff552413">WDF_PDO_EVENT_CALLBACKS_INIT</a> to initialize this structure.</p>

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
<dt>Wdfpdo.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551311">WDF_FDO_EVENT_CALLBACKS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547268">WdfFdoInitSetEventCallbacks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552413">WDF_PDO_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548805">WdfPdoInitSetEventCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_PDO_EVENT_CALLBACKS structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
