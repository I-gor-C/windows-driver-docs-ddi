---
UID: NE.ksmedia.KS_TUNER_TUNING_FLAGS
title: KS_TUNER_TUNING_FLAGS
author: windows-driver-content
description: The KS_TUNER_TUNING_FLAGS enumeration defines tuning flags that describe the granularity of a tuning operation.
old-location: stream\ks_tuner_tuning_flags.htm
ms.assetid: f8742053-0d02-40af-9a6e-7af029db8575
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_TUNER_TUNING_FLAGS
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
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
req.iface: 
---

# KS_TUNER_TUNING_FLAGS enumeration



## -description
<p>The KS_TUNER_TUNING_FLAGS enumeration defines tuning flags that describe the granularity of a tuning operation.</p>


## -syntax

````
typedef enum  { 
  KS_TUNER_TUNING_EXACT   = 1,
  KS_TUNER_TUNING_FINE    = 2,
  KS_TUNER_TUNING_COARSE  = 3
} KS_TUNER_TUNING_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="KS_TUNER_TUNING_EXACT"></a><a id="ks_tuner_tuning_exact"></a><b>KS_TUNER_TUNING_EXACT</b>

<dd>
<p>The tuner should tune directly to the specified frequency and bypass any fine tuning logic.</p>
</dd>

### -field <a id="KS_TUNER_TUNING_FINE"></a><a id="ks_tuner_tuning_fine"></a><b>KS_TUNER_TUNING_FINE</b>

<dd>
<p>The tuning operation should perform a comprehensive search for the best tuning. This flag is used only if the strategy is KS_TUNER_STRATEGY_DRIVER_TUNES.</p>
</dd>

### -field <a id="KS_TUNER_TUNING_COARSE"></a><a id="ks_tuner_tuning_coarse"></a><b>KS_TUNER_TUNING_COARSE</b>

<dd>
<p>The tuning operation should perform a fast search and attempt only to determine if a valid signal is present. This flag is used only if the strategy is KS_TUNER_STRATEGY_DRIVER_TUNES.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565839">KSPROPERTY_TUNER_FREQUENCY_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_TUNER_TUNING_FLAGS enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
