---
UID: NS.ucxusbdevice._USBDEVICE_RESET
title: USBDEVICE_RESET
author: windows-driver-content
description: Contains parameters for a request to reset the specified device. This structure is passed by UCX in request parameters (Parameters.Others.Arg1) of a framework request object of the EVT_UCX_USBDEVICE_RESET callback function.
old-location: buses\_usbdevice_reset.htm
old-project: usbref
ms.assetid: 4C07239D-89AE-4A9F-B7EB-CFFE6D47F10B
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBDEVICE_RESET, USBDEVICE_RESET, *PUSBDEVICE_RESET
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
req.alt-api: USBDEVICE_RESET
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

# USBDEVICE_RESET structure



## -description
<p>Contains parameters for a request to reset the specified device.  This structure is passed by UCX in request parameters (<b>Parameters.Others.Arg1</b>) of a framework request object of the <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-reset.md">EVT_UCX_USBDEVICE_RESET</a> callback function.</p>


## -syntax

````
typedef struct _USBDEVICE_RESET {
#ifdef __cplusplus
  USBDEVICE_MGMT_HEADER Header;
#else 
  USBDEVICE_MGMT_HEADER ;
#endif 
  UCXENDPOINT           DefaultEndpoint;
  ULONG                 EndpointsToDisableCount;
  UCXENDPOINT           *EndpointsToDisable;
} USBDEVICE_RESET, *P_USBDEVICE_RESET;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>A <a href="..\ucxusbdevice\ns-ucxusbdevice--usbdevice-mgmt-header.md">USBDEVICE_MGMT_HEADER</a> structure that contains  the handle for the USB hub or device.</p>
</dd>

### -field DefaultEndpoint

<dd>
<p>The default endpoint for the USB hub or device.</p>
</dd>

### -field EndpointsToDisableCount

<dd>
<p>The number of endpoints to disable. </p>
</dd>

### -field EndpointsToDisable

<dd>
<p>A pointer to an array of handles to endpoints to disable. </p>
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
<a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-reset.md">EVT_UCX_USBDEVICE_RESET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBDEVICE_RESET structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
