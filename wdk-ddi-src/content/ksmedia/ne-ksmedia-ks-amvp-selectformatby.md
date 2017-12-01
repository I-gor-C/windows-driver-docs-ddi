---
UID: NE.ksmedia.KS_AMVP_SELECTFORMATBY
title: KS_AMVP_SELECTFORMATBY
author: windows-driver-content
description: The KS_AMVP_SELECTFORMATBY enumeration specifies the criteria that the Overlay Mixer Filter should use to select the video format.
old-location: stream\ks_amvp_selectformatby.htm
old-project: stream
ms.assetid: b7fb6752-9711-4922-a806-915c362bcffe
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
req.alt-api: KS_AMVP_SELECTFORMATBY
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

# KS_AMVP_SELECTFORMATBY enumeration



## -description
<p>The KS_AMVP_SELECTFORMATBY enumeration specifies the criteria that the Overlay Mixer Filter should use to select the video format.</p>


## -syntax

````
typedef enum  { 
  KS_AMVP_DO_NOT_CARE           = 0,
  KS_AMVP_BEST_BANDWIDTH        = 1,
  KS_AMVP_INPUT_SAME_AS_OUTPUT  = 2
} KS_AMVP_SELECTFORMATBY;
````


## -enum-fields
<dl>

### -field <a id="KS_AMVP_DO_NOT_CARE"></a><a id="ks_amvp_do_not_care"></a><b>KS_AMVP_DO_NOT_CARE</b>

<dd>
<p>The format does not matter.</p>
</dd>

### -field <a id="KS_AMVP_BEST_BANDWIDTH"></a><a id="ks_amvp_best_bandwidth"></a><b>KS_AMVP_BEST_BANDWIDTH</b>

<dd>
<p>Use the largest available bandwidth.</p>
</dd>

### -field <a id="KS_AMVP_INPUT_SAME_AS_OUTPUT"></a><a id="ks_amvp_input_same_as_output"></a><b>KS_AMVP_INPUT_SAME_AS_OUTPUT</b>

<dd>
<p>Use the same format for output as input.</p>
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