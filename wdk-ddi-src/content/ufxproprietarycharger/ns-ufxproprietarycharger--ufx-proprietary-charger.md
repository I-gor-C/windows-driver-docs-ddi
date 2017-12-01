---
UID: NS.ufxproprietarycharger._UFX_PROPRIETARY_CHARGER
title: UFX_PROPRIETARY_CHARGER
author: windows-driver-content
description: Describes the proprietary charger's device power requirements.
old-location: buses\ufx_proprietary_charger.htm
old-project: usbref
ms.assetid: FAAEDAFE-69A8-4092-8301-DB159FD3583D
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UFX_PROPRIETARY_CHARGER, UFX_PROPRIETARY_CHARGER, *PUFX_PROPRIETARY_CHARGER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ufxproprietarycharger.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFX_PROPRIETARY_CHARGER
req.alt-loc: ufxproprietarycharger.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UFX_PROPRIETARY_CHARGER structure



## -description
<p>Describes the proprietary charger's device power requirements.</p>


## -syntax

````
typedef struct _UFX_PROPRIETARY_CHARGER {
  GUID               ChargerId;
  DEVICE_POWER_STATE DxState;
} UFX_PROPRIETARY_CHARGER, *PUFX_PROPRIETARY_CHARGER;
````


## -struct-fields
<dl>

### -field <b>ChargerId</b>

<dd>
<p>Charger identifier used to identify a specific type of charger.</p>
</dd>

### -field <b>DxState</b>

<dd>
<p>The minimum required device power state when it is connected, indicated by one of the <a href="..\wudfddi\ne-wudfddi--device-power-state.md">DEVICE_POWER_STATE</a>-typed flags.</p>
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
<dt>Ufxproprietarycharger.h</dt>
</dl>
</td>
</tr>
</table>