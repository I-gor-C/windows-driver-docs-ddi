---
UID: NS.stiusd._STI_USD_CAPS
title: STI_USD_CAPS
author: windows-driver-content
description: The STI_USD_CAPS structure is used as a parameter for the IStiUSD::GetCapabilities method.
old-location: image\sti_usd_caps.htm
old-project: image
ms.assetid: 24dda069-5f93-469d-8ce3-87b488019b88
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: STI_USD_CAPS, STI_USD_CAPS, *PSTI_USD_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: stiusd.h
req.include-header: Stiusd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STI_USD_CAPS
req.alt-loc: stiusd.h
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
req.iface: IStiUSD
req.product: Windows 10 or later.
---

# STI_USD_CAPS structure



## -description
<p>The STI_USD_CAPS structure is used as a parameter for the <a href="image.istiusd_getcapabilities">IStiUSD::GetCapabilities</a> method.</p>


## -syntax

````
typedef struct _STI_USD_CAPS {
  DWORD dwVersion;
  DWORD dwGenericCaps;
} STI_USD_CAPS, *PSTI_USD_CAPS;
````


## -struct-fields
<dl>

### -field <b>dwVersion</b>

<dd>
<p>STI version number. This value must be STI_VERSION, defined in <i>Sti.h</i>.</p>
</dd>

### -field <b>dwGenericCaps</b>

<dd>
<p>Bit flags indicating driver capabilities. The following flags are defined in <i>Stiusd.h</i>.</p>
<p></p>
<dl>

### -field <a id="STI_USD_GENCAP_NATIVE_PUSHSUPPORT"></a><a id="sti_usd_gencap_native_pushsupport"></a>STI_USD_GENCAP_NATIVE_PUSHSUPPORT

<dd>
<p>The driver supports asynchronous device notifications.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="STI_USD_GENCAP_OPEN_DEVICE_FOR_ME"></a><a id="sti_usd_gencap_open_device_for_me"></a>STI_USD_GENCAP_OPEN_DEVICE_FOR_ME

<dd>
<p><i>Not used.</i></p>
</dd>
</dl>
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
<dt>Stiusd.h (include Stiusd.h)</dt>
</dl>
</td>
</tr>
</table>