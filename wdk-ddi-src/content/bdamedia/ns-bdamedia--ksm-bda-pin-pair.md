---
UID: NS.bdamedia._KSM_BDA_PIN_PAIR
title: KSM_BDA_PIN_PAIR
author: windows-driver-content
description: The KSM_BDA_PIN_PAIR structure describes a method request to retrieve the pin pairing structure (BDA_PIN_PAIRING) between a pair of input and output pins.
old-location: stream\ksm_bda_pin_pair.htm
old-project: stream
ms.assetid: 310a3faf-de71-4965-9511-cb8feca7087c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KSM_BDA_PIN_PAIR, KSM_BDA_PIN_PAIR, *PKSM_BDA_PIN_PAIR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdamedia.h
req.include-header: Bdamedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSM_BDA_PIN_PAIR
req.alt-loc: bdamedia.h
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

# KSM_BDA_PIN_PAIR structure



## -description
<p>The KSM_BDA_PIN_PAIR structure describes a method request to retrieve the pin pairing structure (BDA_PIN_PAIRING) between a pair of input and output pins. </p>


## -syntax

````
typedef struct _KSM_BDA_PIN_PAIR {
  KSMETHOD Method;
  union {
    ULONG InputPinId;
    ULONG InputPinType;
  };
  union {
    ULONG OutputPinId;
    ULONG OutputPinType;
  };
} KSM_BDA_PIN_PAIR, *PKSM_BDA_PIN_PAIR;
````


## -struct-fields
<dl>

### -field Method

<dd>
<p>KSMETHOD structure that describes a method and request type of a method request.</p>
</dd>

### -field InputPinId

<dd>
<p>Member of the union in KSM_BDA_PIN_PAIR that contains the identifier (ID) of an input pin of the filter.</p>
</dd>

### -field InputPinType

<dd>
<p>Member of the union in KSM_BDA_PIN_PAIR that contains the value that specifies the input pin type.</p>
</dd>

### -field OutputPinId

<dd>
<p>Member of the union in KSM_BDA_PIN_PAIR that contains the identifier (ID) of an output pin of the filter.</p>
</dd>

### -field OutputPinType

<dd>
<p>Member of the union in KSM_BDA_PIN_PAIR that contains the value that specifies the output pin type.</p>
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
<dt>Bdamedia.h (include Bdamedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\bdasup\ns-bdasup--bda-pin-pairing.md">BDA_PIN_PAIRING</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ikscontrol-ksmethod.md">KSMETHOD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSM_BDA_PIN_PAIR structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
