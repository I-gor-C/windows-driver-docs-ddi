---
UID: NE.pepfx._GPIO_PIN_CONFIG_TYPE
title: GPIO_PIN_CONFIG_TYPE
author: windows-driver-content
description: The GPIO_PIN_CONFIG_TYPE enumeration describes a connection IO resource.
old-location: kernel\gpio_pin_config_type.htm
old-project: kernel
ms.assetid: 76509992-E5A7-4C2F-84D3-B3FD06ACEFE1
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: VPCI_PNP_ID, VPCI_PNP_ID, *PVPCI_PNP_ID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GPIO_PIN_CONFIG_TYPE
req.alt-loc: pepfx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks.
req.iface: 
---

# GPIO_PIN_CONFIG_TYPE enumeration



## -description
<p>The <b>GPIO_PIN_CONFIG_TYPE</b> enumeration describes a connection IO resource.</p>


## -syntax

````
typedef enum _GPIO_PIN_CONFIG_TYPE { 
  PullDefault,
  PullUp,
  PullDown,
  PullNone
} GPIO_PIN_CONFIG_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PullDefault"></a><a id="pulldefault"></a><a id="PULLDEFAULT"></a><b>PullDefault</b>

<dd>
<p>Indicates that no configuration is applied to this pin.</p>
</dd>

### -field <a id="PullUp"></a><a id="pullup"></a><a id="PULLUP"></a><b>PullUp</b>

<dd>
<p>Indicates that this pin is configured to use a pull-up resistor.</p>
</dd>

### -field <a id="PullDown"></a><a id="pulldown"></a><a id="PULLDOWN"></a><b>PullDown</b>

<dd>
<p>Indicates that this pin is configured to use a pull-down resistor.</p>
</dd>

### -field <a id="PullNone"></a><a id="pullnone"></a><a id="PULLNONE"></a><b>PullNone</b>

<dd>
<p>Indicates that this pin is not configured to use a pull-up or pull-down resistor.</p>
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
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>