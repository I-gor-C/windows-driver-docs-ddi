---
UID: NE.wwan._WWAN_RADIO
title: WWAN_RADIO
author: windows-driver-content
description: The WWAN_RADIO enumeration lists the different types of radio power modes that are supported by the MB device.
old-location: netvista\wwan_radio.htm
old-project: netvista
ms.assetid: f589180c-5379-4f50-876e-48d142b44be4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_RADIO
req.alt-loc: wwan.h
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

# WWAN_RADIO enumeration



## -description
<p>The WWAN_RADIO enumeration lists the different types of radio power modes that are supported by the
  MB device.</p>


## -syntax

````
typedef enum _WWAN_RADIO { 
  WwanRadioOff  = 0,
  WwanRadioOn
} WWAN_RADIO, *PWWAN_RADIO;
````


## -enum-fields
<dl>

### -field <a id="WwanRadioOff"></a><a id="wwanradiooff"></a><a id="WWANRADIOOFF"></a><b>WwanRadioOff</b>

<dd>
<p>The radio power is turned off.</p>
</dd>

### -field <a id="WwanRadioOn"></a><a id="wwanradioon"></a><a id="WWANRADIOON"></a><b>WwanRadioOn</b>

<dd>
<p>The radio power is turned on.</p>
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
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571225">WWAN_RADIO_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567925">NDIS_WWAN_SET_RADIO_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_RADIO enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
