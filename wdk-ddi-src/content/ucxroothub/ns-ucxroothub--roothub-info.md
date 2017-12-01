---
UID: NS.ucxroothub._ROOTHUB_INFO
title: ROOTHUB_INFO
author: windows-driver-content
description: Provides information about a USB root hub. This structure is passed by UCX in the EVT_UCX_ROOTHUB_GET_INFO callback function.
old-location: buses\_roothub_info.htm
old-project: usbref
ms.assetid: 634398E9-7AAA-424C-8C81-287F70CE3578
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ROOTHUB_INFO, ROOTHUB_INFO, *PROOTHUB_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxroothub.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ROOTHUB_INFO
req.alt-loc: ucxroothub.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ROOTHUB_INFO structure



## -description
<p>Provides information about a USB root hub. This structure is passed by UCX in the <a href="buses.evt_ucx_roothub_get_info">EVT_UCX_ROOTHUB_GET_INFO</a> callback function.</p>


## -syntax

````
typedef struct _ROOTHUB_INFO {
  ULONG           Size;
  CONTROLLER_TYPE ControllerType;
  USHORT          NumberOf20Ports;
  USHORT          NumberOf30Ports;
  USHORT          MaxU1ExitLatency;
  USHORT          MaxU2ExitLatency;
} ROOTHUB_INFO, *P_ROOTHUB_INFO;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field <b>ControllerType</b>

<dd>
<p>A <a href="buses._controller_type">CONTROLLER_TYPE</a> value that identifies the type of eXtensible Host Controller Interface (xHCI) which has the root hub.</p>
</dd>

### -field <b>NumberOf20Ports</b>

<dd>
<p>The number of USB 2.0 ports connected to the root hub.</p>
</dd>

### -field <b>NumberOf30Ports</b>

<dd>
<p>The number of USB 3.0 ports connected to the root hub.</p>
</dd>

### -field <b>MaxU1ExitLatency</b>

<dd>
<p>The exit latency for the slowest link for U1 transition.</p>
</dd>

### -field <b>MaxU2ExitLatency</b>

<dd>
<p>The exit latency for the slowest link for U2 transition.</p>
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
<dt>Ucxroothub.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.evt_ucx_roothub_get_info">EVT_UCX_ROOTHUB_GET_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20ROOTHUB_INFO structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
