---
UID: NS.ursdevice._URS_CONFIG
title: URS_CONFIG
author: windows-driver-content
description: Contains pointers to event callback functions implemented by the URS client driver for a USB dual-role controller. Initialize this structure by calling URS_CONFIG_INIT.
old-location: buses\urs_config.htm
ms.assetid: 3857CA53-6992-410A-96D1-EEA9CC586EDF
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: ursdevice.h
req.include-header: Urscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: URS_CONFIG
req.alt-loc: Ursdevice.h
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
ms.keywords: URS_CONFIG, URS_CONFIG, *PURS_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# URS_CONFIG structure



## -description
<p>Contains pointers to event callback functions implemented by the URS client driver for a USB dual-role controller. Initialize this structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt628021">URS_CONFIG_INIT</a>.</p>


## -syntax

````
typedef struct _URS_CONFIG {
  ULONG                                       Size;
  URS_HOST_INTERFACE_TYPE                     HostInterfaceType;
  PFN_URS_DEVICE_FILTER_RESOURCE_REQUIREMENTS EvtUrsFilterRemoveResourceRequirements;
  PFN_URS_SET_ROLE                            EvtUrsSetRole;
} URS_CONFIG, *PURS_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this structure.</p>
</dd>

### -field <b>HostInterfaceType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt628023">URS_HOST_INTERFACE_TYPE</a> type value that indicates the type of USB host controller: EHCI, xHCI, or other.</p>
</dd>

### -field <b>EvtUrsFilterRemoveResourceRequirements</b>

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt595921">EVT_URS_DEVICE_FILTER_RESOURCE_REQUIREMENTS</a> callback function.</p>
</dd>

### -field <b>EvtUrsSetRole</b>

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt595922">EVT_URS_SET_ROLE</a> callback function.</p>
</dd>
</dl>

## -remarks


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
<dt>Ursdevice.h (include Urscx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt628012">UrsDeviceInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt628021">URS_CONFIG_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20URS_CONFIG structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
