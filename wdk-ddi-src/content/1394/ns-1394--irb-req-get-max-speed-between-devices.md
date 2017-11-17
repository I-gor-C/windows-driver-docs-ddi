---
UID: NS.1394._IRB_REQ_GET_MAX_SPEED_BETWEEN_DEVICES
title: IRB_REQ_GET_MAX_SPEED_BETWEEN_DEVICES
author: windows-driver-content
description: This structure contains the fields necessary in order for the Bus driver to carry out a GetMaxSpeedBetweenDevices request.
old-location: ieee\irb_req_get_max_speed_between_devices.htm
ms.assetid: 7B296D94-32DB-4190-935F-F1CC5F566706
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_GET_MAX_SPEED_BETWEEN_DEVICES
req.alt-loc: 1394.h
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
ms.keywords: IRB_REQ_GET_MAX_SPEED_BETWEEN_DEVICES, IRB_REQ_GET_MAX_SPEED_BETWEEN_DEVICES
---

# IRB_REQ_GET_MAX_SPEED_BETWEEN_DEVICES structure



## -description
<p>This structure contains the fields necessary in order for the Bus driver to carry out a
<b>GetMaxSpeedBetweenDevices</b> request.</p>


## -syntax

````
typedef struct _IRB_REQ_GET_MAX_SPEED_BETWEEN_DEVICES {
  ULONG          fulFlags;
  ULONG          ulNumberOfDestinations;
  PDEVICE_OBJECT hDestinationDeviceObjects[64];
  ULONG          fulSpeed;
} IRB_REQ_GET_MAX_SPEED_BETWEEN_DEVICES;
````


## -struct-fields
<dl>

### -field <b>fulFlags</b>

<dd>
<p>Specifies the source device. Zero indicates the calling device. USE_LOCAL_NODE indicates the computer itself.</p>
<div class="alert"><b>Note</b>  In Windows 7, the new 1394 bus driver returns only the speed between the local node and the device. The USE_LOCAL_NODE flag must be set in the <b>u.GetMaxSpeedBetweenDevices.fulFlags</b> parameter.</div>
<div> </div>
</dd>

### -field <b>ulNumberOfDestinations</b>

<dd>
<p>Specifies the number of destination devices.</p>
</dd>

### -field <b>hDestinationDeviceObjects</b>

<dd>
<p>Points to an array of the device objects of the destination devices.</p>
</dd>

### -field <b>fulSpeed</b>

<dd>
<p>Specifies the maximum speed returned.</p>
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
<dt>1394.h</dt>
</dl>
</td>
</tr>
</table>