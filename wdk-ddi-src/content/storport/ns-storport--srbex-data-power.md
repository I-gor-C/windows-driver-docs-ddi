---
UID: NS.storport._SRBEX_DATA_POWER
title: SRBEX_DATA_POWER
author: windows-driver-content
description: The SRBEX_DATA_POWER structure contains the request data for an extended power SRB.
old-location: storage\srbex_data_power.htm
old-project: storage
ms.assetid: 61F5C316-5214-45A6-B4BA-DEE6A224E811
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SRBEX_DATA_POWER, SRBEX_DATA_POWER, *PSRBEX_DATA_POWER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Storport.h, Srb.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SRBEX_DATA_POWER
req.alt-loc: Storport.h
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

# SRBEX_DATA_POWER structure



## -description
<p>The <b>SRBEX_DATA_POWER</b> structure contains the request data for an extended power SRB.</p>


## -syntax

````
typedef struct _SRBEX_DATA_POWER {
  SRBEXDATATYPE           Type;
  ULONG                   Length;
  ULONG                   SrbPowerFlags;
  UCHAR                   Reserved[3];
  STOR_DEVICE_POWER_STATE DevicePowerState;
  STOR_POWER_ACTION       PowerAction;
} SRBEX_DATA_POWER, *PSRBEX_DATA_POWER;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Data type indicator for the bidirectional extended SRB data structure. Set to <b>SrbExDataTypePower</b>.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Length of the data in this structure starting with the <b>SrbPowerFlags</b> member. Set to SRBEX_DATA_POWER_LENGTH.</p>
</dd>

### -field <b>SrbPowerFlags</b>

<dd>
<p>Indicates that the power request is for the adapter if SRB_POWER_FLAGS_ADAPTER_REQUEST is set and that storage device address is reserved. Otherwise, <i>SrbPowerFlags</i> will be <b>NULL</b>, indicating that the request is for the storage device specified by an address at <b>AddressOffset</b> in the <a href="..\srb\ns-srb--storage-request-block.md">STORAGE_REQUEST_BLOCK</a> structure.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved. Set to 0.</p>
</dd>

### -field <b>DevicePowerState</b>

<dd>
<p>An enumerator value of type <a href="..\storport\ne-storport--stor-device-power-state.md">STOR_DEVICE_POWER_STATE</a> that specifies the requested power state of the device. </p>
</dd>

### -field <b>PowerAction</b>

<dd>
<p>An enumerator value of type <a href="storage.stor_power_action">STOR_POWER_ACTION</a> that specifies the type of system shutdown that is about to occur. This value is meaningful only if the device is moving into the D1, D2, or D3 power state as indicated by the <b>DevicePowerState</b> member.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h or Srb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\storport\ne-storport--stor-device-power-state.md">STOR_DEVICE_POWER_STATE</a>
</dt>
<dt>
<a href="storage.stor_power_action">STOR_POWER_ACTION</a>
</dt>
<dt>
<a href="..\srb\ns-srb--storage-request-block.md">STORAGE_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SRBEX_DATA_POWER structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
