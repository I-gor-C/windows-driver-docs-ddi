---
UID: NC.bthddi.PFNBTH_IS_BLUETOOTH_VERSION_AVAILABLE
title: PFNBTH_IS_BLUETOOTH_VERSION_AVAILABLE
author: windows-driver-content
description: The IsBluetoothVersionAvailable function checks whether a given Bluetooth version is supported by the operating system.
old-location: bltooth\isbluetoothversionavailable.htm
old-project: bltooth
ms.assetid: 10662237-18b4-4f37-a704-985b2db0d689
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: IBidiSpl2, UnbindDevice, IBidiSpl2::UnbindDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Desktop
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IsBluetoothVersionAvailable
req.alt-loc: bthddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IBidiSpl2
---

# PFNBTH_IS_BLUETOOTH_VERSION_AVAILABLE callback



## -description
<p>The 
  <i>IsBluetoothVersionAvailable</i> function checks whether a given Bluetooth version is supported by the
  operating system.</p>


## -prototype

````
PFNBTH_IS_BLUETOOTH_VERSION_AVAILABLE IsBluetoothVersionAvailable;

BOOLEAN IsBluetoothVersionAvailable(
  _In_ UCHAR MajorVersion,
  _In_ UCHAR MinorVersion
)
{ ... }
````


## -parameters
<dl>

### -param <i>MajorVersion</i> [in]

<dd>
<p>This parameter specifies the major version number of Bluetooth that is requested.</p>
</dd>

### -param <i>MinorVersion</i> [in]

<dd>
<p>This parameter specifies the minor version number of Bluetooth that is requested.</p>
</dd>
</dl>

## -returns
<p><i>IsBluetoothVersionAvailable</i> returns <b>TRUE</b> if the Bluetooth version that the operating system
     provides is greater than or equal to the Bluetooth version number that is being requested.</p>

## -remarks
<p>Bluetooth profile drivers should call this function before performing any operations that are not
    supported in all Bluetooth versions.</p>

<p>Bluetooth profile drivers should call this function before performing any operations that are not
    supported in all Bluetooth versions.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows Vista, and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bthddi.h (include Bthddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>