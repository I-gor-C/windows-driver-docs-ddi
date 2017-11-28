---
UID: NS.ksmedia.PKSPROPERTY_SELECTOR_S
title: PKSPROPERTY_SELECTOR_S
author: windows-driver-content
description: The KSPROPERTY_SELECTOR_S structure describes filter-based property settings in the PROPSETID_VIDCAP_SELECTOR property set.
old-location: stream\ksproperty_selector_s.htm
old-project: stream
ms.assetid: cc9928b7-fab2-44c1-8613-3a94b5e8dcab
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSPROPERTY_SELECTOR_S, KSPROPERTY_SELECTOR_S, *PKSPROPERTY_SELECTOR_S
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_SELECTOR_S
req.alt-loc: ksmedia.h
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
---

# PKSPROPERTY_SELECTOR_S structure



## -description
<p>The KSPROPERTY_SELECTOR_S structure describes filter-based property settings in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567810">PROPSETID_VIDCAP_SELECTOR</a> property set.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  LONG       Value;
  ULONG      Flags;
  ULONG      Capabilities;
} KSPROPERTY_SELECTOR_S, *PKSPROPERTY_SELECTOR_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff566720">KSP_NODE</a> structure that describes the node, property set, property ID, and request type.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>Specifies the value of a request. For Set requests, the minidriver should set the property specified in <b>Property</b> to this value. For Get requests, the minidriver should return the value of the property specified in <b>Property</b>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Specifies the flags of a request. For Set requests, this value indicates the desired setting. For Get requests, this value contains the current setting.</p>
</dd>

### -field <b>Capabilities</b>

<dd>
<p>Specifies the capabilities of a property. This member has meaning only for Get requests. The minidriver should return the capabilities of the Selector with respect to the property specified in <b>Property</b>.</p>
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
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565217">KSPROPERTY_SELECTOR_NODE_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_SELECTOR_S structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
