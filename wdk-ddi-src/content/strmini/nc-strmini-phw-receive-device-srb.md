---
UID: NC.strmini.PHW_RECEIVE_DEVICE_SRB
title: PHW_RECEIVE_DEVICE_SRB
author: windows-driver-content
description: The minidriver-supplied StrMiniReceiveDevicePacket routine handles class driver requests that apply to the driver as a whole, such as initializing the device, or opening a stream within the device.
old-location: stream\strminireceivedevicepacket.htm
old-project: stream
ms.assetid: 51d8a18d-cd90-4fac-a991-6c0de505576e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StrMiniReceiveDevicePacket
req.alt-loc: strmini.h
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

# PHW_RECEIVE_DEVICE_SRB callback



## -description
<p><i>The minidriver-supplied StrMiniReceiveDevicePacket</i> routine handles class driver requests that apply to the driver as a whole, such as initializing the device, or opening a stream within the device.</p>


## -prototype

````
PHW_RECEIVE_DEVICE_SRB StrMiniReceiveDevicePacket;

VOID StrMiniReceiveDevicePacket(
  _In_ PHW_STREAM_REQUEST_BLOCK pSRB
)
{ ... }
````


## -parameters
<dl>

### -param pSRB [in]

<dd>
<p>Pointer to the stream request block.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The minidriver specifies this routine in the <b>HwReceivePacket</b> member of its <a href="..\strmini\ns-strmini--hw-initialization-data.md">HW_INITIALIZATION_DATA</a> structure. The minidriver passes this structure to the class driver when it registers itself by calling <a href="stream.streamclassregisterminidriver">StreamClassRegisterMinidriver</a>.</p>

<p><i>StrMiniReceiveDevicePacket</i> must handle class driver requests that apply to the driver as a whole, such as initializing the device, or opening a stream within the device. The class driver passes its information in the form of a pointer to a stream request block. The class driver fills in some of the entries in the stream request block. The minidriver, upon completion of the routine, must fill in additional information that the class driver will use to continue processing. </p>

<p>Upon completion of its handling of the request, the minidriver passes the structure back to the class driver by calling <a href="..\strmini\nf-strmini-streamclassdevicenotification.md">StreamClassDeviceNotification</a><b>(DeviceRequestComplete, pSRB-&gt;HwDeviceExtension, pSRB)</b>. </p>

<p>See information about relevant SRB codes in <a href="https://msdn.microsoft.com/library/windows/hardware/ff568295">Stream Class SRB Reference</a>.</p>

<p>When the minidriver finishes its processing of the request, it enters the return status of the operation in <i>pSrb</i>-&gt;<b>Status</b>. The minidriver should enter STATUS_SUCCESS for normal successful processing. If the minidriver does not support that Command value, it should set <i>pSrb</i>-&gt;<b>Status</b> to STATUS_NOT_IMPLEMENTED. If there is a device hardware error that prevents the minidriver from completing the request, it should set <i>pSrb</i>-&gt;<b>Status</b> to STATUS_IO_DEVICE_ERROR. Other error codes the routine uses in specific circumstances are listed above with the specific Command code.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
</table>