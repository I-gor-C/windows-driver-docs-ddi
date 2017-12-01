---
UID: NE.sercx._SERCX_STATUS
title: SERCX_STATUS
author: windows-driver-content
description: The SERCX_STATUS enumeration indicates the status of a serial receive or transmit operation.
old-location: serports\sercx_status.htm
old-project: serports
ms.assetid: 7EF129C7-25C3-49D2-8FC5-FFA1C4E77935
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SENSOR_VALUE_PAIR, SENSOR_VALUE_PAIR, *PSENSOR_VALUE_PAIR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sercx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SERCX_STATUS
req.alt-loc: 1.0\Sercx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Called at IRQL <= DISPATCH_LEVEL.
req.iface: 
req.product: Windows 10 or later.
---

# SERCX_STATUS enumeration



## -description
<p>The <b>SERCX_STATUS</b> enumeration indicates the status of a serial receive or transmit operation.</p>


## -syntax

````
typedef enum _SERCX_STATUS { 
  SerCxStatusSuccess    = STATUS_SUCCESS,
  SerCxStatusCancelled  = STATUS_CANCELLED,
  SerCxStatusTimeout    = STATUS_TIMEOUT
} SERCX_STATUS;
````


## -enum-fields
<dl>

### -field <a id="SerCxStatusSuccess"></a><a id="sercxstatussuccess"></a><a id="SERCXSTATUSSUCCESS"></a><b>SerCxStatusSuccess</b>

<dd>
<p>The operation is proceeding successfully.</p>
</dd>

### -field <a id="SerCxStatusCancelled"></a><a id="sercxstatuscancelled"></a><a id="SERCXSTATUSCANCELLED"></a><b>SerCxStatusCancelled</b>

<dd>
<p>The operation was canceled.</p>
</dd>

### -field <a id="SerCxStatusTimeout"></a><a id="sercxstatustimeout"></a><a id="SERCXSTATUSTIMEOUT"></a><b>SerCxStatusTimeout</b>

<dd>
<p>The operation timed out. This enumeration value applies only to read interval time-outs for receive operations. For more information, see the description of the <b>ReadIntervalTimeout</b> member in <a href="..\ntddser\ns-ntddser--serial-timeouts.md">SERIAL_TIMEOUTS</a>.</p>
</dd>
</dl>

## -remarks
<p>The <a href="..\sercx\nf-sercx-sercxprogressreceive.md">SerCxProgressReceive</a> and <a href="..\sercx\nf-sercx-sercxprogresstransmit.md">SerCxProgressTransmit</a> methods have parameters that are <b>SERCX_STATUS</b> enumeration values.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1.0\Sercx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\sercx\nf-sercx-sercxprogressreceive.md">SerCxProgressReceive</a>
</dt>
<dt>
<a href="..\sercx\nf-sercx-sercxprogresstransmit.md">SerCxProgressTransmit</a>
</dt>
<dt>
<a href="..\ntddser\ns-ntddser--serial-timeouts.md">SERIAL_TIMEOUTS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20SERCX_STATUS enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
