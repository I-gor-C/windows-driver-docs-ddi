---
UID: NC.ufxclient.EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT
title: EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT
author: windows-driver-content
description: The client driver's implementation to initiate proprietary charger detection.
old-location: buses\evt_ufx_device_detect_proprietary_charger.htm
old-project: usbref
ms.assetid: A3396CC8-153E-401A-BAD6-18FEE4D14EE5
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _UFX_HARDWARE_FAILURE_CONTEXT, UFX_HARDWARE_FAILURE_CONTEXT, *PUFX_HARDWARE_FAILURE_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ufxclient.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: PFN_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT
req.alt-loc: Ufxclient.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT callback



## -description
The client driver's implementation to initiate proprietary charger detection.



## -prototype

````
EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT EvtUfxDeviceDetectProprietaryCharger;

void EvtUfxDeviceDetectProprietaryCharger(
  _In_ UFXDEVICE UfxDevice
)
{ ... }

typedef EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT PFN_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT;
````


## -parameters

### -param UfxDevice [in]

The handle to a  USB device object that the client driver received in a previous call to  the <a href="buses.ufxdevicecreate">UfxDeviceCreate</a>.


## -returns
This callback function does not return a value.


## -remarks
<i>EVT_UFX_DEVICE_DETECT_PROPRIETARY_CHARGER</i> is an optional event callback. The client driver is required to implement this event callback only if it supports proprietary charger detection. The driver indicates its support in the <a href="buses.ufxdevicecreate">UfxDeviceCreate</a> call by setting <b>PdcpSupported</b> to TRUE in <a href="buses.ufx_device_capabilities">UFX_DEVICE_CAPABILITIES</a>. If the client driver does not support the functionality, the <b>EvtDeviceProprietaryChargerDetect</b>, <b>EvtDeviceProprietaryChargerSetProperty</b>, and <b>EvtDeviceProprietaryChargerReset</b>
members of the <a href="buses.ufx_device_callbacks">UFX_DEVICE_CALLBACKS</a> structure must be set to NULL in   <b>UfxDeviceCreate</b>.   

The client driver indicates completion of this event by calling the <a href="buses.ufxdeviceproprietarychargerdetectcomplete">UfxDeviceProprietaryChargerDetectComplete</a> method.

The client driver sends a request to the lower filter driver to determine if a proprietary charger is present. In response, the filter driver provides a GUID for each charger type it supports, and a list of that charger’s properties.  If a specific charger is configurable, the filter driver also provides a list of supported PropertyIDs and their possible values to configure the charger.


## -requirements
<table>
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
<dt>Ufxclient.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.ufxdevicecreate">UfxDeviceCreate</a>
</dt>
<dt>
<a href="buses.ufxdeviceproprietarychargerdetectcomplete">UfxDeviceProprietaryChargerDetectComplete</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT callback function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

