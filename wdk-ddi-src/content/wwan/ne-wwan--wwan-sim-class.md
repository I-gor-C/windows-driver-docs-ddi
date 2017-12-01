---
UID: NE.wwan._WWAN_SIM_CLASS
title: WWAN_SIM_CLASS
author: windows-driver-content
description: The WWAN_SIM_CLASS enumeration lists the different types of Subscriber Identity Modules (SIMs) that are supported by the MB device.
old-location: netvista\wwan_sim_class.htm
old-project: netvista
ms.assetid: 4d66874b-bb1d-43e5-a4b2-525face7de81
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: WWAN_SIM_CLASS
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

# WWAN_SIM_CLASS enumeration



## -description
<p>The WWAN_SIM_CLASS enumeration lists the different types of Subscriber Identity Modules (SIMs) that
  are supported by the MB device.</p>


## -syntax

````
typedef enum _WWAN_SIM_CLASS { 
  WwanSimClassUnknown       = 0,
  WwanSimClassSimLogical,
  WwanSimClassSimRemovable,
  WwanSimClassSimRemote,
  WwanSimClassMax
} WWAN_SIM_CLASS, *PWWAN_SIM_CLASS;
````


## -enum-fields
<dl>

### -field <a id="WwanSimClassUnknown"></a><a id="wwansimclassunknown"></a><a id="WWANSIMCLASSUNKNOWN"></a><b>WwanSimClassUnknown</b>

<dd>
<p>The device supports an unknown class of SIM.</p>
</dd>

### -field <a id="WwanSimClassSimLogical"></a><a id="wwansimclasssimlogical"></a><a id="WWANSIMCLASSSIMLOGICAL"></a><b>WwanSimClassSimLogical</b>

<dd>
<p>The device supports a logical or embedded SIM.</p>
</dd>

### -field <a id="WwanSimClassSimRemovable"></a><a id="wwansimclasssimremovable"></a><a id="WWANSIMCLASSSIMREMOVABLE"></a><b>WwanSimClassSimRemovable</b>

<dd>
<p>The device supports a removable SIM.</p>
</dd>

### -field <a id="WwanSimClassSimRemote"></a><a id="wwansimclasssimremote"></a><a id="WWANSIMCLASSSIMREMOTE"></a><b>WwanSimClassSimRemote</b>

<dd>
<p>The device supports a remote SIM that is not physically attached to MB device. For example, a
     tethered cellular telephone modem.</p>
</dd>

### -field <a id="WwanSimClassMax"></a><a id="wwansimclassmax"></a><a id="WWANSIMCLASSMAX"></a><b>WwanSimClassMax</b>

<dd>
<p>The total number of supported SIM classes.</p>
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
<a href="..\wwan\ns-wwan--wwan-device-caps.md">WWAN_DEVICE_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SIM_CLASS enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
