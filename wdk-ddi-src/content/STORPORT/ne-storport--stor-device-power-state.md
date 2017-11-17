---
UID: NE.storport._STOR_DEVICE_POWER_STATE
title: STOR_DEVICE_POWER_STATE
author: windows-driver-content
description: The STOR_DEVICE_POWER_STATE enumerator specifies a device power state.
old-location: storage\stor_device_power_state.htm
ms.assetid: 563ece3e-1359-4e3c-9ae7-61b94bf90ad0
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STOR_DEVICE_POWER_STATE
req.alt-loc: storport.h
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
ms.keywords: STORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER
req.iface: 
req.product: Windows 10 or later.
---

# STOR_DEVICE_POWER_STATE enumeration



## -description
<p>The STOR_DEVICE_POWER_STATE enumerator specifies a device power state.</p>


## -syntax

````
typedef enum _STOR_DEVICE_POWER_STATE { 
  StorPowerDeviceUnspecified  = 0,
  StorPowerDeviceD0           = 1,
  StorPowerDeviceD1           = 2,
  StorPowerDeviceD2           = 3,
  StorPowerDeviceD3           = 4,
  StorPowerDeviceMaximum      = 5
} STOR_DEVICE_POWER_STATE, *PSTOR_DEVICE_POWER_STATE;
````


## -enum-fields
<dl>

### -field <a id="StorPowerDeviceUnspecified"></a><a id="storpowerdeviceunspecified"></a><a id="STORPOWERDEVICEUNSPECIFIED"></a><b>StorPowerDeviceUnspecified</b>

<dd>
<p>Device power state unspecified.</p>
</dd>

### -field <a id="StorPowerDeviceD0"></a><a id="storpowerdeviced0"></a><a id="STORPOWERDEVICED0"></a><b>StorPowerDeviceD0</b>

<dd>
<p>The D0 device power state.</p>
</dd>

### -field <a id="StorPowerDeviceD1"></a><a id="storpowerdeviced1"></a><a id="STORPOWERDEVICED1"></a><b>StorPowerDeviceD1</b>

<dd>
<p>The D1 device power state.</p>
</dd>

### -field <a id="StorPowerDeviceD2"></a><a id="storpowerdeviced2"></a><a id="STORPOWERDEVICED2"></a><b>StorPowerDeviceD2</b>

<dd>
<p>The D2 device power state.</p>
</dd>

### -field <a id="StorPowerDeviceD3"></a><a id="storpowerdeviced3"></a><a id="STORPOWERDEVICED3"></a><b>StorPowerDeviceD3</b>

<dd>
<p>The D3 device power state.</p>
</dd>

### -field <a id="StorPowerDeviceMaximum"></a><a id="storpowerdevicemaximum"></a><a id="STORPOWERDEVICEMAXIMUM"></a><b>StorPowerDeviceMaximum</b>

<dd>
<p>The upper delimiting value on device power states.</p>
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
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565389">SCSI_POWER_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20STOR_DEVICE_POWER_STATE enumeration%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
