---
UID: NS.bdasup._BDA_FILTER_TEMPLATE
title: BDA_FILTER_TEMPLATE
author: windows-driver-content
description: The BDA_FILTER_TEMPLATE structure describes the template topology for a BDA filter.
old-location: stream\bda_filter_template.htm
old-project: stream
ms.assetid: 93078225-3487-46db-b13e-e2013be86d97
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: BDA_FILTER_TEMPLATE, BDA_FILTER_TEMPLATE, *PBDA_FILTER_TEMPLATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdasup.h
req.include-header: Bdasup.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_FILTER_TEMPLATE
req.alt-loc: bdasup.h
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
req.iface: 
---

# BDA_FILTER_TEMPLATE structure



## -description
<p>The BDA_FILTER_TEMPLATE structure describes the template topology for a BDA filter. </p>


## -syntax

````
typedef struct _BDA_FILTER_TEMPLATE {
  const KSFILTER_DESCRIPTOR *pFilterDescriptor;
  ULONG                     ulcPinPairs;
  const BDA_PIN_PAIRING     *pPinPairs;
} BDA_FILTER_TEMPLATE, *PBDA_FILTER_TEMPLATE;
````


## -struct-fields
<dl>

### -field <b>pFilterDescriptor</b>

<dd>
<p>Points to a KSFILTER_DESCRIPTOR structure that describes a template for a filter for the BDA device. </p>
</dd>

### -field <b>ulcPinPairs</b>

<dd>
<p>Number of pairs of pins in the <b>pPinPairs</b> array.</p>
</dd>

### -field <b>pPinPairs</b>

<dd>
<p>Array of BDA_PIN_PAIRING structures that describe the topology between a pair of the filter's input and output pins. </p>
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
<dt>Bdasup.h (include Bdasup.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556438">BdaCreateFilterFactory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556464">BdaInitFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556544">BDA_PIN_PAIRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562553">KSFILTER_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20BDA_FILTER_TEMPLATE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
