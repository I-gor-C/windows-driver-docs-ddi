---
UID: NE.wwan._WWAN_REGISTER_ACTION
title: WWAN_REGISTER_ACTION
author: windows-driver-content
description: The WWAN_REGISTER_ACTION enumeration lists the different provider network registration actions that are supported by the MB device.
old-location: netvista\wwan_register_action.htm
ms.assetid: 8c343094-0927-4cdd-be39-93dcb25f6bf6
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_REGISTER_ACTION
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
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_REGISTER_ACTION enumeration



## -description
<p>The WWAN_REGISTER_ACTION enumeration lists the different provider network registration actions that
  are supported by the MB device.</p>


## -syntax

````
typedef enum _WWAN_REGISTER_ACTION { 
  WwanRegisterActionAutomatic  = 0,
  WwanRegisterActionManual,
  WwanRegisterActionMax
} WWAN_REGISTER_ACTION, *PWWAN_REGISTER_ACTION;
````


## -enum-fields
<dl>

### -field <a id="WwanRegisterActionAutomatic"></a><a id="wwanregisteractionautomatic"></a><a id="WWANREGISTERACTIONAUTOMATIC"></a><b>WwanRegisterActionAutomatic</b>

<dd>
<p>Automatically register with provider and then packet-attach, if required.</p>
</dd>

### -field <a id="WwanRegisterActionManual"></a><a id="wwanregisteractionmanual"></a><a id="WWANREGISTERACTIONMANUAL"></a><b>WwanRegisterActionManual</b>

<dd>
<p>Manually register with provider and then packet-attach, if required.</p>
</dd>

### -field <a id="WwanRegisterActionMax"></a><a id="wwanregisteractionmax"></a><a id="WWANREGISTERACTIONMAX"></a><b>WwanRegisterActionMax</b>

<dd>
<p>The total number of supported registration actions.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571236">WWAN_SET_REGISTER_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_REGISTER_ACTION enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
