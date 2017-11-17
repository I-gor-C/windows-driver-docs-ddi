---
UID: NS.usbfnbase._USBFN_BUS_CONFIGURATION_INFO
title: USBFN_BUS_CONFIGURATION_INFO
author: windows-driver-content
description: Configuration packet that stores information about an available USB configuration.
old-location: buses\usbfn_bus_configuration_info.htm
ms.assetid: 26F11BC8-0F43-4E52-B2E1-2C3C6B327CF0
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: usbfnbase.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBFN_BUS_CONFIGURATION_INFO
req.alt-loc: usbfnbase.h
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
ms.keywords: USBFN_BUS_CONFIGURATION_INFO, USBFN_BUS_CONFIGURATION_INFO, *PUSBFN_BUS_CONFIGURATION_INFO
req.iface: 
req.product: Windows 10 or later.
---

# USBFN_BUS_CONFIGURATION_INFO structure



## -description
<p>Configuration packet that stores information about 
an available USB configuration.</p>


## -syntax

````
typedef struct _USBFN_BUS_CONFIGURATION_INFO {
  WCHAR    ConfigurationName[MAX_CONFIGURATION_NAME_LENGTH];
  BOOLEAN  IsCurrent;
  BOOLEAN  IsActive;
} USBFN_BUS_CONFIGURATION_INFO, *PUSBFN_BUS_CONFIGURATION_INFO;
````


## -struct-fields
<dl>

### -field <b> ConfigurationName</b>

<dd>
<p>A NULL-terminated string that indicates the name of a configuration.</p>
</dd>

### -field <b> IsCurrent</b>

<dd>
<p>Indicates whether this configuration is the 
    current configuration.</p>
</dd>

### -field <b> IsActive</b>

<dd>
<p>    Indicates whether the configuration is active. This is a read-only information that is returned by USB function class extension (UFX) and is ignored in requests sent to UFX.
</p>
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
<dt>Usbfnbase.h</dt>
</dl>
</td>
</tr>
</table>