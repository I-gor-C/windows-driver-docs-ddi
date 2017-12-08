---
UID: NE.wditypes._WDI_WPS_CONFIGURATION_METHOD
title: WDI_WPS_CONFIGURATION_METHOD
author: windows-driver-content
description: The WDI_WPS_CONFIGURATION_METHOD enumeration defines WPS configuration methods.
old-location: netvista\wdi_wps_configuration_method.htm
old-project: netvista
ms.assetid: 116B19BD-959F-4711-B3FB-9880539B7849
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_WPS_CONFIGURATION_METHOD
req.alt-loc: wditypes.hpp
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
req.iface: 
req.product: Windows 10 or later.
---

# WDI_WPS_CONFIGURATION_METHOD enumeration



## -description
<p>The WDI_WPS_CONFIGURATION_METHOD enumeration defines WPS configuration methods.</p>


## -syntax

````
typedef enum _WDI_WPS_CONFIGURATION_METHOD { 
  WDI_WPS_CONFIGURATION_METHOD_NULL           = 0,
  WDI_WPS_CONFIGURATION_METHOD_DISPLAY        = 0x0008,
  WDI_WPS_CONFIGURATION_METHOD_NFC_TAG        = 0x0020,
  WDI_WPS_CONFIGURATION_METHOD_NFC_INTERFACE  = 0x0040,
  WDI_WPS_CONFIGURATION_METHOD_PUSHBUTTON     = 0x0080,
  WDI_WPS_CONFIGURATION_METHOD_KEYPAD         = 0x0100,
  WDI_WPS_CONFIGURATION_METHOD_WFDS_DEFAULT   = 0x1000
} WDI_WPS_CONFIGURATION_METHOD;
````


## -enum-fields
<dl>

### -field WDI_WPS_CONFIGURATION_METHOD_NULL

<dd>
<p>WFDS.</p>
</dd>

### -field WDI_WPS_CONFIGURATION_METHOD_DISPLAY

<dd>
<p>Pin display.</p>
</dd>

### -field WDI_WPS_CONFIGURATION_METHOD_NFC_TAG

<dd>
<p>NFC tag.</p>
</dd>

### -field WDI_WPS_CONFIGURATION_METHOD_NFC_INTERFACE

<dd>
<p>NFC interface.</p>
</dd>

### -field WDI_WPS_CONFIGURATION_METHOD_PUSHBUTTON

<dd>
<p>Push button.</p>
</dd>

### -field WDI_WPS_CONFIGURATION_METHOD_KEYPAD

<dd>
<p>Pin keypad.</p>
</dd>

### -field WDI_WPS_CONFIGURATION_METHOD_WFDS_DEFAULT

<dd>
<p>WFDS.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>