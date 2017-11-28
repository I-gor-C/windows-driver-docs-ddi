---
UID: NS.ucxusbdevice._ADDRESS0_OWNERSHIP_ACQUIRE
title: ADDRESS0_OWNERSHIP_ACQUIRE
author: windows-driver-content
description: Contains parameters for configuring the device.
old-location: buses\_address0_ownership_acquire.htm
old-project: usbref
ms.assetid: D2FECBA5-21DF-411C-BBDB-968328E18C12
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ADDRESS0_OWNERSHIP_ACQUIRE, ADDRESS0_OWNERSHIP_ACQUIRE, *PADDRESS0_OWNERSHIP_ACQUIRE
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
req.alt-api: ADDRESS0_OWNERSHIP_ACQUIRE
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

# ADDRESS0_OWNERSHIP_ACQUIRE structure



## -description
<p>Contains parameters for configuring the device. </p>


## -syntax

````
typedef struct _ADDRESS0_OWNERSHIP_ACQUIRE {
#if __cplusplus
  USBDEVICE_MGMT_HEADER Header;
#else 
  USBDEVICE_MGMT_HEADER ;
#endif 
} ADDRESS0_OWNERSHIP_ACQUIRE, *P_ADDRESS0_OWNERSHIP_ACQUIRE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt188075">USBDEVICE_MGMT_HEADER</a> structure that contains  the handle for the USB hub or device.</p>
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