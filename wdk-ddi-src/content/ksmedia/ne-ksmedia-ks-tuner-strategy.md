---
UID: NE.ksmedia.KS_TUNER_STRATEGY
title: KS_TUNER_STRATEGY
author: windows-driver-content
description: The KS_TUNER_STRATEGY enumeration defines tuning method strategies.
old-location: stream\ks_tuner_strategy.htm
old-project: stream
ms.assetid: 333b1b11-cc6e-4546-9638-e5dcb4c2607c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_TUNER_STRATEGY
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

# KS_TUNER_STRATEGY enumeration



## -description
<p>The KS_TUNER_STRATEGY enumeration defines tuning method strategies.</p>


## -syntax

````
typedef enum  { 
  KS_TUNER_STRATEGY_PLL              = 0X01,
  KS_TUNER_STRATEGY_SIGNAL_STRENGTH  = 0X02,
  KS_TUNER_STRATEGY_DRIVER_TUNES     = 0X04
} KS_TUNER_STRATEGY;
````


## -enum-fields
<dl>

### -field <a id="KS_TUNER_STRATEGY_PLL"></a><a id="ks_tuner_strategy_pll"></a><b>KS_TUNER_STRATEGY_PLL</b>

<dd>
<p>The tuning accuracy for the device is measured by a phase locked loop (PLL) offset.</p>
</dd>

### -field <a id="KS_TUNER_STRATEGY_SIGNAL_STRENGTH"></a><a id="ks_tuner_strategy_signal_strength"></a><b>KS_TUNER_STRATEGY_SIGNAL_STRENGTH</b>

<dd>
<p>The tuning accuracy for the device is measured by signal strength.</p>
</dd>

### -field <a id="KS_TUNER_STRATEGY_DRIVER_TUNES"></a><a id="ks_tuner_strategy_driver_tunes"></a><b>KS_TUNER_STRATEGY_DRIVER_TUNES</b>

<dd>
<p>The minidriver has total control over the fine tuning process. No fine tuning is done by <i>Kstvtune.ax</i>.</p>
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
<a href="stream.ksproperty_tuner_mode_caps_s">KSPROPERTY_TUNER_MODE_CAPS_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_TUNER_STRATEGY enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
