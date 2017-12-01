---
UID: NS.ucxusbdevice._USBDEVICE_HUB_INFO
title: USBDEVICE_HUB_INFO
author: windows-driver-content
description: Contains parameters for a request to get information about the specified hub. This structure is passed by UCX in request parameters (Parameters.Others.Arg1) of a framework request object of the EVT_UCX_USBDEVICE_HUB_INFO callback function.
old-location: buses\_usbdevice_hub_info.htm
old-project: usbref
ms.assetid: F403179A-B339-432D-AAF9-E7D9965F8B00
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBDEVICE_HUB_INFO, USBDEVICE_HUB_INFO, *PUSBDEVICE_HUB_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBDEVICE_HUB_INFO
req.alt-loc: ucxusbdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# USBDEVICE_HUB_INFO structure



## -description
<p>Contains parameters for a request to get information about the specified hub. This structure is passed by UCX in request parameters (<b>Parameters.Others.Arg1</b>) of a framework request object of the <a href="buses.evt_ucx_usbdevice_hub_info">EVT_UCX_USBDEVICE_HUB_INFO</a> callback function.</p>


## -syntax

````
typedef struct _USBDEVICE_HUB_INFO {
#if __cplusplus
  USBDEVICE_MGMT_HEADER Header;
#else 
  USBDEVICE_MGMT_HEADER ;
#endif 
  ULONG                 NumberOfPorts;
  ULONG                 NumberOfTTs;
  ULONG                 TTThinkTime;
} USBDEVICE_HUB_INFO, *P_USBDEVICE_HUB_INFO;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>A <a href="buses._usbdevice_mgmt_header">USBDEVICE_MGMT_HEADER</a> structure that contains  the handle for the USB hub or device.</p>
</dd>

### -field <b>NumberOfPorts</b>

<dd>
<p>The count of ports available for the USB hub, filled by the client driver.</p>
</dd>

### -field <b>NumberOfTTs</b>

<dd>
<p>The count of TT hubs, filled by the client driver.</p>
</dd>

### -field <b>TTThinkTime</b>

<dd>
<p>The ThinkTime property of the TT hub, filled by the client driver.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucxusbdevice.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.evt_ucx_usbdevice_hub_info">EVT_UCX_USBDEVICE_HUB_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBDEVICE_HUB_INFO structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
