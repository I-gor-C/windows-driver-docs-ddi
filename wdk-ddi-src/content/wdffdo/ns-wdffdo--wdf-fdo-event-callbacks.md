---
UID: NS.wdffdo._WDF_FDO_EVENT_CALLBACKS
title: WDF_FDO_EVENT_CALLBACKS
author: windows-driver-content
description: The WDF_FDO_EVENT_CALLBACKS structure contains pointers to a function driver's PnP event callback functions.
old-location: wdf\wdf_fdo_event_callbacks.htm
ms.assetid: 61e268aa-782a-42d5-8965-b935156033cb
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdffdo.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_FDO_EVENT_CALLBACKS
req.alt-loc: wdffdo.h
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
ms.keywords: WDF_FDO_EVENT_CALLBACKS, WDF_FDO_EVENT_CALLBACKS, *PWDF_FDO_EVENT_CALLBACKS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_FDO_EVENT_CALLBACKS structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_FDO_EVENT_CALLBACKS</b> structure contains pointers to a function driver's PnP event callback functions.</p>


## -syntax

````
typedef struct _WDF_FDO_EVENT_CALLBACKS {
  ULONG                                       Size;
  PFN_WDF_DEVICE_FILTER_RESOURCE_REQUIREMENTS EvtDeviceFilterAddResourceRequirements;
  PFN_WDF_DEVICE_FILTER_RESOURCE_REQUIREMENTS EvtDeviceFilterRemoveResourceRequirements;
  PFN_WDF_DEVICE_REMOVE_ADDED_RESOURCES       EvtDeviceRemoveAddedResources;
} WDF_FDO_EVENT_CALLBACKS, *PWDF_FDO_EVENT_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>EvtDeviceFilterAddResourceRequirements</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/7d9b38b5-989d-45a3-8771-57a8d1f98725">EvtDeviceFilterAddResourceRequirements</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceFilterRemoveResourceRequirements</b>

<dd>
<p>A pointer to the driver's <a href="wdf.evtdevicefilterremoveresourcerequirements">EvtDeviceFilterRemoveResourceRequirements</a> event callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtDeviceRemoveAddedResources</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/b18c2b34-db6d-4553-9340-556da1fd7991">EvtDeviceRemoveAddedResources</a> event callback function, or <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_FDO_EVENT_CALLBACKS</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547268">WdfFdoInitSetEventCallbacks</a> method.</p>

<p>Drivers must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551313">WDF_FDO_EVENT_CALLBACKS_INIT</a> to initialize the structure.</p>

<p>A driver that specifies an <a href="https://msdn.microsoft.com/7d9b38b5-989d-45a3-8771-57a8d1f98725">EvtDeviceFilterAddResourceRequirements</a> event callback function must also specify an <a href="https://msdn.microsoft.com/b18c2b34-db6d-4553-9340-556da1fd7991">EvtDeviceRemoveAddedResources</a> event callback function.</p>

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
<dt>Wdffdo.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551313">WDF_FDO_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547268">WdfFdoInitSetEventCallbacks</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552409">WDF_PDO_EVENT_CALLBACKS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548805">WdfPdoInitSetEventCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_FDO_EVENT_CALLBACKS structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
