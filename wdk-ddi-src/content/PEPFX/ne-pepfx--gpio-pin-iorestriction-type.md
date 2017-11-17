---
UID: NE.pepfx._GPIO_PIN_IORESTRICTION_TYPE
title: GPIO_PIN_IORESTRICTION_TYPE
author: windows-driver-content
description: The GPIO_PIN_IORESTRICTION_TYPE enumeration describes the functions that a GPIO pin is limited to performing.
old-location: kernel\gpio_pin_iorestriction_type.htm
ms.assetid: 381A59EE-BA1C-4810-842B-1D3E4D964486
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: kernel
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GPIO_PIN_IORESTRICTION_TYPE
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
req.irql: PASSIVE_LEVEL
ms.keywords: VPCI_PNP_ID, VPCI_PNP_ID, *PVPCI_PNP_ID
req.iface: 
---

# GPIO_PIN_IORESTRICTION_TYPE enumeration



## -description
<p>The <b>GPIO_PIN_IORESTRICTION_TYPE</b> enumeration describes the functions that a GPIO pin is limited to performing.</p>


## -syntax

````
typedef enum _GPIO_PIN_IORESTRICTION_TYPE { 
  IoRestrictionNone,
  IoRestrictionInputOnly,
  IoRestrictionOutputOnly,
  IoRestrictionNoneAndPreserve
} GPIO_PIN_IORESTRICTION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="IoRestrictionNone"></a><a id="iorestrictionnone"></a><a id="IORESTRICTIONNONE"></a><b>IoRestrictionNone</b>

<dd>
<p>Indicates that the GPIO pin is not restricted to either input or output. When no IO restriction is described, it is assumed to be <b>IoRestrictionNone</b>. </p>
</dd>

### -field <a id="IoRestrictionInputOnly"></a><a id="iorestrictioninputonly"></a><a id="IORESTRICTIONINPUTONLY"></a><b>IoRestrictionInputOnly</b>

<dd>
<p>Indicates that the GPIO pin is restricted to input. </p>
</dd>

### -field <a id="IoRestrictionOutputOnly"></a><a id="iorestrictionoutputonly"></a><a id="IORESTRICTIONOUTPUTONLY"></a><b>IoRestrictionOutputOnly</b>

<dd>
<p>Indicates that the GPIO pin is restricted to output. </p>
</dd>

### -field <a id="IoRestrictionNoneAndPreserve"></a><a id="iorestrictionnoneandpreserve"></a><a id="IORESTRICTIONNONEANDPRESERVE"></a><b>IoRestrictionNoneAndPreserve</b>

<dd>
<p>Indicates that the GPIO pin is not restricted to either input or output and that the mode should be preserved when the driver is unloaded. </p>
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