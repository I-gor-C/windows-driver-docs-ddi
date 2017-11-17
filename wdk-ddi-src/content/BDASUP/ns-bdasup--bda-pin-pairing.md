---
UID: NS.bdasup._BDA_PIN_PAIRING
title: BDA_PIN_PAIRING
author: windows-driver-content
description: The BDA_PIN_PAIRING structure describes the topology between a pair of input and output pins.
old-location: stream\bda_pin_pairing.htm
ms.assetid: 0d05455d-32ea-4f88-8752-7f5fe40b8b29
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: bdasup.h
req.include-header: Bdasup.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_PIN_PAIRING
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
ms.keywords: BDA_PIN_PAIRING, BDA_PIN_PAIRING, *PBDA_PIN_PAIRING
req.iface: 
---

# BDA_PIN_PAIRING structure



## -description
<p>The BDA_PIN_PAIRING structure describes the topology between a pair of input and output pins. </p>


## -syntax

````
typedef struct _BDA_PIN_PAIRING {
  ULONG       ulInputPin;
  ULONG       ulOutputPin;
  ULONG       ulcMaxInputsPerOutput;
  ULONG       ulcMinInputsPerOutput;
  ULONG       ulcMaxOutputsPerInput;
  ULONG       ulcMinOutputsPerInput;
  ULONG       ulcTopologyJoints;
  const ULONG *pTopologyJoints;
} BDA_PIN_PAIRING, *PBDA_PIN_PAIRING;
````


## -struct-fields
<dl>

### -field <b>ulInputPin</b>

<dd>
<p>Index of the element in the zero-based array of pin types (KSPIN_DESCRIPTOR_EX array) that indicates the input pin of the pair. </p>
</dd>

### -field <b>ulOutputPin</b>

<dd>
<p>Index of the element in the zero-based array of pin types (KSPIN_DESCRIPTOR_EX array) that indicates the output pin of the pair.</p>
</dd>

### -field <b>ulcMaxInputsPerOutput</b>

<dd>
<p>Maximum number of input pins per output pin. The network provider creates duplicates of nodes that are controlled by the input pin depending on the value specified in <b>ulcMaxInputsPerOutput</b>.</p>
</dd>

### -field <b>ulcMinInputsPerOutput</b>

<dd>
<p>Minimum number of input pins per output pin. The network provider creates duplicates of nodes that are controlled by the input pin depending on the value specified in <b>ulcMinInputsPerOutput</b>.</p>
</dd>

### -field <b>ulcMaxOutputsPerInput</b>

<dd>
<p>Maximum number of output pins per input pin. The network provider creates duplicates of nodes that are controlled by the output pin depending on the value specified in <b>ulcMaxOutputsPerInput</b>.</p>
</dd>

### -field <b>ulcMinOutputsPerInput</b>

<dd>
<p>Minimum number of output pins per input pin. The network provider creates duplicates of nodes that are controlled by the output pin depending on the value specified in <b>ulcMinOutputsPerInput</b>.</p>
</dd>

### -field <b>ulcTopologyJoints</b>

<dd>
<p>Number of joints in the <b>pTopologyJoints</b> array.</p>
</dd>

### -field <b>pTopologyJoints</b>

<dd>
<p>Array of joint values. The value given to a joint corresponds to the index of an element in a array of template connections (KSTOPOLOGY_CONNECTION or BDA_TEMPLATE_CONNECTION array). A topology joint marks the point in the template topology where control of nodes switches from the input pin to the output pin. Those nodes that occur upstream of the topology joint are controlled through the input pin. Those nodes that occur downstream of the topology joint are controlled through the output pin.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556523">BDA_FILTER_TEMPLATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556558">BDA_TEMPLATE_CONNECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567148">KSTOPOLOGY_CONNECTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20BDA_PIN_PAIRING structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
